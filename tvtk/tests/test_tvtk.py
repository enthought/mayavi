"""Tests for tvtk objects.

Some of these tests are copied from test_tvtk_base.  This is just to
make sure that the generated code works well.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004, Enthought, Inc.
# License: BSD Style.

import unittest
import cPickle
import weakref
import vtk
import new
import sys
import gc
import numpy
import vtk

from tvtk import tvtk_base
from tvtk.common import get_tvtk_name, configure_input_data

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
    raise ImportError, msg

# Only used for testing.
from tvtk.tvtk_classes import tvtk_helper

def mysum(arr):
    val = arr
    while type(val) == numpy.ndarray:
        val = numpy.sum(val)
    return val

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
            self.assertEqual(tvtk_helper._cache.has_key(i), True)
        vtk.vtkObject.GlobalWarningDisplayOn()

    def test_custom(self):
        """Test if custom modules can be imported."""

        # Hack to simulate a module inside tvtk.custom.
        mod = new.module('xml_data_reader')
        class XMLDataReader:
            def f(self):
                return 'f'
        setattr(mod, 'XMLDataReader', XMLDataReader)
        sys.modules['tvtk.custom.xml_data_reader'] = mod

        # Now test if this is the one imported.
        r = tvtk.XMLDataReader()
        self.assertEqual(r.f(), 'f')
        self.assertEqual(r.__class__.__bases__, ())

        # Clean up.
        del sys.modules['tvtk.custom.xml_data_reader']

    def test_basic(self):
        """Test a simple tvtk pipeline."""
        # If this works without any problems, we are ok.
        cs = tvtk.ConeSource()
        m = tvtk.PolyDataMapper()
        if vtk_major_version < 6:
            m.input = cs.output # This should work
            m.input = cs.get_output() # This should also work.
        else:
            m.input_connection = cs.output_port # This should work.
            m.set_input_data(cs.get_output()) # This should also work.
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
        p.color = (0,1,0)
        p.diffuse_color = (1,1,1)
        p.specular_color = (1,1,0)
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
        test = t['splitting'].help != t['non_manifold_traversal'].help
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
        junk = [vtk.vtkConeSource() for i in range(5)]

        # Now get another ConeSource and ensure the hash is different.
        cs = tvtk.ConeSource()
        o = cs.output
        if hasattr(o, 'producer_port'):
            src = o.producer_port.producer
        else:
            src = cs.executive.algorithm

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
        p = tvtk.Property(opacity=0.1, color=(1,0,0), representation='p')
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
        [m.set_element(i, j, i*4 +j) for i in range(4) for j in range(4)]
        s = cPickle.dumps(m)
        del m
        m = cPickle.loads(s)
        for i in range(4):
            for j in range(4):
                self.assertEqual(m.get_element(i, j), i*4 + j)
        # Test the from/to_array functions.
        a = numpy.array(range(16), dtype=float)
        a.shape = 4,4
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
        s = cPickle.dumps(p)
        del p
        p = cPickle.loads(s)
        self.assertEqual(p.specular_color, sc)
        self.assertEqual(p.diffuse_color, val)
        self.assertEqual(p.ambient_color, val)
        self.assertEqual(p.color, (0.5, 0.5, 0.5))

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
        a = numpy.array([[0.,0,0],[1,1,1]])
        f.from_array(a)
        self.assertEqual(f.number_of_components, 3)
        self.assertEqual(f.number_of_tuples, 2)
        self.assertEqual(mysum(f.to_array() - a), 0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i-j), 0.0)
        self.assertEqual(f[0], (0.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1.,1.,1.))
        self.assertEqual(repr(f), '[(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]')
        f.append((2,2,2))
        f.extend([[3,3,3], [4,4,4]])
        self.assertEqual(len(f), 5)
        self.assertEqual(f.number_of_components, 3)
        self.assertEqual(f.number_of_tuples, 5)
        f[1] = [-1,-1,-1]
        self.assertEqual(f[1], (-1.0, -1.0, -1.0))
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

        # Check a 5D arrray
        a = numpy.array([[0.,0,0, 0, 0],[1,1,1, 1, 1]])
        f.from_array(a)
        self.assertEqual(mysum(f.to_array()- a), 0.0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i - j), 0.0)
        self.assertEqual(f[0], (0.0, 0.0, 0.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1.,1.,1., 1., 1.))
        self.assertEqual(repr(f),
                         '[(0.0, 0.0, 0.0, 0.0, 0.0), (1.0, 1.0, 1.0, 1.0, 1.0)]')
        f.append((2,2,2,2,2))
        f.extend([[3,3,3,3,3], [4,4,4,4,4]])
        self.assertEqual(len(f), 5)
        self.assertEqual(f.number_of_components, 5)
        self.assertEqual(f.number_of_tuples, 5)
        self.assertEqual(f[-1], (4., 4.,4.,4.,4.))
        f[1] = [-1,-1,-1, -1,-1]
        self.assertEqual(f[1], (-1.0, -1.0, -1.0,-1.0, -1.0))
        self.assertRaises(IndexError, f.__getitem__, 100)
        self.assertRaises(IndexError, f.__setitem__, 100, 100)

    def test_points(self):
        """Test if vtkPoints behaves in a Pythonic fashion."""
        f = tvtk.Points()
        a = numpy.array([[0.,0,0],[1,1,1]])
        f.from_array(a)
        self.assertEqual(mysum(f.to_array() - a), 0)
        for i, j in zip(a, f):
            self.assertEqual(mysum(i - j), 0)

        a[0,0] = 1.0 # Should change the VTK data!
        # Make sure that everything works even when the original array
        # is deleted.
        del a
        self.assertEqual(f[0], (1.0, 0.0, 0.0))
        self.assertEqual(f[-1], (1.,1.,1.))
        self.assertEqual(repr(f), '[(1.0, 0.0, 0.0), (1.0, 1.0, 1.0)]')
        f.append((2,2,2))
        f.extend([[3,3,3], [4,4,4]])
        self.assertEqual(len(f), 5)
        f[1] = [-1,-1,-1]
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
        data = numpy.array([[0,0,0,10], [1,0,0,20],
                            [0,1,0,20], [0,0,1,30]], 'f')
        triangles = numpy.array([[0,1,3], [0,3,2],
                                 [1,2,3], [0,2,1]])
        points = data[:,:3]
        temperature = data[:,-1]
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
            self.assertEqual(z.data, (m, 'input_connection', None, cs.output_port))
            m.input_connection = None
            self.assertEqual(z.data, (m, 'input_connection', cs.output_port, None))
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
        sg.extent = [0,-1, 0,-1, 0,-1]

    def test_information_keys(self):
        """Test if vtk information objects can be created."""
        s = tvtk.StructuredPoints()
        x = s.FIELD_ARRAY_TYPE()
        y = tvtk.Information()
        x.get(y)

    def test_parent_child_bounds(self):
        """CubeAxesActor2D's bounds should be writable."""
        c = tvtk.CubeAxesActor2D()
        c.bounds = (0,1,0,1,0,1)

    def test_parent_child_input(self):
        """Case where parent has GetInput and child SetInput."""
        if vtk_major_version == 6 and vtk_minor_version > 1:
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

    def test_image_data_scalar_type(self):
        """Does ImageData support all scalar types?.
        Setting scalar type is no longer supported on VTK 6."""
        if vtk_major_version < 6:
            img = tvtk.ImageData()
            # There are 22 scalar types in VTK-5.2.  We should be able to
            # use them all.
            for i in range(0, 22):
                img.scalar_type = i

    def test_null_string_wrapper(self):
        "Check if a null string default is wrapped as a String trait."
        cap = tvtk.CaptionActor2D()
        self.assertEqual(('caption', 'GetCaption') in cap._updateable_traits_, True)
        self.assertEqual('caption' in cap._full_traitnames_list_, True)

# This separates out any tests for the entire module that would affect
# the functioning of the other tests.
class TestTVTKModule(unittest.TestCase):
    def test_all_instantiable(self):
        """Test if all the TVTK classes are instantiable."""
        # This is a comprehensive test that instantiates every single
        # non-abstract tvtk class.  This takes a while.
        ok = True
        ignore = []
        if vtk.vtkVersion.GetVTKMajorVersion() >= 5 and \
            vtk.vtkVersion.GetVTKMinorVersion() == 8:
                ignore = ['vtkAxesTransformRepresentation']
        # Turn off VTK warnings.
        vtk.vtkObject.GlobalWarningDisplayOff()
        names = [name for name in dir(vtk) \
                 if name.startswith('vtk') and \
                 not name.startswith('vtkQt')]
        for name in names:
            if name in ignore:
                continue
            klass = getattr(vtk, name)
            if hasattr(klass, '__bases__') \
                    and not issubclass(klass, object):
                try:
                    obj = klass()
                except (TypeError, NotImplementedError):
                    # These classes are abstract and can't/shouldn't
                    # be instantiated.
                    pass
                else:
                    t_name = get_tvtk_name(name)
                    skip = ['ObjectBase']
                    if t_name not in skip:
                        k = getattr(tvtk, t_name)
                        try:
                            obj = k()
                        except TraitError, msg:
                            print "class:", t_name, msg
                            ok = False
        # Now clear out the cache so other tests can run.
        tvtk_helper._cache.clear()
        # Turn on warnings.
        vtk.vtkObject.GlobalWarningDisplayOn()
        # Now raise an error if things were not OK.
        if not ok:
            raise TraitError, \
                  "Errors occured during this test, see printed messages."


if __name__ == "__main__":
    unittest.main()
