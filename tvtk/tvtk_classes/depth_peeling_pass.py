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


class DepthPeelingPass(RenderPass):
    """
    DepthPeelingPass - Implement an Order Independent Transparency
    
    Superclass: RenderPass
    
    Render the translucent polygonal geometry of a scene without sorting
    polygons in the view direction.
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    The depth peeling algorithm works by rendering the translucent
    polygonal geometry multiple times (once for each peel). The actually
    rendering of the translucent polygonal geometry is peformed by its
    delegate translucent_pass. This delegate is therefore used multiple
    times.
    
    Its delegate is usually set to a TranslucentPass.
    
    See Also:
    
    RenderPass, TranslucentPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDepthPeelingPass, obj, update, **traits)
    
    def _get_translucent_pass(self):
        return wrap_vtk(self._vtk_obj.GetTranslucentPass())
    def _set_translucent_pass(self, arg):
        old_val = self._get_translucent_pass()
        self._wrap_call(self._vtk_obj.SetTranslucentPass,
                        deref_vtk(arg))
        self.trait_property_changed('translucent_pass', old_val, arg)
    translucent_pass = traits.Property(_get_translucent_pass, _set_translucent_pass, help=\
        """
        Delegate for rendering the translucent polygonal geometry. If it
        is NULL, nothing will be rendered and a warning will be emitted.
        It is usually set to a TranslucentPass. Initial value is a
        NULL pointer.
        """
    )

    maximum_number_of_peels = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        In case of depth peeling, define the maximum number of peeling
        layers. Initial value is 4. A special value of 0 means no maximum
        limit. It has to be a positive value.
        """
    )
    def _maximum_number_of_peels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPeels,
                        self.maximum_number_of_peels)

    occlusion_ratio = traits.Trait(0.0, traits.Range(0.0, 0.5, enter_set=True, auto_set=False), help=\
        """
        In case of use of depth peeling technique for rendering
        translucent material, define the threshold under which the
        algorithm stops to iterate over peel layers. This is the ratio of
        the number of pixels that have been touched by the last layer
        over the total number of pixels of the viewport area. Initial
        value is 0.0, meaning rendering have to be exact. Greater values
        may speed-up the rendering with small impact on the quality.
        """
    )
    def _occlusion_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOcclusionRatio,
                        self.occlusion_ratio)

    def _get_last_rendering_used_depth_peeling(self):
        return self._vtk_obj.GetLastRenderingUsedDepthPeeling()
    last_rendering_used_depth_peeling = traits.Property(_get_last_rendering_used_depth_peeling, help=\
        """
        Tells if the last time this pass was executed, the depth peeling
        algorithm was actually used. Initial value is false.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('occlusion_ratio', 'GetOcclusionRatio'), ('maximum_number_of_peels',
    'GetMaximumNumberOfPeels'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maximum_number_of_peels',
    'occlusion_ratio'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DepthPeelingPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['maximum_number_of_peels',
            'occlusion_ratio']),
            title='Edit DepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

