"""The view for the TVTK pipeline browser plugin.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.envisage.core.plugin import Plugin
from enthought.envisage.workbench.api import View
from enthought.traits.api import Instance
from enthought.tvtk.pipeline.browser import PipelineBrowser
from enthought.tvtk.plugins.scene.services import ITVTKSCENE

# Local imports.
from enthought.tvtk.plugins.browser.services import ITVTKBROWSER


######################################################################
# `BrowserView` class.
######################################################################
class BrowserView(View):

    # The pipeline browser instance we manage.
    browser = Instance(PipelineBrowser)

    ######################################################################
    # `View` interface
    ######################################################################
    def _create_contents(self, parent):
        """ Creates the toolkit-specific control that represents the view.
        
        'parent' is the toolkit-specific control that is the view's parent.

        """
        app = self.window.application
        scene_service = app.get_service(ITVTKSCENE)
        scene_service.on_trait_change(self.scene_editors_changed, 'editors_items')
                
        browser = PipelineBrowser()
        browser.show(parent=parent)
        self.control = browser.ui.control
        self.browser = browser

        # Add this view to the plugin's views.  We do this here and
        # not at initialization to allow someone listening to the
        # plugin's view_items trait to use the created browser.
        browser_service = app.get_service(ITVTKBROWSER)
        browser_service.views.append(self)
        
        return self.control

    ######################################################################
    # Non-public interface
    ######################################################################
    def scene_editors_changed(self, list_event):
        """This is called when the items of the editors trait of the
        ScenePlugin change.  This is used to add and remove objects
        from the pipeline."""
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
