"""Actions for the help menu.

"""
# Authors: Gael Varoquaux <gael.varoquaux[at]normalesup.org>
#          Prabhu Ramachandran
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os import path
import os
import sys
from os.path import join, dirname

# Enthought library imports.
from pyface.action.api import Action
from traitsui.api import auto_close_message

# Local imports
import mayavi.api
from mayavi.core.common import error
from mayavi.preferences.api import preference_manager

# To find the html documentation directory, first look under the
# standard place.  If that directory doesn't exist, assume you
# are running from the source.
local_dir = dirname(mayavi.api.__file__)
HTML_DIR = join(local_dir, 'html')
if not path.exists(HTML_DIR):
    HTML_DIR = join(dirname(dirname(local_dir)),
                                    'build', 'docs', 'html', 'mayavi')
    if not path.exists(HTML_DIR):
        HTML_DIR = None

def browser_open(url):
    if sys.platform == 'darwin':
            os.system('open %s &' % url)
    else:
        import webbrowser
        webbrowser.open(url, autoraise=1)


def open_help_index(*args):
    """ Open the mayavi user manual index in a browser.
    """
    # If the HTML_DIR was found, bring up the documentation in a
    # web browser.  Otherwise, bring up an error message.
    if HTML_DIR:
        auto_close_message("Opening help in web browser...")
        browser_open(join(HTML_DIR, 'index.html'))
    else:
        browser_open('https://docs.enthought.com/mayavi/mayavi/')


def open_tvtk_docs(*args):
    """ Open the TVTK class browser.
    """
    from tvtk.tools.tvtk_doc import TVTKClassChooser
    TVTKClassChooser().edit_traits()


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


######################################################################
# `TVTKClassBrowser` class.
######################################################################
class TVTKClassBrowser(Action):
    """ An action that opens the tvtk interactive class browser. """

    tooltip       = "The TVTK interactive class browser"

    description   = "The TVTK interactive class browser"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        open_tvtk_docs()
