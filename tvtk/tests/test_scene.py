""" Tests for the garbage collection of TVTK Scene objects.
"""
# Author: Deepak Surti
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
import weakref
import gc

from traits.etsconfig.api import ETSConfig
from tvtk.pyface.tvtk_scene import TVTKScene

class TestScene(unittest.TestCase):
    def setUp(self):
        self.object_collected = []

    def object_collected_callback(self, reference):
        self.object_collected.append(True)

    def test_some_object_garbage_collected(self):
        """ This is a sample test which demonstrates that after deleting
            an object instance, it should not be necessary to force garbage
            collection, which is not currently true for TVTKScene and Scene
            qt, wx implementations.
            See:test_tvtk_scene_garbage_collected
                test_qt_scene_garbage_collected
                test_wx_scene_garbage_collected
        """
        class A():
            pass

        a = A()
        r = weakref.ref(a, self.object_collected_callback)
        del a
        self.assertEqual(self.object_collected, [True])
        self.assertEqual(r(), None)

    def test_tvtk_scene_garbage_collected(self):
        """ Test the garbage collection of TVTScene object."""
        scene = TVTKScene()
        scene_weakref = weakref.ref(scene, self.object_collected_callback)
        del scene
        ################################################################
        # Without forcing garbage collection, TVTKScene is not collected
        ################################################################
        gc.collect()
        self.assertEqual(self.object_collected, [True])
        self.assertEqual(scene_weakref(), None)
        self.assertEqual(gc.collect(), 0)
    
    @unittest.skipIf(ETSConfig.toolkit == 'wx',
                     "Skip qt test when running wx")
    def test_qt_scene_garbage_collected(self):
        """ Test the garbage collection of qt Scene implementation."""
        from tvtk.pyface.ui.qt4.scene import Scene
        scene = Scene()
        scene_weakref = weakref.ref(scene, self.object_collected_callback)
        del scene
        ################################################################
        # Without forcing garbage collection, Scene is not collected
        ################################################################
        gc.collect()
        self.assertEqual(self.object_collected, [True])
        self.assertEqual(scene_weakref(), None)
        self.assertEqual(gc.collect(), 0)

    @unittest.skip("Skip wx test as it causes segmentation fault")
    def test_wx_scene_garbage_collected(self):
        """ Test the garbage collection of wx Scene implementation."""
        from tvtk.pyface.ui.wx.scene import Scene
        scene = Scene()
        scene_weakref = weakref.ref(scene, self.object_collected_callback)
        del scene
        ################################################################
        # Without forcing garbage collection, Scene is not collected
        ################################################################
        gc.collect()
        self.assertEqual(self.object_collected, [True])
        self.assertEqual(scene_weakref(), None)
        self.assertEqual(gc.collect(), 0)

if __name__ == "__main__":
    unittest.main()
