# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class MINCImageReader(ImageReader2):
    """
    MINCImageReader - A reader for MINC files.
    
    Superclass: ImageReader2
    
    MINC is a net_cdf-based medical image file format that was developed
    at the Montreal Neurological Institute in 1992. This class will read
    a MINC file into VTK, rearranging the data to match the VTK x, y, and
    z dimensions, and optionally rescaling real-valued data to VTK_FLOAT
    if rescale_real_values_on() is set. If rescale_real_values is off, then
    the data will be stored in its original data type and the
    get_rescale_slope(), get_rescale_intercept() method can be used to
    retrieve global rescaling parameters. If the original file had a time
    dimension, the set_time_step() method can be used to specify a time
    step to read. All of the original header information can be accessed
    though the get_image_attributes() method.
    
    See Also:
    
    MINCImageWriter MINCImageAttributes
    
    Thanks:
    
    Thanks to David Gobbi for writing this class and Atamai Inc. for
    contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMINCImageReader, obj, update, **traits)
    
    rescale_real_values = tvtk_base.false_bool_trait(help=\
        """
        Rescale real data values to float.  If this is done, the
        rescale_slope and rescale_intercept will be set to 1 and 0
        respectively.  This is off by default.
        """
    )
    def _rescale_real_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRescaleRealValues,
                        self.rescale_real_values_)

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the time step to read.
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    def _get_data_range(self):
        return self._vtk_obj.GetDataRange()
    data_range = traits.Property(_get_data_range, help=\
        """
        Get the scalar range of the output from the information in the
        file header.  This is more efficient that computing the scalar
        range, but in some cases the MINC file stores an incorrect
        valid_range and the data_range will be incorrect.
        """
    )

    def _get_direction_cosines(self):
        return wrap_vtk(self._vtk_obj.GetDirectionCosines())
    direction_cosines = traits.Property(_get_direction_cosines, help=\
        """
        Get a matrix that describes the orientation of the data. The
        three columns of the matrix are the direction cosines for the x,
        y and z dimensions respectively.
        """
    )

    def _get_image_attributes(self):
        return wrap_vtk(self._vtk_obj.GetImageAttributes())
    image_attributes = traits.Property(_get_image_attributes, help=\
        """
        Get the image attributes, which contain patient information and
        other useful metadata.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Get the number of time steps in the file.
        """
    )

    def _get_rescale_intercept(self):
        return self._vtk_obj.GetRescaleIntercept()
    rescale_intercept = traits.Property(_get_rescale_intercept, help=\
        """
        Get the slope and intercept for rescaling the scalar values to
        real data values.  To convert scalar values to real values, use
        the equation y = x*_rescale_slope + rescale_intercept.
        """
    )

    def _get_rescale_slope(self):
        return self._vtk_obj.GetRescaleSlope()
    rescale_slope = traits.Property(_get_rescale_slope, help=\
        """
        Get the slope and intercept for rescaling the scalar values to
        real data values.  To convert scalar values to real values, use
        the equation y = x*_rescale_slope + rescale_intercept.
        """
    )

    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('file_name', 'GetFileName'), ('data_byte_order', 'GetDataByteOrder'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('debug', 'GetDebug'), ('header_size', 'GetHeaderSize'),
    ('data_spacing', 'GetDataSpacing'), ('swap_bytes', 'GetSwapBytes'),
    ('time_step', 'GetTimeStep'), ('data_origin', 'GetDataOrigin'),
    ('file_lower_left', 'GetFileLowerLeft'), ('file_name_slice_offset',
    'GetFileNameSliceOffset'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('data_extent', 'GetDataExtent'),
    ('progress_text', 'GetProgressText'), ('rescale_real_values',
    'GetRescaleRealValues'), ('file_name_slice_spacing',
    'GetFileNameSliceSpacing'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('file_dimensionality', 'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'rescale_real_values',
    'swap_bytes', 'data_byte_order', 'data_extent', 'data_origin',
    'data_spacing', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'number_of_scalar_components',
    'progress_text', 'time_step'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MINCImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MINCImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'rescale_real_values',
            'swap_bytes'], ['data_byte_order'], ['data_extent', 'data_origin',
            'data_spacing', 'file_dimensionality', 'file_name',
            'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
            'file_prefix', 'header_size', 'number_of_scalar_components',
            'time_step']),
            title='Edit MINCImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MINCImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

