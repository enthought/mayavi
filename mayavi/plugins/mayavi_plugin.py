"""The Mayavi plugin.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

from traits.api import List
from envisage.api import Plugin, ServiceOffer

# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])
# The mayavi package ID.
ID = 'mayavi'

###############################################################################
# `MayaviPlugin` class.
###############################################################################
class MayaviPlugin(Plugin):

    # Extension point Ids.
    SERVICE_OFFERS = 'envisage.ui.workbench.service_offers'
    PREFERENCES       = 'envisage.preferences'

    # The plugins name.
    name = 'Mayavi plugin'

    # Our ID.
    id = ID

    ###### Contributions to extension points made by this plugin ######

    # Services we contribute.
    service_offers = List(contributes_to=SERVICE_OFFERS)

    # Preferences.
    preferences = List(contributes_to=PREFERENCES)

    def _preferences_default(self):
        """ Trait initializer. """
        return ['pkgfile://%s/preferences/preferences.ini' % ID]


    ######################################################################
    # Private methods.
    def _service_offers_default(self):
        """ Trait initializer. """
        engine_service_offer = ServiceOffer(
            protocol = 'mayavi.core.engine.Engine',
            factory  = PKG + '.envisage_engine.EnvisageEngine'
        )

        script_service_offer = ServiceOffer(
            protocol = 'mayavi.plugins.script.Script',
            factory  = PKG + '.script.Script'
        )
        return [engine_service_offer, script_service_offer]

