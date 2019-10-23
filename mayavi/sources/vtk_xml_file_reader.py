"""A VTK XML file reader object.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import basename

# Enthought library imports.
from traits.api import Instance, List, Str, Bool, Button
from traitsui.api import View, Group, Item, Include
from tvtk.api import tvtk

# Local imports.
from mayavi.core.common import error
from mayavi.core.file_data_source import FileDataSource
from mayavi.core.trait_defs import DEnum
from mayavi.core.pipeline_info import (PipelineInfo,
        get_tvtk_dataset_name)


######################################################################
# Utility functions.
######################################################################
def find_file_data_type(file_name):
    "Parses the named file to see what type of data there is."
    r = tvtk.XMLFileReadTester(file_name=file_name)
    if r.test_read_file():
        return r.file_data_type
    else:
        error("File %s is not a valid VTK XML file!"%(file_name))


def get_array_type(arr):
    """Returns if the array is a scalar ('scalars'), vector
    ('vectors') or tensor ('tensors').  It looks at the number of
    components to decide.  If it has a wierd number of components it
    returns the empty string.
    """
    n = arr.number_of_components
    ret = {1: 'scalars', 3: 'vectors', 4: 'scalars', 9:'tensors'}
    return ret.get(n) or ''


def get_attribute_list(data):
    """ Gets scalar, vector and tensor information from the given data
    (either cell or point data).
    """
    attr = {'scalars':[], 'vectors':[], 'tensors':[]}
    if data is not None:
        n = data.number_of_arrays
        for i in range(n):
            name = data.get_array_name(i)
            arr = data.get_array(i)
            if arr is not None:
                # Some VTK datasets claim they have n arrays, but
                # actually some of these are None (eg the output of a
                # tvtk.GraphToPolyData())
                t = get_array_type(arr)
                if len(t) > 0 and name is not None:
                    attr[t].extend([name])

    def _mk_first(lst, value):
        """Makes the specified `value` the first item in `lst`."""
        lst.remove(value)
        lst.insert(0, value)

    attr1 = attr.copy()
    for a in attr:
        v = getattr(data, a)
        if v is not None:
            name = v.name
            if name is not None:
                try:
                    _mk_first(attr[a], v.name)
                except ValueError:
                    # Sometimes we have a multi-component scalar.
                    attr1[a].insert(0, name)
    return attr1


def get_all_attributes(obj):
    """Gets the scalar, vector and tensor attributes that are
    available in the given VTK data object.
    """
    point_attr = get_attribute_list(obj.point_data)
    cell_attr = get_attribute_list(obj.cell_data)
    return point_attr, cell_attr


######################################################################
# `VTKXMLFileReader` class
######################################################################
class VTKXMLFileReader(FileDataSource):

    """A VTK XML file reader.  The reader supports all the different
    types of data sets.  This reader also supports a time series.
    Currently, this reader assumes that there is only one output that
    has configurable attributes.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    ########################################
    # Dynamic traits: These traits are dynamic and are automatically
    # updated depending on the contents of the file.

    # The active point scalar name.  An empty string indicates that
    # the attribute is "deactivated".  This is useful when you have
    # both point and cell attributes and want to use cell data by
    # default.
    point_scalars_name = DEnum(values_name='_point_scalars_list',
                               desc='scalar point data attribute to use')
    # The active point vector name.
    point_vectors_name = DEnum(values_name='_point_vectors_list',
                               desc='vectors point data attribute to use')
    # The active point tensor name.
    point_tensors_name = DEnum(values_name='_point_tensors_list',
                               desc='tensor point data attribute to use')

    # The active cell scalar name.
    cell_scalars_name = DEnum(values_name='_cell_scalars_list',
                               desc='scalar cell data attribute to use')
    # The active cell vector name.
    cell_vectors_name = DEnum(values_name='_cell_vectors_list',
                               desc='vectors cell data attribute to use')
    # The active cell tensor name.
    cell_tensors_name = DEnum(values_name='_cell_tensors_list',
                               desc='tensor cell data attribute to use')
    ########################################

    # The VTK data file reader.
    reader = Instance(tvtk.XMLReader)

    refresh = Button('Update reader')

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    # Our view.
    view = View(Group(Include('time_step_group'),
                      Item(name='point_scalars_name'),
                      Item(name='point_vectors_name'),
                      Item(name='point_tensors_name'),
                      Item(name='cell_scalars_name'),
                      Item(name='cell_vectors_name'),
                      Item(name='cell_tensors_name'),
                      Item(name='reader'),
                      Item(name='refresh', show_label=False)
                      ))

    ########################################
    # Private traits.

    # These private traits store the list of available data
    # attributes.  The non-private traits use these lists internally.
    _point_scalars_list = List(Str)
    _point_vectors_list = List(Str)
    _point_tensors_list = List(Str)
    _cell_scalars_list = List(Str)
    _cell_vectors_list = List(Str)
    _cell_tensors_list = List(Str)

    # This filter allows us to change the attributes of the data
    # object and will ensure that the pipeline is properly taken care
    # of.  Directly setting the array in the VTK object will not do
    # this.
    _assign_attribute = Instance(tvtk.AssignAttribute, args=(),
                                 allow_none=False)

    # Toggles if this is the first time this object has been used.
    _first = Bool(True)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(VTKXMLFileReader, self).__get_pure_state__()
        for name in ('_assign_attribute', '_first'):
            d.pop(name, None)
        # Pickle the 'point_scalars_name' etc. since these are
        # properties and not in __dict__.
        attr = {}
        for name in ('point_scalars', 'point_vectors',
                     'point_tensors', 'cell_scalars',
                     'cell_vectors', 'cell_tensors'):
            d.pop('_' + name + '_list', None)
            d.pop('_' + name + '_name', None)
            x = name + '_name'
            attr[x] = getattr(self, x)
        d.update(attr)
        return d

    def __set_pure_state__(self, state):
        # The reader has its own file_name which needs to be fixed.
        state.reader.file_name = state.file_path.abs_pth
        # Now call the parent class to setup everything.
        super(VTKXMLFileReader, self).__set_pure_state__(state)

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

        # Call the parent method to do its thing.  This will typically
        # start all our children.
        super(VTKXMLFileReader, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Call the parent method to do its thing.
        super(VTKXMLFileReader, self).stop()


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
        self.reader.update()
        pnt_attr, cell_attr = get_all_attributes(self.reader.output)

        def _setup_data_traits(obj, attributes, d_type):
            """Given the object, the dict of the attributes from the
            `get_all_attributes` function and the data type
            (point/cell) data this will setup the object and the data.
            """
            attrs = ['scalars', 'vectors', 'tensors']
            aa = obj._assign_attribute
            data = getattr(obj.reader.output, '%s_data'%d_type)
            for attr in attrs:
                values = attributes[attr]
                values.append('')
                setattr(obj, '_%s_%s_list'%(d_type, attr), values)
                if len(values) > 1:
                    default = getattr(obj, '%s_%s_name'%(d_type, attr))
                    if obj._first and len(default) == 0:
                        default = values[0]
                    getattr(data, 'set_active_%s'%attr)(default)
                    aa.assign(default, attr.upper(),
                              d_type.upper() +'_DATA')
                    aa.update()
                    kw = {'%s_%s_name'%(d_type, attr): default,
                          'trait_change_notify': False}
                    obj.trait_set(**kw)

        _setup_data_traits(self, cell_attr, 'cell')
        _setup_data_traits(self, pnt_attr, 'point')
        if self._first:
            self._first = False
        # Propagate the data changed event.
        self.data_changed = True

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
        else:
            if self.reader is None:
                d_type = find_file_data_type(fpath.get())
                self.reader = eval('tvtk.XML%sReader()'%d_type)
            reader = self.reader
            reader.file_name = value
            reader.update()
            aa = self._assign_attribute
            self.configure_input(aa, self.reader)
            self.update_data()
            aa.update()
            outputs = [aa]
            self.outputs = outputs

            self.output_info.datasets = [get_tvtk_dataset_name(outputs[0])]

            # Change our name on the tree view
            self.name = self._get_name()

    def _set_data_name(self, data_type, attr_type, value):
        if value is None:
            return

        reader_output = self.reader.output
        if len(value) == 0:
            # If the value is empty then we deactivate that attribute.
            d = getattr(reader_output, attr_type + '_data')
            method = getattr(d, 'set_active_%s'%data_type)
            method(None)
            self.data_changed = True
            return

        aa = self._assign_attribute
        data = None
        if attr_type == 'point':
            data = reader_output.point_data
        elif attr_type == 'cell':
            data = reader_output.cell_data

        method = getattr(data, 'set_active_%s'%data_type)
        method(value)
        aa.assign(value, data_type.upper(), attr_type.upper() +'_DATA')
        aa.update()
        # Fire an event, so the changes propagate.
        self.data_changed = True

    def _point_scalars_name_changed(self, value):
        self._set_data_name('scalars', 'point', value)

    def _point_vectors_name_changed(self, value):
        self._set_data_name('vectors', 'point', value)

    def _point_tensors_name_changed(self, value):
        self._set_data_name('tensors', 'point', value)

    def _cell_scalars_name_changed(self, value):
        self._set_data_name('scalars', 'cell', value)

    def _cell_vectors_name_changed(self, value):
        self._set_data_name('vectors', 'cell', value)

    def _cell_tensors_name_changed(self, value):
        self._set_data_name('tensors', 'cell', value)

    def _get_name(self):
        """ Gets the name to display on the tree view.
        """
        fname = basename(self.file_path.get())
        ret = "VTK XML file (%s)"%fname
        if len(self.file_list) > 1:
            ret += " (timeseries)"
        if '[Hidden]' in self.name:
            ret += ' [Hidden]'

        return ret

    def _refresh_fired(self):
        self.reader.modified()
        self.update_data()
