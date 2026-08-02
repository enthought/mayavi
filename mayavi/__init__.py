# Author: Prabhu Ramachandran, Gael Varoquaux
# Copyright (c) Enthought, Inc.
# License: BSD Style.
""" A tool for easy and interactive visualization of data.
    Part of the Mayavi project of the Enthought Tool Suite.
"""

try:
    from importlib.metadata import version

    __version__ = version("mayavi")
except Exception:
    __version__ = "0.0.0"

# Keep Qt off the wayland platform, where VTK render windows cannot embed.
# This has to happen before pyface creates the QApplication, which it does
# as an import side effect deeper in mayavi (see tvtk/WORKAROUNDS.md).
from tvtk.qt_x11 import steer_qt_to_x11 as _steer_qt_to_x11
_steer_qt_to_x11()
del _steer_qt_to_x11


def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `mayavi` directory
        src="tools/static",
        # directory in the `nbextension/` namespace
        dest="mayavi",
        require="mayavi/x3d/x3dom"
    )]
