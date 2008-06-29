"""Actions for the help menu.

"""
# Authors: Gael Varoquaux <gael.varoquaux[at]normalesup.org>
#          Prabhu Ramachandran
# Copyright (c) 2007-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import webbrowser
from os.path import join, dirname

# Enthought library imports.
from enthought.pyface.action.api import Action
from enthought.traits.ui.api import auto_close_message

# Local imports
import enthought.mayavi.api
HTML_DIR = join(dirname(enthought.mayavi.api.__file__), 'html')

######################################################################
# `HelpIndex` class.
######################################################################
class HelpIndex(Action):
    """ An action that pop up the help in a browser. """

    tooltip       = "The Mayavi2 user guide"

    description   = "The Mayavi2 user guide"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """

        auto_close_message("Opening help in web browser...")
        webbrowser.open(join(HTML_DIR, 'index.html'),
                        new=1, autoraise=1)

