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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class FastSplatter(ImageAlgorithm):
    """
    FastSplatter - A splatter optimized for splatting single kernels.
    
    Superclass: ImageAlgorithm
    
    FastSplatter takes any PointSet as input (of which PolyData
    and UnstructuredGrid inherit).  Each point in the data set is
    considered to be an impulse.  These impulses are convolved with a
    given splat image.  In other words, the splat image is added to the
    final image at every place where there is an input point.
    
    Note that point and cell data are thrown away.  If you want a
    sampling of unstructured points consider GaussianSplatter or
    ShepardMethod.
    
    Use input port 0 for the impulse data (vtk_point_set), and input port 1
    for the splat image (vtk_image_data)
    
    Bugs:
    
    Any point outside of the extents of the image is thrown away, even if
    it is close enough such that it's convolution with the splat image
    would overlap the extents.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFastSplatter, obj, update, **traits)
    
    limit_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'clamp': 1, 'none': 0, 'scale': 2, 'freeze_scale': 3}), help=\
        """
        Set/get the way voxel values will be limited.  If this is set to
        None (the default), the output can have arbitrarily large values.
         If set to clamp, the output will be clamped to
        [_min_value,_max_value].  If set to scale, the output will be
        linearly scaled between min_value and max_value.
        """
    )
    def _limit_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitMode,
                        self.limit_mode_)

    output_dimensions = traits.Array(shape=(3,), value=(100, 100, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDimensions,
                        self.output_dimensions)

    model_bounds = traits.Array(shape=(6,), value=(0.0, -1.0, 0.0, -1.0, 0.0, -1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    max_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        See the limit_mode method.
        """
    )
    def _max_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxValue,
                        self.max_value)

    min_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        See the limit_mode method.
        """
    )
    def _min_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinValue,
                        self.min_value)

    def _get_number_of_points_splatted(self):
        return self._vtk_obj.GetNumberOfPointsSplatted()
    number_of_points_splatted = traits.Property(_get_number_of_points_splatted, help=\
        """
        This returns the number of points splatted (as opposed to
        discarded for being outside the image) during the previous pass.
        """
    )

    def set_splat_connection(self, *args):
        """
        V.set_splat_connection(AlgorithmOutput)
        C++: void SetSplatConnection(AlgorithmOutput *)
        Convenience function for connecting the splat algorithm source.
        This is provided mainly for convenience using the filter with
        para_view, VTK users should prefer set_input_connection(_1, splat)
        instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSplatConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('model_bounds', 'GetModelBounds'), ('output_dimensions',
    'GetOutputDimensions'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('limit_mode', 'GetLimitMode'),
    ('max_value', 'GetMaxValue'), ('min_value', 'GetMinValue'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'limit_mode', 'max_value', 'min_value',
    'model_bounds', 'output_dimensions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FastSplatter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FastSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['limit_mode'], ['max_value', 'min_value',
            'model_bounds', 'output_dimensions']),
            title='Edit FastSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FastSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

