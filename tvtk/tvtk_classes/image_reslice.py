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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageReslice(ThreadedImageAlgorithm):
    """
    ImageReslice - Reslices a volume along a new set of axes.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageReslice is the swiss-army-knife of image geometry filters: It
    can permute, rotate, flip, scale, resample, deform, and pad image
    data in any combination with reasonably high efficiency.  Simple
    operations such as permutation, resampling and padding are done with
    similar efficiently to the specialized ImagePermute,
    ImageResample, and ImagePad filters.  There are a number of
    tasks that ImageReslice is well suited for:
    
    1) Application of simple rotations, scales, and translations to an
    image. It is often a good idea to use ImageChangeInformation to
    center the image first, so that scales and rotations occur around the
    center rather than around the lower-left corner of the image.
    
    2) Resampling of one data set to match the voxel sampling of a second
    data set via the set_information_input() method, e.g. for the purpose
    of comparing two images or combining two images. A transformation,
    either linear or nonlinear, can be applied at the same time via the
    set_reslice_transform method if the two images are not in the same
    coordinate space.
    
    3) Extraction of slices from an image volume.  The most convenient
    way to do this is to use set_reslice_axes_direction_cosines() to specify
    the orientation of the slice.  The direction cosines give the x, y,
    and z axes for the output volume.  The method
    set_output_dimensionality(_2) is used to specify that want to output a
    slice rather than a volume.  The set_reslice_axes_origin() command is
    used to provide an (x,y,z) point that the slice will pass through.
    You can use both the reslice_axes and the reslice_transform at the same
    time, in order to extract slices from a volume that you have applied
    a transformation to.
    
    Caveats:
    
    This filter is very inefficient if the output X dimension is 1.
    
    See Also:
    
    AbstractTransform Matrix4x4
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReslice, obj, update, **traits)
    
    transform_input_sampling = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to transform the spacing, origin and extent of
        the Input (or the information_input) according to the direction
        cosines and origin of the reslice_axes before applying them as the
        default output spacing, origin and extent (default: On).
        """
    )
    def _transform_input_sampling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransformInputSampling,
                        self.transform_input_sampling_)

    auto_crop_output = tvtk_base.false_bool_trait(help=\
        """
        Turn this on if you want to guarantee that the extent of the
        output will be large enough to ensure that none of the data will
        be cropped (default: Off).
        """
    )
    def _auto_crop_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoCropOutput,
                        self.auto_crop_output_)

    interpolate = tvtk_base.false_bool_trait(help=\
        """
        Convenient methods for switching between nearest-neighbor and
        linear interpolation. interpolate_on() is equivalent to
        set_interpolation_mode_to_linear() and interpolate_off() is equivalent
        to set_interpolation_mode_to_nearest_neighbor() You should not use
        these methods if you use the set_interpolation_mode methods.
        """
    )
    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    optimization = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off optimizations (default on, they should only be
        turned off for testing purposes).
        """
    )
    def _optimization_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOptimization,
                        self.optimization_)

    mirror = tvtk_base.false_bool_trait(help=\
        """
        Turn on mirror-pad feature (default: Off). This will override the
        wrap-pad.
        """
    )
    def _mirror_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMirror,
                        self.mirror_)

    wrap = tvtk_base.false_bool_trait(help=\
        """
        Turn on wrap-pad feature (default: Off).
        """
    )
    def _wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrap,
                        self.wrap_)

    border = tvtk_base.true_bool_trait(help=\
        """
        Extend the apparent input border by a half voxel (default: On).
        This changes how interpolation is handled at the borders of the
        input image: if the center of an output voxel is beyond the edge
        of the input image, but is within a half voxel width of the edge
        (using the input voxel width), then the value of the output voxel
        is calculated as if the input's edge voxels were duplicated past
        the edges of the input. This has no effect if Mirror or Wrap are
        on.
        """
    )
    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    interpolation_mode = traits.Trait('nearest_neighbor',
    tvtk_base.TraitRevPrefixMap({'nearest_neighbor': 0, 'linear': 1, 'cubic': 3}), help=\
        """
        Set interpolation mode (default: nearest neighbor).
        """
    )
    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    background_level = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set background grey level (for single-component images).
        """
    )
    def _background_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundLevel,
                        self.background_level)

    def _get_reslice_transform(self):
        return wrap_vtk(self._vtk_obj.GetResliceTransform())
    def _set_reslice_transform(self, arg):
        old_val = self._get_reslice_transform()
        self._wrap_call(self._vtk_obj.SetResliceTransform,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_transform', old_val, arg)
    reslice_transform = traits.Property(_get_reslice_transform, _set_reslice_transform, help=\
        """
        Set a transform to be applied to the resampling grid that has
        been defined via the reslice_axes and the output Origin, Spacing
        and Extent.  Note that applying a transform to the resampling
        grid (which lies in the output coordinate system) is equivalent
        to applying the inverse of that transform to the input volume. 
        Nonlinear transforms such as GridTransform and
        ThinPlateSplineTransform can be used here.
        """
    )

    background_color = traits.Array(shape=(4,), value=(0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color)

    output_dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Force the dimensionality of the output to either 1, 2, 3 or 0
        (default: 3).  If the dimensionality is 2d, then the Z extent of
        the output is forced to (0,0) and the Z origin of the output is
        forced to 0.0 (i.e. the output extent is confined to the xy
        plane).  If the dimensionality is 1d, the output extent is
        confined to the x axis. For 0d, the output extent consists of a
        single voxel at (0,0,0).
        """
    )
    def _output_dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDimensionality,
                        self.output_dimensionality)

    output_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the extent for the output data.  The default output extent is
        the input extent permuted through the reslice_axes.
        """
    )
    def _output_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputExtent,
                        self.output_extent)

    reslice_axes_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the origin for the reslice_axes (i.e. the first three
        elements of the final column of the reslice_axes matrix). This
        will modify the current reslice_axes matrix, or create new matrix
        if none exists.
        """
    )
    def _reslice_axes_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResliceAxesOrigin,
                        self.reslice_axes_origin)

    reslice_axes_direction_cosines = traits.Array(shape=(9,), value=(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the direction cosines for the reslice_axes (i.e. the first
        three elements of each of the first three columns of the
        reslice_axes matrix).  This will modify the current reslice_axes
        matrix, or create a new matrix if none exists.
        """
    )
    def _reslice_axes_direction_cosines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResliceAxesDirectionCosines,
                        self.reslice_axes_direction_cosines)

    output_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the origin for the output data.  The default output origin is
        the input origin permuted through the reslice_axes.
        """
    )
    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    def _set_stencil(self, arg):
        old_val = self._get_stencil()
        self._wrap_call(self._vtk_obj.SetStencil,
                        deref_vtk(arg))
        self.trait_property_changed('stencil', old_val, arg)
    stencil = traits.Property(_get_stencil, _set_stencil, help=\
        """
        Use a stencil to limit the calculations to a specific region of
        the output.  Portions of the output that are 'outside' the
        stencil will be cleared to the background color.
        """
    )

    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    def _set_information_input(self, arg):
        old_val = self._get_information_input()
        self._wrap_call(self._vtk_obj.SetInformationInput,
                        deref_vtk(arg))
        self.trait_property_changed('information_input', old_val, arg)
    information_input = traits.Property(_get_information_input, _set_information_input, help=\
        """
        Set a ImageData from which the default Spacing, Origin, and
        whole_extent of the output will be copied.  The spacing, origin,
        and extent will be permuted according to the reslice_axes.  Any
        values set via set_output_spacing, set_output_origin, and
        set_output_extent will override these values.  By default, the
        Spacing, Origin, and whole_extent of the Input are used.
        """
    )

    def _get_reslice_axes(self):
        return wrap_vtk(self._vtk_obj.GetResliceAxes())
    def _set_reslice_axes(self, arg):
        old_val = self._get_reslice_axes()
        self._wrap_call(self._vtk_obj.SetResliceAxes,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_axes', old_val, arg)
    reslice_axes = traits.Property(_get_reslice_axes, _set_reslice_axes, help=\
        """
        This method is used to set up the axes for the output voxels. The
        output Spacing, Origin, and Extent specify the locations of the
        voxels within the coordinate system defined by the axes. The
        reslice_axes are used most often to permute the data, e.g. to
        extract ZY or XZ slices of a volume as 2d XY images.
        
        The first column of the matrix specifies the x-axis vector (the
        fourth element must be set to zero), the second column specifies
        the y-axis, and the third column the z-axis.  The fourth column
        is the origin of the axes (the fourth element must be set to
        one).
        
        An alternative to set_reslice_axes() is to use
        set_reslice_axes_direction_cosines() to set the directions of the
        axes and set_reslice_axes_origin() to set the origin of the axes.
        """
    )

    output_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the voxel spacing for the output data.  The default output
        spacing is the input spacing permuted through the reslice_axes.
        """
    )
    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    def report_references(self, *args):
        """
        V.report_references(GarbageCollector)
        C++: virtual void ReportReferences(GarbageCollector *)
        Report object referenced by instances of this class.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReportReferences, *my_args)
        return ret

    def set_output_extent_to_default(self):
        """
        V.set_output_extent_to_default()
        C++: void SetOutputExtentToDefault()
        Set the extent for the output data.  The default output extent is
        the input extent permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputExtentToDefault()
        return ret
        

    def set_output_origin_to_default(self):
        """
        V.set_output_origin_to_default()
        C++: void SetOutputOriginToDefault()
        Set the origin for the output data.  The default output origin is
        the input origin permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputOriginToDefault()
        return ret
        

    def set_output_spacing_to_default(self):
        """
        V.set_output_spacing_to_default()
        C++: void SetOutputSpacingToDefault()
        Set the voxel spacing for the output data.  The default output
        spacing is the input spacing permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputSpacingToDefault()
        return ret
        

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
    'GetResliceAxesDirectionCosines'), ('number_of_threads',
    'GetNumberOfThreads'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('interpolation_mode', 'GetInterpolationMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_crop_output', 'border', 'debug',
    'global_warning_display', 'interpolate', 'mirror', 'optimization',
    'release_data_flag', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'background_color', 'background_level',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_spacing', 'progress_text',
    'reslice_axes_direction_cosines', 'reslice_axes_origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageReslice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_crop_output', 'border', 'interpolate', 'mirror',
            'optimization', 'transform_input_sampling', 'wrap'],
            ['interpolation_mode'], ['background_color', 'background_level',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_spacing', 'reslice_axes_direction_cosines',
            'reslice_axes_origin']),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

