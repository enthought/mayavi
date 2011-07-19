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

from tvtk.tvtk_classes.volume_ray_cast_function import VolumeRayCastFunction


class VolumeRayCastMIPFunction(VolumeRayCastFunction):
    """
    VolumeRayCastMIPFunction - A maximum intensity projection ray
    caster for volumes
    
    Superclass: VolumeRayCastFunction
    
    VolumeRayCastMIPFunction is a volume ray cast function that
    computes the maximum value encountered along the ray. This is either
    the maximum scalar value, or the maximum opacity, as defined by the
    maximize_method. The color and opacity returned by this function is
    based on the color, scalar opacity, and gradient opacity transfer
    functions defined in the VolumeProperty of the Volume.
    
    See Also:
    
    VolumeRayCastFunction VolumeRayCastMapper VolumeProperty
    VolumeRayCastCompositeFunction VolumeRayCastIsosurfaceFunction
    Volume VolumeProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastMIPFunction, obj, update, **traits)
    
    maximize_method = traits.Trait('scalar_value',
    tvtk_base.TraitRevPrefixMap({'opacity': 1, 'scalar_value': 0}), help=\
        """
        Set the maximize_method to either scalar_value or Opacity.
        """
    )
    def _maximize_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximizeMethod,
                        self.maximize_method_)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximize_method', 'GetMaximizeMethod'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maximize_method'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastMIPFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastMIPFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['maximize_method'], []),
            title='Edit VolumeRayCastMIPFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastMIPFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

