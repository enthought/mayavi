# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, List, Str, Bool
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from tvtk.common import is_old_pipeline

# Local imports.
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.filter import Filter
from mayavi.core.trait_defs import DEnum
from mayavi.sources.vtk_xml_file_reader import get_all_attributes

################################################################################
# `SetActiveAttribute` class.
################################################################################
class SetActiveAttribute(Filter):
    """
    This filter lets a user set the active data attribute (scalars,
    vectors and tensors) on a VTK dataset.  This is particularly useful
    if you need to do something like compute contours of one scalar on
    the contour of another scalar.
    """

    # Note: most of this code is from the XMLFileDataReader.

    # The version of this class.  Used for persistence.
    __version__ = 0

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

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

    # Our view.
    view = View(Group(Item(name='point_scalars_name'),
                      Item(name='point_vectors_name'),
                      Item(name='point_tensors_name'),
                      Item(name='cell_scalars_name'),
                      Item(name='cell_vectors_name'),
                      Item(name='cell_tensors_name'),
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
        d = super(SetActiveAttribute, self).__get_pure_state__()
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

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def update_data(self):
        self.data_changed = True

    def update_pipeline(self):
        if len(self.inputs) == 0 or len(self.inputs[0].outputs) == 0:
            return

        aa = self._assign_attribute
        self.configure_connection(aa, self.inputs[0])
        self._update()
        self._set_outputs([aa])

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _update(self):
        """Updates the traits for the fields that are available in the
        input data.
        """
        if len(self.inputs) == 0 or len(self.inputs[0].outputs) == 0:
            return

        input = self.inputs[0].get_output_object()
        if self._first and is_old_pipeline():
            # Force all attributes to be defined and computed
            input.update()
        pnt_attr, cell_attr = get_all_attributes(
            self.inputs[0].get_output_dataset()
        )

        self._setup_data_traits(cell_attr, 'cell')
        self._setup_data_traits(pnt_attr, 'point')
        if self._first:
            self._first = False

    def _setup_data_traits(self, attributes, d_type):
        """Given the dict of the attributes from the
        `get_all_attributes` function and the data type (point/cell)
        data this will setup the object and the data.
        """
        attrs = ['scalars', 'vectors', 'tensors']
        aa = self._assign_attribute
        input = self.inputs[0].get_output_dataset()
        data = getattr(input, '%s_data'%d_type)
        for attr in attrs:
            values = attributes[attr]
            values.append('')
            setattr(self, '_%s_%s_list'%(d_type, attr), values)
            if len(values) > 1:
                default = getattr(self, '%s_%s_name'%(d_type, attr))
                if self._first and len(default) == 0:
                    default = values[0]
                getattr(data, 'set_active_%s'%attr)(default)
                aa.assign(default, attr.upper(),
                          d_type.upper() +'_DATA')
                aa.update()
                kw = {'%s_%s_name'%(d_type, attr): default,
                      'trait_change_notify': False}
                self.trait_set(**kw)

    def _set_data_name(self, data_type, attr_type, value):
        if value is None or len(self.inputs) == 0:
            return

        input = self.inputs[0].get_output_dataset()
        if len(value) == 0:
            # If the value is empty then we deactivate that attribute.
            d = getattr(input, attr_type + '_data')
            method = getattr(d, 'set_active_%s'%data_type)
            method(None)
            self.data_changed = True
            return

        aa = self._assign_attribute
        data = None
        if attr_type == 'point':
            data = input.point_data
        elif attr_type == 'cell':
            data = input.cell_data

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
