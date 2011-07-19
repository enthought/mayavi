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


class ImageResample(ImageReslice):
    """
    ImageResample - Resamples an image to be larger or smaller.
    
    Superclass: ImageReslice
    
    This filter produces an output with different spacing (and extent)
    than the input.  Linear interpolation can be used to resample the
    data. The Output spacing can be set explicitly or relative to input
    spacing with the set_axis_magnification_factor method.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageResample, obj, update, **traits)
    
    dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Dimensionality is the number of axes which are considered during
        execution. To process images dimensionality would be set to 2.
        This has the same effect as setting the magnification of the
        third axis to 1.0
        """
    )
    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

    def get_axis_magnification_factor(self, *args):
        """
        V.get_axis_magnification_factor(int, Information) -> float
        C++: double GetAxisMagnificationFactor(int axis,
            Information *inInfo=0)
        Set/Get Magnification factors. Zero is a reserved value
        indicating values have not been computed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAxisMagnificationFactor, *my_args)
        return ret

    def set_axis_magnification_factor(self, *args):
        """
        V.set_axis_magnification_factor(int, float)
        C++: void SetAxisMagnificationFactor(int axis, double factor)
        Set/Get Magnification factors. Zero is a reserved value
        indicating values have not been computed.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisMagnificationFactor, *args)
        return ret

    def set_axis_output_spacing(self, *args):
        """
        V.set_axis_output_spacing(int, float)
        C++: void SetAxisOutputSpacing(int axis, double spacing)
        Set desired spacing. Zero is a reserved value indicating spacing
        has not been set.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisOutputSpacing, *args)
        return ret

    _updateable_traits_ = \
    (('auto_crop_output', 'GetAutoCropOutput'), ('release_data_flag',
    'GetReleaseDataFlag'), ('interpolate', 'GetInterpolate'), ('debug',
    'GetDebug'), ('background_level', 'GetBackgroundLevel'),
    ('reslice_axes_origin', 'GetResliceAxesOrigin'), ('mirror',
    'GetMirror'), ('wrap', 'GetWrap'), ('output_dimensionality',
    'GetOutputDimensionality'), ('background_color',
    'GetBackgroundColor'), ('transform_input_sampling',
    'GetTransformInputSampling'), ('dimensionality', 'GetDimensionality'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_spacing', 'GetOutputSpacing'), ('output_extent',
    'GetOutputExtent'), ('border', 'GetBorder'), ('progress_text',
    'GetProgressText'), ('output_origin', 'GetOutputOrigin'),
    ('optimization', 'GetOptimization'),
    ('reslice_axes_direction_cosines', 'GetResliceAxesDirectionCosines'),
    ('number_of_threads', 'GetNumberOfThreads'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('abort_execute',
    'GetAbortExecute'), ('interpolation_mode', 'GetInterpolationMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_crop_output', 'border', 'debug',
    'global_warning_display', 'interpolate', 'mirror', 'optimization',
    'release_data_flag', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'background_color', 'background_level',
    'dimensionality', 'number_of_threads', 'output_dimensionality',
    'output_extent', 'output_origin', 'output_spacing', 'progress_text',
    'reslice_axes_direction_cosines', 'reslice_axes_origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageResample, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_crop_output', 'border', 'interpolate', 'mirror',
            'optimization', 'transform_input_sampling', 'wrap'],
            ['interpolation_mode'], ['background_color', 'background_level',
            'dimensionality', 'number_of_threads', 'output_dimensionality',
            'output_extent', 'output_origin', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin']),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

