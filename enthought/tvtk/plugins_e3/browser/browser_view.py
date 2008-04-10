""" The TVTK pipeline browser view. """


# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.pyface.workbench.api import View
from enthought.traits.api import Instance


class BrowserView(View):
    """ The TVTK pipeline browser view. """

    #### 'IWorkbenchPart' interface ###########################################
    
    # The part's globally unique identifier.
    id = 'enthought.tvtk.plugins.browser.browser_view'

    # The part's name (displayed to the user).
    name = 'TVTK Pipeline Browser'

    #### 'IView' interface ####################################################

    # The position of the view relative to the item specified in the
    # 'relative_to' trait.
    position = 'left'
    
    #### 'BrowserView' interface ##############################################

    # The pipeline browser instance that we wrap.
    browser = Instance('enthought.tvtk.pipeline.browser.PipelineBrowser')

    # The scene manager.
    scene_manager = Instance(
        'enthought.tvtk.plugins_e3.scene.scene_manager.SceneManager'
    )

    ###########################################################################
    # 'IWorkbenchPart' interface.
    ###########################################################################

    def create_control(self, parent):
        """ Create the toolkit-specific control that represents the view. """

        from enthought.tvtk.pipeline.browser import PipelineBrowser
                
        self.browser = PipelineBrowser()
        self.browser.show(parent=parent)

        # Listen for scenes being added/removed.
        self.scene_manager.on_trait_change(
            self._on_scene_editors_changed, 'editors_items'
        )
        
        return self.browser.ui.control

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _on_scene_editors_changed(self, list_event):
        """ Dynamic trait change handler.

        This is called when the items of the editors trait of the ScenePlugin
        change.  This is used to add and remove objects from the pipeline.

        """

        browser = self.browser
        
        # Remove any removed scenes.
        for editor in list_event.removed:
            scene = editor.scene
            if scene in browser.renwins:
                browser.renwins.remove(scene)
                browser.root_object.remove(scene.render_window)
                
        # Add any added scenes.
        for editor in list_event.added:
            scene = editor.scene
            browser.renwins.append(scene)
            browser.root_object.append(scene.render_window)

        return

#### EOF ######################################################################
