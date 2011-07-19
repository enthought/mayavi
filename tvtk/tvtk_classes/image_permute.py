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

from tvtk.tvtk_classes.image_reslice import ImageReslice


class ImagePermute(ImageReslice):
    """
    ImagePermute -  Permutes axes of input.
    
    Superclass: ImageReslice
    
    ImagePermute reorders the axes of the input. Filtered axes specify
    the input axes which become X, Y, Z.  The input has to have the same
    scalar type of the output. The filter does copy the data when it
    executes. This filter is actually a very thin wrapper around
    ImageReslice.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImagePermute, obj, update, **traits)
    
    filtered_axes = traits.Array(shape=(3,), value=(0, 1, 2), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        The filtered axes are the input axes that get relabeled to X,Y,Z.
        """
    )
    def _filtered_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxes,
                        self.filtered_axes)

    _updateable_traits_ = \
    (('auto_crop_output', 'GetAutoCropOutput'), ('release_data_flag',
    'GetReleaseDataFlag'), ('interpolate', 'GetInterpolate'), ('debug',
    'GetDebug'), ('output_extent', 'GetOutputExtent'),
    ('reslice_axes_origin', 'GetResliceAxesOrigin'), ('mirror',
    'GetMirror'), ('wrap', 'GetWrap'), ('output_dimensionality',
    'GetOutputDimensionality'), ('background_color',
    'GetBackgroundColor'), ('transform_input_sampling',
    'GetTransformInputSampling'), ('background_level',
    'GetBackgroundLevel'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_spacing', 'GetOutputSpacing'),
    ('border', 'GetBorder'), ('progress_text', 'GetProgressText'),
    ('output_origin', 'GetOutputOrigin'), ('optimization',
    'GetOptimization'), ('reslice_axes_direction_cosines',
    'GetResliceAxesDirectionCosines'), ('interpolation_mode',
    'GetInterpolationMode'), ('number_of_threads', 'GetNumberOfThreads'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('abort_execute', 'GetAbortExecute'), ('filtered_axes',
    'GetFilteredAxes'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_crop_output', 'border', 'debug',
    'global_warning_display', 'interpolate', 'mirror', 'optimization',
    'release_data_flag', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'background_color', 'background_level',
    'filtered_axes', 'number_of_threads', 'output_dimensionality',
    'output_extent', 'output_origin', 'output_spacing', 'progress_text',
    'reslice_axes_direction_cosines', 'reslice_axes_origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImagePermute, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_crop_output', 'border', 'interpolate', 'mirror',
            'optimization', 'transform_input_sampling', 'wrap'],
            ['interpolation_mode'], ['background_color', 'background_level',
            'filtered_axes', 'number_of_threads', 'output_dimensionality',
            'output_extent', 'output_origin', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin']),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

