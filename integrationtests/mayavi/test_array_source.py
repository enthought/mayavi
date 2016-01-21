"""Tests for the ArraySource data source for MayaVi.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
from io import BytesIO
import copy
import numpy

# Enthought library imports.
from traits.api import TraitError

# Local imports.
from common import TestCase


class TestArraySource(TestCase):
    def check_input_validation(self, obj):
        """Tests if only the correct forms of input arrays are supported."""
        # These should work.
        obj.scalar_data = numpy.zeros((2,2), 'd')
        obj.scalar_data = numpy.zeros((2,2,2), 'd')
        obj.scalar_data = None
        obj.vector_data = numpy.zeros((2,2,3), 'd')
        obj.vector_data = numpy.zeros((2,2,2,3), 'd')
        obj.vector_data = None

        # These should not.
        self.assertRaises(TraitError, setattr, obj, 'scalar_data', [1,2,3])
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((2,2,2,3), 'd'))
        obj.scalar_data = None
        self.assertRaises(TraitError, setattr, obj, 'vector_data', [[1,2,3]])
        self.assertRaises(TraitError, setattr, obj, 'vector_data',
                          numpy.zeros((2,2,2,1), 'd'))
        obj.vector_data = None

        obj.scalar_data = numpy.zeros((2,2), 'd')
        self.assertRaises(TraitError, setattr, obj, 'vector_data',
                          numpy.zeros((4,4,3), 'd'))
        obj.vector_data = numpy.zeros((2,2,3), 'd')
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((4,3), 'i'))
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((2,2,2), 'i'))
        obj.scalar_data = numpy.zeros((2,2), 'f')

        # Clean up the object so it can be used for further testing.
        obj.scalar_data = obj.vector_data = None

    def make_2d_data(self):
        s = numpy.array([[0, 1],[2, 3]], 'd')
        v = numpy.array([[[1,1,1], [1,0,0]],[[0,1,0], [0,0,1]]], 'd')
        tps = numpy.transpose
        s, v = tps(s), tps(v, (1, 0, 2))
        return s, v

    def make_3d_data(self):
        s = numpy.array([[[0, 1],[2, 3]],
                           [[4, 5],[6, 7]]], 'd')
        v = numpy.array([[[[0,0,0],
                             [1,0,0]],
                            [[0,1,0],
                             [1,1,0]]],
                           [[[0,0,1],
                             [1,0,1]],
                            [[0,1,1],
                             [1,1,1]]]], 'd')
        tps = numpy.transpose
        s, v = tps(s), tps(v, (2, 1, 0, 3))
        return s, v

    def check(self):
        script = self.script
        s = script.engine.current_scene
        d1, d2 = s.children
        s1, v1 = d1.children[0].children[1:]
        expect = list(self.make_2d_data())
        tps = numpy.transpose
        expect[0] = tps(expect[0])
        expect[1] = tps(expect[1], (1, 0, 2))
        sc1 = s1.actor.mapper.input.point_data.scalars.to_array()
        assert numpy.allclose(sc1.flatten(), expect[0].flatten())
        vec1 = s1.actor.mapper.input.point_data.vectors.to_array()
        assert numpy.allclose(vec1.flatten(), expect[1].flatten())

        s2, v2 = d2.children[0].children[1:]
        expect = list(self.make_3d_data())
        tps = numpy.transpose
        expect[0] = tps(expect[0])
        expect[1] = tps(expect[1], (2, 1, 0, 3))
        sc2 = s2.actor.mapper.input.point_data.scalars.to_array()
        assert numpy.allclose(sc2.flatten(), expect[0].flatten())
        vec2 = s2.actor.mapper.input.point_data.vectors.to_array()
        assert numpy.allclose(vec2.flatten(), expect[1].flatten())

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        script = self.script
        from mayavi.sources.array_source import ArraySource
        from mayavi.modules.outline import Outline
        from mayavi.modules.surface import Surface
        from mayavi.modules.vectors import Vectors

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        d = ArraySource()
        self.check_input_validation(d)
        sc, vec = self.make_2d_data()
        d.origin = (-1, -1, 0)
        d.scalar_data = sc
        d.vector_data = vec

        script.add_source(d)

        # Create an outline for the data.
        o = Outline()
        script.add_module(o)
        # View the data.
        s = Surface()
        script.add_module(s)
        v = Vectors()
        script.add_module(v)

        # Add a 3D data source
        d = ArraySource()
        sc, vec = self.make_3d_data()
        d.scalar_data = sc
        d.vector_data = vec
        script.add_source(d)
        # Create an outline for the data.
        o = Outline()
        script.add_module(o)
        # View a slice.
        s = Surface()
        script.add_module(s)
        v = Vectors()
        script.add_module(v)

        # Set the scene to a suitable view.
        s.scene.z_plus_view()
        c = s.scene.camera
        c.azimuth(-30)
        c.elevation(30)

        self.check()

        ############################################################
        # Test if saving a visualization and restoring it works.

        bg = s.scene.background
        # Save visualization.
        f = BytesIO()
        f.name = abspath('test.mv2') # We simulate a file.
        script.save_visualization(f)
        f.seek(0) # So we can read this saved data.

        # Remove existing scene.
        engine = script.engine
        engine.close_scene(s)

        # Load visualization
        script.load_visualization(f)
        s = engine.current_scene

        # Set the scene to a suitable view.
        s.scene.z_plus_view()
        c = s.scene.camera
        c.azimuth(-30)
        c.elevation(30)
        s.scene.background = bg

        self.check()

        ############################################################
        # Test if the MayaVi2 visualization can be deepcopied.

        # Pop the source object.
        sources = s.children
        s.children = []
        # Add it back to see if that works without error.
        s.children.extend(sources)

        s.scene.reset_zoom()

        self.check()

        # Now deepcopy the source and replace the existing one with
        # the copy.  This basically simulates cutting/copying the
        # object from the UI via the right-click menu on the tree
        # view, and pasting the copy back.
        sources1 = copy.deepcopy(sources)
        s.children[:] = sources
        s.scene.reset_zoom()
        self.check()

        # If we have come this far, we are golden!


if __name__ == "__main__":
    t = TestArraySource()
    t.test()
