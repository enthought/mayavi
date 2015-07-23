""" Tests for the garbage collection of Scene objects.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
import weakref
import gc

from traits.etsconfig.api import ETSConfig

from tvtk.pyface.scene import Scene
from tvtk.tests.common import restore_gc_state


class TestScene(unittest.TestCase):

    @unittest.skipIf(
        ETSConfig.toolkit=='wx', 'Test segfaults using WX (issue #216)')
    def test_scene_garbage_collected(self):

        # given
        scene_collected = []
        scene_weakref = None

        def scene_collected_callback(weakref):
            scene_collected.append(True)

        def do():
            scene = Scene()
            reference = weakref.ref(scene, scene_collected_callback)
            scene.close()
            return reference

        # when
        with restore_gc_state():
            gc.disable()
            scene_weakref = do()

        # The Scene should have been collected.
        self.assertTrue(scene_collected[0])
        self.assertIsNone(scene_weakref())


if __name__ == "__main__":
    unittest.main()
