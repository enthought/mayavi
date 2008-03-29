"""Actions for the help menu.

"""
# Author: Gael Varoquaux <gael.varoquaux[at]normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import webbrowser
import os

# Local imports
from enthought.mayavi.action.common import WorkbenchAction

import enthought.mayavi.api
HTML_DIR = os.path.dirname(enthought.mayavi.api.__file__) + os.sep \
        + 'html' + os.sep
from enthought.traits.ui.api import auto_close_message

######################################################################
# `HelpIndex` class.
######################################################################
class HelpIndex(WorkbenchAction):
    """ An action that pop up the help in a browser. """

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self):
        """ Performs the action. """

        auto_close_message("Opening help in web browser...")
        webbrowser.open(HTML_DIR + 'user_guide.html',
                        new=1, autoraise=1)

