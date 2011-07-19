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


class ImageFlip(ImageReslice):
    """
    ImageFlip - This flips an axis of an image. Right becomes left ...
    
    Superclass: ImageReslice
    
    ImageFlip will reflect the data along the filtered axis.  This
    filter is actually a thin wrapper around ImageReslice.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageFlip, obj, update, **traits)
    
    preserve_image_extent = tvtk_base.true_bool_trait(help=\
        """
        preserve_image_extent_off wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the image_extent is always preserved).
        """
    )
    def _preserve_image_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveImageExtent,
                        self.preserve_image_extent_)

    flip_about_origin = tvtk_base.false_bool_trait(help=\
        """
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a ImageData.
        """
    )
    def _flip_about_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipAboutOrigin,
                        self.flip_about_origin_)

    filtered_axes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Keep the mis-named Axes variations around for compatibility with
        old scripts. Axis is singular, not plural...
        """
    )
    def _filtered_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxes,
                        self.filtered_axes)

    filtered_axis = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify which axis will be flipped.  This must be an integer
        between 0 (for x) and 2 (for z). Initial value is 0.
        """
    )
    def _filtered_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxis,
                        self.filtered_axis)

    _updateable_traits_ = \
    (('auto_crop_output', 'GetAutoCropOutput'), ('release_data_flag',
    'GetReleaseDataFlag'), ('interpolate', 'GetInterpolate'), ('debug',
    'GetDebug'), ('output_extent', 'GetOutputExtent'),
    ('reslice_axes_origin', 'GetResliceAxesOrigin'), ('mirror',
    'GetMirror'), ('wrap', 'GetWrap'), ('filtered_axis',
    'GetFilteredAxis'), ('background_color', 'GetBackgroundColor'),
    ('output_dimensionality', 'GetOutputDimensionality'),
    ('transform_input_sampling', 'GetTransformInputSampling'),
    ('background_level', 'GetBackgroundLevel'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_spacing', 'GetOutputSpacing'),
    ('border', 'GetBorder'), ('progress_text', 'GetProgressText'),
    ('output_origin', 'GetOutputOrigin'), ('preserve_image_extent',
    'GetPreserveImageExtent'), ('optimization', 'GetOptimization'),
    ('reslice_axes_direction_cosines', 'GetResliceAxesDirectionCosines'),
    ('interpolation_mode', 'GetInterpolationMode'), ('number_of_threads',
    'GetNumberOfThreads'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('filtered_axes', 'GetFilteredAxes'), ('flip_about_origin',
    'GetFlipAboutOrigin'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_crop_output', 'border', 'debug',
    'flip_about_origin', 'global_warning_display', 'interpolate',
    'mirror', 'optimization', 'preserve_image_extent',
    'release_data_flag', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'background_color', 'background_level',
    'filtered_axes', 'filtered_axis', 'number_of_threads',
    'output_dimensionality', 'output_extent', 'output_origin',
    'output_spacing', 'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageFlip, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_crop_output', 'border', 'flip_about_origin',
            'interpolate', 'mirror', 'optimization', 'preserve_image_extent',
            'transform_input_sampling', 'wrap'], ['interpolation_mode'],
            ['background_color', 'background_level', 'filtered_axes',
            'filtered_axis', 'number_of_threads', 'output_dimensionality',
            'output_extent', 'output_origin', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin']),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

