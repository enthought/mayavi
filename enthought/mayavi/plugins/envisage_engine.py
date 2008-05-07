"""The MayaVi Engine meant to be used with Envisage.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.plugins.scene.i_scene_manager import \
            ISceneManager
from enthought.tvtk.plugins.scene.ui.actions import NewScene
from enthought.tvtk.plugins.scene import scene_editor 
from enthought.pyface.api import GUI
from enthought.pyface.workbench.api import WorkbenchWindow

# Local imports.
from enthought.mayavi.core.scene import Scene
#from enthought.mayavi.preference_manager import PreferenceManager
from enthought.mayavi.engine import Engine


######################################################################
# `EnvisageEngine` class
######################################################################
class EnvisageEngine(Engine):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The envisage application.
    window = Instance(WorkbenchWindow)

    # The preference manager.
    #preference_manager = Instance(PreferenceManager)
    
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
        scene_manager = self.window.get_service(ISceneManager)
        for scene in scene_manager.scenes:
            self.add_scene(scene)

        # Create the preference manager.  We do this here since at
        # this point we are guaranteed that the mayavi2 plugin is
        # running.
        #self.preference_manager = PreferenceManager(engine=self)
        
        # Setup a handler that is invoked when a new Scene is
        # added/removed.
        scene_manager.on_trait_change(self._scene_editors_changed,
                                      'scenes_items')

        # Call the parent start method.
        super(EnvisageEngine, self).start()

    def new_scene(self):
        """Creates a new VTK scene window.
        """
        action = NewScene(window=self.window)
        action.perform(None)
        
        # Flush the UI.
        GUI.process_events()
        return self.scenes[-1]

    def close_scene(self, scene):
        """Given a VTK scene instance, this method closes it.
        """
        active_window = self.window 
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
        SceneManager change.  This is used to update `self.scenes`."""
        # Remove any removed scenes.
        for scene in list_event.removed:
            self.remove_scene(scene)
        # Add any new scenes.
        for scene in list_event.added:
            self.add_scene(scene)

