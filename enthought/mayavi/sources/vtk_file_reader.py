"""A VTK file reader object.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought library imports.
from enthought.traits.api import Trait, Instance, List, Str
from enthought.traits.ui.api import View, Group, Item, Include
from enthought.tvtk.api import tvtk

# Local imports.
from enthought.mayavi.core.file_data_source import FileDataSource
from enthought.mayavi.core.traits import DEnum


########################################################################
# `VTKFileReader` class
########################################################################
class VTKFileReader(FileDataSource):

    """A VTK file reader.  This does not handle the new XML file
    format but only the older format.  The reader supports all the
    different types of data sets.  This reader also supports a time
    series.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    ########################################
    # Dynamic traits: These traits are dummies and are dynamically
    # updated depending on the contents of the file.

    # The active scalar name.
    scalars_name = DEnum(values_name='_scalars_list',
                         desc='scalar data attribute to use')
    # The active vector name.
    vectors_name = DEnum(values_name='_vectors_list',
                         desc='vector data attribute to use')
    # The active tensor name.
    tensors_name = DEnum(values_name='_tensors_list',
                         desc='tensor data attribute to use')

    # The active normals name.
    normals_name = DEnum(values_name='_normals_list',
                         desc='normals to use')
    # The active tcoord name.
    t_coords_name = DEnum(values_name='_t_coords_list',
                          desc='t_coords data to use')
    # The active field_data name.
    field_data_name = DEnum(values_name='_field_data_list',
                            desc='field data to use')
    ########################################

    # The VTK data file reader.
    reader = Instance(tvtk.DataSetReader, args=())    

    # Our view.
    view = View(Group(Include('time_step_group'),
                      Item(name='scalars_name'),
                      Item(name='vectors_name'),
                      Item(name='tensors_name'),
                      Item(name='normals_name'),
                      Item(name='t_coords_name'),
                      Item(name='field_data_name'),
                      Item(name='reader'),
                      ))

    ########################################
    # Private traits.

    # These private traits store the list of available data
    # attributes.  The non-private traits use these lists internally.
    _scalars_list = List(Str)
    _vectors_list = List(Str)
    _tensors_list = List(Str)
    _normals_list = List(Str)
    _t_coords_list = List(Str)
    _field_data_list = List(Str)    

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(VTKFileReader, self).__get_pure_state__()
        # These traits are dynamically created.
        for name in ('scalars', 'vectors', 'tensors',
                     'normals', 't_coords', 'field_data'):
            d.pop('_' + name + '_list', None)
            d.pop('_' + name + '_name', None)

        return d
        
    def __set_pure_state__(self, state):
        # The reader has its own file_name which needs to be fixed.
        state.reader.file_name = state.file_path.abs_pth
        # Now call the parent class to setup everything.
        super(VTKFileReader, self).__set_pure_state__(state)

    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.
        """
        # Do nothing if we are already running.
        if self.running:
            return

        # Update the data just in case.
        self.update_data()
        self.update()

        # Call the parent method to do its thing.  This will typically
        # start all our children.
        super(VTKFileReader, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Call the parent method to do its thing.
        super(VTKFileReader, self).stop()
    
    
    ######################################################################
    # `FileDataSource` interface
    ######################################################################
    def update(self):
        if len(self.file_path.get()) == 0:
            return
        reader = self.reader
        reader.update()
        self.render()

    def update_data(self):
        if len(self.file_path.get()) == 0:
            return
        attrs = ['scalars', 'vectors', 'tensors', 'normals',
                 't_coords', 'field_data']
        reader = self.reader
        for attr in attrs:
            n = getattr(reader, 'number_of_%s_in_file'%attr)
            method = getattr(reader, 'get_%s_name_in_file'%attr)
            values = [method(x) for x in range(n)]
            setattr(self, '_%s_list'%attr, values)
    
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
            self.update_data()
            self.update()
            
            # Setup the outputs by resetting self.outputs.  Changing
            # the outputs automatically fires a pipeline_changed
            # event.
            try:
                n = self.reader.number_of_outputs
            except AttributeError: # for VTK >= 4.5
                n = self.reader.number_of_output_ports
            outputs = []
            for i in range(n):
                outputs.append(self.reader.get_output(i))
            self.outputs = outputs

            # Fire data_changed just in case the outputs are not
            # really changed.  This can happen if the dataset is of
            # the same type as before.
            self.data_changed = True

            # Change our name on the tree view
            self.name = self._get_name()

    def _set_data_name(self, data_type, value):
        if not value or not data_type:
            return
        reader = self.reader
        setattr(reader, data_type, value)
        self.update()
        # Fire an event, so the changes propagate.
        self.data_changed = True

    def _scalars_name_changed(self, value):
        self._set_data_name('scalars_name', value)

    def _vectors_name_changed(self, value):
        self._set_data_name('vectors_name', value)

    def _tensors_name_changed(self, value):
        self._set_data_name('tensors_name', value)

    def _normals_name_changed(self, value):
        self._set_data_name('normals_name', value)

    def _t_coords_name_changed(self, value):
        self._set_data_name('t_coords_name', value)

    def _field_data_name_changed(self, value):
        self._set_data_name('field_data_name', value)

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

