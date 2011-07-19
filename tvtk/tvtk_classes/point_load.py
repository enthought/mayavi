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


class PointLoad(ImageAlgorithm):
    """
    PointLoad - compute stress tensors given point load on
    semi-infinite domain
    
    Superclass: ImageAlgorithm
    
    PointLoad is a source object that computes stress tensors on a
    volume. The tensors are computed from the application of a point load
    on a semi-infinite domain. (The analytical results are adapted from
    Saada - see text.) It also is possible to compute effective stress
    scalars if desired. This object serves as a specialized data
    generator for some of the examples in the text.
    
    See Also:
    
    TensorGlyph, HyperStreamline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointLoad, obj, update, **traits)
    
    compute_effective_stress = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off computation of effective stress scalar. These methods
        do nothing. The effective stress is always computed.
        """
    )
    def _compute_effective_stress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeEffectiveStress,
                        self.compute_effective_stress_)

    sample_dimensions = traits.Array(shape=(3,), value=(50, 50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the dimensions of the volume. A stress tensor will be
        computed for each point in the volume.
        """
    )
    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    model_bounds = traits.Array(shape=(6,), value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    poissons_ratio = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set/Get Poisson's ratio.
        """
    )
    def _poissons_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoissonsRatio,
                        self.poissons_ratio)

    load_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get value of applied load.
        """
    )
    def _load_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLoadValue,
                        self.load_value)

    _updateable_traits_ = \
    (('compute_effective_stress', 'GetComputeEffectiveStress'),
    ('model_bounds', 'GetModelBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('load_value', 'GetLoadValue'),
    ('poissons_ratio', 'GetPoissonsRatio'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('sample_dimensions',
    'GetSampleDimensions'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_effective_stress', 'debug',
    'global_warning_display', 'release_data_flag', 'load_value',
    'model_bounds', 'poissons_ratio', 'progress_text',
    'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointLoad, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_effective_stress'], [], ['load_value',
            'model_bounds', 'poissons_ratio', 'sample_dimensions']),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

