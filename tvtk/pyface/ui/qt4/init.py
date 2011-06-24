#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license.
#
# Author: Riverbank Computing Limited
# Description: <Enthought pyface package component>
#
# In an e-mail to enthought-dev on 2008.09.12 at 2:49 AM CDT, Phil Thompson said:
# The advantage is that all of the PyQt code in ETS can now be re-licensed to
# use the BSD - and I hereby give my permission for that to be done. It's
# been on my list of things to do.
#------------------------------------------------------------------------------


# Standard library imports.
import sys

# Major package imports.
import os

# PyQt4 version check crash PySide toolkit
from pyface.qt import qt_api
if qt_api == 'pyqt':
    from PyQt4 import QtGui, QtCore

    # Check the version numbers are late enough.
    if QtCore.QT_VERSION < 0x040200:
        raise RuntimeError, "Need Qt v4.2 or higher, but got v%s" % QtCore.QT_VERSION_STR

    if QtCore.PYQT_VERSION < 0x040100:
        raise RuntimeError, "Need PyQt v4.1 or higher, but got v%s" % QtCore.PYQT_VERSION_STR
else:
    from PySide import QtGui, QtCore

# It's possible that it has already been initialised.
_app = QtGui.QApplication.instance()

if _app is None:
    _app = QtGui.QApplication(sys.argv)

#### EOF ######################################################################
