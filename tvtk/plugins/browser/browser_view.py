""" The TVTK pipeline browser view. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from pyface.workbench.api import View
from traits.api import Instance, on_trait_change


class BrowserView(View):
    """ The TVTK pipeline browser view. """

    #### 'IWorkbenchPart' interface ###########################################

    # The part's name (displayed to the user).
    name = 'TVTK Pipeline Browser'

    #### 'IView' interface ####################################################

    # The position of the view relative to the item specified in the
    # 'relative_to' trait.
    position = 'left'

    #### 'BrowserView' interface ##############################################

    # The pipeline browser instance that we are a view of.
    browser = Instance('tvtk.pipeline.browser.PipelineBrowser')

    # The scene manager.
    scene_manager = Instance(
        'tvtk.plugins.scene.i_scene_manager.ISceneManager'
    )

    ###########################################################################
    # 'IWorkbenchPart' interface.
    ###########################################################################

    def create_control(self, parent):
        """ Create the toolkit-specific control that represents the view. """

        from tvtk.pipeline.browser import PipelineBrowser

        self.browser = PipelineBrowser()
        self.browser.show(parent=parent)

        return self.browser.ui.control

    ###########################################################################
    # Private interface.
    ###########################################################################

    #### Trait change handlers ################################################

    @on_trait_change('scene_manager:scenes_items')
    def _on_scenes_changed(self, event):
        """ Dynamic trait change handler.

        This is called when scenes are added/removed from the scene manager, it
        is used to add and remove objects from the pipeline.

        """

        # Scenes that were removed.
        map(self._remove_scene, event.removed)

        # Scenes that were added.
        map(self._add_scene, event.added)

        return

    #### Methods ##############################################################

    def _add_scene(self, scene):
        """ Add the specified scene to the pipeline browser. """

        self.browser.renwins.append(scene)
        self.browser.root_object.append(scene.render_window)

        return

    def _remove_scene(self, scene):
        """ Remove the specified scene from the pipeline browser. """

        if scene in self.browser.renwins:
            self.browser.renwins.remove(scene)
            self.browser.root_object.remove(scene.render_window)

        return

#### EOF ######################################################################
