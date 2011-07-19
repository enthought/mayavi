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

from tvtk.tvtk_classes.render_pass import RenderPass


class ShadowMapPass(RenderPass):
    """
    ShadowMapPass - Implement a shadow mapping render pass.
    
    Superclass: RenderPass
    
    Render the opaque polygonal geometry of a scene with shadow maps (a
    technique to render hard shadows in hardware).
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    Its delegate is usually set to a OpaquePass.
    
    Implementation:
    
    The first pass of the algorithm is to generate a shadow map per light
    (depth map from the light point of view) by rendering the opaque
    objects with the OCCLUDER property keys. The second pass is to render
    the opaque objects with the RECEIVER keys.
    
    See Also:
    
    RenderPass, OpaquePass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShadowMapPass, obj, update, **traits)
    
    def _get_opaque_pass(self):
        return wrap_vtk(self._vtk_obj.GetOpaquePass())
    def _set_opaque_pass(self, arg):
        old_val = self._get_opaque_pass()
        self._wrap_call(self._vtk_obj.SetOpaquePass,
                        deref_vtk(arg))
        self.trait_property_changed('opaque_pass', old_val, arg)
    opaque_pass = traits.Property(_get_opaque_pass, _set_opaque_pass, help=\
        """
        Pass that render the opaque geometry, with no camera pass
        (otherwise it does not work with Ice-T). Initial value is a NULL
        pointer. Typically a sequence pass with a light pass and opaque
        pass. This should be the Opaque pass of the ShadowMapBakerPass
        without the CameraPass.
        """
    )

    def _get_shadow_map_baker_pass(self):
        return wrap_vtk(self._vtk_obj.GetShadowMapBakerPass())
    def _set_shadow_map_baker_pass(self, arg):
        old_val = self._get_shadow_map_baker_pass()
        self._wrap_call(self._vtk_obj.SetShadowMapBakerPass,
                        deref_vtk(arg))
        self.trait_property_changed('shadow_map_baker_pass', old_val, arg)
    shadow_map_baker_pass = traits.Property(_get_shadow_map_baker_pass, _set_shadow_map_baker_pass, help=\
        """
        Pass that generates the shadow maps. the ShadowMapPass will
        use the Resolution ivar of this pass. Initial value is a NULL
        pointer.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShadowMapPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

