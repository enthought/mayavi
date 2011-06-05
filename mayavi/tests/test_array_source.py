"""
Tests for the ArraySource class.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

import unittest
import pickle
import numpy

# Enthought library imports.
from traits.api import TraitError
from mayavi.sources.array_source import ArraySource
from mayavi.modules.outline import Outline
from mayavi.modules.surface import Surface


class TestArraySource(unittest.TestCase):
    def setUp(self):
        """Initial setting up of test fixture, automatically called by TestCase before any other test method is invoked"""
        d = ArraySource()
        self.data = d

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase after the test methods have been invoked"""
        return

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

    def test_input_validation(self):
        """Tests if only the correct forms of input arrays are supported."""
        obj = self.data
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

    def test_2d_data(self):
        """Generic tests for 2D data arrays."""
        d = self.data
        sc, vec = self.make_2d_data()
        d.origin = (-1, -1, 0)
        d.scalar_data = sc
        d.vector_data = vec
        d.start()  # Start the object so it flushes the pipeline etc.

        # Create an outline for the data.
        o = Outline()
        d.add_child(o)
        o.start()
        self.assertEqual(tuple(o.actor.actor.bounds),
                         (-1., 0., -1., 0., 0., 0.))
        # Create a surface module.
        surf = Surface()
        d.add_child(surf)
        self.assertEqual(surf.running, True)

        tps = numpy.transpose
        expect = [tps(sc), tps(vec, (1, 0, 2))]
        sc1 = surf.actor.mapper.input.point_data.scalars.to_array()
        self.assertEqual(numpy.allclose(sc1.flatten(),
                         expect[0].flatten()), True)
        vec1 = surf.actor.mapper.input.point_data.vectors.to_array()
        self.assertEqual(numpy.allclose(vec1.flatten(),
                         expect[1].flatten()), True)

    def test_3d_data(self):
        "Test for 3D data arrays."
        # Add a 3D data source
        d = self.data
        sc, vec = self.make_3d_data()
        d.scalar_data = sc
        d.vector_data = vec
        d.start()  # Start the object so it flushes the pipeline etc.

        # Create an outline for the data.
        o = Outline()
        d.add_child(o)
        o.start()
        self.assertEqual(tuple(o.actor.actor.bounds),
                         (0, 1., 0., 1., 0., 1.))
        # Create a surface module.
        surf = Surface()
        d.add_child(surf)
        self.assertEqual(surf.running, True)

        tps = numpy.transpose
        expect = [tps(sc),  tps(vec, (2,1,0,3))]
        sc2 = surf.actor.mapper.input.point_data.scalars.to_array()
        self.assertEqual(numpy.allclose(sc2.flatten(),
                         expect[0].flatten()), True)
        vec2 = surf.actor.mapper.input.point_data.vectors.to_array()
        self.assertEqual(numpy.allclose(vec2.flatten(),
                         expect[1].flatten()), True)

    def test_pickle(self):
        "Test if pickling works."

        # Test if saving a visualization and restoring it works.
        d = self.data
        sc, vec = self.make_3d_data()
        d.scalar_data = sc
        d.vector_data = vec
        d.spacing = [1, 2, 3]
        d.origin  = [4, 5, 6]
        d.start()  # Start the object so it flushes the pipeline etc.

        # Create an outline for the data.
        o = Outline()
        d.add_child(o)
        o.start()
        # Create a surface module.
        surf = Surface()
        d.add_child(surf)

        data = pickle.dumps(d)
        del d, surf, o
        d = pickle.loads(data)
        # We must explicitly start the object.
        d.start()
        mm = d.children[0]
        o, surf = mm.children

        # Test the unpciked state.
        self.assertEqual(tuple(o.actor.actor.bounds),
                         (4., 5., 5., 7., 6., 9.))
        self.assertEqual(surf.running, True)
        self.assertEqual(o.running, True)
        self.assertEqual(d.running, True)
        self.assertEqual(numpy.allclose(d.spacing, [1, 2, 3]), True)
        self.assertEqual(numpy.allclose(d.origin,  [4, 5, 6]), True)

        tps = numpy.transpose
        expect = [tps(sc),  tps(vec, (2,1,0,3))]
        sc2 = surf.actor.mapper.input.point_data.scalars.to_array()
        self.assertEqual(numpy.allclose(sc2.flatten(),
                         expect[0].flatten()), True)
        vec2 = surf.actor.mapper.input.point_data.vectors.to_array()
        self.assertEqual(numpy.allclose(vec2.flatten(),
                         expect[1].flatten()), True)



if __name__ == '__main__':
    unittest.main()
