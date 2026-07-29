"""Abstracts all VTK related modules into one module.  This makes it trivial to
support local VTK classes that a user may have built.

By default it imports all of VTK and then looks for a tvtk_local module and
imports everything from that.  In order to add local classes to the TVTK build
one may simply provide a tvtk_local.py module somewhere with any classes that
need to be wrapped.

"""

# Author: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007-2021,  Enthought, Inc.
# License: BSD Style.

from vtk import *
try:
    from vtk.util.vtkAlgorithm import VTKPythonAlgorithmBase
except ImportError:
    pass

try:
    from tvtk_local import *
except ImportError:
    pass


vtk_version = vtkVersion.GetVTKVersion()

# Remove classes that crash or hang when wrapped on a specific runtime VTK.
# Deleting the name here hides the class from code generation (code_gen.py
# checks hasattr) and from wrapping.  See tvtk/WORKAROUNDS.md for the full
# map of where VTK workarounds live.
if vtk_version in ["9.4.0", "9.4.1", "9.4.2"]:
    # Instantiating these using TVTK causes a crash on VTK 9.4.x so skipping.
    try:
        del vtkIOSSReader, vtkIOSSCellGridReader
    except NameError:
        pass
    if vtk_version == "9.4.2":
        # vtkXOpenGLRenderWindow segfaults when being deconstructed on 9.4.2
        try:
            del vtkXOpenGLRenderWindow
        except NameError:
            pass
