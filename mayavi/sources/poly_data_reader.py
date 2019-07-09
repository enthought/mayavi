"""A PolyData file reader object.
"""
# Author:   R.Sreekanth <sreekanth [at] aero.iitb.ac.in>
#               Suyog Dutt Jain <suyog.jain [at] aero.iitb.ac.in>
# Copyright (c) 2009-2015, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought imports.
from traits.api import Instance, Str,Dict
from traitsui.api import View, Item, Group, Include
from tvtk.api import tvtk

# Local imports
from mayavi.core.file_data_source import FileDataSource
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.common import error

########################################################################
# `PolyDataReader` class
########################################################################
class PolyDataReader(FileDataSource):

    """A PolyData file reader. The reader supports all the
    different types of poly data files.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The PolyData file reader
    reader = Instance(tvtk.Object, allow_none=False,
                      record=True)

    ######################################################################
    # Private Traits
    _reader_dict = Dict(Str, Instance(tvtk.Object))

    # Our View.
    view = View(Group(Include('time_step_group'),
                      Item(name='base_file_name'),
                      Item(name='reader',
                           style='custom',
                           resizable=True),
                      show_labels=False),
                resizable=True)

    #output_info = PipelineInfo(datasets=['none'])
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])


    ######################################################################
    # `object` interface
    ######################################################################
    def __set_pure_state__(self, state):
        # The reader has its own file_name which needs to be fixed.
        state.reader.file_name = state.file_path.abs_pth
        # Now call the parent class to setup everything.
        super(PolyDataReader, self).__set_pure_state__(state)

    ######################################################################
    # `FileDataSource` interface
    ######################################################################
    def update(self):
        self.reader.update()
        if len(self.file_path.get()) == 0:
            return
        self.render()

    def has_output_port(self):
        """ Return True as the reader has output port."""
        return True

    def get_output_object(self):
        """ Return the reader output port."""
        return self.reader.output_port

    ######################################################################
    # Non-public interface
    ######################################################################
    def _file_path_changed(self, fpath):
        value = fpath.get()
        if len(value) == 0:
            return

        # Extract the file extension
        splitname = value.strip().split('.')
        extension = splitname[-1].lower()
        # Select polydata reader based on file type
        old_reader = self.reader
        if extension in self._reader_dict:
            self.reader = self._reader_dict[extension]
        else:
            error('Invalid extension for file: %s'%value)
            return

        old_fname = self.reader.file_name
        self.reader.file_name = value.strip()
        self.reader.update()
        self.reader.update_information()

        if old_reader is not None:
            old_reader.on_trait_change(self.render, remove=True)
        self.reader.on_trait_change(self.render)

        self.outputs = [self.reader]
        if old_fname != value:
            self.data_changed = True

        # Change our name on the tree view
        self.name = self._get_name()

    def _get_name(self):
        """ Returns the name to display on the tree view.  Note that
        this is not a property getter.
        """
        fname = basename(self.file_path.get())
        ret = "%s"%fname
        if len(self.file_list) > 1:
            ret += " (timeseries)"
        if '[Hidden]' in self.name:
            ret += ' [Hidden]'

        return ret

    def __reader_dict_default(self):
        """Default value for reader dict."""
        rd = {'stl':tvtk.STLReader(),
             'stla':tvtk.STLReader(),
             'stlb':tvtk.STLReader(),
             'txt':tvtk.SimplePointsReader(),
             'raw':tvtk.ParticleReader(),
             'ply':tvtk.PLYReader(),
             'pdb':tvtk.PDBReader(),
             'slc':tvtk.SLCReader(),
             'xyz':tvtk.XYZMolReader(),
             'obj':tvtk.OBJReader(),
             'facet':tvtk.FacetReader(),
             'cube':tvtk.GaussianCubeReader(),
             'g':tvtk.BYUReader(),
            }
        return rd

    # Callable to check if the reader can actually read the file
    @classmethod
    def can_read(cls,filename):
        """ Class method to check if the reader can actually
        read the file. Returns 'True' if it can read it succesfully
        else 'False'
        """
        # Extract the file extension
        splitname = filename.strip().split('.')
        extension = splitname[-1].lower()

        if extension == 'xyz':
            from vtk import vtkObject
            o = vtkObject
            w = o.GetGlobalWarningDisplay()
            o.SetGlobalWarningDisplay(0) # Turn it off.

            r = tvtk.XYZMolReader()
            r.file_name = filename
            r.update()
            o.SetGlobalWarningDisplay(w)

            if len(r.output.points) != 0:
                return True
            return False

        return None
