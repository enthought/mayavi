# Copyright (c) Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.

# Keep Qt off the wayland platform, where VTK render windows cannot embed.
# tvtk.pyface submodules import traitsui, and pyface creates the QApplication
# as an import side effect of that (see tvtk/WORKAROUNDS.md).
from tvtk.qt_x11 import steer_qt_to_x11 as _steer_qt_to_x11
_steer_qt_to_x11()
del _steer_qt_to_x11
