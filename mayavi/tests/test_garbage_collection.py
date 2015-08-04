""" Tests for the garbage collection of objects in mayavi package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

from numpy import sqrt, sin, mgrid
from traits.api import Instance, HasTraits
from traitsui.api import View, Item
from traits.etsconfig.api import ETSConfig
from tvtk.pyface.scene_editor import SceneEditor
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
        class MlabApp(HasTraits):

            # The scene model.
            scene = Instance(MlabSceneModel, ())

            view = View(Item(name='scene',
                             editor=SceneEditor(scene_class=MayaviScene),
                             show_label=False,
                             resizable=True,
                             height=500,
                             width=500),
                        resizable=True
                        )

            def __init__(self, **traits):
                self.generate_data()

            def generate_data(self):
                # Create some data
                X, Y = mgrid[-2:2:100j, -2:2:100j]
                R = 10*sqrt(X**2 + Y**2)
                Z = sin(R)/R
                self.scene.mlab.surf(X, Y, Z, colormap='gist_earth')

        def close_fn(o):
            o.owner.ui = None
            if ETSConfig.toolkit == 'qt4':
                o.control = None
            o.dispose()

        def create_fn():
            app = MlabApp()
            return app.edit_traits()

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
