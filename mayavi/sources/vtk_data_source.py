"""This source manages a VTK dataset given to it.  When this source is
pickled or persisted, it saves the data given to it in the form of a
gzipped string.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2015, Enthought, Inc.
# License: BSD Style.

import sys
import os
import tempfile

import numpy as np

# Enthought library imports.
from traits.api import Instance, List, Str, Bool, Int
from traitsui.api import View, Group, Item
from apptools.persistence.state_pickler \
     import gzip_string, gunzip_string, set_state

# Local imports.
from tvtk.api import tvtk
from tvtk import messenger
from tvtk.array_handler import array2vtk
from tvtk.common import is_old_pipeline, configure_input_data
from mayavi.core.source import Source
from mayavi.core.common import handle_children_state
from mayavi.core.trait_defs import DEnum
from mayavi.core.pipeline_info import (PipelineInfo,
                                       get_tvtk_dataset_name)
from .utils import has_attributes
from .vtk_xml_file_reader import get_all_attributes


######################################################################
# Utility functions.
######################################################################
def write_dataset_to_string(data):
    """Given a dataset, convert the dataset to an ASCII string that can
    be stored for persistence.
    """
    w = tvtk.DataSetWriter(write_to_output_string=1)
    warn = w.global_warning_display
    configure_input_data(w, data)
    w.global_warning_display = 0
    w.update()
    if w.output_string_length == 0:
        # Some VTK versions (5.2) have a bug when writing structured
        # grid datasets and produce empty output.  We work around this
        # by writing to a file and then reading that output.
        w.write_to_output_string = 0
        fh, fname = tempfile.mkstemp('.vtk')
        os.close(fh); os.remove(fname)
        w.file_name = fname
        w.write()
        # Read the data and delete the file.
        sdata = open(fname).read()
        os.remove(fname)
    else:
        sdata = w.output_string
    w.global_warning_display = warn
    return sdata


######################################################################
# `VTKDataSource` class
######################################################################
class VTKDataSource(Source):

    """This source manages a VTK dataset given to it.  When this
    source is pickled or persisted, it saves the data given to it in
    the form of a gzipped string.

    Note that if the VTK dataset has changed internally and you need
    to notify the mayavi pipeline to flush the data just call the
    `modified` method of the VTK dataset and the mayavi pipeline will
    update automatically.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The VTK dataset to manage.
    data = Instance(tvtk.DataSet, allow_none=False)

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    ########################################
    # Dynamic traits: These traits are dynamic and are updated on the
    # _update_data method.

    # The active point scalar name.
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
    # Our view.

    view = View(Group(Item(name='point_scalars_name'),
                      Item(name='point_vectors_name'),
                      Item(name='point_tensors_name'),
                      Item(name='cell_scalars_name'),
                      Item(name='cell_vectors_name'),
                      Item(name='cell_tensors_name'),
                      Item(name='data'),
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

    # The ID of the observer for the data.
    _observer_id = Int(-1)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(VTKDataSource, self).__get_pure_state__()
        for name in ('_assign_attribute', '_first', '_observer'):
            d.pop(name, None)
        for name in ('point_scalars', 'point_vectors',
                     'point_tensors', 'cell_scalars',
                     'cell_vectors', 'cell_tensors'):
            d.pop('_' + name + '_list', None)
            d.pop('_' + name + '_name', None)
        data = self.data
        if data is not None:
            sdata = write_dataset_to_string(data)
            if sys.version_info[0] > 2:
                z = gzip_string(sdata.encode('ascii'))
            else:
                z = gzip_string(sdata)
            d['data'] = z
        return d

    def __set_pure_state__(self, state):
        z = state.data
        if z is not None:
            if sys.version_info[0] > 2:
                d = gunzip_string(z).decode('ascii')
            else:
                d = gunzip_string(z)
            r = tvtk.DataSetReader(read_from_input_string=1,
                                   input_string=d)
            warn = r.global_warning_display
            r.global_warning_display = 0
            r.update()
            r.global_warning_display = warn
            self.data = r.output
        # Now set the remaining state without touching the children.
        set_state(self, state, ignore=['children', 'data'])
        # Setup the children.
        handle_children_state(self.children, state.children)
        # Setup the children's state.
        set_state(self, state, first=['children'], ignore=['*'])

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
        self._update_data()

        # Call the parent method to do its thing.  This will typically
        # start all our children.
        super(VTKDataSource, self).start()

    def update(self):
        """Invoke this to flush data changes downstream.  This is
        typically used when you change the data object and want the
        mayavi pipeline to refresh.
        """
        # This tells the VTK pipeline that the data has changed.  This
        # will fire the data_changed event automatically.
        self.data.modified()
        if has_attributes(self.data):
            self._assign_attribute.update()

    def add_attribute(self, array, name, category='point'):
        """Add an attribute to the dataset to specified category ('point' or
        'cell').

        One may add a scalar, vector (3/4 components) or a tensor (9 components).

        Note that it is the user's responsibility to set the correct size of
        the arrays.

        Parameters
        ----------

        array: numpy array/list : array data to add.

        name: str: name of the array.

        category: 'point'/'cell': the category of the attribute data.

        """
        array = np.asarray(array)
        assert len(array.shape) <= 2, "Only 2D arrays can be added."
        data = getattr(self.data, '%s_data' % category)
        if len(array.shape) == 2:
            assert array.shape[1] in [1, 3, 4, 9], \
                    "Only Nxm arrays where (m in [1,3,4,9]) are supported"
            va = tvtk.to_tvtk(array2vtk(array))
            va.name = name
            data.add_array(va)
            mapping = {1: 'scalars', 3: 'vectors', 4: 'scalars',
                       9: 'tensors'}
            attribute = '_%s_%s_list' % (category, mapping[array.shape[1]])
        else:
            va = tvtk.to_tvtk(array2vtk(array))
            va.name = name
            data.add_array(va)
            attribute = '_%s_scalars_list' % category
        names = set(getattr(self, attribute) + [name])
        setattr(self, attribute, sorted(names))

    def remove_attribute(self, name, category='point'):
        """Remove an attribute by its name and optional category (point and
        cell).  Returns the removed array.
        """
        type = self._find_array_list(name, category)
        data = getattr(self.data, '%s_data' % category)
        data.remove_array(name)
        attr_list = getattr(self, '_%s_%s_list' % (category, type))
        return attr_list.remove(name)

    def rename_attribute(self, name1, name2, category='point'):
        """Rename a particular attribute from `name1` to `name2`.
        """
        type = self._find_array_list(name1, category)
        data = getattr(self.data, '%s_data' % category)
        arr = data.get_array(name1)
        arr.name = name2
        attribute = '_%s_%s_list' % (category, type)
        attr_list = getattr(self, attribute)
        attr_list.remove(name1)
        attr_list.append(name2)
        setattr(self, attribute, sorted(attr_list))

    ######################################################################
    # Non-public interface
    ######################################################################
    def _data_changed(self, old, new):
        if has_attributes(self.data):
            aa = self._assign_attribute
            self.configure_input_data(aa, new)
            self._update_data()
            aa.update()
            self.outputs = [aa]
        else:
            tp = tvtk.TrivialProducer()
            tp.set_output(self.data)
            self.outputs = [tp]
        self.data_changed = True

        self.output_info.datasets = [get_tvtk_dataset_name(self.outputs[0])]

        # Add an observer to the VTK dataset after removing the one
        # for the old dataset.  We use the messenger to avoid an
        # uncollectable reference cycle.  See the
        # tvtk.messenger module documentation for details.
        if old is not None:
            old.remove_observer(self._observer_id)
        self._observer_id = new.add_observer('ModifiedEvent',
                                             messenger.send)
        new_vtk = tvtk.to_vtk(new)
        messenger.connect(new_vtk, 'ModifiedEvent',
                          self._fire_data_changed)

        # Change our name so that our label on the tree is updated.
        self.name = self._get_name()

    def _fire_data_changed(self, *args):
        """Simply fire the `data_changed` event."""
        self.data_changed = True

    def _set_data_name(self, data_type, attr_type, value):
        if value is None:
            return

        dataset = self.data
        if len(value) == 0:
            # If the value is empty then we deactivate that attribute.
            d = getattr(dataset, attr_type + '_data')
            method = getattr(d, 'set_active_%s'%data_type)
            method(None)
            self.data_changed = True
            return

        aa = self._assign_attribute
        data = None
        if attr_type == 'point':
            data = dataset.point_data
        elif attr_type == 'cell':
            data = dataset.cell_data
        method = getattr(data, 'set_active_%s'%data_type)
        method(value)
        aa.assign(value, data_type.upper(), attr_type.upper() +'_DATA')
        if data_type == 'scalars' and dataset.is_a('vtkImageData'):
            # Set the scalar_type for image data, if not you can either
            # get garbage rendered or worse.
            s = getattr(dataset, attr_type + '_data').scalars
            r = s.range
            if is_old_pipeline():
                dataset.scalar_type = s.data_type
                aa.output.scalar_type = s.data_type
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

    def _update_data(self):
        if self.data is None:
            return
        pnt_attr, cell_attr = get_all_attributes(self.data)

        pd = self.data.point_data
        scalars = pd.scalars
        if self.data.is_a('vtkImageData') and scalars is not None:
            # For some reason getting the range of the scalars flushes
            # the data through to prevent some really strange errors
            # when using an ImagePlaneWidget.
            r = scalars.range
            if is_old_pipeline():
                self._assign_attribute.output.scalar_type = scalars.data_type
                self.data.scalar_type = scalars.data_type

        def _setup_data_traits(obj, attributes, d_type):
            """Given the object, the dict of the attributes from the
            `get_all_attributes` function and the data type
            (point/cell) data this will setup the object and the data.
            """
            attrs = ['scalars', 'vectors', 'tensors']
            aa = obj._assign_attribute
            data = getattr(obj.data, '%s_data'%d_type)
            for attr in attrs:
                values = sorted(attributes[attr])
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

        _setup_data_traits(self, pnt_attr, 'point')
        _setup_data_traits(self, cell_attr, 'cell')
        if self._first:
            self._first = False
        # Propagate the data changed event.
        self.data_changed = True

    def _get_name(self):
        """ Gets the name to display on the tree.
        """
        ret = "VTK Data (uninitialized)"
        if self.data is not None:
            typ = self.data.__class__.__name__
            ret = "VTK Data (%s)" % typ
        if '[Hidden]' in self.name:
            ret += ' [Hidden]'
        return ret

    def _find_array_list(self, name, category='point'):
        """Return information on which kind of attribute contains the
        specified named array in a particular category."""
        types = ['scalars', 'vectors', 'tensors']
        for type in types:
            attr = '_%s_%s_list' % (category, type)
            names = getattr(self, attr)
            if name in names:
                return type
        raise KeyError('No %s array named %s available in dataset'
                       % (category, name))
