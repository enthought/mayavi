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


class SphereHandleRepresentation(HandleRepresentation):
    """
    SphereHandleRepresentation - A spherical rendition of point in 3d
    space
    
    Superclass: HandleRepresentation
    
    This class is a concrete implementation of HandleRepresentation.
    It renders handles as spherical blobs in 3d space.
    
    See Also:
    
    HandleRepresentation HandleWidget SphereSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereHandleRepresentation, obj, update, **traits)
    
    translation_mode = tvtk_base.true_bool_trait(help=\
        """
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated simultaneously as the
        point moves (i.e., the left and middle mouse buttons act the
        same).  Otherwise, only the cursor focal point moves, which is
        constrained by the bounds of the point representation. (Note that
        the bounds can be scaled up using the right mouse button.)
        """
    )
    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

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

    sphere_radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _sphere_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphereRadius,
                        self.sphere_radius)

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
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('sphere_radius',
    'GetSphereRadius'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('translation_mode', 'GetTranslationMode'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('tolerance',
    'GetTolerance'), ('active_representation', 'GetActiveRepresentation'),
    ('hot_spot_size', 'GetHotSpotSize'), ('pickable', 'GetPickable'),
    ('need_to_render', 'GetNeedToRender'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'),
    ('constrained', 'GetConstrained'), ('world_position',
    'GetWorldPosition'), ('use_bounds', 'GetUseBounds'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'translation_mode', 'use_bounds', 'visibility',
    'allocated_render_time', 'display_position', 'estimated_render_time',
    'handle_size', 'hot_spot_size', 'place_factor',
    'render_time_multiplier', 'sphere_radius', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereHandleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'need_to_render', 'translation_mode', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'display_position', 'estimated_render_time',
            'handle_size', 'hot_spot_size', 'place_factor',
            'render_time_multiplier', 'sphere_radius', 'tolerance',
            'world_position']),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

