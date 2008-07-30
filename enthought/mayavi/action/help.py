"""Actions for the help menu.

"""
# Authors: Gael Varoquaux <gael.varoquaux[at]normalesup.org>
#          Prabhu Ramachandran
# Copyright (c) 2007-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import webbrowser
from os import path
import os
import sys
from os.path import join, dirname

# Enthought library imports.
from enthought.pyface.action.api import Action
from enthought.traits.ui.api import auto_close_message

# Local imports
import enthought.mayavi.api
from enthought.mayavi.core.common import error
from enthought.mayavi.preferences.api import preference_manager

# To find the html documentation directory, first look under the
# standard place.  If that directory doesn't exist, assume you
# are running from the source.
local_dir = dirname(enthought.mayavi.api.__file__)
HTML_DIR = join(local_dir, 'html')
if not path.exists(HTML_DIR):
    HTML_DIR = join(dirname(dirname(local_dir)), 'docs', 'html', 'mayavi')
    if not path.exists(HTML_DIR):
        HTML_DIR = None

def browser_open(url):
    if sys.platform == 'darwin':
            os.system('open %s &' % url)
    elif webbrowser._iscommand('firefox') and \
                    preference_manager.root.open_help_in_light_browser:
        # Firefox is installed, let's use it, we know how to make it
        # chromeless.
        firefox = webbrowser.get('firefox')
        firefox._invoke(['-chrome', url], remote=False, autoraise=True)
    else:
        webbrowser.open(url, new=1, autoraise=1)


def open_help_index():
    # If the HTML_DIR was found, bring up the documentation in a
    # web browser.  Otherwise, bring up an error message.
    if HTML_DIR:
        auto_close_message("Opening help in web browser...")
        browser_open(join(HTML_DIR, 'index.html'))
    else:
        error("Could not find the user guide in your installation " \
            "or the source tree.")

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
        open_help_index()

