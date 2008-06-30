"""Tests for the mlab interface to Mayavi
"""
# Author: Gael Varoquaux
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from inspect import getmembers

# Local imports.
from common import TestCase


class TestMlab(TestCase):

    def test(self):        
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
       

if __name__ == "__main__":
    t = TestMlab()
    t.main()
