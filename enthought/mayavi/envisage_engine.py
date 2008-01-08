"""The MayaVi Engine meant to be used with Envisage.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.plugins.scene.services import ITVTKSCENE
from enthought.tvtk.plugins.scene import scene_editor
from enthought.tvtk.plugins.scene.actions import NewScene
from enthought.pyface.api import GUI

# Local imports.
from enthought.mayavi.core.scene import Scene
from enthought.mayavi.preference_manager import PreferenceManager
from enthought.mayavi.engine import Engine, get_active_window


######################################################################
# `EnvisageEngine` class
######################################################################
class EnvisageEngine(Engine):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The envisage application.
    application = Instance('enthought.envisage.core.application.Application')

    # The preference manager.
    preference_manager = Instance(PreferenceManager)
    
    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for x in ['application',]:
            d.pop(x, None)
        return d    

    ######################################################################
    # `Engine` interface
    ######################################################################
    def start(self):
        """This is called by the plugin when the plugin actually
        starts."""
        
        # Add all the existing scenes from the scene plugin.
        instance = self.application.get_service(ITVTKSCENE)
        for editor in instance.editors:
            scene = Scene(scene=editor.scene, name=editor.name)
            scene.sync_trait('name', editor)
            scene.start()
            self.scenes.append(scene)

        # Create the preference manager.  We do this here since at
        # this point we are guaranteed that the mayavi2 plugin is
        # running.
        self.preference_manager = PreferenceManager(engine=self)
        
        # Setup a handler that is invoked when a new Scene is
        # added/removed.
        instance.on_trait_change(self._scene_editors_changed, 'editors_items')

        # Call the parent start method.
        super(EnvisageEngine, self).start()

    def new_scene(self):
        """Creates a new VTK scene window.
        """
        active_window = get_active_window(self.application)
        action = NewScene(window=active_window)
        action.perform()
        
        # Flush the UI.
        GUI.process_events()
        return self.scenes[-1]

    def close_scene(self, scene):
        """Given a VTK scene instance, this method closes it.
        """
        active_window = get_active_window(self.application)
        s = scene.scene
        for editor in active_window.editors[:]:
            if isinstance(editor, scene_editor.SceneEditor):
                if id(editor.scene) == id(s):
                    editor.close()
                    break
        # Flush the UI.
        GUI.process_events()

    ######################################################################
    # Non-public interface
    ######################################################################
    def _scene_editors_changed(self, list_event):
        """This is called when the items of the editors trait of the
        ScenePlugin change.  This is used to update `self.scenes`."""
        # Remove any removed scenes.
        for editor in list_event.removed:
            scene = editor.scene
            remove = [x for x in self.scenes if x.scene == scene]
            for x in remove:
                x.stop()
                self.scenes.remove(x)
        # Add any new scenes.
        for editor in list_event.added:
            scene = Scene(scene=editor.scene, name=editor.name)
            scene.sync_trait('name', editor)
            scene.start()
            self.scenes.append(scene)

