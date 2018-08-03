"""Tests for tvtk objects.

Some of these tests are copied from test_tvtk_base.  This is just to
make sure that the generated code works well.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2016, Enthought, Inc.
# License: BSD Style.

import unittest
import pickle
import weakref
import sys
import gc
import traceback
import types
import inspect
import re
import numpy
import vtk

from tvtk import tvtk_base
from tvtk.common import get_tvtk_name, configure_input_data, is_version_7

from traits.api import TraitError

vtk_major_version = vtk.vtkVersion.GetVTKMajorVersion()
vtk_minor_version = vtk.vtkVersion.GetVTKMinorVersion()

try:
    from tvtk.api import tvtk
except ImportError:
    msg = """
You need to build the tvtk_classes.zip file to run this test.
To generate tvtk_classes.zip you must do the following::

  $ cd ../ # This is the enthought/tvtk directory
  $ python code_gen.py
"""
    raise ImportError(msg)

# Only used for testing.
from tvtk.tvtk_classes import tvtk_helper

PY_VER = sys.version_info[0]
if PY_VER > 2:
    long = int


def mysum(arr):
    val = arr
    while type(val) == numpy.ndarray:
        val = numpy.sum(val)
    return val


def has_subclass(tvtk_class):
    """ Return True if `tvtk_class` has a subclass (excluding itself)
    Unfortunately because of the VTK API we cannot tell whether the
    subclass is abstract or not
    """
    def is_sub_class(x):
        return (inspect.isclass(x) and
                issubclass(x, tvtk_class) and
                x is not tvtk_class)
    # wish there was an iterator version of inspect.getmembers
    return bool(inspect.getmembers(tvtk, is_sub_class))


def skipUnlessTVTKHasattr(attr):
    if hasattr(tvtk, attr):
        return lambda func: func
    message = "{} is not available on this build of TVTK"
    return unittest.skip(message.format(attr))


class TestTVTK(unittest.TestCase):
    def test_wrap_vtk(self):
        """Test if the wrap_vtk function works."""
        o = vtk.vtkVolume()
        w = tvtk_helper.wrap_vtk(o)
        self.assertEqual(w.__class__.__name__, 'Volume')
        w1 = tvtk_helper.wrap_vtk(w)
        self.assertEqual(w, w1)
        del w1, w, o

        class A:
            pass
        a = A()
        w = tvtk_helper.wrap_vtk(a)
        self.assertEqual(a, w)

    def test_cache(self):
        """Test the caching of ancestor classes."""
        # Shut off pesky warnings.
        vtk.vtkObject.GlobalWarningDisplayOff()
        o = tvtk.ImageFFT()
        vtk_ver = vtk.vtkVersion().GetVTKVersion()
        if vtk_ver[:3] in ['4.2', '4.4']:
            cached = ['ImageFourierFilter', 'ImageDecomposeFilter',
                      'ImageIterateFilter', 'ImageToImageFilter',
                      'ImageSource', 'Source', 'ProcessObject',
                      'Object', 'ObjectBase']
        else:
            cached = ['ImageFourierFilter', 'ImageDecomposeFilter',
                      'ImageIterateFilter', 'ThreadedImageAlgorithm',
                      'ImageAlgorithm', 'Algorithm', 'Object',
                      'ObjectBase']

        for i in cached:
            self.assertIn(i, tvtk_helper._cache)
        vtk.vtkObject.GlobalWarningDisplayOn()

    def test_custom(self):
        """Test if custom modules can be imported."""

        # First clear the cache. Another module may have already imported
        # the same class and this would compromise the test
        from tvtk.tvtk_classes import tvtk_helper
        tvtk_helper._cache.clear()

        # Hack to simulate a module inside tvtk.custom.
        mod = types.ModuleType('xml_data_reader')

        class XMLDataReader:
            def f(self):
                return 'f'
        setattr(mod, 'XMLDataReader', XMLDataReader)
        sys.modules['tvtk.custom.xml_data_reader'] = mod

        # Now test if this is the one imported.
        r = tvtk.XMLDataReader()
        self.assertEqual(r.f(), 'f')
        if len(vtk.vtkObjectBase.__bases__) > 0:
            if vtk_major_version == 7 or PY_VER < 3:
                expect = ()
            else:
                expect = (object,)
        else:
            expect = tuple()

        self.assertEqual(r.__class__.__bases__, expect)

        # Clean up.
        del sys.modules['tvtk.custom.xml_data_reader']
        tvtk_helper._cache.clear()

    def test_basic(self):
        """Test a simple tvtk pipeline."""
        # If this works without any problems, we are ok.
        cs = tvtk.ConeSource()
        m = tvtk.PolyDataMapper()
        if vtk_major_version < 6:
            m.input = cs.output  # This should work
            m.input = cs.get_output()  # This should also work.
        else:
            m.input_connection = cs.output_port  # This should work.
            m.set_input_data(cs.get_output())  # This should also work.
        a = tvtk.Actor()
        a.mapper = m
        cs.resolution = 36
        p = a.property
        p.representation = 'w'

    def test_do_change(self):
        """Test if VTK object changes when trait is changed."""
        p = tvtk.Property()
        p.edge_visibility = not p.edge_visibility
        p.representation = 'p'
        p.interpolation = 'phong'
        p.opacity = 0.5
        p.color = (0, 1, 0)
        p.diffuse_color = (1, 1, 1)
        p.specular_color = (1, 1, 0)
        for t, g in p._updateable_traits_:
            val = getattr(p._vtk_obj, g)()
            if t in ['representation', 'interpolation']:
                self.assertEqual(val, getattr(p, t + '_'))
            else:
                self.assertEqual(val, getattr(p, t))

    def test_auto_update(self):
        """Test if traits are updated when the VTK object changes."""
        p = tvtk.Property()
        obj = p._vtk_obj
        obj.SetEdgeVisibility(1)
        self.assertEqual(p.edge_visibility, 1)

        obj.SetOpacity(0.5)
        self.assertEqual(p.opacity, 0.5)

        obj.SetRepresentationToPoints()
        self.assertEqual(p.representation, 'points')

        # color traits have been made non updateable
        if vtk_major_version <= 5 and vtk_minor_version < 10:
            val = (1.0, 1.0, 0.0)
            obj.SetColor(val)
            self.assertEqual(p.color, val)

        val = (1.0, 0.0, 0.0)
        obj.SetDiffuseColor(val)
        self.assertEqual(p.diffuse_color, val)

        val = (0.0, 1.0, 0.0)
        obj.SetSpecularColor(val)
        self.assertEqual(p.specular_color, val)

    def test_obj_del(self):
        """Test object deletion and reference cycles."""
        p = tvtk.Property()
        p.representation = 0
        ref = weakref.ref(p)
        del p
        self.assertEqual(ref(), None)

    def test_help_trait(self):
        """Test if the help attribute is correct."""
        n = tvtk.PolyDataNormals()
        t = n.traits()
        test = t['splitting'].desc != t['non_manifold_traversal'].desc
        self.assertEqual(test, True)

    def test_object_cache(self):
        """Test if object cache works."""
        cs = tvtk.ConeSource()
        hash1 = hash(cs)
        o = cs.output
        if hasattr(o, 'producer_port'):
            src = o.producer_port.producer
        else:
            src = cs.executive.algorithm
        self.assertEqual(src, cs)
        self.assertEqual(hash1, hash(src))
        del cs, src
        gc.collect()
        # The test sometimes fails as VTK seems to generate objects with the
        # same memory address and hash, we try to force it to allocate more
        # objects so as to not end up reusing the same address and hash.
        junk = [tvtk.ConeSource() for i in range(50)]

        # Now get another ConeSource and ensure the hash is different.
        cs = tvtk.ConeSource()
        o = cs.output
        if hasattr(o, 'producer_port'):
            src = o.producer_port.producer
        else:
            src = cs.executive.algorithm

        ##############################################################
        # This assertion is related to a bug fixed in VTK 6 onwards
        # For VTK 5.x this test is inconsistent, hence skipeed for 5.x
        # See http://review.source.kitware.com/#/c/15095/
        ##############################################################
        if vtk_major_version > 5:
            self.assertEqual(hash1 != hash(src), True)
        self.assertEqual(hash(cs), hash(src))

        # Test for a bug with collections and the object cache.
        r = tvtk.Renderer()

        def _get_props(obj):
            if hasattr(obj, 'view_props'):
                return obj.view_props
            else:
                return obj.props

        p = _get_props(r)
        l1 = len(tvtk_base._object_cache)
        p1 = _get_props(r)
        del p1
        l2 = len(tvtk_base._object_cache)
        self.assertEqual(l1, l2)

    def test_init_traits(self):
        """Test if the objects traits can be set in __init__."""
        p = tvtk.Property(opacity=0.1, color=(1, 0, 0), representation='p')
        self.assertEqual(p.opacity, 0.1)
        self.assertEqual(p.color, (1.0, 0.0, 0.0))
        self.assertEqual(p.representation, 'points')

        # Test case where the object traits are wrong.
        self.assertRaises(TraitError, tvtk.Property, foo='bar')

        cs = tvtk.ConeSource(radius=0.1, height=0.5, resolution=32)
        self.assertEqual(cs.radius, 0.1)
        self.assertEqual(cs.height, 0.5)
        self.assertEqual(cs.resolution, 32)

        # Test case where the object traits are wrong.
        self.assertRaises(TraitError, tvtk.ConeSource, foo=1)

    def test_matrix4x4(self):
        """Test if Matrix4x4 works nicely."""
        m = tvtk.Matrix4x4()
        [m.set_element(i, j, i*4 + j) for i in range(4) for j in range(4)]
        s = pickle.dumps(m)
        del m
        m = pickle.loads(s)
        for i in range(4):
            for j in range(4):
                self.assertEqual(m.get_element(i, j), i*4 + j)
        # Test the from/to_array functions.
        a = numpy.array(list(range(16)), dtype=float)
        a.shape = 4, 4
        m = tvtk.Matrix4x4()
        m.from_array(a)
        b = m.to_array()
        self.assertEqual(numpy.allclose(a, b), True)

    def test_property(self):
        """Test if Property's color works ok in all circumstances."""
        p = tvtk.Property()
        val = (0., 1., 0.)
        p.color = val
        p.specular = 1.0
        self.assertEqual(p.specular_color, val)
        self.assertEqual(p.diffuse_color, val)
        self.assertEqual(p.ambient_color, val)

        sc = (1., 0., 1.)
        p.specular_color = sc
        self.assertEqual(p.specular_color, sc)
        self.assertEqual(p.diffuse_color, val)
        self.assertEqual(p.ambient_color, val)
        self.assertEqual(p.color, (0.5, 0.5, 0.5))

        # Test pickling.
        s = pickle.dumps(p)
        del p
        p = pickle.loads(s)
        self.assertEqual(p.specular_color, sc)
        self.assertEqual(p.diffuse_color, val)
        self.assertEqual(p.ambient_color, val)
        self.assertEqual(p.color, (0.5, 0.5, 0.5))

    def test_points_lookup(self):
        """ Test if points can be looked up with both int and long keys.
            Fixes GH Issue 173.
        """
        points = tvtk.Points()
        points.insert_next_point((0, 1, 2))
        pt = points[0]
        self.assertEqual(pt, (0, 1, 2))
        ptl = points[long(0)]
        self.assertEqual(ptl, (0, 1, 2))
        get_pt = points.get_point(0)
        self.assertEqual(get_pt, (0, 1, 2))
        get_ptl = points.get_point(long(0))
        self.assertEqual(get_ptl, (0, 1, 2))

    def test_cell_array(self):
        """ Test if cell array insertion updates number of cells.
            Fixes GH Issue 178.
        """
        cell_array = tvtk.CellArray()
        line1 = tvtk.Line()
        self.assertEqual(cell_array.number_of_cells, 0)
        cell_array.insert_next_cell(line1)
        self.assertEqual(cell_array.number_of_cells, 1)
        line2 = tvtk.Line()
        cell_array.insert_next_cell(line2)
        self.assertEqual(cell_array.number_of_cells, 2)

    def test_collection(self):
        """Test if Collection objects work nicely."""
        ac = tvtk.ActorCollection()
        self.assertEqual(len(ac), 0)
        self.assertRaises(IndexError, ac.__getitem__, 0)
        a_list = []
        a = tvtk.Actor()
        a_list.append(a)
        ac.append(a)
        self.assertRaises(TypeError, ac.__getitem__, 's')
        self.assertEqual(len(ac), 1)
        a = tvtk.Actor()
        a_list.append(a)
        ac.append(a)
        self.assertEqual(len(ac), 2)

        # Test iterator nature.
        for i, j in zip(ac, a_list):
            self.assertEqual(i._vtk_obj, j._vtk_obj)
        for i, j in enumerate(ac):
            self.assertEqual(a_list[i]._vtk_obj, j._vtk_obj)

        # Test __setitem__.
        ac[0] = a_list[1]
        ac[1] = a_list[0]
        self.assertEqual(ac[0]._vtk_obj, a_list[1]._vtk_obj)
        self.assertEqual(ac[1]._vtk_obj, a_list[0]._vtk_obj)
        self.assertRaises(TypeError, ac.__setitem__, 's', a_list[1])

        # Test __delitem__.
        del ac[-2]
        self.assertEqual(ac[0]._vtk_obj, a_list[0]._vtk_obj)
        self.assertEqual(len(ac), 1)
        self.assertRaises(TypeError, ac.__delitem__, 1.414)
        del ac[0]
        self.assertEqual(len(ac), 0)

        # Test __repr__.
        self.assertEqual(repr(ac), '[]')

        # test extend.
        ac.extend(a_list)
        self.assertEqual(len(ac), 2)
        for i, j in enumerate(ac):
            self.assertEqual(a_list[i]._vtk_obj, j._vtk_obj)

        # Test the prop collection.
        pc = tvtk.PropCollection()
        a = tvtk.Actor()
        pc.append(a)
        self.assertEqual(pc[0], a)
        for i in pc:
            self.assertEqual(i, a)

    def test_set_scalars(self):
        """Test if SetScalars works without a segfault."""
        mesh = tvtk.PolyData()
        sc = tvtk.FloatArray()
        # If this does not segfault, we are OK.
        mesh.point_data.scalars = sc

    def test_data_array(self):
        """Test if vtkDataArrays behave in a Pythonic fashion."""
        # Check a 3D array.
        f = tvtk.FloatArray()
        a = numpy.array([[0., 0, 0], [1, 1, 1]])
        f.from_array(a)
        self.assertEqual(f.number_of_components, 3)
        self.assertEqual(f.number_of_tuples, 2)
        self.assertEqual(mysum(f.to_array() - a), 0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i-j), 0.0)
        self.assertEqual(f[0], (0.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1., 1., 1.))
        self.assertEqual(repr(f), '[(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]')
        f.append((2, 2, 2))
        f.extend([[3, 3, 3], [4, 4, 4]])
        self.assertEqual(len(f), 5)
        self.assertEqual(f.number_of_components, 3)
        self.assertEqual(f.number_of_tuples, 5)
        f[1] = [-1, -1, -1]
        self.assertEqual(f[1], (-1.0, -1.0, -1.0))
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

        # Check a 5D arrray
        a = numpy.array([[0., 0, 0, 0, 0], [1, 1, 1, 1, 1]])
        f.from_array(a)
        self.assertEqual(mysum(f.to_array() - a), 0.0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i - j), 0.0)
        self.assertEqual(f[0], (0.0, 0.0, 0.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1., 1., 1., 1., 1.))
        self.assertEqual(
            repr(f), '[(0.0, 0.0, 0.0, 0.0, 0.0), (1.0, 1.0, 1.0, 1.0, 1.0)]')
        f.append((2, 2, 2, 2, 2))
        f.extend([[3, 3, 3, 3, 3], [4, 4, 4, 4, 4]])
        self.assertEqual(len(f), 5)
        self.assertEqual(f.number_of_components, 5)
        self.assertEqual(f.number_of_tuples, 5)
        self.assertEqual(f[-1], (4., 4., 4., 4., 4.))
        f[1] = [-1, -1, -1, -1, -1]
        self.assertEqual(f[1], (-1.0, -1.0, -1.0, -1.0, -1.0))
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

    def test_points(self):
        """Test if vtkPoints behaves in a Pythonic fashion."""
        f = tvtk.Points()
        a = numpy.array([[0., 0, 0], [1, 1, 1]])
        f.from_array(a)
        self.assertEqual(mysum(f.to_array() - a), 0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i - j), 0)

        a[0, 0] = 1.0  # Should change the VTK data!
        # Make sure that everything works even when the original array
        # is deleted.
        del a
        self.assertEqual(f[0], (1.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1., 1., 1.))
        self.assertEqual(repr(f), '[(1.0, 0.0, 0.0), (1.0, 1.0, 1.0)]')
        f.append((2, 2, 2))
        f.extend([[3, 3, 3], [4, 4, 4]])
        self.assertEqual(len(f), 5)
        f[1] = [-1, -1, -1]
        self.assertEqual(f[1], (-1.0, -1.0, -1.0))
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

    def test_idlist(self):
        """Test if vtkIdList behaves in a Pythonic fashion."""
        f = tvtk.IdList()
        a = numpy.array([0, 1, 2, 3])
        f.from_array(a)
        for i, j in zip(a, f):
            self.assertEqual(i, j)
        self.assertEqual(f[-1], 3)
        self.assertEqual(f[0], 0)
        if sys.version_info[0] > 2:
            self.assertEqual(repr(f), '[0, 1, 2, 3]')
        else:
            if type(f[0]) is long:
                self.assertEqual(repr(f), '[0L, 1L, 2L, 3L]')
            else:
                self.assertEqual(repr(f), '[0, 1, 2, 3]')
        f.append(4)
        f.extend([5, 6])
        self.assertEqual(len(f), 7)
        f[1] = -1
        self.assertEqual(f[1], -1)
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

    def test_array_conversion(self):
        """Test if Numeric/VTK array conversion works."""
        # This is only a simple test.
        data = numpy.array(
            [[0, 0, 0, 10], [1, 0, 0, 20], [0, 1, 0, 20], [0, 0, 1, 30]], 'f')
        triangles = numpy.array([[0, 1, 3], [0, 3, 2], [1, 2, 3], [0, 2, 1]])
        points = data[:, :3]
        temperature = data[:, -1]
        mesh = tvtk.PolyData()
        mesh.points = points
        mesh.polys = triangles
        mesh.point_data.scalars = temperature

        # Test if a normal float array also works.
        temp = tvtk.FloatArray()
        temp.from_array(temperature)
        mesh.point_data.scalars = temp

    def test_append_poly_data_input(self):
        """Test if AppendPolyData has its get_input wrapped right."""
        a = tvtk.AppendPolyData()
        self.assertEqual(hasattr(a, 'get_input'), True)
        self.assertEqual(a.input, None)

    def test_property_change_notification(self):
        """Test if changes to properties generate notification events."""
        # Create a dummy class to test with.
        class Junk:
            def f(self, obj, name, old, new):
                self.data = obj, name, old, new
        z = Junk()
        cs = tvtk.ConeSource()
        m = tvtk.PolyDataMapper()
        if vtk_major_version < 6:
            m.on_trait_change(z.f, 'input')
            m.input = cs.output
            self.assertEqual(z.data, (m, 'input', None, cs.output))
            m.input = None
            self.assertEqual(z.data, (m, 'input', cs.output, None))
            m.on_trait_change(z.f, 'input', remove=True)
            m.input = cs.output
        else:
            m.on_trait_change(z.f, 'input_connection')
            m.input_connection = cs.output_port
            self.assertEqual(
                z.data, (m, 'input_connection', None, cs.output_port))
            m.input_connection = None
            self.assertEqual(
                z.data, (m, 'input_connection', cs.output_port, None))
            m.on_trait_change(z.f, 'input_connection', remove=True)
            m.input_connection = cs.output_port
        a = tvtk.Actor()
        a.on_trait_change(z.f, 'mapper')
        a.on_trait_change(z.f, 'property')
        a.mapper = m
        self.assertEqual(z.data, (a, 'mapper', None, m))
        old = a.property
        new = tvtk.Property()
        a.property = new
        self.assertEqual(z.data, (a, 'property', old, new))

        # Check if property notification occurs on add_input/remove_input
        a = tvtk.AppendPolyData()
        pd = tvtk.PolyData()
        if vtk_major_version < 6:
            a.on_trait_change(z.f, 'input')
            a.add_input(pd)
            old, new = None, pd
            self.assertEqual(z.data, (a, 'input', old, new))
            a.remove_input(pd)
            old, new = pd, None
            self.assertEqual(z.data, (a, 'input', old, new))
            a.remove_all_inputs()
            old, new = None, None
            self.assertEqual(z.data, (a, 'input', old, new))
        else:
            a.add_input_data(pd)
            self.assertEqual(a.input, pd)
            a.remove_input_data(pd)
            self.assertEqual(a.input, None)
            a.remove_all_inputs()
            self.assertEqual(a.input, None)

    def test_tuple_array_handling(self):
        """Test if methods can take any sequence rather than only tuples."""
        sg = tvtk.StructuredGridGeometryFilter()
        # setting a bogus value triggers an error since VTK assumes
        # that we want the extent set in the passed object.  If we use
        # an Array type instead of a Tuple then we can pass in
        # a list and it should work OK.
        sg.extent = [0, -1, 0, -1, 0, -1]

    def test_information_keys(self):
        """Test if vtk information objects can be created."""
        s = tvtk.StructuredPoints()
        x = s.FIELD_ARRAY_TYPE()
        y = tvtk.Information()
        x.get(y)

    def test_parent_child_bounds(self):
        """CubeAxesActor2D's bounds should be writable."""
        c = tvtk.CubeAxesActor2D()
        c.bounds = (0, 1, 0, 1, 0, 1)

    def test_parent_child_input(self):
        """Case where parent has GetInput and child SetInput."""
        if (vtk_major_version >= 6 and vtk_minor_version > 1) or \
            vtk_major_version >= 7:
            vm = tvtk.SmartVolumeMapper()
        else:
            vm = tvtk.VolumeTextureMapper2D()
        # In this case if the wrapping is not done right, the input
        # trait is made read-only which is a bug.  We set the input
        # below to test this.
        configure_input_data(vm, tvtk.ImageData())
        spw = tvtk.StructuredPointsWriter()
        if vtk_major_version < 6:
            spw.input = None
        else:
            spw.input_connection = None

    @unittest.skipIf(
        vtk_major_version >= 6, "Setting scalar type is no longer supported on VTK 6")
    def test_image_data_scalar_type(self):
        """Does ImageData support all scalar types?.
        """
        img = tvtk.ImageData()
        # There are 22 scalar types in VTK-5.2.  We should be able to
        # use them all.
        for i in range(0, 22):
            img.scalar_type = i

    def test_null_string_wrapper(self):
        "Check if a null string default is wrapped as a String trait."
        cap = tvtk.CaptionActor2D()
        self.assertEqual(
            ('caption', 'GetCaption') in cap._updateable_traits_, True)
        self.assertEqual('caption' in cap._full_traitnames_list_, True)

    def test_spider_plot_actor_set_axis_label(self):
        """ Test SpiderPlotActor Get/SetAxisLabel works
        """
        # SpiderPlotActor.SetAxisLabel accepts two arguments
        # that are of different type, we need to make sure they
        # are coded as is
        actor = tvtk.SpiderPlotActor()
        actor.set_axis_label(1, 'ss')
        self.assertEqual(actor.get_axis_label(1), 'ss')

    def test_image_convolve_kernel(self):
        """ Test that setting the kernels in ImageConvolve works
        """
        tvtk_filter = tvtk.ImageConvolve()
        expected = numpy.arange(9.)

        if vtk_major_version < 6:
            # Before VTK 6, the ImageConvolve.GetKernel3x3
            # requires an array as argument

            # Set the kernel
            tvtk_filter.set_kernel3x3(expected)

            # Get it back
            result = numpy.empty(9)
            tvtk_filter.get_kernel3x3(result)

            self.assertTrue(numpy.allclose(result, expected), True)

            with self.assertRaises(TypeError):
                # VTK Set method raises the TypeError
                tvtk_filter.set_kernel3x3(range(2))

        else:
            # Since VTK 6.x, ImageConvolve.GetKernel3x3
            # can take either no argument or an array
            # With that change in the API, kernel3x3
            # is a Trait (similarly for kernel3x3x3, ...)
            tvtk_filter.kernel3x3 = expected

            # Get it back
            result = numpy.empty(9)
            tvtk_filter._vtk_obj.GetKernel3x3(result)

            self.assertTrue(numpy.allclose(result, expected), True)

            # The shape is validated by Trait
            with self.assertRaises(TraitError):
                tvtk_filter.kernel3x3 = range(2)

    @skipUnlessTVTKHasattr('DistanceRepresentation2D')
    def test_distance_representation_2d_point1_world_position(self):
        """ Test that Position attributes in DistanceRepresentation2D works
        """
        tvtk_filter = tvtk.DistanceRepresentation2D()
        tvtk_filter.instantiate_handle_representation()

        if vtk_major_version < 6:
            # Before VTK 6, the DistanceRepresentation2D.GetPoint1WorldPosition
            # requires an array as argument

            # Set the kernel
            expected = (1, 2, 3)
            tvtk_filter.set_point1_world_position(expected)

            # Get it back
            result = numpy.empty(3)
            tvtk_filter.get_point1_world_position(result)

            self.assertTrue(numpy.allclose(result, expected), True)

            with self.assertRaises(TypeError):
                # VTK Set method raises the TypeError
                tvtk_filter.set_point1_world_position(range(2))
        else:
            # Since VTK 6.x, DistanceRepresentation2D.GetPoint1WorldPosition
            # can take either no argument or an array
            # With that change in the API, point1_world_position
            # is a Trait (similarly for point2_world_position ...)

            # Set the position
            expected = (1, 2, 3)
            tvtk_filter.point1_world_position = expected

            # Get it back
            result = numpy.empty(3)
            tvtk_filter._vtk_obj.GetPoint1WorldPosition(result)

            self.assertTrue(numpy.allclose(result, expected), True)

            # The shape is validated by Trait
            with self.assertRaises(TraitError):
                tvtk_filter.point1_world_position = range(2)

    @skipUnlessTVTKHasattr('XOpenGLRenderWindow')
    def test_xopengl_render_window(self):
        """ Test that setting the position to a render window works
        Issue #357
        """
        window = tvtk.XOpenGLRenderWindow()

        # Setting it to some valid value
        window.position = (1, 1)

        # But setting to some invalid value outside of update_traits
        # should fail as long as Traits is doing its job
        with self.assertRaises(TraitError):
            window.position = 1

    @unittest.skipIf(vtk_major_version < 6,
                     ('vtkHardwareSelector.PropColorValue is not available '
                      'for vtk version < 6'))
    @skipUnlessTVTKHasattr('HardwareSelector')
    def test_hardware_selector_prop_color_value(self):
        """ Test that PropColorValue of HardwareSelector works
        Issue #360
        """
        selector = tvtk.HardwareSelector()

        # Setting it to some valid value
        selector.prop_color_value = (0.1, 0.4, 0.2)

        # But setting to some invalid value outside of update_traits
        # should fail as long as Traits is doing its job
        with self.assertRaises(TraitError):
            selector.prop_color_value = (-100., 10., 1.)

    @skipUnlessTVTKHasattr('AxesTransformRepresentation')
    def test_axes_transform_representation_tolerance(self):
        """ Test the tolerance of AxesTransformRepresentation is set properly
        """
        tvtk_obj = tvtk.AxesTransformRepresentation()
        vtk_obj = vtk.vtkAxesTransformRepresentation()

        self.assertTrue(tvtk_obj.tolerance <= vtk_obj.GetToleranceMaxValue())
        self.assertTrue(tvtk_obj.tolerance >= vtk_obj.GetToleranceMinValue())

    @skipUnlessTVTKHasattr('ObjectFactory')
    def test_object_factory_enableflag_api(self):
        """ Test ObjectFactory Get/SetEnableFlag API
        """
        # It is an abstract class, can't instantiate
        klass = tvtk.ObjectFactory

        if has_subclass(klass):
            # If we place this check as a unittest.skipIf decorator,
            # this would cause garbage collection tests in the test suite to fail
            # as the some classes are kept live
            raise unittest.SkipTest(('ObjectFactory has a subclass. '
                                     'This may cause the TVTK API to be different '
                                     'from if it had not'))

        # The Set/Get methods require many args
        # they should be coded as such
        self.assertTrue(hasattr(klass, 'set_enable_flag'))
        self.assertTrue(hasattr(klass, 'get_enable_flag'))

    @skipUnlessTVTKHasattr('ContextDevice2D')
    def test_contextdevice2d_matrix_api(self):
        """ Test ContextDevice2D Get/SetMatrix API
        """
        # It is an abstract class, can't instantiate
        klass = tvtk.ContextDevice2D

        if has_subclass(klass):
            # If we place this check as a unittest.skipIf decorator,
            # this would cause garbage collection tests in the test suite to fail
            # as the some classes are kept live
            raise unittest.SkipTest(('ContextDevice2D has a subclass. '
                                     'This may cause the TVTK API to be different '
                                     'from if it had not'))

        # The Set/Get methods require many args
        # they should be coded as such
        self.assertTrue(hasattr(klass, 'set_matrix'))
        self.assertTrue(hasattr(klass, 'get_matrix'))

    def test_algorithm_methods_are_wrapped(self):
        x = tvtk.Algorithm()
        self.assertTrue(hasattr(x, 'get_input_algorithm'))
        self.assertTrue(callable(x.get_input_algorithm))
        # It should also expose input_algorithm as a property trait.
        self.assertTrue(hasattr(x, 'input_algorithm'))

    def test_vtk_python_algorithm_base_is_wrapped(self):
        from tvtk import vtk_module
        name = 'VTKPythonAlgorithmBase'
        if hasattr(vtk_module, name):
            self.assertTrue(hasattr(tvtk, name))
            # Should be able to instantiate this wrapped class.
            getattr(tvtk, name)()

    def test_to_vtk_returns_vtk_object(self):
        # Given
        x = tvtk.ContourFilter()
        # When
        v = tvtk.to_vtk(x)
        # Then
        self.assertEqual(v.GetClassName(), 'vtkContourFilter')
        self.assertTrue(v is x._vtk_obj)

    def test_to_tvtk_returns_tvtk_object(self):
        # Given
        v = vtk.vtkContourFilter()
        # When
        x = tvtk.to_tvtk(v)
        # Then
        self.assertEqual(x.class_name, 'vtkContourFilter')
        self.assertTrue(isinstance(x, tvtk_base.TVTKBase))
        self.assertTrue(isinstance(x, tvtk.ContourFilter))
        self.assertTrue(v is x._vtk_obj)

    def test_to_tvtk_wraps_subclass_of_vtk(self):
        # Given
        class MyAlgorithm(vtk.vtkPythonAlgorithm):
            pass

        a = MyAlgorithm()
        # When
        ta = tvtk.to_tvtk(a)

        # Then
        self.assertTrue(isinstance(ta, tvtk.PythonAlgorithm))

        # Given
        class B(MyAlgorithm):
            pass

        b = B()
        # When
        tb = tvtk.to_tvtk(b)

        # Then
        self.assertTrue(isinstance(tb, tvtk.PythonAlgorithm))


# This separates out any tests for the entire module that would affect
# the functioning of the other tests.
class TestTVTKModule(unittest.TestCase):

    def tearDown(self):
        tvtk_helper._cache.clear()
        vtk.vtkObject.GlobalWarningDisplayOn()

    def setUp(self):
        vtk.vtkObject.GlobalWarningDisplayOff()
        self.names = []
        # Filter the ones that are abstract or not implemented
        for name in dir(vtk):
            if (not name.startswith('vtk') or name.startswith('vtkQt') or
                    len(name) <= 3):
                continue
            vtk_klass = getattr(vtk, name)
            tvtk_klass_name = get_tvtk_name(name)
            tvtk_klass = getattr(tvtk, tvtk_klass_name, None)
            if hasattr(vtk_klass, '__bases__') and tvtk_klass is not None:
                try:
                    obj = vtk_klass()
                except (TypeError, NotImplementedError):
                    continue
                else:
                    self.names.append(name)

    def test_all_instantiable(self):
        """Test if all the TVTK classes can be instantiated"""
        errors = []
        for name in self.names:
            tvtk_name = get_tvtk_name(name)
            tvtk_klass = getattr(tvtk, tvtk_name, None)
            try:
                tvtk_klass()
            except TraitError:
                errors.append(traceback.format_exc())
        if len(errors) > 0:
            message = "Not all classes could be instantiated:\n{0}\n"
            raise AssertionError(message.format(''.join(errors)))

    def test_trait_with_range(self):
        '''Test if all the attributes with MinValue/MaxValue are traits
        with Range
        '''
        def to_camel_case(text):
            """ Convert text to CamelCase"""
            def replace_func(matched):
                word = matched.group(0).strip("_")
                return word[0].upper()+word[1:].lower()
            return re.sub(r'(_?[a-zA-Z]+)', replace_func, text)

        def get_min_max_value(vtk_klass, vtk_attr_name):
            """ Return (min, max) of a VTK attribute

            If MaxValue or MinValue is not available
            (None, None) is returned
            """
            get_min_method = 'Get' + vtk_attr_name + 'MinValue'
            get_max_method = 'Get' + vtk_attr_name + 'MaxValue'
            try:
                return (getattr(vtk_klass(), get_min_method)(),
                        getattr(vtk_klass(), get_max_method)())
            except AttributeError:
                return None, None

        for name in self.names:
            vtk_klass = getattr(vtk, name)
            tvtk_klass_name = get_tvtk_name(name)

            try:
                obj = getattr(tvtk, tvtk_klass_name)()
            except Exception:
                # testing for instantiation is above
                pass

            for trait_name in obj.editable_traits():
                vtk_attr_name = to_camel_case(trait_name)
                min_value, max_value = get_min_max_value(vtk_klass,
                                                         vtk_attr_name)

                # Explicitly checking for None instead of bool(value)
                # since min_value/max_value could be int(0)
                if max_value is not None and min_value is not None:
                    # If max and min values are defined, setting the trait
                    # to outside this range should fail
                    with self.assertRaises(TraitError):
                        setattr(obj, trait_name, (min_value-1, max_value))
                    with self.assertRaises(TraitError):
                        setattr(obj, trait_name, (min_value, max_value+1))

    def test_no_trait_has_ptr_address_as_value(self):
        '''Test if none of the TVTK classes' traits has a value of "*_p_void"
        '''
        errors_trait_is_ptr = []
        for name in self.names:
            tvtk_klass_name = get_tvtk_name(name)
            try:
                obj = getattr(tvtk, tvtk_klass_name)()
            except Exception:
                # testing for instantiation is above
                pass

            # Had to use `_full_traitnames_list_` instead of calling
            # editable_traits(), otherwise looping over the trait name
            # and getting the attribute (getattr) cause Segfault for
            # AxisActor.title_prop3d, DataSetCellIterator.cell_type
            # DataSetCellIterator.number_of_points ...etc
            for trait_name in obj._full_traitnames_list_:
                try:
                    trait = getattr(obj, trait_name)
                except (TypeError, TraitError):
                    pass  # this is tested in another test
                else:
                    if isinstance(trait, str) and trait.endswith('_p_void'):
                        errors_trait_is_ptr.append(
                            (tvtk_klass_name, trait_name, trait))

        if errors_trait_is_ptr:
            message = 'These traits are invalid:\n'
            message += '\n'.join(('tvtk.{0}.{1} = {2!r}'.format(*error)
                                  for error in errors_trait_is_ptr))
            self.fail(message)

    def test_all_traits_can_be_obtained(self):
        '''Test if all of the traits can be obtained
        '''
        errors_getting_trait = []
        for name in self.names:
            tvtk_klass_name = get_tvtk_name(name)
            try:
                obj = getattr(tvtk, tvtk_klass_name)()
            except Exception:
                # testing for instantiation is above
                pass

            for trait_name in obj._full_traitnames_list_:
                try:
                    trait = getattr(obj, trait_name)
                except Exception as exception:
                    errors_getting_trait.append(
                        (tvtk_klass_name, trait_name, str(exception)))

        if errors_getting_trait:
            message = 'These traits cannot be obtained:\n'
            message += '\n'.join(('tvtk.{0}.{1} : {2}'.format(*error)
                                  for error in errors_getting_trait))
            self.fail(message)

    def test_import_tvtk_does_not_import_gui(self):
        from subprocess import check_output, STDOUT

        output = check_output(
            [sys.executable, "-v", "-c",
             "from tvtk.api import tvtk; p = tvtk.Property()"], stderr=STDOUT
        )
        output = output.decode('ascii')
        self.assertFalse('QtCore' in output)
        self.assertFalse('wx' in output)

    @unittest.skipIf(PY_VER > 2, "Irrelevant for python 3")
    def test_unicode_traits(self):
        reader = tvtk.DelimitedTextReader()
        self.assertIsInstance(reader.unicode_record_delimiters, unicode)
        self.assertIsInstance(reader.unicode_string_delimiters, unicode)
        self.assertIsInstance(reader.unicode_field_delimiters, unicode)

if __name__ == "__main__":
    unittest.main()
