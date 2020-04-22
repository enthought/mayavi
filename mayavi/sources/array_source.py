"""A simple source that allows one to view a suitably shaped numpy
array as ImageData.  This supports both scalar and vector data.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import numpy as np
from vtk.util import vtkConstants

# Enthought library imports
from traits.api import (Instance, Trait, Str, Bool, Button, DelegatesTo, List,
                        Int, OBJECT_IDENTITY_COMPARE)
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from tvtk.array_handler import array2vtk, get_vtk_array_type
from tvtk.common import is_old_pipeline
from tvtk.vtk_module import VTK_MAJOR_VERSION

# Local imports
from mayavi.core.source import Source
from mayavi.core.pipeline_info import PipelineInfo


def _check_scalar_array(obj, name, value):
    """Validates a scalar array passed to the object."""
    if value is None:
        return None
    arr = np.asarray(value)
    assert len(arr.shape) in [2, 3], "Scalar array must be 2 or 3 dimensional"
    vd = obj.vector_data
    if vd is not None:
        assert vd.shape[:-1] == arr.shape, \
               "Scalar array must match already set vector data.\n"\
               "vector_data.shape = %s, given array shape = %s" % (vd.shape,
                                                                   arr.shape)
    return arr


_check_scalar_array.info = 'a 2D or 3D numpy array'


def _check_vector_array(obj, name, value):
    """Validates a vector array passed to the object."""
    if value is None:
        return None
    arr = np.asarray(value)
    assert len(arr.shape) in [3, 4], "Vector array must be 3 or 4 dimensional"
    assert arr.shape[-1] == 3, \
        "The vectors must be three dimensional with `array.shape[-1] == 3`"
    sd = obj.scalar_data
    if sd is not None:
        assert arr.shape[:-1] == sd.shape, \
               "Vector array must match already set scalar data.\n"\
               "scalar_data.shape = %s, given array shape = %s" % (sd.shape,
                                                                   arr.shape)
    return arr


_check_vector_array.info = 'a 3D or 4D numpy array with shape[-1] = 3'


######################################################################
# 'ArraySource' class.
######################################################################
class ArraySource(Source):

    """A simple source that allows one to view a suitably shaped numpy
    array as ImageData.  This supports both scalar and vector data.
    """

    # The scalar array data we manage.
    scalar_data = Trait(
        None,
        _check_scalar_array,
        comparison_mode=OBJECT_IDENTITY_COMPARE
    )

    # The name of our scalar array.
    scalar_name = Str('scalar')

    # The vector array data we manage.
    vector_data = Trait(
        None,
        _check_vector_array,
        comparison_mode=OBJECT_IDENTITY_COMPARE
    )


    # The name of our vector array.
    vector_name = Str('vector')

    # The spacing of the points in the array.
    spacing = DelegatesTo('change_information_filter', 'output_spacing',
                          desc='the spacing between points in array')

    # The origin of the points in the array.
    origin = DelegatesTo('change_information_filter', 'output_origin',
                         desc='the origin of the points in array')

    # Fire an event to update the spacing and origin. This
    # is here for backwards compatability. Firing this is no
    # longer needed.
    update_image_data = Button('Update spacing and origin')

    # The image data stored by this instance.
    image_data = Instance(tvtk.ImageData, (), allow_none=False)

    # Use an ImageChangeInformation filter to reliably set the
    # spacing and origin on the output
    change_information_filter = Instance(tvtk.ImageChangeInformation, args=(),
                                         kw={'output_spacing': (1.0, 1.0, 1.0),
                                             'output_origin': (0.0, 0.0, 0.0)})

    # Should we transpose the input data or not.  Transposing is
    # necessary to make the numpy array compatible with the way VTK
    # needs it.  However, transposing numpy arrays makes them
    # non-contiguous where the data is copied by VTK.  Thus, when the
    # user explicitly requests that transpose_input_array is false
    # then we assume that the array has already been suitably
    # formatted by the user.
    transpose_input_array = Bool(
        True,
        desc='if input array should be transposed (if True '
        'VTK will copy the input data)'
    )

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['image_data'])

    # Specify the order of dimensions. The default is: [0, 1, 2]
    dimensions_order = List(Int, [0, 1, 2])

    # Our view.
    view = View(Group(Item(name='transpose_input_array'),
                      Item(name='scalar_name'),
                      Item(name='vector_name'),
                      Item(name='spacing'),
                      Item(name='origin'),
                      show_labels=True)
                )

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        # Set the scalar and vector data at the end so we pop it here.
        sd = traits.pop('scalar_data', None)
        vd = traits.pop('vector_data', None)
        # Now set the other traits.
        super(ArraySource, self).__init__(**traits)
        self.configure_input_data(self.change_information_filter,
                                  self.image_data)

        # And finally set the scalar and vector data.
        if sd is not None:
            self.scalar_data = sd
        if vd is not None:
            self.vector_data = vd

        self.outputs = [self.change_information_filter]
        self.on_trait_change(self._information_changed, 'spacing,origin')

    def __get_pure_state__(self):
        d = super(ArraySource, self).__get_pure_state__()
        d.pop('image_data', None)
        return d

    ######################################################################
    # ArraySource interface.
    ######################################################################
    def update(self):
        """Call this function when you change the array data
        in-place."""
        d = self.image_data
        d.modified()
        pd = d.point_data
        if self.scalar_data is not None:
            pd.scalars.modified()
        if self.vector_data is not None:
            pd.vectors.modified()
        self.change_information_filter.update()
        self.data_changed = True

    def add_attribute(self, array, name, category='point'):
        """Add an attribute to the dataset to specified category ('point' or
        'cell').

        One may add a scalar, vector (3/4 components) or a tensor (9
        components).

        Note that it is the user's responsibility to set the correct size of
        the arrays. Also no automatic transposing of the data is done.

        Parameters
        ----------

        array: numpy array/list : array data to add.

        name: str: name of the array.

        category: 'point'/'cell': the category of the attribute data.

        """
        array = np.asarray(array)
        assert len(array.shape) <= 2, "Only 2D arrays can be added."
        data = getattr(self.image_data, '%s_data' % category)
        if len(array.shape) == 2:
            assert array.shape[1] in [1, 3, 4, 9], \
                    "Only N x m arrays where (m in [1,3,4,9]) are supported"
        va = tvtk.to_tvtk(array2vtk(array))
        va.name = name
        data.add_array(va)

    def remove_attribute(self, name, category='point'):
        """Remove an attribute by its name and optional category (point and
        cell).  Returns the removed array.
        """
        data = getattr(self.image_data, '%s_data' % category)
        data.remove_array(name)

    def rename_attribute(self, name1, name2, category='point'):
        """Rename a particular attribute from `name1` to `name2`.
        """
        data = getattr(self.image_data, '%s_data' % category)
        arr = data.get_array(name1)
        arr.name = name2

    ######################################################################
    # Non-public interface.
    ######################################################################

    def _image_data_changed(self, value):
        self.configure_input_data(self.change_information_filter, value)

    def _scalar_data_changed(self, data):
        img_data = self.image_data
        if data is None:
            img_data.point_data.scalars = None
            self.data_changed = True
            return
        dims = list(data.shape)
        if len(dims) == 2:
            dims.append(1)

        # set the dimension indices
        dim0, dim1, dim2 = self.dimensions_order

        img_data.origin = tuple(self.origin)
        img_data.dimensions = tuple(dims)
        img_data.extent = 0, dims[dim0]-1, 0, dims[dim1]-1, 0, dims[dim2]-1
        if VTK_MAJOR_VERSION <= 7:
            if is_old_pipeline():
                img_data.update_extent = 0, dims[dim0]-1, 0, dims[dim1]-1, 0, dims[dim2]-1
            else:
                update_extent = [0, dims[dim0]-1, 0, dims[dim1]-1, 0, dims[dim2]-1]
                self.change_information_filter.set_update_extent(update_extent)
        if self.transpose_input_array:
            img_data.point_data.scalars = np.ravel(np.transpose(data))
        else:
            img_data.point_data.scalars = np.ravel(data)
        img_data.point_data.scalars.name = self.scalar_name
        # This is very important and if not done can lead to a segfault!
        typecode = data.dtype
        if is_old_pipeline():
            img_data.scalar_type = get_vtk_array_type(typecode)
            img_data.update() # This sets up the extents correctly.
        else:
            filter_out_info = self.change_information_filter.get_output_information(0)
            img_data.set_point_data_active_scalar_info(filter_out_info,
                                                       get_vtk_array_type(typecode), -1)
            img_data.modified()
        img_data.update_traits()
        self.change_information_filter.update()

        # Now flush the mayavi pipeline.
        self.data_changed = True

    def _vector_data_changed(self, data):
        img_data = self.image_data
        if data is None:
            img_data.point_data.vectors = None
            self.data_changed = True
            return
        dims = list(data.shape)
        if len(dims) == 3:
            dims.insert(2, 1)
            data = np.reshape(data, dims)

        img_data.origin = tuple(self.origin)
        img_data.dimensions = tuple(dims[:-1])
        img_data.extent = 0, dims[0]-1, 0, dims[1]-1, 0, dims[2]-1
        if VTK_MAJOR_VERSION <= 7:
            if is_old_pipeline():
                img_data.update_extent = 0, dims[0]-1, 0, dims[1]-1, 0, dims[2]-1
            else:
                self.change_information_filter.update_information()
                update_extent = [0, dims[0]-1, 0, dims[1]-1, 0, dims[2]-1]
                self.change_information_filter.set_update_extent(update_extent)
        sz = np.size(data)
        if self.transpose_input_array:
            data_t = np.transpose(data, (2, 1, 0, 3))
        else:
            data_t = data
        img_data.point_data.vectors = np.reshape(data_t, (sz//3, 3))
        img_data.point_data.vectors.name = self.vector_name
        if is_old_pipeline():
            img_data.update() # This sets up the extents correctly.
        else:
            img_data.modified()
        img_data.update_traits()
        self.change_information_filter.update()

        # Now flush the mayavi pipeline.
        self.data_changed = True

    def _scalar_name_changed(self, value):
        if self.scalar_data is not None:
            self.image_data.point_data.scalars.name = value
            self.data_changed = True

    def _vector_name_changed(self, value):
        if self.vector_data is not None:
            self.image_data.point_data.vectors.name = value
            self.data_changed = True

    def _transpose_input_array_changed(self, value):
        if self.scalar_data is not None:
            self._scalar_data_changed(self.scalar_data)
        if self.vector_data is not None:
            self._vector_data_changed(self.vector_data)

    def _information_changed(self):
        self.change_information_filter.update()
        self.data_changed = True
