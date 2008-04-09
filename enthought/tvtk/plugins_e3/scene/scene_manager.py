""" Manage the TVTK scenes. """


# Enthought library imports.
from enthought.traits.api import Any, HasTraits, List, Instance, Property
from enthought.tvtk.plugins_e3.scene.scene_editor import SceneEditor


class SceneManager(HasTraits):
    """ Manage the TVTK scenes. """

    #### 'SceneManager' interface #############################################
    
    # A list of scene editors.
    editors = List(SceneEditor)

    # The currently active scene editor.
    current_editor = Property(Instance(SceneEditor))

    #### Private interface ####################################################

    # Shadow trait for the 'current_editor' property.
    _current_editor = Any
    
    ###########################################################################
    # 'SceneManager' interface.
    ###########################################################################

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
    
#### EOF ######################################################################



