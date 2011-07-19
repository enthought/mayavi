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


class PointHandleRepresentation3D(HandleRepresentation):
    """
    PointHandleRepresentation3D - represent the position of a point in
    3d space
    
    Superclass: HandleRepresentation
    
    This class is used to represent a HandleWidget. It represents a
    position in 3d world coordinates using a x-y-z cursor. The cursor can
    be configured to show a bounding box and/or shadows.
    
    See Also:
    
    HandleRepresentation HandleWidget Cursor3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointHandleRepresentation3D, obj, update, **traits)
    
    y_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe y-shadows.
        """
    )
    def _y_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYShadows,
                        self.y_shadows_)

    translation_mode = tvtk_base.true_bool_trait(help=\
        """
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the set_bounds() method.)
        """
    )
    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    z_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe z-shadows.
        """
    )
    def _z_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZShadows,
                        self.z_shadows_)

    outline = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe bounding box.
        """
    )
    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    x_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe x-shadows.
        """
    )
    def _x_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXShadows,
                        self.x_shadows_)

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

    hot_spot_size = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
    )
    def _hot_spot_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHotSpotSize,
                        self.hot_spot_size)

    def all_off(self):
        """
        V.all_off()
        C++: void AllOff()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOff()
        return ret
        

    def all_on(self):
        """
        V.all_on()
        C++: void AllOn()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOn()
        return ret
        

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        Methods to make this class properly act like a
        WidgetRepresentation.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    _updateable_traits_ = \
    (('display_position', 'GetDisplayPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('x_shadows', 'GetXShadows'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('y_shadows', 'GetYShadows'),
    ('active_representation', 'GetActiveRepresentation'),
    ('hot_spot_size', 'GetHotSpotSize'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('constrained', 'GetConstrained'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('outline',
    'GetOutline'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('world_position', 'GetWorldPosition'), ('z_shadows', 'GetZShadows'),
    ('reference_count', 'GetReferenceCount'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('translation_mode',
    'GetTranslationMode'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'outline', 'pickable',
    'translation_mode', 'use_bounds', 'visibility', 'x_shadows',
    'y_shadows', 'z_shadows', 'allocated_render_time', 'display_position',
    'estimated_render_time', 'handle_size', 'hot_spot_size',
    'place_factor', 'render_time_multiplier', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'need_to_render', 'outline', 'translation_mode', 'use_bounds',
            'visibility', 'x_shadows', 'y_shadows', 'z_shadows'], [],
            ['allocated_render_time', 'display_position', 'estimated_render_time',
            'handle_size', 'hot_spot_size', 'place_factor',
            'render_time_multiplier', 'tolerance', 'world_position']),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

