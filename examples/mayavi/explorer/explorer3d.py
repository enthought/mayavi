#!/usr/bin/env python
""" The entry point for an Envisage application. """

# Standard library imports.
import sys
import os.path
import logging

# Enthought library imports.
from mayavi.plugins.app import get_plugins, setup_logger
from traits.api import List
from envisage.api import Plugin, ServiceOffer
from envisage.ui.workbench.api import WorkbenchApplication
from pyface.workbench.api import Perspective, PerspectiveItem

logger = logging.getLogger()

###############################################################################
# `ExplorerPerspective` class.
###############################################################################
class ExplorerPerspective(Perspective):
    """ An default perspective for the app. """

    # The perspective's name.
    name = 'Explorer3D'

    # Should this perspective be enabled or not?
    enabled = True

    # Should the editor area be shown in this perspective?
    show_editor_area = True

    # View IDs.
    EXPLORER_VIEW = 'explorer3d.Explorer3D'

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id=EXPLORER_VIEW, position='left'),
    ]

###############################################################################
# `ExplorerPlugin` class.
###############################################################################
class ExplorerPlugin(Plugin):

    # Extension points we contribute to.
    PERSPECTIVES = 'envisage.ui.workbench.perspectives'
    VIEWS             = 'envisage.ui.workbench.views'
    SERVICE_OFFERS = 'envisage.ui.workbench.service_offers'

    # The plugin's unique identifier.
    id = 'explorer3d.Explorer3D'

    # The plugin's name (suitable for displaying to the user).
    name = '3D function explorer'

    # Perspectives.
    perspectives = List(contributes_to=PERSPECTIVES)

    # Services we contribute.
    service_offers = List(contributes_to=SERVICE_OFFERS)

    # Views.
    views = List(contributes_to=VIEWS)


    ######################################################################
    # Private methods.
    def _perspectives_default(self):
        """ Trait initializer. """
        return [ExplorerPerspective]

    def _service_offers_default(self):
        """ Trait initializer. """
        explorer_service_offer = ServiceOffer(
            protocol = 'explorer_app.Explorer3D',
            factory  = 'explorer_app.Explorer3D'
        )

        return [explorer_service_offer]

    def _views_default(self):
        """ Trait initializer. """
        return [self._explorer_view_factory]

    def _explorer_view_factory(self, window, **traits):
        """ Factory method for explorer views. """
        from pyface.workbench.traits_ui_view import \
                TraitsUIView

        explorer = self._get_explorer(window)
        tui_engine_view = TraitsUIView(obj=explorer,
                                       id='explorer3d.Explorer3D',
                                       name='Explorer3D',
                                       window=window,
                                       position='left',
                                       **traits
                                       )
        return tui_engine_view

    def _get_explorer(self, window):
        """Return the explorer service."""
        return window.get_service('explorer_app.Explorer3D')


######################################################################
def main():

    # Get the default mayavi plugins.
    plugins = get_plugins()
    # Inject our plugin up front so our perspective becomes the default.
    plugins.insert(0, ExplorerPlugin())

    # Create an Envisage application.
    id = 'explorer3d.Explorer3D'
    application = WorkbenchApplication(id=id,
                                       plugins = plugins
                                       )
    # This needs to be done here since the ETSConfig.application_home is
    # not set correctly up to this point.
    setup_logger(logger, 'explorer3d.log', mode=logging.ERROR)

    # Start the application.
    application.run()

# Application entry point.
if __name__ == '__main__':
    main()

