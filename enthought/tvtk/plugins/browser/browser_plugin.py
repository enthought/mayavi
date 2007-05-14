#!/usr/bin/env python
"""A TVTK pipeline browser plugin.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.envisage.api import Plugin
from enthought.traits.api import List

# Local imports.
from enthought.tvtk.plugins.browser.browser_view import BrowserView
from enthought.tvtk.plugins.browser.services import ITVTKBROWSER

######################################################################
# `BrowserPlugin` class.
######################################################################
class BrowserPlugin(Plugin):

    # A list of views created by the plugin.
    views = List(BrowserView)

    ######################################################################
    # `Plugin` interface.
    ######################################################################
    def start(self, application):
        """Starts the plugin."""
        # Register the browser service.
        application.register_service(ITVTKBROWSER, self)
