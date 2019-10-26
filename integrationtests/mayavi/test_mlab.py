"""Tests for the mlab interface to Mayavi
"""
# Author: Gael Varoquaux
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from inspect import getmembers
import sys
from time import sleep

# Enthought library imports
from pyface.api import GUI

# Local imports.
from common import TestCase

def is_timer_running(timer):
    """Written to work around a pyface bug.
    """
    if hasattr(timer, 'isActive'):
        # The Qt backend's IsRunning does not work correctly.
        return timer.isActive()
    else:
        return timer.IsRunning()


def run_mlab_examples():
    from mayavi import mlab
    from mayavi.tools.animator import Animator

    ############################################################
    # run all the "test_foobar" functions in the mlab module.
    for name, func in getmembers(mlab):
        if not callable(func) or not name[:4] in ('test', 'Test'):
            continue

        if sys.platform == 'win32' and name == 'test_mesh_mask_custom_colors':
            # fixme: This test does not seem to work on win32, disabling for now.
            continue

        mlab.clf()
        GUI.process_events()
        obj = func()

        if isinstance(obj, Animator):
            obj.delay = 10
            # Close the animation window.
            obj.close()
            while is_timer_running(obj.timer):
                GUI.process_events()
                sleep(0.05)

        # Mayavi has become too fast: the operator cannot see if the
        # Test function was succesful.
        GUI.process_events()
        sleep(0.1)


class TestMlab(TestCase):

    def test(self):
        self.main()

    def do(self):
        ############################################################
        # Imports.
        from mayavi import mlab

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()
        s.scene.isometric_view()

        ############################################################
        # run all the "test_foobar" functions in the mlab module.
        run_mlab_examples()

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

        # Test glyphs with number-only coordinates
        mlab.points3d(0, 0, 0, resolution=50)

if __name__ == "__main__":
    t = TestMlab()
    t.test()
