""" Tests for the garbage collection of objects in mayavi package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

from tvtk.tests.common import TestGarbageCollection
from mayavi.tools.mlab_scene_model import MlabSceneModel

class TestMayaviGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """
    def test_mlab_scene_model(self):
        """ Tests if MlabSceneModel can be garbage collected."""
        def obj_fn():
            return MlabSceneModel()

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(obj_fn, close_fn)
