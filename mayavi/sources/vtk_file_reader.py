"""A VTK file reader object.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2015, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports.
from mayavi.core.pipeline_info import (PipelineInfo,
        get_tvtk_dataset_name)
from .utils import has_attributes
from .vtk_xml_file_reader import VTKXMLFileReader


########################################################################
# `VTKFileReader` class
########################################################################
class VTKFileReader(VTKXMLFileReader):

    """A VTK file reader.  This does not handle the new XML file
    format but only the older format.  The reader supports all the
    different types of data sets.  This reader also supports a time
    series.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The VTK data file reader.
    reader = Instance(tvtk.DataSetReader, args=(),
                      kw={'read_all_scalars':True,
                          'read_all_vectors': True,
                          'read_all_tensors': True,
                          'read_all_fields': True} )

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `FileDataSource` interface
    ######################################################################

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
            self.name = 'No VTK file'
            return
        else:
            self.reader.file_name = value
            self.update()

            # Setup the outputs by resetting self.outputs.  Changing
            # the outputs automatically fires a pipeline_changed
            # event.
            try:
                n = self.reader.number_of_outputs
            except AttributeError: # for VTK >= 4.5
                n = self.reader.number_of_output_ports

            if n > 0:
                outputs = []
                for i in range(n):
                    outputs.append(self.reader.get_output(i))

                # FIXME: currently handling only one output (the first one)
                # with assign attributes.
                if has_attributes(outputs[0]):
                    aa = self._assign_attribute
                    self.configure_input_data(aa, outputs[0])
                    self.update_data()
                    aa.update()
                    outputs[0] = aa.output

                self.outputs = outputs

                # FIXME: The output info is only based on the first output.
                self.output_info.datasets = [get_tvtk_dataset_name(outputs[0])]

            # Change our name on the tree view
            self.name = self._get_name()

    def _get_name(self):
        """ Gets the name to display on the tree view.
        """
        fname = basename(self.file_path.get())
        ret = "VTK file (%s)"%fname
        if len(self.file_list) > 1:
            ret += " (timeseries)"
        if '[Hidden]' in self.name:
            ret += ' [Hidden]'

        return ret
