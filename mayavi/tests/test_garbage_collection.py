""" Tests for the garbage collection of objects in mayavi package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

from pyface.api import GUI, ApplicationWindow
from traits.api import Instance
from tvtk.tests.common import TestGarbageCollection
from mayavi.core.ui.mayavi_scene import MayaviScene
from mayavi.core.engine import Engine
from mayavi.core.null_engine import NullEngine
from mayavi.tools.mlab_scene_model import MlabSceneModel



class TestMayaviGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """
    def test_mlab_scene_model_with_gui(self):
        """ Tests if MlabSceneModel with GUI can be garbage collected."""

        class MlabSceneModelWindow(ApplicationWindow):
            scene = Instance(MlabSceneModel, ())

        gui = GUI()

        def close(win):
            win.close()

        def open(gui):
            window = MlabSceneModelWindow(size=(60, 60))
            window.open()
            return window

        def create_fn():
            return open(gui)

        def close_fn(o):
            # Start the GUI event loop!
            gui.invoke_after(500, close, o)
            gui.start_event_loop()

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_mlab_scene_model(self):
        """ Tests if MlabSceneModel can be garbage collected."""

        def create_fn():
            return MlabSceneModel()

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_scene(self):
        """ Tests if core Scene can be garbage collected."""
        def create_fn():
            e = NullEngine()
            e.start()
            scene = e.new_scene()
            return scene

        def close_fn(o):
            o.closing = True

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_mayavi_scene(self):
        """ Tests if Mayavi UI Scene can be garbage collected."""
        def create_fn():
            scene = MayaviScene(parent=None)
            return scene

        def close_fn(o):
            o.closing = True

    def test_null_engine(self):
        """ Tests if core Null Engine can be garbage collected."""
        def create_fn():
            e = NullEngine()
            e.start()
            e.new_scene()
            e.new_scene()
            e.new_scene()
            return e

        def close_fn(o):
            o.stop()

        self.check_object_garbage_collected(create_fn, close_fn)

    def test_engine(self):
        """ Tests if core Engine can be garbage collected."""
        def create_fn():
            e = Engine()
            e.start()
            return e

        def close_fn(o):
            o.stop()

        self.check_object_garbage_collected(create_fn, close_fn)
