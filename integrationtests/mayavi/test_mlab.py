"""Tests for the mlab interface to Mayavi
"""
# Author: Gael Varoquaux
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from inspect import getmembers
from time import sleep

# Local imports.
from common import TestCase


class TestMlab(TestCase):

    def test(self):       
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from enthought.mayavi import mlab
              
        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        ############################################################
        # run all the "test_foobar" functions in the mlab module.
        for name, func in getmembers(mlab):
            if not callable(func) or not name[:4] in ('test', 'Test'):
                continue
            mlab.clf()
            func()
            # Mayavi has become too fast: the operator cannot see if the
            # Test function was succesful.
            sleep(0.1)
     
        ############################################################
        # Test some specific corner-cases
        import numpy
        x, y, z = numpy.mgrid[1:10, 1:10, 1:10]
        u, v, w = numpy.mgrid[1:10, 1:10, 1:10]
        s = numpy.sqrt(u**2 + v**2)
        
        mlab.clf()
        # Test the extra argument "scalars"
        mlab.quiver3d(x, y, z, u, v, w, scalars=s)

        # Test surf with strange-shaped inputs
        X, Y = numpy.ogrid[-10:10, -10:10]
        Z = X**2 + Y**2
        mlab.surf(X, Y, Z)
        mlab.surf(X.ravel(), Y.ravel(), Z)

        x, y, z = numpy.mgrid[-10:10, -10:10, -3:2]
        mlab.flow(x, y, z)

        # Test glyphs with number-only coordinnates
        mlab.points3d(0, 0, 0, resolution=50)

if __name__ == "__main__":
    t = TestMlab()
    t.test()
