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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class SubPixelPositionEdgels(PolyDataAlgorithm):
    """
    SubPixelPositionEdgels - adjust edgel locations based on gradients.
    
    Superclass: PolyDataAlgorithm
    
    SubPixelPositionEdgels is a filter that takes a series of linked
    edgels (digital curves) and gradient maps as input. It then adjusts
    the edgel locations based on the gradient data. Specifically, the
    algorithm first determines the neighboring gradient magnitudes of an
    edgel using simple interpolation of its neighbors. It then fits the
    following three data points: negative gradient direction gradient
    magnitude, edgel gradient magnitude and positive gradient direction
    gradient magnitude to a quadratic function. It then solves this
    quadratic to find the maximum gradient location along the gradient
    orientation.  It then modifies the edgels location along the gradient
    orientation to the calculated maximum location. This algorithm does
    not adjust an edgel in the direction orthogonal to its gradient
    vector.
    
    See Also:
    
    ImageData ImageGradient LinkEdgels
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSubPixelPositionEdgels, obj, update, **traits)
    
    target_flag = tvtk_base.false_bool_trait(help=\
        """
        These methods can make the positioning look for a target scalar
        value instead of looking for a maximum.
        """
    )
    def _target_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetFlag,
                        self.target_flag_)

    target_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        These methods can make the positioning look for a target scalar
        value instead of looking for a maximum.
        """
    )
    def _target_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetValue,
                        self.target_value)

    def _get_grad_maps(self):
        return wrap_vtk(self._vtk_obj.GetGradMaps())
    def _set_grad_maps(self, arg):
        old_val = self._get_grad_maps()
        self._wrap_call(self._vtk_obj.SetGradMaps,
                        deref_vtk(arg))
        self.trait_property_changed('grad_maps', old_val, arg)
    grad_maps = traits.Property(_get_grad_maps, _set_grad_maps, help=\
        """
        Set/Get the gradient data for doing the position adjustments.
        """
    )

    _updateable_traits_ = \
    (('target_value', 'GetTargetValue'), ('progress_text',
    'GetProgressText'), ('target_flag', 'GetTargetFlag'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'target_flag', 'progress_text', 'target_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SubPixelPositionEdgels, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['target_flag'], [], ['target_value']),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

