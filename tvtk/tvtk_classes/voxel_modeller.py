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


class VoxelModeller(ImageAlgorithm):
    """
    VoxelModeller - convert an arbitrary dataset to a voxel
    representation
    
    Superclass: ImageAlgorithm
    
    VoxelModeller is a filter that converts an arbitrary data set to a
    structured point (i.e., voxel) representation. It is very similar to
    ImplicitModeller, except that it doesn't record distance; instead
    it records occupancy. By default it supports a compact output of 0/1
    VTK_BIT. Other vtk scalar types can be specified. The Foreground and
    Background values of the output can also be specified. NOTE: Not all
    vtk filters/readers/writers support the VTK_BIT scalar type. You may
    want to use VTK_CHAR as an alternative.
    
    See Also:
    
    ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVoxelModeller, obj, update, **traits)
    
    scalar_type = traits.Trait('bit',
    tvtk_base.TraitRevPrefixMap({'short': 4, 'int': 6, 'double': 11, 'float': 10, 'unsigned_long': 9, 'long': 8, 'char': 2, 'unsigned_int': 7, 'unsigned_char': 3, 'unsigned_short': 5, 'bit': 1}), help=\
        """
        Control the scalar type of the output image. The default is
        VTK_BIT. NOTE: Not all filters/readers/writers support the
        VTK_BIT scalar type. You may want to use VTK_CHAR as an
        alternative.
        """
    )
    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    background_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the Foreground/Background values of the output. The
        Foreground value is set when a voxel is occupied. The Background
        value is set when a voxel is not occupied. The default
        foreground_value is 1. The default background_value is 0.
        """
    )
    def _background_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundValue,
                        self.background_value)

    maximum_distance = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify distance away from surface of input geometry to sample.
        Smaller values make large increases in performance. Default is
        1.0.
        """
    )
    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    model_bounds = traits.Array(shape=(6,), value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the position in space to perform the voxelization.
        Default is (0, 0, 0, 0, 0, 0)
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    foreground_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the Foreground/Background values of the output. The
        Foreground value is set when a voxel is occupied. The Background
        value is set when a voxel is not occupied. The default
        foreground_value is 1. The default background_value is 0.
        """
    )
    def _foreground_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForegroundValue,
                        self.foreground_value)

    sample_dimensions = traits.Array(shape=(3,), value=(50, 50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the i-j-k dimensions on which to sample the distance
        function. Default is (50, 50, 50)
        """
    )
    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds([float, float, float], [float, float, float])
             -> float
        C++: double ComputeModelBounds(double origin[3], double ar[3])
        Compute the model_bounds based on the input geometry.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *args)
        return ret

    _updateable_traits_ = \
    (('scalar_type', 'GetScalarType'), ('model_bounds', 'GetModelBounds'),
    ('maximum_distance', 'GetMaximumDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('foreground_value',
    'GetForegroundValue'), ('background_value', 'GetBackgroundValue'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('sample_dimensions', 'GetSampleDimensions'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_type', 'background_value',
    'foreground_value', 'maximum_distance', 'model_bounds',
    'progress_text', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VoxelModeller, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['scalar_type'], ['background_value',
            'foreground_value', 'maximum_distance', 'model_bounds',
            'sample_dimensions']),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

