""" Tests for the garbage collection of TVTKScene objects.

"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
import weakref
import gc

from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.tests.common import restore_gc_state


class TestTVTKScene(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
