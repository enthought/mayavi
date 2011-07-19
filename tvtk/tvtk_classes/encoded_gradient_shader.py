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

from tvtk.tvtk_classes.object import Object


class EncodedGradientShader(Object):
    """
    EncodedGradientShader - Compute shading tables for encoded normals.
    
    Superclass: Object
    
    EncodedGradientShader computes shading tables for encoded normals
    that indicates the amount of diffuse and specular illumination that
    is received from all light sources at a surface location with that
    normal. For diffuse illumination this is accurate, but for specular
    illumination it is approximate for perspective projections since the
    center view direction is always used as the view direction. Since the
    shading table is dependent on the volume (for the transformation that
    must be applied to the normals to put them into world coordinates)
    there is a shading table per volume. This is necessary because
    multiple volumes can share a volume mapper.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEncodedGradientShader, obj, update, **traits)
    
    zero_normal_diffuse_intensity = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
    )
    def _zero_normal_diffuse_intensity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZeroNormalDiffuseIntensity,
                        self.zero_normal_diffuse_intensity)

    zero_normal_specular_intensity = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
    )
    def _zero_normal_specular_intensity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZeroNormalSpecularIntensity,
                        self.zero_normal_specular_intensity)

    active_component = traits.Trait(0, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        Set the active component for shading. This component's ambient /
        diffuse / specular / specular power values will be used to create
        the shading table. The default is 1.0
        """
    )
    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    def update_shading_table(self, *args):
        """
        V.update_shading_table(Renderer, Volume,
            EncodedGradientEstimator)
        C++: void UpdateShadingTable(Renderer *ren, Volume *vol,
            EncodedGradientEstimator *gradest)
        Cause the shading table to be updated
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateShadingTable, *my_args)
        return ret

    _updateable_traits_ = \
    (('zero_normal_specular_intensity', 'GetZeroNormalSpecularIntensity'),
    ('reference_count', 'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('zero_normal_diffuse_intensity',
    'GetZeroNormalDiffuseIntensity'), ('debug', 'GetDebug'),
    ('active_component', 'GetActiveComponent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'active_component',
    'zero_normal_diffuse_intensity', 'zero_normal_specular_intensity'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EncodedGradientShader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EncodedGradientShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['active_component',
            'zero_normal_diffuse_intensity', 'zero_normal_specular_intensity']),
            title='Edit EncodedGradientShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EncodedGradientShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

