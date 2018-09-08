"""Tests for tvtk_base.py.  These only test the basic functionality of
the code in tvtk_base.  More tests for TVTK objects should be in
test_tvtk.py.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2018, Enthought, Inc.
# License: BSD Style.

import unittest
import pickle
import weakref
import vtk
import gc
import imp

from traits import api as traits
from tvtk import tvtk_base
from tvtk.common import get_tvtk_name, camel2enthought


# An elementary class based on vtkProperty that is used only for
# testing.
class Prop(tvtk_base.TVTKBase):
    def __init__(self, obj=None, update=1, **traits):
        tvtk_base.TVTKBase.__init__(
            self, vtk.vtkProperty, obj, update, **traits
        )

    edge_visibility = tvtk_base.false_bool_trait

    def _edge_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeVisibility, self.edge_visibility_)

    representation = traits.Trait(
        'surface',
        tvtk_base.TraitRevPrefixMap(
            {'points': 0, 'wireframe': 1, 'surface': 2})
    )

    def _representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentation, self.representation_)

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0))

    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    specular_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0))

    def _specular_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecularColor,
                        self.specular_color, 1)

    diffuse_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0))

    def _diffuse_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuseColor,
                        self.diffuse_color, 1)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0))

    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color)

    _updateable_traits_ = (('edge_visibility', 'GetEdgeVisibility'),
                           ('opacity', 'GetOpacity'),
                           ('specular_color', 'GetSpecularColor'),
                           ('color', 'GetColor'),
                           ('diffuse_color', 'GetDiffuseColor'),
                           ('representation', 'GetRepresentation'))


class TestTVTKBase(unittest.TestCase):
    def test_tvtk_name(self):
        """Test VTK to TVTK class name conversion."""
        v_name = ['vtkFooBar', 'vtkXMLDataReader',
                  'vtk3DSReader', 'vtk2000Bug']
        t_name = ['FooBar', 'XMLDataReader',
                  'ThreeDSReader', 'Two000Bug']
        for i, vn in enumerate(v_name):
            tn = get_tvtk_name(vn)
            self.assertEqual(tn, t_name[i])

        num = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
               'Six', 'Seven', 'Eight', 'Nine']
        for i in range(10):
            vn = 'vtk%dA' % i
            tn = get_tvtk_name(vn)
            self.assertEqual(tn, '%sA' % num[i])

    def test_camel2enthought(self):
        """Test CamelCase to Enthought style name conversion."""
        v_name = ['GetFooBar', 'GetOBBTree', 'XMLDataReader',
                  'GetFooXML', 'HTMLIsSGML', '_SetMe', '_XYZTest',
                  'Actor2D', 'Actor3D', 'Actor6D', 'PLOT3DReader',
                  'Actor61Dimension', 'GL2PSExporter',
                  'Volume16Reader']
        t_name = ['get_foo_bar', 'get_obb_tree', 'xml_data_reader',
                  'get_foo_xml', 'html_is_sgml', '_set_me',
                  '_xyz_test', 'actor2d', 'actor3d', 'actor6_d',
                  'plot3d_reader', 'actor61_dimension',
                  'gl2ps_exporter', 'volume16_reader']
        for i, vn in enumerate(v_name):
            tn = camel2enthought(vn)
            self.assertEqual(tn, t_name[i])

    def test_do_change(self):
        """Test if VTK object changes when trait is changed."""
        p = Prop()
        p.edge_visibility = not p.edge_visibility
        p.representation = 'p'
        p.opacity = 0.5
        p.color = (0, 1, 0)
        p.diffuse_color = (1, 1, 1)
        p.specular_color = (1, 1, 0)
        for t, g in p._updateable_traits_:
            val = getattr(p._vtk_obj, g)()
            if t == 'representation':
                self.assertEqual(val, getattr(p, t + '_'))
            else:
                self.assertEqual(val, getattr(p, t))

    def test_wrap_call_is_graceful_on_failure(self):
        # Given
        p = Prop()

        # When
        try:
            # Make a mistake
            p._wrap_call(p._vtk_obj.SetLineWidth, 'a')
        except TypeError:
            pass

        # Then
        # The _in_set should be reset to zero.
        self.assertEqual(p._in_set, 0)

    def test_auto_update(self):
        """Test trait updation when the VTK object changes."""
        p = Prop()
        obj = p._vtk_obj
        obj.SetEdgeVisibility(1)
        self.assertEqual(p.edge_visibility, 1)

        obj.SetOpacity(0.5)
        self.assertEqual(p.opacity, 0.5)

        obj.SetRepresentationToPoints()
        self.assertEqual(p.representation, 'points')

        val = (1.0, 1.0, 0.0)
        obj.SetColor(val)
        self.assertEqual(p.color, val)

        val = (1.0, 0.0, 0.0)
        obj.SetDiffuseColor(val)
        self.assertEqual(p.diffuse_color, val)

        val = (0.0, 1.0, 0.0)
        obj.SetSpecularColor(val)
        self.assertEqual(p.specular_color, val)

    def test_setup_teardown_observers(self):
        """If setup_observers and teardown_observers work correctly."""
        p = Prop()
        # Turn off the observers.
        p.teardown_observers()
        obj = p._vtk_obj
        obj.SetEdgeVisibility(1)
        self.assertEqual(p.edge_visibility, 0)

        obj.SetOpacity(0.5)
        self.assertEqual(p.opacity, 1.0)

        obj.SetRepresentationToPoints()
        self.assertEqual(p.representation, 'surface')

        # Setup the observers again.
        p.update_traits()
        p.setup_observers()

        self.assertEqual(p.edge_visibility, 1)
        self.assertEqual(p.opacity, 0.5)
        self.assertEqual(p.representation, 'points')

        obj.SetEdgeVisibility(0)
        self.assertEqual(p.edge_visibility, 0)

        obj.SetOpacity(1.0)
        self.assertEqual(p.opacity, 1.0)

        obj.SetRepresentationToSurface()
        self.assertEqual(p.representation, 'surface')

    def test_pickle(self):
        """Test if pickling works."""
        p = Prop()
        p.edge_visibility = 1
        p.representation = 'p'
        p.opacity = 0.5
        p.color = (0, 1, 0)
        p.diffuse_color = (0, 1, 1)
        p.specular_color = (1, 1, 0)

        s = pickle.dumps(p)
        del p

        p = pickle.loads(s)

        self.assertEqual(p.edge_visibility, 1)
        self.assertEqual(p.opacity, 0.5)
        self.assertEqual(p.representation, 'points')
        val = (0.0, 1.0, 1.0)
        self.assertEqual(p.color, val)
        val = (0.0, 1.0, 1.0)
        self.assertEqual(p.diffuse_color, val)
        val = (1.0, 1.0, 0.0)
        self.assertEqual(p.specular_color, val)

        # test if pickling also works on an existing object.
        d = p.__getstate__()
        del p
        p = Prop()
        addr = p._vtk_obj.__this__
        p.__setstate__(d)
        # Make sure its the same object.
        self.assertEqual(addr, p._vtk_obj.__this__)

        self.assertEqual(p.edge_visibility, 1)
        self.assertEqual(p.opacity, 0.5)
        self.assertEqual(p.representation, 'points')
        val = (0.0, 1.0, 1.0)
        self.assertEqual(p.color, val)

    def test_rev_prefix_map(self):
        """Test the reverse prefix map trait we use."""
        p = Prop()
        p.representation = 'p'
        p.representation = 'wire'
        p.representation = 'points'
        p.representation = 2
        self.assertEqual(p.representation, 'surface')
        self.assertRaises(traits.TraitError, setattr, p,
                          'representation', 'points1')
        self.assertRaises(traits.TraitError, setattr, p,
                          'representation', 'POINTS')

    def test_deref_vtk(self):
        """Test the `deref_vtk` function."""
        p = Prop()
        o = tvtk_base.deref_vtk(p)
        self.assertEqual(o.IsA('vtkProperty'), True)
        o1 = tvtk_base.deref_vtk(o)
        self.assertEqual(o1.IsA('vtkProperty'), True)

        o = tvtk_base.deref_vtk(self)
        self.assertEqual(o.__class__.__name__, 'TestTVTKBase')

    def test_obj_del(self):
        """Test object deletion and reference cycles."""
        p = Prop()
        p.representation = 0
        ref = weakref.ref(p)
        del p
        self.assertEqual(ref(), None)

    def test_global_disable_update(self):
        # Given
        p = Prop()
        vp = tvtk_base.deref_vtk(p)

        # When
        with tvtk_base.global_disable_update():
            vp.SetOpacity(0.5)
            vp.Modified()

        # Then
        self.assertEqual(p.opacity, 1.0)

        # When
        vp.SetOpacity(0.4)

        # Then
        self.assertEqual(p.opacity, 0.4)

    def test_strict_traits(self):
        """Test if TVTK objects use strict traits."""
        p = Prop()
        self.assertRaises(traits.TraitError, setattr, p, 'foo', 1)
        self.assertRaises(traits.TraitError, setattr, p, '_foo', 1)
        self.assertRaises(traits.TraitError, setattr, p, '__foo', 1)

    def test_init_traits(self):
        """Test if the objects traits can be set in __init__."""
        p = Prop(opacity=0.1, color=(1, 0, 0), representation='p')
        self.assertEqual(p.opacity, 0.1)
        self.assertEqual(p.color, (1.0, 0.0, 0.0))
        self.assertEqual(p.representation, 'points')

        # Test case where the object traits are wrong.
        self.assertRaises(traits.TraitError, Prop, foo='bar')

    def test_zz_object_cache(self):
        """Test if object cache works correctly."""
        # HACK!  The zz in the method name ensures that this is run
        # last.  The reloading messes up some of the other tests
        # because the Prop classes base class is different.

        l1 = len(tvtk_base._object_cache)
        p = Prop()
        addr = p._vtk_obj.__this__
        self.assertEqual(l1 + 1, len(tvtk_base._object_cache))
        self.assertEqual(p, tvtk_base._object_cache.get(addr))

        del p
        gc.collect()  # Force collection.
        self.assertEqual(l1, len(tvtk_base._object_cache))
        self.assertEqual(addr in tvtk_base._object_cache, False)

        # Check reload-safety.
        p = Prop()
        l1 = len(tvtk_base._object_cache)
        imp.reload(tvtk_base)
        self.assertEqual(l1, len(tvtk_base._object_cache))

    # Reloading causes havoc with nosetests based tests so we skip in
    # that case.  Unittest will see the test just fine.
    test_zz_object_cache.__test__ = False


if __name__ == "__main__":
    unittest.main()
