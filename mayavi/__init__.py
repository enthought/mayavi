# Author: Prabhu Ramachandran, Gael Varoquaux
# Copyright (c) 2004-2016, Enthought, Inc.
# License: BSD Style.
""" A tool for easy and interactive visualization of data.
    Part of the Mayavi project of the Enthought Tool Suite.
"""

__version__ = '4.5.0'

__requires__ = [
    'apptools',
    'traits',
    'traitsui',
]

__extras_require__ = {
    'app': [
        'envisage',
    ],
}


# Try forcing the use of wx 2.8 before any other import.
import sys
if not 'wx' in sys.modules:
    try:
        # Try forcing the use of wx 2.8
        from traits.etsconfig.api import ETSConfig
        if ETSConfig.toolkit in ('wx', ''):
            import wxversion
            wxversion.ensureMinimal('2.8')
    except ImportError:
        """ wxversion not installed """


def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `mayavi` directory
        src="tools/static",
        # directory in the `nbextension/` namespace
        dest="mayavi",
    )]
