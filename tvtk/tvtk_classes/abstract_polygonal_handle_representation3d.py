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

from tvtk.tvtk_classes.handle_representation import HandleRepresentation


class AbstractPolygonalHandleRepresentation3D(HandleRepresentation):
    """
    AbstractPolygonalHandleRepresentation3D - represent a user defined
    handle geometry in 3d while maintaining a fixed orientation w.r.t the
    camera.
    
    Superclass: HandleRepresentation
    
    This class serves as the geometrical representation of a
    HandleWidget. The handle can be represented by an arbitrary
    polygonal data (vtk_poly_data), set via set_handle(vtk_poly_data *). The
    actual position of the handle will be initially assumed to be
    (0,0,0). You can specify an offset from this position if desired.
    This class differs from PolygonalHandleRepresentation3D in that
    the handle will always remain front facing, ie it maintains a fixed
    orientation with respect to the camera. This is done by using
    Followers internally to render the actors.
    
    See Also:
    
    PolygonalHandleRepresentation3D HandleRepresentation
    HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractPolygonalHandleRepresentation3D, obj, update, **traits)
    
    handle_visibility = tvtk_base.true_bool_trait(help=\
        """
        Toogle the visibility of the handle on and off
        """
    )
    def _handle_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleVisibility,
                        self.handle_visibility_)

    label_visibility = tvtk_base.false_bool_trait(help=\
        """
        A label may be associated with the seed. The string can be set
        via set_label_text. The visibility of the label can be turned on /
        off.
        """
    )
    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    def _set_selected_property(self, arg):
        old_val = self._get_selected_property()
        self._wrap_call(self._vtk_obj.SetSelectedProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_property', old_val, arg)
    selected_property = traits.Property(_get_selected_property, _set_selected_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    def _get_handle(self):
        return wrap_vtk(self._vtk_obj.GetHandle())
    def _set_handle(self, arg):
        old_val = self._get_handle()
        self._wrap_call(self._vtk_obj.SetHandle,
                        deref_vtk(arg))
        self.trait_property_changed('handle', old_val, arg)
    handle = traits.Property(_get_handle, _set_handle, help=\
        """
        Set/get the handle polydata.
        """
    )

    label_text = traits.String(r"0", enter_set=True, auto_set=False, help=\
        """
        A label may be associated with the seed. The string can be set
        via set_label_text. The visibility of the label can be turned on /
        off.
        """
    )
    def _label_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelText,
                        self.label_text)

    def _get_label_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextActor())
    label_text_actor = traits.Property(_get_label_text_actor, help=\
        """
        Get the label text actor
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Get the transform used to transform the generic handle polydata
        before placing it in the render window
        """
    )

    def set_label_text_scale(self, *args):
        """
        V.set_label_text_scale([float, float, float])
        C++: virtual void SetLabelTextScale(double scale[3])
        Scale text (font size along each dimension).
        """
        ret = self._wrap_call(self._vtk_obj.SetLabelTextScale, *args)
        return ret

    def set_uniform_scale(self, *args):
        """
        V.set_uniform_scale(float)
        C++: virtual void SetUniformScale(double scale)
        The handle may be scaled uniformly in all three dimensions using
        this API. The handle can also be scaled interactively using the
        right mouse button.
        """
        ret = self._wrap_call(self._vtk_obj.SetUniformScale, *args)
        return ret

    _updateable_traits_ = \
    (('display_position', 'GetDisplayPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_visibility',
    'GetHandleVisibility'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('tolerance',
    'GetTolerance'), ('dragable', 'GetDragable'), ('label_visibility',
    'GetLabelVisibility'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('active_representation', 'GetActiveRepresentation'), ('pickable',
    'GetPickable'), ('label_text', 'GetLabelText'), ('need_to_render',
    'GetNeedToRender'), ('reference_count', 'GetReferenceCount'),
    ('place_factor', 'GetPlaceFactor'), ('constrained', 'GetConstrained'),
    ('world_position', 'GetWorldPosition'), ('use_bounds',
    'GetUseBounds'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'handle_visibility', 'label_visibility',
    'need_to_render', 'pickable', 'use_bounds', 'visibility',
    'allocated_render_time', 'display_position', 'estimated_render_time',
    'handle_size', 'label_text', 'place_factor', 'render_time_multiplier',
    'tolerance', 'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractPolygonalHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'handle_visibility', 'label_visibility', 'need_to_render',
            'use_bounds', 'visibility'], [], ['allocated_render_time',
            'display_position', 'estimated_render_time', 'handle_size',
            'label_text', 'place_factor', 'render_time_multiplier', 'tolerance',
            'world_position']),
            title='Edit AbstractPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

