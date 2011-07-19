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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class RectilinearWipeRepresentation(WidgetRepresentation):
    """
    RectilinearWipeRepresentation - represent a
    RectilinearWipeWidget
    
    Superclass: WidgetRepresentation
    
    This class is used to represent and render a
    RectilinearWipeWidget. To use this class, you need to specify an
    instance of a ImageRectilinearWipe and ImageActor. This
    provides the information for this representation to construct and
    place itself.
    
    The class may be subclassed so that alternative representations can
    be created.  The class defines an API and a default implementation
    that the RectilinearWipeWidget interacts with to render itself in
    the scene.
    
    Caveats:
    
    The separation of the widget event handling and representation
    enables users and developers to create new appearances for the
    widget. It also facilitates parallel processing, where the client
    application handles events, and remote representations of the widget
    are slaves to the client (and do not handle events).
    
    See Also:
    
    RectilinearWipeWidget WidgetRepresentation AbstractWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectilinearWipeRepresentation, obj, update, **traits)
    
    tolerance = traits.Trait(5, traits.Range(1, 10, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    def _set_image_actor(self, arg):
        old_val = self._get_image_actor()
        self._wrap_call(self._vtk_obj.SetImageActor,
                        deref_vtk(arg))
        self.trait_property_changed('image_actor', old_val, arg)
    image_actor = traits.Property(_get_image_actor, _set_image_actor, help=\
        """
        Specify an instance of ImageActor to decorate.
        """
    )

    def _get_rectilinear_wipe(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearWipe())
    def _set_rectilinear_wipe(self, arg):
        old_val = self._get_rectilinear_wipe()
        self._wrap_call(self._vtk_obj.SetRectilinearWipe,
                        deref_vtk(arg))
        self.trait_property_changed('rectilinear_wipe', old_val, arg)
    rectilinear_wipe = traits.Property(_get_rectilinear_wipe, _set_rectilinear_wipe, help=\
        """
        Specify an instance of ImageRectilinearWipe to manipulate.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        Get the properties for the widget. This can be manipulated to set
        different colors, line widths, etc.
        """
    )

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('need_to_render', 'GetNeedToRender'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('pickable', 'GetPickable'), ('tolerance',
    'GetTolerance'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectilinearWipeRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RectilinearWipeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier', 'tolerance']),
            title='Edit RectilinearWipeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectilinearWipeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

