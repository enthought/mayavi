"""Creates a pseudo-package called `tvtk` that lets one use the tvtk
classes in a clean and quick manner.  The `TVTK` class is instantiated
and this instance serves as the `tvtk` 'module'.  For more details on
this see the devel.txt in the TVTK documentation directory.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007-2015,  Enthought, Inc.
# License: BSD Style.

from __future__ import print_function

from os.path import exists, join, dirname, isdir

# The tvtk wrapper code is all typically inside one zip file.  We try to
# find this file and then create the 'tvtk' module wrapper from that.  If
# the ZIP file is extracted into a tvtk_classes directory the ZIP file is
# not used and the tvtk_classes directory is inserted into sys.path and
# the directory contents are used for the tvtk classes -- note that you
# must have the following structure
# tvtk_classes/tvtk_classes/__init__.py.  This is handy for tools like
# pydev (Eclipse). If neither the tvtk_classes directory or the zip file
# is found an error is raised.

_zip = join(dirname(__file__), 'tvtk_classes.zip')
tvtk_class_dir = join(dirname(__file__), 'tvtk_classes')

if not ( exists(tvtk_class_dir) and isdir(tvtk_class_dir)
         or exists(_zip)):
    raise ImportError("TVTK not built properly. "
        "Unable to find either a directory: %s or a file: %s "
        "with the TVTK classes." % (tvtk_class_dir, _zip) )

# Check if the VTK version is the same as that used to build TVTK.
from tvtk.tvtk_classes.vtk_version import vtk_build_version

# Make sure VTK is installed.
try:
    import vtk
except ImportError as m:
    msg = '%s\n%s\nDo you have vtk installed properly?\n' \
          'VTK (and build instructions) can be obtained from http://www.vtk.org\n' \
         % (m, '_'*80)
    raise ImportError(msg)

vtk_version = vtk.vtkVersion().GetVTKVersion()[:3]
if vtk_version != vtk_build_version:
    msg = '*'*80 + "\n" + \
          'WARNING: Imported VTK version (%s) does not match the one used\n'\
          '         to build the TVTK classes (%s). This may cause problems.\n'\
          '         Please rebuild TVTK.\n'%(vtk_version, vtk_build_version) +\
          '*'*80 + '\n'
    print(msg)

# Now setup TVTK itself.
from tvtk.tvtk_classes import tvtk_helper
tvtk = tvtk_helper.TVTK()
