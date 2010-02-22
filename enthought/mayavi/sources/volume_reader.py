"""A Volume file reader"""
# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Str
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.api import tvtk

# Local imports.
from enthought.mayavi.core.source import Source
from enthought.mayavi.core.pipeline_info import PipelineInfo


########################################################################
# `VolumeReader` class
########################################################################
class VolumeReader(Source):

    """A Volume reader. 
    """

    # The version of this class.  Used for persistence.
    __version__ = 0
    
    file_prefix = Str('', desc='File prefix for the volume files')

    # The VTK data file reader.
    reader = Instance(tvtk.Volume16Reader, args=(), allow_none=False,
                      record=True)
    
    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['image_data'])

    ########################################
    # View related code.
    # Our view.
    view = View(Group(Item(name='reader', style='custom',
                            resizable=True),
                      show_labels=False),
                resizable=True)                

    ######################################################################
    # `Source` interface
    ######################################################################
    
    def __init__(self, file_prefix='', configure=True, **traits):
        super(VolumeReader, self).__init__(**traits)            
        if configure:
            self.reader.edit_traits(kind='livemodal')
         
        self.file_prefix = self.reader.file_prefix
            
    def update(self):
        if len(self.file_prefix) == 0:
            return
        self.reader.update()
        self.render()


    ######################################################################
    # Non-public interface
    ######################################################################
    def _file_prefix_changed(self, value):
        if len(value) == 0:
            return
        else:
            self.reader.file_prefix = value
            self._update_reader_output()
        
    def _update_reader_output(self):
        self.reader.update()
        self.reader.update_information()
        self.reader.on_trait_change(self.render)
        self.outputs = [self.reader.output]
        self.data_changed = True   
