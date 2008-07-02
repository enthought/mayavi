"""Actions for the help menu.

"""
# Authors: Gael Varoquaux <gael.varoquaux[at]normalesup.org>
#          Prabhu Ramachandran
# Copyright (c) 2007-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import webbrowser
from os import path
from os.path import join, dirname

# Enthought library imports.
from enthought.pyface.action.api import Action
from enthought.traits.ui.api import auto_close_message

# Local imports
import enthought.mayavi.api
from enthought.mayavi.core.common import error

# To find the html documentation directory, first look under the
# standard place.  If that directory doesn't exist, assume you
# are running from the source.
local_dir = dirname(enthought.mayavi.api.__file__)
HTML_DIR = join(local_dir, 'html')
if not path.exists(HTML_DIR):
    HTML_DIR = join(dirname(dirname(local_dir)), 'docs', 'mayavi',
        'user_guide', 'build', 'html')
    if not path.exists(HTML_DIR):
        HTML_DIR = None

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

        # If the HTML_DIR was found, bring up the documentation in a
        # web browser.  Otherwise, bring up an error message.
        if HTML_DIR:
            auto_close_message("Opening help in web browser...")
            webbrowser.open(join(HTML_DIR, 'index.html'),
                            new=1, autoraise=1)
        else:
            error("Could not find the user guide in your installation " \
                "or the source tree.")
