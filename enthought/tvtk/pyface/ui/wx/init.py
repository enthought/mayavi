#------------------------------------------------------------------------------
#
#  Copyright (c) 2007, Riverbank Computing Limited
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#------------------------------------------------------------------------------

# Major package imports.
import wx


# Check the version number is late enough.
if wx.VERSION < (2, 6):
    raise RuntimeError, "Need wx version 2.6 or higher, but got %s" % str(wx.VERSION)

# It's possible that it has already been initialised.
_app = wx.GetApp()

if _app is None:
    _app = wx.PySimpleApp()

    # Before we can load any images we have to initialize wxPython's image
    # handlers.
    wx.InitAllImageHandlers()

#### EOF ######################################################################
