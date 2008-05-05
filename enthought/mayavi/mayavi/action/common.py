"""Common code for all actions.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.workbench.action.workbench_action import WorkbenchAction
# Local imports.
from enthought.mayavi.services import IMAYAVI

######################################################################
# Utility functions.
######################################################################
def get_imayavi(window):
    """Returns the IMAYAVI service given a workbench window."""
    app = window.application
    return app.get_service(IMAYAVI)
