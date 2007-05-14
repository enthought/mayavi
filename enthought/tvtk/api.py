# Author: Prabhu Ramachandran
# License: BSD style

# Pseudo-package that lets one use tvtk.

from os.path import exists, join, dirname
import sys

# The tvtk wrapper code is all inside one zip file.  We try to find
# this file and put it in sys.path and then create the 'tvtk' module
# wrapper from that.  If the zip file is not found, nothing is done.

_zip = join(dirname(__file__), 'tvtk_classes.zip')
if exists(_zip) and _zip not in sys.path:
    sys.path.append(_zip)
    # Check if the VTK version is the same as that used to build TVTK.
    from tvtk_classes.vtk_version import vtk_build_version
    import vtk
    vtk_version = vtk.vtkVersion().GetVTKVersion()[:3]
    if vtk_version != vtk_build_version:
        msg = '*'*80 + "\n" + \
              'WARNING: Imported VTK version (%s) does not match the one used\n'\
              '         to build the TVTK classes (%s). This may cause problems.\n'\
              '         Please rebuild TVTK.\n'%(vtk_version, vtk_build_version) +\
              '*'*80 + '\n'
        print msg

    # Now setup TVTK itself.
    from tvtk_classes import tvtk_helper
    tvtk = tvtk_helper.TVTK()

    # Clean up names users should not see.
    del tvtk_helper, vtk

# Clean up names users should not see.
del _zip, sys, exists, join, dirname
