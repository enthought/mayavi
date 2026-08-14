""" Tests for the garbage collection of TVTKScene objects.

"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import sys
import unittest
import weakref
import gc

from traits.etsconfig.api import ETSConfig
from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.tests.common import restore_gc_state
from tvtk.vtk_module import vtkRenderWindow


class TestTVTKScene(unittest.TestCase):

    @unittest.skipIf(
        sys.platform.startswith('win') or ETSConfig.toolkit == 'null',
        'CI with windows fails due to lack of OpenGL, or toolkit is null.'
    )
    def test_offscreen_render_window_left_to_vtk(self):
        # An offscreen scene must use whatever concrete render window VTK's
        # own factory picks, and no other.  We used to instantiate
        # EGLRenderWindow whenever the class existed, which since the wheels
        # started shipping EGL support means always -- and segfaulted on every
        # machine with no EGL driver behind it.  See
        # https://github.com/enthought/mayavi/issues/1332
        scene = TVTKScene(off_screen_rendering=True)
        try:
            renwin = scene.render_window
            self.assertEqual(
                renwin.class_name, vtkRenderWindow().GetClassName()
            )
            self.assertTrue(renwin.off_screen_rendering)
        finally:
            scene.close()

    @unittest.skipIf(
        sys.platform.startswith('win') or ETSConfig.toolkit == 'null',
        'CI with windows fails due to lack of OpenGL, or toolkit is null.'
    )
    def test_tvtk_scene_garbage_collected(self):

        # given
        scene_collected = []
        scene_weakref = None

        def scene_collected_callback(weakref):
            scene_collected.append(True)

        def do():
            scene = TVTKScene()
            reference = weakref.ref(scene, scene_collected_callback)
            scene.close()
            return reference

        # when
        with restore_gc_state():
            gc.disable()
            scene_weakref = do()

        # The TVTK Scene should have been collected.
        self.assertTrue(scene_collected[0])
