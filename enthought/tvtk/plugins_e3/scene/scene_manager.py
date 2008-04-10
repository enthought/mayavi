""" Manage the TVTK scenes. """


# Enthought library imports.
from enthought.pyface.tvtk.scene import Scene
from enthought.pyface.workbench.api import WorkbenchWindow
from enthought.traits.api import Any, HasTraits, List, Instance, Property
from enthought.traits.api import on_trait_change
from enthought.tvtk.plugins_e3.scene.scene_editor import SceneEditor


class SceneManager(HasTraits):
    """ Manage the TVTK scenes. """

    #### 'SceneManager' interface #############################################

    # The currently active scene editor.
    current_editor = Property(Instance(SceneEditor))

    # The currently active scene.
    current_scene = Property(Instance(Scene))

    # A list of all open scene editors.
    editors = List(SceneEditor)
    
    # The workbench window that the manager is in (there is one scene manager
    # per workbench window).
    window = Instance(WorkbenchWindow)
    
    #### Private interface ####################################################

    # Shadow trait for the 'current_editor' property.
    _current_editor = Any

    ###########################################################################
    # 'SceneManager' interface.
    ###########################################################################

    #### Trait properties #####################################################
    
    def _get_current_editor(self):
        """ Property getter. """

        le = len(self.editors)
        if le == 0:
            editor = None

        elif le == 1:
            editor = self.editors[0]

        else:
            editor = self._current_editor

        return editor

    def _set_current_editor(self, editor):
        """ Property setter. """
        
        self._current_editor = editor

        return

    def _get_current_scene(self):
        """ Property getter. """

        if self.current_editor is not None:
            current_scene = self.current_editor.scene
            
        else:
            current_scene = None

        return
    
    #### Trait change handlers ################################################

    @on_trait_change('window:editor_opened')
    def _on_editor_opened(self, obj, trait_name, old, new):
        """ Dynamic trait change handler. """

        if isinstance(new, SceneEditor):
            self.editors.append(new)
            
        return

    @on_trait_change('window:editor_closed')
    def _on_editor_closed(self, obj, trait_name, old, new):
        """ Dynamic trait change handler. """

        if isinstance(new, SceneEditor):
            self.editors.remove(new)
            
        return

    @on_trait_change('window:active_editor')
    def _on_active_editor_changed(self, obj, trait_name, old, new):
        """ Dynamic trait change handler. """

        if isinstance(new, SceneEditor):
            self.current_editor = new

        else:
            self.current_editor = None
            
        return
    
#### EOF ######################################################################



