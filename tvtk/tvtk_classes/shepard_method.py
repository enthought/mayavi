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


class ShepardMethod(ImageAlgorithm):
    """
    ShepardMethod - sample unstructured points onto structured points
    using the method of Shepard
    
    Superclass: ImageAlgorithm
    
    ShepardMethod is a filter used to visualize unstructured point
    data using Shepard's method. The method works by resampling the
    unstructured points onto a structured points set. The influence
    functions are described as "inverse distance weighted". Once the
    structured points are computed, the usual visualization techniques
    (e.g., iso-contouring or volume rendering) can be used visualize the
    structured points.
    
    Caveats:
    
    The input to this filter is any dataset type. This filter can be used
    to resample any form of data, i.e., the input data need not be
    unstructured.
    
    The bounds of the data (i.e., the sample space) is automatically
    computed if not set by the user.
    
    If you use a maximum distance less than 1.0, some output points may
    never receive a contribution. The final value of these points can be
    specified with the "_null_value" instance variable.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShepardMethod, obj, update, **traits)
    
    maximum_distance = traits.Trait(0.25, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify influence distance of each input point. This distance is
        a fraction of the length of the diagonal of the sample space.
        Thus, values of 1.0 will cause each input point to influence all
        points in the structured point dataset. Values less than 1.0 can
        improve performance significantly.
        """
    )
    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    sample_dimensions = traits.Array(shape=(3,), value=(50, 50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the i-j-k dimensions on which to sample the distance
        function.
        """
    )
    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    model_bounds = traits.Array(shape=(6,), value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    null_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the Null value for output points not receiving a contribution
        from the input points.
        """
    )
    def _null_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullValue,
                        self.null_value)

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds([float, float, float], [float, float, float])
             -> float
        C++: double ComputeModelBounds(double origin[3], double ar[3])
        Compute model_bounds from input geometry.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *args)
        return ret

    _updateable_traits_ = \
    (('model_bounds', 'GetModelBounds'), ('maximum_distance',
    'GetMaximumDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('sample_dimensions', 'GetSampleDimensions'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('null_value',
    'GetNullValue'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum_distance', 'model_bounds', 'null_value',
    'progress_text', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShepardMethod, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['maximum_distance', 'model_bounds',
            'null_value', 'sample_dimensions']),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

