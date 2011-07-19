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


class VolumeRayCastCompositeFunction(VolumeRayCastFunction):
    """
    VolumeRayCastCompositeFunction - a ray function for compositing
    
    Superclass: VolumeRayCastFunction
    
    VolumeRayCastCompositeFunction is a ray function that can be used
    within a VolumeRayCastMapper. This function performs compositing
    along the ray according to the properties stored in the
    VolumeProperty for the volume.
    
    See Also:
    
    VolumeRayCastMapper VolumeProperty Volume
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastCompositeFunction, obj, update, **traits)
    
    composite_method = traits.Trait('interpolate_first',
    tvtk_base.TraitRevPrefixMap({'interpolate_first': 1, 'classify_first': 0}), help=\
        """
        Set the composite_method to either Classify First or Interpolate
        First
        """
    )
    def _composite_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompositeMethod,
                        self.composite_method_)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('composite_method', 'GetCompositeMethod'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'composite_method'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastCompositeFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastCompositeFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['composite_method'], []),
            title='Edit VolumeRayCastCompositeFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastCompositeFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

