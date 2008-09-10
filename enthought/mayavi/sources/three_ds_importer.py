"""An importer for 3D Studio files.

"""
# Author: Prabhu Ramachandran <prabhu at aero dot iitb dot ac dot in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought imports.
from enthought.tvtk.api import tvtk
from enthought.traits.api import Instance

# Local imports
from enthought.mayavi.sources.vrml_importer import VRMLImporter


######################################################################
# `ThreeDSImporter` class.
######################################################################
class ThreeDSImporter(VRMLImporter):

    # The 3DS importer.
    reader = Instance(tvtk.ThreeDSImporter, args=(),
                      kw={'compute_normals':True},
                      allow_none=False, record=True)

    ######################################################################
    # Non-public interface
    ######################################################################
    def _file_name_changed(self, value):
        # This hack is necessary since for some reason the importer
        # does not clear out the earlier actors.
        self.reader = reader = tvtk.ThreeDSImporter(compute_normals=True)
        reader.file_name = value
        if self.scene is not None:
            self.reader.render_window = self.scene.render_window

        name = "3DStudio file (%s)"%basename(self.file_name)
        if '[Hidden]' in self.name:
            name += ' [Hidden]'
        self.name = name

        self._file_path.set(value)
        self._update_reader()
        self.render()
