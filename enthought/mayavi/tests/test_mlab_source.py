"""
Test for MlabSource and its subclasses.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest
import numpy as N

from enthought.mayavi.tools import sources

################################################################################
# `TestMGlyphSource`
################################################################################ 
class TestMGlyphSource(unittest.TestCase):
    def setUp(self):
        self.x = x = N.ones(10, float)
        self.y = y = N.ones(10, float)*2.0
        self.z = z = N.linspace(0, 10, 10)
        self.v = v = N.ones((10, 3), float)*10.0
        self.s = s = N.ones(10, float)
        src = sources.MGlyphSource()
        src.reset(x=x, y=y, z=z, u=v[:,0], v=v[:,1], w=v[:,2], scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.v, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, v, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(N.alltrue(src.points[:,0].ravel() == x), True)
        self.assertEqual(N.alltrue(src.points[:,1].ravel() == y), True)
        self.assertEqual(N.alltrue(src.points[:,2].ravel() == z), True)
        # Check the vectors and scalars.
        self.assertEqual(N.alltrue(src.vectors == v), True)
        self.assertEqual(N.alltrue(src.scalars == s), True)

    def check_dataset(self):
        """Check the TVTK dataset."""
        x, y, z, v, s, src = self.get_data()
        # Check if the dataset is setup right.
        pts = src.dataset.points.to_array()
        self.assertEqual(N.alltrue(pts[:,0].ravel() == x), True)
        self.assertEqual(N.alltrue(pts[:,1].ravel() == y), True)
        self.assertEqual(N.alltrue(pts[:,2].ravel() == z), True)
        vec = src.dataset.point_data.vectors.to_array()
        sc = src.dataset.point_data.scalars.to_array()
        self.assertEqual(N.alltrue(vec == v), True)
        self.assertEqual(N.alltrue(sc == s), True)

    def test_reset(self):
        "Test the reset method."
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5.0
        s *= 10
        v *= 0.1
        src.reset(x=x, u=v[:,0], v=v[:,1], w=v[:,2], scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2.0
        y *= 2.0
        z *= 2.0
        v *= 2.0
        s *= 2.0
        src.x = x
        src.y = y
        src.z = z 
        src.u = v[:,0]
        src.v = v[:,1]
        src.w = v[:,2]
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2.0
        z *= 2.0
        s *= 2.0
        src.set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()


################################################################################
# `TestMArraySource`
################################################################################ 
class TestMArraySource(unittest.TestCase):
    def setUp(self):
        x, y, z = N.ogrid[-10:10:11j, 
                          -10:10:12j, 
                          -10:10:20j]
        self.x, self.y, self.z = x, y, z
        dims = (x.shape[0], y.shape[1], z.shape[2])
        self.v = v = N.ones(dims + (3,), float)
        v[...,2] = 2
        v[...,2] = 3 
        self.s = s = N.ones(dims, float)
        src = sources.MArraySource()
        src.reset(x=x, y=y, z=z, u=v[...,0], v=v[...,1], w=v[...,2], scalars=s)
        self.src = src

    def tearDown(self):
        return

    def get_data(self):
        return self.x, self.y, self.z, self.v, self.s, self.src

    def check_traits(self):
        """Check if the sources traits are set correctly."""
        x, y, z, v, s, src = self.get_data()
        # Check if points are set correctly.
        self.assertEqual(N.alltrue(src.x == x), True)
        self.assertEqual(N.alltrue(src.y == y), True)
        self.assertEqual(N.alltrue(src.z == z), True)
        # Check the vectors and scalars.
        self.assertEqual(N.alltrue(src.vectors == v), True)
        self.assertEqual(N.alltrue(src.scalars == s), True)

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
        self.assertEqual(N.all(ds.origin == origin), True)
        self.assertEqual(N.allclose(ds.spacing, spacing), True)
        self.assertEqual(N.allclose(ds.dimensions, dimensions), True)

        vec = src.dataset.point_data.vectors.to_array()
        sc = src.dataset.point_data.scalars.to_array()
        v1 = v.transpose((2, 0, 1, 3))
        self.assertEqual(N.alltrue(vec.ravel() == v1.ravel()), True)
        s1 = s.transpose()
        self.assertEqual(N.alltrue(sc.ravel() == s1.ravel()), True)

    def test_reset(self):
        "Test the reset method."
        x, y, z, v, s, src = self.get_data()
        self.check_traits()
        self.check_dataset()

        # Call reset again with just a few things changed to see if it
        # works correctly.
        x *= 5.0
        s *= 10
        v *= 0.1
        src.reset(x=x, u=v[...,0], v=v[...,1], w=v[...,2], scalars=s)

        self.check_traits()
        self.check_dataset()

    def test_handlers(self):
        "Test if the various static handlers work correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2.0
        y *= 2.0
        z *= 2.0
        v *= 2.0
        s *= 2.0
        src.x = x
        src.y = y
        src.z = z 
        src.u = v[...,0]
        src.v = v[...,1]
        src.w = v[...,2]
        src.scalars = s
        self.check_traits()
        self.check_dataset()

    def test_set(self):
        "Test if the set method works correctly."
        x, y, z, v, s, src = self.get_data()
        x *= 2.0
        z *= 2.0
        s *= 2.0
        src.set(x=x, z=z, scalars=s)
        self.check_traits()
        self.check_dataset()



if __name__ == '__main__':
    unittest.main()

