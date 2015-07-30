""" Tests for the garbage collection of objects in tvtk package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
from traits.etsconfig.api import ETSConfig

from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.pyface.api import DecoratedScene, Scene
from tvtk.pyface.scene_model import SceneModel
from tvtk.tests.common import TestGarbageCollection

class TestTVTKGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """
    def test_tvtk_scene(self):
        """ Tests if TVTK scene can be garbage collected."""
        def create_fn():
            return TVTKScene()

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)
    
    @unittest.skipIf(
        ETSConfig.toolkit=='wx', 'Test segfaults using WX (issue #216)')
    def test_scene(self):
        """ Tests if Scene can be garbage collected."""
        def create_fn():
            return Scene()

        def close_fn(o):
            o.close()

        self.check_object_garbage_collected(create_fn, close_fn)

    @unittest.skipIf(
        ETSConfig.toolkit=='wx', 'Test segfaults using WX (issue #216)')
    def test_decorated_scene(self):
        """ Tests if Decorated Scene can be garbage collected."""
        def create_fn():
            return DecoratedScene(parent=None)

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)
    
    def test_scene_model(self):
        """ Tests if SceneModel can be garbage collected."""
        def create_fn():
            return SceneModel()

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)
