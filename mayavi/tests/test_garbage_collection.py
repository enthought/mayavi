""" Tests for the garbage collection of objects in mayavi package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

from tvtk.tests.common import TestGarbageCollection
from mayavi.core.engine import Engine
from mayavi.core.null_engine import NullEngine
from mayavi.tools.mlab_scene_model import MlabSceneModel

class TestMayaviGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """
    def test_mlab_scene_model(self):
        """ Tests if MlabSceneModel can be garbage collected."""
        def create_fn():
            return MlabSceneModel()

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_scene(self):
        """ Tests if core Scene can be garbage collected."""
        def create_fn():
            e = NullEngine()
            e.start()
            e.new_scene()
            scene = e.scenes[-1]
            return scene

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_null_engine(self):
        """ Tests if core Null Engine can be garbage collected."""
        def create_fn():
            e = NullEngine()
            e.start()
            return e

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_engine(self):
        """ Tests if core Engine can be garbage collected."""
        def create_fn():
            e = Engine()
            e.start()
            return e

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(create_fn, close_fn)
