"""A Chaco file reader.
"""
# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Str
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports.
from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo

########################################################################
# `ChacoReader` class
########################################################################
class ChacoReader(Source):

    """A Chaco reader.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    base_name = Str('', desc='basename of the Chaco files')

    # The VTK data file reader.
    reader = Instance(tvtk.ChacoReader, args=(), allow_none=False,
                      record=True)

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['unstructured_grid'])

    ########################################
    # View related code.
    # Our view.
    view = View(Group(Item(name='reader', style='custom',
                           resizable=True),
                      show_labels=False),
                resizable=True)

    ######################################################################
    # `FileDataSource` interface
    ######################################################################
    def __init__(self, base_name='', configure=True, **traits):
        super(ChacoReader, self).__init__(**traits)
        if configure:
            self.reader.edit_traits(kind='livemodal')
        self.base_name = self.reader.base_name

    def update(self):
        if len(self.base_name) == 0:
            return
        self.reader.update()
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
    def _base_name_changed(self, value):
        if len(value) == 0:
            return
        else:
            self.reader.base_name = value
            self._update_reader_output()

    def _update_reader_output(self):
        self.reader.update()
        self.reader.update_information()
        self.reader.on_trait_change(self.render)
        self.outputs = [self.reader]
        self.data_changed = True
