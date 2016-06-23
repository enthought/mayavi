# Author: Prabhu Ramachandran
# License: BSD style
# Copyright (c) 2004, Enthought, Inc.
""" A Traits-based wrapper for the Visualization Toolkit.
    Part of the Mayavi project of the Enthought Tool Suite.
"""

from os.path import exists, join, dirname, isdir
import logging

# use a null handler when used as a library
logging.getLogger('tvtk').addHandler(logging.NullHandler())

# The tvtk wrapper code is all typically inside one zip file.  We try to
# find this file and put it in __path__ and then create the 'tvtk' module
# wrapper from that.  If the ZIP file is extracted into a tvtk_classes
# directory the ZIP file is not used and the tvtk_classes directory is
# inserted into sys.path and the directory contents are used for the tvtk
# classes -- note that you must have the following structure
# tvtk_classes/tvtk_classes/__init__.py.  This is handy for tools like
# pydev (Eclipse).

# We add the path to the local __path__ here, in the __init__, so that
# the unpickler can directly unpickle the TVTK classes.

_zip = join(dirname(__file__), 'tvtk_classes.zip')
tvtk_class_dir = join(dirname(__file__), 'tvtk_classes')

if exists(tvtk_class_dir) and isdir(tvtk_class_dir):
    # Nothing to do, it will imported anyhow.
    pass
elif exists(_zip):
    __path__.append(_zip)
