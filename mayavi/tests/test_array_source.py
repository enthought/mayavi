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
        d = ArraySource()
        self.data = d

    def make_2d_data(self):
        s = numpy.array([[0, 1], [2, 3]], 'd')
        v = numpy.array([[[1, 1, 1], [1, 0, 0]], [[0, 1, 0], [0, 0, 1]]], 'd')
        tps = numpy.transpose
        s, v = tps(s), tps(v, (1, 0, 2))
        return s, v

    def make_3d_data(self):
        s = numpy.array([[[0, 1], [2, 3]],
                         [[4, 5], [6, 7]]], 'd')
        v = numpy.array([[[[0, 0, 0],
                           [1, 0, 0]],
                          [[0, 1, 0],
                           [1, 1, 0]]],
                         [[[0, 0, 1],
                           [1, 0, 1]],
                          [[0, 1, 1],
                           [1, 1, 1]]]], 'd')
        tps = numpy.transpose
        s, v = tps(s), tps(v, (2, 1, 0, 3))
        return s, v

    def test_input_validation(self):
        """Tests if only the correct forms of input arrays are supported."""
        obj = self.data
        # These should work.
        obj.scalar_data = numpy.zeros((2, 2), 'd')
        obj.scalar_data = numpy.zeros((2, 2, 2), 'd')
        obj.scalar_data = None
        obj.vector_data = numpy.zeros((2, 2, 3), 'd')
        obj.vector_data = numpy.zeros((2, 2, 2, 3), 'd')
        obj.vector_data = None

        # These should not.
        self.assertRaises(TraitError, setattr, obj, 'scalar_data', [1, 2, 3])
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((2, 2, 2, 3), 'd'))
        obj.scalar_data = None
        self.assertRaises(TraitError, setattr, obj, 'vector_data', [[1, 2, 3]])
        self.assertRaises(TraitError, setattr, obj, 'vector_data',
                          numpy.zeros((2, 2, 2, 1), 'd'))
        obj.vector_data = None

        obj.scalar_data = numpy.zeros((2, 2), 'd')
        self.assertRaises(TraitError, setattr, obj, 'vector_data',
                          numpy.zeros((4, 4, 3), 'd'))
        obj.vector_data = numpy.zeros((2, 2, 3), 'd')
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((4, 3), 'i'))
        self.assertRaises(TraitError, setattr, obj, 'scalar_data',
                          numpy.zeros((2, 2, 2), 'i'))
        obj.scalar_data = numpy.zeros((2, 2), 'f')

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
        expect = [tps(sc),  tps(vec, (2, 1, 0, 3))]
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
        d.origin = [4, 5, 6]
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
        expect = [tps(sc),  tps(vec, (2, 1, 0, 3))]
        sc2 = surf.actor.mapper.input.point_data.scalars.to_array()
        self.assertEqual(numpy.allclose(sc2.flatten(),
                         expect[0].flatten()), True)
        vec2 = surf.actor.mapper.input.point_data.vectors.to_array()
        self.assertEqual(numpy.allclose(vec2.flatten(),
                         expect[1].flatten()), True)


class TestArraySourceAttributes(unittest.TestCase):
    def setUp(self):
        s1 = numpy.ones((2, 2))
        src = ArraySource(scalar_data=s1, scalar_name='s1')
        self.src = src

    def test_add_attribute_works_for_point_data(self):
        # Given
        src = self.src
        s1 = src.scalar_data

        # When
        s2 = s1.ravel() + 1.0
        src.add_attribute(s2, 's2')
        v1 = numpy.ones((4, 3))
        src.add_attribute(v1, 'v1')
        t1 = numpy.ones((4, 9))
        src.add_attribute(t1, 't1')

        # Then
        self.assertTrue(
            numpy.allclose(
                src.image_data.point_data.get_array('s2').to_array(), s2
            )
        )
        self.assertTrue(
            numpy.allclose(
                src.image_data.point_data.get_array('v1').to_array(), v1
            )
        )
        self.assertTrue(
            numpy.allclose(
                src.image_data.point_data.get_array('t1').to_array(), t1)
        )

    def test_add_attribute_works_for_cell_data(self):
        # Given
        src = self.src
        s1 = src.scalar_data

        # When
        s2 = s1.ravel() + 1.0
        src.add_attribute(s2, 's2', category='cell')
        v1 = numpy.ones((4, 3))
        src.add_attribute(v1, 'v1', category='cell')
        t1 = numpy.ones((4, 9))
        src.add_attribute(t1, 't1', category='cell')

        # Then
        self.assertTrue(
            numpy.allclose(
                src.image_data.cell_data.get_array('s2').to_array(), s2
            )
        )
        self.assertTrue(
            numpy.allclose(
                src.image_data.cell_data.get_array('v1').to_array(), v1
            )
        )
        self.assertTrue(
            numpy.allclose(
                src.image_data.cell_data.get_array('t1').to_array(), t1
            )
        )

    def test_add_attribute_raises_errors(self):
        # Given
        src = self.src

        # When/Then
        data = numpy.ones((4, 3, 3))
        self.assertRaises(AssertionError, src.add_attribute, data, 's2')

        data = numpy.ones((4, 5))
        self.assertRaises(AssertionError, src.add_attribute, data, 's2')

    def test_remove_attribute(self):
        # Given
        src = self.src
        s1 = src.scalar_data

        # When
        s2 = s1.ravel() + 1.0
        src.add_attribute(s2, 's2')
        src.remove_attribute('s2')

        # Then
        self.assertEqual(src.image_data.point_data.get_array('s2'), None)
        self.assertTrue(
            numpy.allclose(
                src.image_data.point_data.get_array('s1').to_array(),
                s1.ravel()
            )
        )

    def test_rename_attribute(self):
        # Given
        src = self.src
        s1 = src.scalar_data
        s2 = s1.ravel() + 1.0
        src.add_attribute(s2, 's2')

        # When
        src.rename_attribute('s2', 's3')

        # Then
        self.assertTrue(
            numpy.all(src.image_data.point_data.get_array('s3') == s2)
        )
        self.assertEqual(src.image_data.point_data.get_array('s2'), None)


if __name__ == '__main__':
    unittest.main()
