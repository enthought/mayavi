# Author: Prabhu Ramachandran, Gael Varoquaux
# Copyright (c) 2004-2024, Enthought, Inc.
# License: BSD Style.
""" A tool for easy and interactive visualization of data.
    Part of the Mayavi project of the Enthought Tool Suite.
"""

try:
    from importlib.metadata import version

    __version__ = version("mayavi")
except Exception:
    __version__ = "0.0.0"


def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `mayavi` directory
        src="tools/static",
        # directory in the `nbextension/` namespace
        dest="mayavi",
        require="mayavi/x3d/x3dom"
    )]
