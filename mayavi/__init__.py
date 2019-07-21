# Author: Prabhu Ramachandran, Gael Varoquaux
# Copyright (c) 2004-2019, Enthought, Inc.
# License: BSD Style.
""" A tool for easy and interactive visualization of data.
    Part of the Mayavi project of the Enthought Tool Suite.
"""

__version__ = '4.7.1'

__requires__ = [
    'apptools',
    'envisage',
    'numpy',
    'pyface>=6.1.1',
    'pygments',  # This is only needed for the Qt backend but we add it anyway.
    'traits>=4.6.0',
    'traitsui>=6.0.0',
    'vtk'
]

__extras_require__ = {
    'app': [
        'envisage',
    ],
}


def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `mayavi` directory
        src="tools/static",
        # directory in the `nbextension/` namespace
        dest="mayavi",
        require="mayavi/x3d/x3dom"
    )]
