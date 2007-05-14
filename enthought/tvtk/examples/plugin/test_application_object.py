"""A runnable that binds the loaded scene plugins into the python shell.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.api import ApplicationObject

from enthought.traits.api import Any
from enthought.tvtk.plugins.scene.services import ITVTKSCENE

##########################################################################
# `TestApplicationObject` class
##########################################################################
class TestApplicationObject(ApplicationObject):
    """ A runnable that binds the ITVTKSCENE service to the python
    shell."""

    # FIXME: the base class does not define this (yet).  If this is
    # defined then the core plugin injects the application before
    # running the code in init.
    application = Any
    
    ###########################################################################
    # 'ApplicationObject' interface.
    ###########################################################################

    def init(self):
        """ Runs the application object!

        This simply binds the tvtk scene plugin on the python shell.

        """

        app = self.application
        tsp = app.get_service(ITVTKSCENE)
        ps = app.get_service('enthought.plugins.IPythonShell')
        ps.bind('scene_plugin', tsp)
        
