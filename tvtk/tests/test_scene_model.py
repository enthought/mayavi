""" Tests for the garbage collection of Scene objects.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
import weakref
import gc

from tvtk.pyface.scene_model import SceneModel
from tvtk.tests.common import restore_gc_state


class TestSceneModel(unittest.TestCase):

    def test_scene_model_garbage_collected(self):

        # given
        scene_model_collected = []
        scene_model_weakref = None

        def scene_model_collected_callback(weakref):
            scene_model_collected.append(True)

        def do():
            scene_model = SceneModel()
            reference = weakref.ref(scene_model, scene_model_collected_callback)
            scene_model.closed = True
            return reference

        # when
        with restore_gc_state():
            gc.disable()
            scene_model_weakref = do()

        # The Scene should have been collected.
        self.assertTrue(scene_model_collected[0])
        self.assertIsNone(scene_model_weakref())


if __name__ == "__main__":
    unittest.main()
