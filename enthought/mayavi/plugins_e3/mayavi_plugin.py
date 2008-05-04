"""The Mayavi plugin.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc. 
# License: BSD Style.

from enthought.traits.api import List
from enthought.envisage.api import Plugin, ServiceFactory

# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])
# The mayavi package ID.
ID = 'enthought.mayavi'

###############################################################################
# `MayaviPlugin` class.
###############################################################################
class MayaviPlugin(Plugin):

    # Extension point Ids.
    SERVICE_FACTORIES = 'enthought.envisage.service_factories'
    PREFERENCES       = 'enthought.envisage.preferences'

    # The plugins name.
    name = 'Mayavi plugin'

    ###### Contributions to extension points made by this plugin ######

    # Services we contribute.
    service_factories = List(contributes_to=SERVICE_FACTORIES)

    # Preferences.
    preferences = List(contributes_to=PREFERENCES)

    def _preferences_default(self):
        """ Trait initializer. """
        return ['pkgfile://%s/preferences/preferences.ini' % ID]


    ######################################################################
    # Private methods.
    def _service_factories_default(self):
        """ Trait initializer. """
        engine_service_factory = ServiceFactory(
            protocol = 'enthought.mayavi.engine.Engine',
            factory  = PKG + '.envisage_engine.EnvisageEngine',
            scope    = 'window'
        )

        script_service_factory = ServiceFactory(
            protocol = 'enthought.mayavi.plugins_e3.script.Script',
            factory  = PKG + '.script.Script',
            scope    = 'window'
        )
        return [engine_service_factory, script_service_factory]

