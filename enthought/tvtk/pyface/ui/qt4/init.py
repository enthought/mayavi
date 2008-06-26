#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
# 
# This software is provided without warranty under the terms of the GPL v2
# license.
# 
# Author: Riverbank Computing Limited
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------


# Standard library imports.
import sys

# Major package imports.
from PyQt4 import QtCore, QtGui


# Check the version numbers are late enough.
if QtCore.QT_VERSION < 0x040200:
    raise RuntimeError, "Need Qt v4.2 or higher, but got v%s" % QtCore.QT_VERSION_STR

if QtCore.PYQT_VERSION < 0x040100:
    raise RuntimeError, "Need PyQt v4.1 or higher, but got v%s" % QtCore.PYQT_VERSION_STR

# It's possible that it has already been initialised.
_app = QtGui.QApplication.instance()

if _app is None:
    _app = QtGui.QApplication(sys.argv)

#### EOF ######################################################################
