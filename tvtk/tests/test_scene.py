""" Tests for the garbage collection of Scene objects.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
import gc

from traits.etsconfig.api import ETSConfig

from tvtk.pyface.scene import Scene
from tvtk.tests.common import restore_gc_state


class TestScene(unittest.TestCase):

    @unittest.skipIf(
        ETSConfig.toolkit=='wx', 'Test segfaults using WX (issue #216)')
    def test_scene_garbage_collected(self):

        def do():
            scene = Scene(None)
            scene.close()

        # when
        with restore_gc_state():
            gc.collect()
            do()

        # All created cycles should be collectable.
        self.assertEqual(gc.collect(), 0)


if __name__ == "__main__":
    unittest.main()
