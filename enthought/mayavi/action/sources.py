"""An action to open various source files.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import isfile

# Enthought library imports.
from enthought.pyface.api import FileDialog, OK
from enthought.pyface.action.api import Action

# Local imports
from enthought.mayavi.plugins.script import get_imayavi
from enthought.mayavi.core.common import error


######################################################################
# Utility functions
######################################################################
def get_scene(mayavi):
    """Given a mayavi script instance, get the current scene.  If none
    is available create a new one.
    """
    s = mayavi.engine.current_scene
    if s is None:
        mayavi.engine.new_scene()
        s = mayavi.engine.current_scene
    return s

######################################################################
# `OpenImageFile` class.
######################################################################
class OpenImageFile(Action):
    """ An action that opens a new image file. """

    tooltip       = "Import a PNG/JPG/BMP/PNM/TIFF image"

    description   = "Import a PNG/JPG/BMP/PNM/TIFF image"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = 'All files (*.*)|*.*|' \
                   'PNG files (*.png)|*.png|'\
                   'JPEG files (*.jpg)|*.jpg|'\
                   'JPEG files (*.jpeg)|*.jpeg|'\
                   'BMP files (*.bmp)|*.bmp|'\
                   'PNM files (*.pnm)|*.pnm|'\
                   'TIFF files (*.tiff)|*.tiff'
                   
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open PNG/JPG/BMP/PNM/TIFF images',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            from enthought.mayavi.sources.image_reader import ImageReader
            try:
                s.scene.busy = True
                r = ImageReader()
                r.initialize(dialog.path)
                mv.add_source(r)
            finally:
                s.scene.busy = False

######################################################################
# `Open3DSFile` class.
######################################################################
class Open3DSFile(Action):
    """ An action that opens a new 3DS file. """

    tooltip       = "Import a 3D Studio file"

    description   = "Import a 3D Studio file"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = '3D Studio files (*.3ds)|*.3ds|' + FileDialog.WILDCARD_ALL
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open 3D Studio file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            from enthought.mayavi.sources.three_ds_importer import ThreeDSImporter
            try:
                s.scene.busy = True
                r = ThreeDSImporter()
                r.initialize(dialog.path)
                mv.add_source(r)
            finally:
                s.scene.busy = False


######################################################################
# `OpenPLOT3DFile` class.
######################################################################
class OpenPLOT3DFile(Action):
    """ An action that opens a new PLOT3D file. """

    tooltip       = "Open a PLOT3D data file"

    description   = "Open a PLOT3D data file"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = FileDialog.WILDCARD_ALL
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open PLOT3D XYZ co-ordinate file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
        else:
            return
        xyz = dialog.path
        dialog = FileDialog(parent=parent,
                            title='Open PLOT3D Q solution file',
                            action='open', wildcard=wildcard
                            )
        q = ''
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
            q = dialog.path
            
        from enthought.mayavi.sources.plot3d_reader import PLOT3DReader
        try:
            s.scene.busy = True
            r = PLOT3DReader()
            r.initialize(xyz, q)
            mv.add_source(r)
        finally:
            s.scene.busy = False


######################################################################
# `OpenVRMLFile` class.
######################################################################
class OpenVRMLFile(Action):
    """ An action that opens a new VRML file. """

    tooltip       = "Import a VRML2 data file"

    description   = "Import a VRML2 data file"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = 'VRML2 files (*.wrl)|*.wrl|' + FileDialog.WILDCARD_ALL
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open VRML2 file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            from enthought.mayavi.sources.vrml_importer import VRMLImporter
            try:
                s.scene.busy = True
                r = VRMLImporter()
                r.initialize(dialog.path)
                mv.add_source(r)
            finally:
                s.scene.busy = False


######################################################################
# `OpenVTKFile` class.
######################################################################
class OpenVTKFile(Action):
    """ An action that opens a new VTK file. """

    tooltip       = "Open a VTK data file"

    description   = "Open a VTK data file"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = 'VTK files (*.vtk)|*.vtk|' + FileDialog.WILDCARD_ALL
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open VTK file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            from enthought.mayavi.sources.vtk_file_reader import VTKFileReader

            try:
                s.scene.busy = True
                r = VTKFileReader()
                r.initialize(dialog.path)
                mv.add_source(r)
            finally:
                s.scene.busy = False


######################################################################
# `OpenVTKXMLFile` class.
######################################################################
class OpenVTKXMLFile(Action):
    """ An action that opens a new VTK XML file. """

    tooltip       = "Open a VTK XML data file"

    description   = "Open a VTK XML data file"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return

        wildcard = 'All files (*.*)|*.*|' \
                   'VTK XML files (*.xml)|*.xml|'\
                   'Image Data (*.vti)|*.vti|'\
                   'Poly Data (*.vtp)|*.vtp|'\
                   'Rectilinear Grid (*.vtr)|*.vtr|'\
                   'Structured Grid (*.vts)|*.vts|'\
                   'Unstructured Grid (*.vtu)|*.vtu|'\
                   'Parallel Image Data (*.pvti)|*.pvti|'\
                   'Parallel Poly Data (*.pvtp)|*.pvtp|'\
                   'Parallel Rectilinear Grid (*.pvtr)|*.pvtr|'\
                   'Parallel Structured Grid (*.pvts)|*.pvts|'\
                   'Parallel Unstructured Grid (*.pvtu)|*.pvtu'
                   
        parent = self.window.control
        dialog = FileDialog(parent=parent,
                            title='Open VTK XML file',
                            action='open', wildcard=wildcard
                            )
        if dialog.open() == OK:
            if not isfile(dialog.path):
                error("File '%s' does not exist!"%dialog.path, parent)
                return
            from enthought.mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader
            try:
                s.scene.busy = True
                r = VTKXMLFileReader()
                r.initialize(dialog.path)
                mv.add_source(r)
            finally:
                s.scene.busy = False


######################################################################
# `ParametricSurfaceSource` class.
######################################################################
class ParametricSurfaceSource(Action):
    """ An action that creates a ParametricSurface source. """

    tooltip       = "Create a parametric surface source"

    description   = "Create a parametric surface source"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return
        from enthought.mayavi.sources.parametric_surface import ParametricSurface
        s = ParametricSurface()
        mv.add_source(s)


######################################################################
# `PointLoadSource` class.
######################################################################
class PointLoadSource(Action):
    """ An action that creates a PointLoad source. """

    tooltip       = "Simulates a point load on a cube of data (for tensors)"

    description   = "Simulates a point load on a cube of data (for tensors)"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        mv = get_imayavi(self.window)
        s = get_scene(mv)
        if s is None:
            return
        from enthought.mayavi.sources.point_load import PointLoad
        s = PointLoad()
        mv.add_source(s)
