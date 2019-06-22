"""
Test for MlabSource and its subclasses.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest
import numpy as np
from mock import patch

from tvtk.api import tvtk
from mayavi.tools import sources
from mayavi.sources.vtk_data_source import VTKDataSource


###############################################################################
# `TestMGlyphSource`
###############################################################################
class TestMGlyphSource(unittest.TestCase):
    def setUp(self):
        self.x = x = np.ones(10, float)
        self.y = y = np.ones(10, float)*2.0
        self.z = z = np.linspace(0, 10, 10)
        self.v = v = np.ones((10, 3), float)*10.0
        self.s = s = np.ones(10, float)
        src = sources.MGlyphSource()
        src.reset(x=x, y=y, z=z, u=v[:, 0], v=v[:, 1], w=v[:, 2], scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.v, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, v, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.points[:, 0].ravel() == x.ravel()),
                         True)
        self.assertEqual(np.alltrue(src.points[:, 1].ravel() == y.ravel()),
                         True)
        self.assertEqual(np.alltrue(src.points[:, 2].ravel() == z.ravel()),
                         True)
        # Check the vectors and scalars.
        self.assertEqual(np.alltrue(src.vectors == v), True)
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, v, s, src = self.get_data()
        # Check if the dataset is setup right.
        pts = src.dataset.points.to_array()
        self.assertEqual(np.alltrue(pts[:, 0].ravel() == x.ravel()), True)
        self.assertEqual(np.alltrue(pts[:, 1].ravel() == y.ravel()), True)
        self.assertEqual(np.alltrue(pts[:, 2].ravel() == z.ravel()), True)
        vec = src.dataset.point_data.vectors.to_array()
        sc = src.dataset.point_data.scalars.to_array()
        self.assertEqual(np.alltrue(vec == v), True)
        self.assertEqual(np.alltrue(sc == s.ravel()), True)

    def test_reset_with_same_size_data(self):
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        v *= 0.1
        src.reset(x=x, u=v[:, 0], v=v[:, 1], w=v[:, 2], scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_reset_with_resized_data(self):
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()
        # Call reset again with just a few things changed to see if it
        # works correctly.

        self.x = x = np.ones(20, float)*30.0
        self.y = y = np.ones(20, float)*30.0
        self.z = z = np.ones(20, float)*30.0
        self.s = s = np.ones(20, float)
        self.v = v = np.ones((20, 3), float)*30.0

        src.reset(x=x, y=y, z=z, u=v[:, 0], v=v[:, 1], w=v[:, 2],
                  scalars=s)
        self.check_traits()
        self.check_dataset()

    def test_reset_strange_shape(self):
        " Test the reset method when the inputs are 2-d arrays."

        x, y, z, v, s, src = self.get_data()
        self.x = x = np.reshape(x, (5, 2))
        self.y = y = np.reshape(y, (5, 2))
        self.z = z = np.reshape(z, (5, 2))
        u = np.reshape(v[:, 0], (5, 2))
        vv = np.reshape(v[:, 1], (5, 2))
        w = np.reshape(v[:, 2], (5, 2))
        self.s = s = np.reshape(s, (5, 2))
        src.reset(x=x, y=y, z=z, u=u, v=vv, w=w, scalars=s)
        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2
        y *= 2
        z *= 2
        v *= 2
        s *= 2
        src.x = x
        src.y = y
        src.z = z
        src.u = v[:, 0]
        src.v = v[:, 1]
        src.w = v[:, 2]
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_handlers_strange_shape(self):
        """Test if the various static handlers work correctly for strange shapes.
        """
        # Initialize with 2-d array data.
        x, y, z, v, s, src = self.get_data()
        x = np.reshape(x, (5, 2))
        y = np.reshape(y, (5, 2))
        z = np.reshape(z, (5, 2))
        u = np.reshape(v[:, 0], (5, 2))
        vv = np.reshape(v[:, 1], (5, 2))
        w = np.reshape(v[:, 2], (5, 2))
        s = np.reshape(s, (5, 2))
        src.reset(x=x, y=y, z=z, u=u, v=vv, w=w, scalars=s)

        # modify variables in src to check handlers
        self.x = src.x = 2*x
        self.y = src.y = 2*y
        self.z = src.z = 2*z
        src.u = 2*z
        src.v = 2*vv
        src.w = 2*w
        self.v[:, 0] = src.u.ravel()
        self.v[:, 1] = src.v.ravel()
        self.v[:, 2] = src.w.ravel()
        self.s = src.scalars = 2*s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2
        z *= 2
        s *= 2
        src.trait_set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()

    def test_strange_shape(self):
        " Test the MGlyphSource with strange shapes for the arguments "
        x, y, z, v, s, src = self.get_data()
        x = y = z = v = s = 0
        src.reset(x=x, y=y, z=z, u=v, v=v, w=v, scalars=None)
        src.reset(x=x, y=y, z=z, u=v, v=v, w=v, scalars=s)
        x = y = z = v = s = 1
        src.trait_set(x=x, y=y, z=z, u=v, v=v, w=v, scalars=None)
        src.trait_set(x=x, y=y, z=z, u=v, v=v, w=v, scalars=s)

    @patch('mayavi.tools.engine_manager.options.backend', 'test')
    def test_reset_changes_pipeline(self):
        # Given
        from mayavi import mlab
        x, y, z = np.random.random((3, 10))
        g = mlab.points3d(x, y, z, x*x + y*y + z*z)
        bounds = g.actor.actor.bounds

        # When
        x, y, z = np.random.random((3, 20))
        g.mlab_source.reset(x=x, y=y, z=z, scalars=x*x + y*y + z*z)

        # Then
        self.assertFalse(np.allclose(bounds, g.actor.actor.bounds))


class TestMVerticalSource(unittest.TestCase):
    def setUp(self):
        self.x = x = np.ones(10, float)
        self.y = y = np.ones(10, float)*2.0
        self.z = z = np.linspace(0, 10, 10)
        self.s = s = np.ones(10, float)
        src = sources.MVerticalGlyphSource()
        src.reset(x=x, y=y, z=z, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.points[:, 0].ravel() == x), True)
        self.assertEqual(np.alltrue(src.points[:, 1].ravel() == y), True)
        self.assertEqual(np.alltrue(src.points[:, 2].ravel() == z), True)
        # Check the vectors and scalars.
        self.assertEqual(np.alltrue(src.vectors[:, -1] == s), True)
        self.assertEqual(np.alltrue(src.vectors[:, :-1] == 1), True)
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, s, src = self.get_data()
        # Check if the dataset is setup right.
        pts = src.dataset.points.to_array()
        self.assertEqual(np.alltrue(pts[:, 0].ravel() == x), True)
        self.assertEqual(np.alltrue(pts[:, 1].ravel() == y), True)
        self.assertEqual(np.alltrue(pts[:, 2].ravel() == z), True)
        vec = src.dataset.point_data.vectors.to_array()
        sc = src.dataset.point_data.scalars.to_array()
        self.assertEqual(np.alltrue(vec[:, -1] == s), True)
        self.assertEqual(np.alltrue(vec[:, :-1] == 1), True)
        self.assertEqual(np.alltrue(sc == s), True)

    def test_reset(self):
        "Test the reset method."
        x, y, z, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        src.reset(x=x, scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_reset1(self):

        "Test the reset method."
        x, y, z, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()
        # Call reset again with just a few things changed to see if it
        # works correctly.

        self.x = x = np.ones(20, float)*30.0
        self.y = y = np.ones(20, float)*30.0
        self.z = z = np.ones(20, float)*30.0
        points = np.ones((20, 3), float)*30.0
        self.s = s = np.ones(20, float)

        src.reset(x=x, y=y, z=z, scalars=s, points=points)
        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        y *= 2
        z *= 2
        s *= 2
        src.x = x
        src.y = y
        src.z = z
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        z *= 2
        s *= 2
        src.trait_set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()


class TestMArraySource(unittest.TestCase):
    def setUp(self):
        x, y, z = np.ogrid[-10:10:11j, -10:10:12j, -10:10:20j]
        self.x, self.y, self.z = x, y, z
        dims = (x.shape[0], y.shape[1], z.shape[2])
        self.v = v = np.ones(dims + (3, ), float)
        v[..., 2] = 2
        v[..., 2] = 3
        self.s = s = np.ones(dims, float)
        src = sources.MArraySource()
        src.reset(
            x=x, y=y, z=z, u=v[..., 0], v=v[..., 1], w=v[..., 2], scalars=s
        )
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.v, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, v, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.x == x), True)
        self.assertEqual(np.alltrue(src.y == y), True)
        self.assertEqual(np.alltrue(src.z == z), True)
        # Check the vectors and scalars.
        self.assertEqual(np.alltrue(src.vectors == v), True)
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, v, s, src = self.get_data()
        # Check if the dataset is setup right.
        dx = x[1, 0, 0] - x[0, 0, 0]
        dy = y[0, 1, 0] - y[0, 0, 0]
        dz = z[0, 0, 1] - z[0, 0, 0]
        origin = [x.min(), y.min(), z.min()]
        spacing = [dx, dy, dz]
        dimensions = (x.shape[0], y.shape[1], z.shape[2])
        ds = src.dataset
        self.assertEqual(np.all(src.m_data.origin == origin), True)
        self.assertEqual(np.allclose(src.m_data.spacing, spacing), True)
        self.assertEqual(np.allclose(ds.dimensions, dimensions), True)

        vec = src.dataset.point_data.vectors.to_array()
        sc = src.dataset.point_data.scalars.to_array()
        v1 = v.transpose((2, 0, 1, 3))
        self.assertEqual(np.alltrue(vec.ravel() == v1.ravel()), True)
        s1 = s.transpose()
        self.assertEqual(np.alltrue(sc.ravel() == s1.ravel()), True)

    def test_reset(self):
        "Test the reset method."
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        v *= 0.1
        src.reset(x=x, u=v[..., 0], v=v[..., 1], w=v[..., 2], scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_reset1(self):
        "Test the reset method."
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()
        # Call reset again with just a few things changed to see if it
        # works correctly.

        x, y, z = np.ogrid[-10:10:11j, -10:10:12j, -10:10:20j]
        self.x, self.y, self.z = x, y, z

        dims = (x.shape[0], y.shape[1], z.shape[2])
        self.v = v = np.ones(dims + (3, ), float)
        v[..., 2] = 2
        v[..., 2] = 3
        self.s = s = np.ones(dims, float)
        src = sources.MArraySource()
        src.reset(
            x=x,
            y=y,
            z=z,
            u=v[..., 0],
            v=v[..., 1],
            w=v[..., 2],
            scalars=s,
            vectors=v
        )
        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2
        y *= 2
        z *= 2
        v *= 2
        s *= 2
        src.x = x
        src.y = y
        src.z = z
        src.u = v[..., 0]
        src.v = v[..., 1]
        src.w = v[..., 2]
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2
        z *= 2
        s *= 2
        src.trait_set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()


class TestMLineSource(unittest.TestCase):
    def setUp(self):
        self.x = x = np.ones(10, float)
        self.y = y = np.ones(10, float) * 2.0
        self.z = z = np.linspace(0, 10, 10)
        self.s = s = np.ones(10, float)
        src = sources.MLineSource()
        src.reset(x=x, y=y, z=z, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.points[:, 0].ravel() == x), True)
        self.assertEqual(np.alltrue(src.points[:, 1].ravel() == y), True)
        self.assertEqual(np.alltrue(src.points[:, 2].ravel() == z), True)
        # Check the scalars.
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, s, src = self.get_data()
        # Check if the dataset is setup right.
        pts = src.dataset.points.to_array()
        self.assertEqual(np.alltrue(pts[:, 0].ravel() == x), True)
        self.assertEqual(np.alltrue(pts[:, 1].ravel() == y), True)
        self.assertEqual(np.alltrue(pts[:, 2].ravel() == z), True)
        sc = src.dataset.point_data.scalars.to_array()
        self.assertEqual(np.alltrue(sc == s), True)

    def test_reset(self):
        "Test the reset method."
        x, y, z, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        src.reset(x=x, scalars=s)

        self.check_traits()
        self.check_dataset()

        y *= 6
        x *= 4
        src.reset(x=x, y=y)

        self.check_traits()
        self.check_dataset()

        s *= 4.5
        y /= 4
        src.reset(y=y, s=s)

        self.check_traits()
        self.check_dataset()

    def test_reset1(self):

        "Test the reset method."
        x, y, z, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()
        # Call reset again with just a few things changed to see if it
        # works correctly.

        self.x = x = np.ones(20, float)*30.0
        self.y = y = np.ones(20, float)*30.0
        self.z = z = np.ones(20, float)*30.0
        points = np.ones((20, 3), float)*30.0
        self.s = s = np.ones(20, float)
        src.reset(x=x, y=y, z=z, scalars=s, points=points)
        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        y *= 2
        z *= 2
        s *= 2
        src.x = x
        src.y = y
        src.z = z
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        z *= 2
        s *= 2
        src.trait_set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()

        y *= 2
        s *= 2
        src.trait_set(y=y, scalars=s)
        self.check_traits()
        self.check_dataset()

    @patch('mayavi.tools.engine_manager.options.backend', 'test')
    def test_reset_changes_pipeline(self):
        # Given
        from mayavi import mlab
        x = np.linspace(0, 1, 10)
        lines = mlab.plot3d(x, x, x, x)
        bounds = lines.actor.actor.bounds

        # When
        x = np.linspace(0, 2, 20)
        lines.mlab_source.reset(x=x, y=x, z=x, scalars=x)

        # Then
        self.assertFalse(np.allclose(bounds, lines.actor.actor.bounds))

    def test_set_without_scalars_works(self):
        # Given
        x, y, z, s, src = self.get_data()
        src = sources.MLineSource()
        src.reset(x=x, y=y, z=z)

        # When
        src.m_data = VTKDataSource(data=src.dataset)
        src.set(y=y+1)

        # Then
        self.assertTrue(np.allclose(src.y, y + 1))

        # When
        src.reset(x=x, y=y+1, z=z+1)

        # Then
        self.assertTrue(np.allclose(src.y, y + 1))
        self.assertTrue(np.allclose(src.z, z + 1))

    def test_set_without_scalars_attribute_works(self):
        # Given
        class MySource(sources.MlabSource):
            x = sources.ArrayNumberOrNone

        src = MySource(x=1.0, dataset=tvtk.PolyData())
        src.m_data = VTKDataSource(data=src.dataset)

        # When
        src.update()

        # Then
        np.testing.assert_almost_equal(src.x, 1.0)


class TestMArray2DSource(unittest.TestCase):
    def setUp(self):
        x, y = np.mgrid[-10:10:11j, -10:10:12j]

        self.x, self.y = x, y
        dims = (x.shape[0], y.shape[1])
        self.s = s = np.ones(dims, float)
        src = sources.MArray2DSource()
        src.reset(x=x, y=y, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, s, src = self.get_data()

        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.x == x), True)
        self.assertEqual(np.alltrue(src.y == y), True)
        # Check the scalars.
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, s, src = self.get_data()
        # Check if the dataset is setup right.
        x = np.atleast_2d(x.squeeze().T)[0, :].squeeze()
        y = np.atleast_2d(y.squeeze())[0, :].squeeze()
        dx = x[1] - x[0]
        dy = y[1] - y[0]

        origin = [x.min(), y.min(), 0]
        spacing = [dx, dy, 1]
        ds = src.dataset
        self.assertEqual(np.all(ds.origin == origin), True)
        self.assertEqual(np.allclose(src.m_data.spacing, spacing), True)

        sc = src.dataset.point_data.scalars.to_array()
        s1 = s.transpose()
        self.assertEqual(np.alltrue(sc.ravel() == s1.ravel()), True)

    def test_reset(self):
        x, y, s, src = self.get_data()

        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        src.reset(x=x, y=y, scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, s, src = self.get_data()
        x *= 2
        y *= 2
        s *= 2
        src.x = x
        src.y = y
        src.scalars = s

        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, s, src = self.get_data()
        x *= 2
        s *= 2
        src.trait_set(x=x, scalars=s)

        self.check_traits()
        self.check_dataset()

        y *= 9
        s *= 2
        src.trait_set(y=y, scalars=s)
        self.check_traits()
        self.check_dataset()


class TestMGridSource(unittest.TestCase):
    def setUp(self):
        self.x = x = np.ones([10, 10], float)
        self.y = y = np.ones([10, 10], float) * 2.0
        self.z = z = np.ones([10, 10], float) * 3.0
        self.s = s = np.ones([10, 10], float)
        src = sources.MGridSource()
        src.reset(x=x, y=y, z=z, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, s, src = self.get_data()

        # Check if points are set correctly.
        self.assertEqual(
            np.alltrue(src.points[:, 0].ravel() == x.ravel()), True
        )
        self.assertEqual(
            np.alltrue(src.points[:, 1].ravel() == y.ravel()), True
        )
        self.assertEqual(
            np.alltrue(src.points[:, 2].ravel() == z.ravel()), True
        )
        # Check the  scalars.

        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, s, src = self.get_data()
        # Check if the dataset is setup right.

        pts = src.dataset.points.to_array()
        self.assertEqual(np.alltrue(pts[:, 0].ravel() == x.ravel()), True)
        self.assertEqual(np.alltrue(pts[:, 1].ravel() == y.ravel()), True)
        self.assertEqual(np.alltrue(pts[:, 2].ravel() == z.ravel()), True)
        sc = src.dataset.point_data.scalars.to_array()
        self.assertEqual(np.alltrue(sc == s.ravel()), True)

    def test_reset(self):
        "Test the reset method."

        x, y, z, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10

        src.reset(x=x, scalars=s)
        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        y *= 2
        z *= 2
        s *= 2
        src.x = x
        src.y = y
        src.z = z
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, s, src = self.get_data()
        x *= 2
        z *= 2
        s *= 2
        src.trait_set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()

    @patch('mayavi.tools.engine_manager.options.backend', 'test')
    def test_reset_changes_pipeline(self):
        # Given
        from mayavi import mlab
        s = slice(0, 1, 10j)
        x, y = np.mgrid[s, s]
        obj = mlab.mesh(x, y, x*y, scalars=x)
        bounds = obj.actor.actor.bounds

        # When
        s = slice(0, 5, 20j)
        x, y = np.mgrid[s, s]
        obj.mlab_source.reset(x=x, y=y, z=x*y, scalars=x)

        # Then
        self.assertFalse(np.allclose(bounds, obj.actor.actor.bounds))


class TestMArray2DSourceNoArgs(unittest.TestCase):
    """Special Test Case for MArray2DSource when both x and y are specified as
    None"""

    def setUp(self):

        x = None
        y = None

        self.x, self.y = x, y

        if x is not None and y is not None:
            dims = (x.shape[0], y.shape[1])
        else:
            dims = (10, 10)

        self.s = s = np.ones(dims, float)
        src = sources.MArray2DSource()
        src.reset(x=x, y=y, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, s, src = self.get_data()
        # Check if points are set correctly.

        if x is not None and y is not None:
            self.assertEqual(np.alltrue(src.x == x), True)
            self.assertEqual(np.alltrue(src.y == y), True)

        else:
            nx, ny = s.shape
            x1, y1 = np.mgrid[-nx/2.:nx/2, -ny/2.:ny/2]
            self.assertEqual(np.alltrue(src.x == x1), True)
            self.assertEqual(np.alltrue(src.y == y1), True)

        # Check the scalars.
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, s, src = self.get_data()
        # Check if the dataset is setup right.

        nx, ny = src.scalars.shape

        if x is None and y is None:
            x, y = np.mgrid[-nx/2.:nx/2, -ny/2.:ny/2]

        x = np.atleast_2d(x.squeeze().T)[0, :].squeeze()
        y = np.atleast_2d(y.squeeze())[0, :].squeeze()
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        origin = [x.min(), y.min(), 0]
        spacing = [dx, dy, 1]
        ds = src.dataset
        self.assertEqual(np.all(ds.origin == origin), True)
        self.assertEqual(np.allclose(ds.spacing, spacing), True)

        sc = src.dataset.point_data.scalars.to_array()
        s1 = s.transpose()
        self.assertEqual(np.alltrue(sc.ravel() == s1.ravel()), True)

    def test_reset(self):
        "Test the reset method."
        x, y, s, src = self.get_data()

        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.

        s *= 10
        src.reset(x=x, y=y, scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, s, src = self.get_data()
        s *= 2
        src.scalars = s

        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, s, src = self.get_data()
        s *= 2
        src.trait_set(x=x, y=y, scalars=s)

        self.check_traits()
        self.check_dataset()


class TestMTriangularMeshSource(unittest.TestCase):
    def setUp(self):
        x, y, z = np.array([0, 0, 0]), np.array([0, 0, 1]), np.array([0, 1, 1])
        s = np.array([0.1, 0.2, 0.3])
        self.x, self.y, self.z, self.s = x, y, z, s
        self.triangles = triangles = np.array([[0, 1, 2]])

        src = sources.MTriangularMeshSource()
        src.reset(x=x, y=y, z=z, triangles=triangles, scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.triangles, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, triangles, s, src = self.get_data()

        # Check if points are set correctly.
        self.assertEqual(np.alltrue(src.x == x), True)
        self.assertEqual(np.alltrue(src.y == y), True)
        self.assertEqual(np.alltrue(src.z == z), True)
        # Check the scalars.
        self.assertEqual(np.alltrue(src.scalars == s), True)

    def test_reset(self):
        "Test the reset method."

        x, y, z, triangles, s, src = self.get_data()
        self.check_traits()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5
        s *= 10
        src.reset(x=x, y=y, z=z, triangles=triangles, scalars=s)

        self.check_traits()

    def test_changed_size(self):
        """ Change the number of the points, and establish
            to new points, to check that we don't get errors with the
            dimensions of the scalars.
        """
        n = 100
        _, _, _, _, _, src = self.get_data()
        triangles = np.c_[np.arange(n - 3),
                          np.arange(n - 3) + 1, n - 1 - np.arange(n - 3)]
        x, y, z = np.random.random((3, n))
        src.reset(x=x, y=y, z=z, triangles=triangles)

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, triangles, s, src = self.get_data()
        x *= 2
        y *= 2
        s *= 2
        src.x = x
        src.y = y
        src.scalars = s
        src.triangles = triangles

        self.check_traits()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, triangles, s, src = self.get_data()
        x *= 2
        s *= 2
        src.trait_set(x=x, scalars=s)

        self.check_traits()

        y *= 9
        s *= 2
        src.trait_set(y=y, scalars=s)

        self.check_traits()

    @patch('mayavi.tools.engine_manager.options.backend', 'test')
    def test_reset_changes_pipeline(self):
        # Given
        from mayavi import mlab
        obj = mlab.triangular_mesh(
            self.x, self.y, self.z, self.triangles, scalars=self.s
        )
        bounds = obj.actor.actor.bounds

        # When
        n = 10
        x, y, z = np.random.random((3, n))
        triangles = np.c_[np.arange(n-3),
                          np.arange(n-3)+1,
                          n-1-np.arange(n-3)]

        obj.mlab_source.reset(x=x, y=y, z=z, triangles=triangles, scalars=z)

        # Then
        self.assertFalse(np.allclose(bounds, obj.actor.actor.bounds))


if __name__ == '__main__':
    unittest.main()
