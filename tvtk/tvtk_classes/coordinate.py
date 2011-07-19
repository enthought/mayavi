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


class Coordinate(Object):
    """
    Coordinate - perform coordinate transformation, and represent
    position, in a variety of vtk coordinate systems
    
    Superclass: Object
    
    Coordinate represents position in a variety of coordinate systems,
    and converts position to other coordinate systems. It also supports
    relative positioning, so you can create a cascade of Coordinate
    objects (no loops please!) that refer to each other. The typical
    usage of this object is to set the coordinate system in which to
    represent a position (e.g.,
    set_coordinate_system_to_normalized_display()), set the value of the
    coordinate (e.g., set_value()), and then invoke the appropriate method
    to convert to another coordinate system (e.g.,
    get_computed_world_value()).
    
    The coordinate systems in vtk are as follows: <PRE>
     DISPLAY -             x-y pixel values in window
     NORMALIZED DISPLAY -  x-y (0,1) normalized values
     VIEWPORT -            x-y pixel values in viewport
     NORMALIZED VIEWPORT - x-y (0,1) normalized value in viewport
     VIEW -                x-y-z (-1,1) values in camera coordinates. (z
    is depth)
     WORLD -               x-y-z global coordinate values
     USERDEFINED -         x-y-z in User defined space </PRE>
    
    If you cascade Coordinate objects, you refer to another
    Coordinate object which in turn can refer to others, and so on.
    This allows you to create composite groups of things like Actor2D
    that are positioned relative to one another. Note that in cascaded
    sequences, each Coordinate object may be specified in different
    coordinate systems!
    
    See Also:
    
    Actor2D ScalarBarActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCoordinate, obj, update, **traits)
    
    coordinate_system = traits.Trait('world',
    tvtk_base.TraitRevPrefixMap({'normalized_display': 1, 'normalized_viewport': 3, 'world': 5, 'display': 0, 'viewport': 2, 'view': 4}), help=\
        """
        Set/get the coordinate system which this coordinate is defined
        in. The options are Display, Normalized Display, Viewport,
        Normalized Viewport, View, and World.
        """
    )
    def _coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordinateSystem,
                        self.coordinate_system_)

    def _get_reference_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetReferenceCoordinate())
    def _set_reference_coordinate(self, arg):
        old_val = self._get_reference_coordinate()
        self._wrap_call(self._vtk_obj.SetReferenceCoordinate,
                        deref_vtk(arg))
        self.trait_property_changed('reference_coordinate', old_val, arg)
    reference_coordinate = traits.Property(_get_reference_coordinate, _set_reference_coordinate, help=\
        """
        If this coordinate is relative to another coordinate, then
        specify that coordinate as the reference_coordinate. If this is
        NULL the coordinate is assumed to be absolute.
        """
    )

    def _get_viewport(self):
        return wrap_vtk(self._vtk_obj.GetViewport())
    def _set_viewport(self, arg):
        old_val = self._get_viewport()
        self._wrap_call(self._vtk_obj.SetViewport,
                        deref_vtk(arg))
        self.trait_property_changed('viewport', old_val, arg)
    viewport = traits.Property(_get_viewport, _set_viewport, help=\
        """
        If you want this coordinate to be relative to a specific
        Viewport (vtk_renderer) then you can specify that here. NOTE:
        this is a raw pointer, not a weak pointer not a reference counted
        object to avoid reference cycle loop between rendering classes
        and filter classes.
        """
    )

    value = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    def get_computed_display_value(self, *args):
        """
        V.get_computed_display_value(Viewport) -> (int, int)
        C++: int *GetComputedDisplayValue(Viewport *)
        Return the computed value in a specified coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedDisplayValue, *my_args)
        return ret

    def get_computed_double_display_value(self, *args):
        """
        V.get_computed_double_display_value(Viewport) -> (float, float)
        C++: double *GetComputedDoubleDisplayValue(Viewport *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedDoubleDisplayValue, *my_args)
        return ret

    def get_computed_double_viewport_value(self, *args):
        """
        V.get_computed_double_viewport_value(Viewport) -> (float, float)
        C++: double *GetComputedDoubleViewportValue(Viewport *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedDoubleViewportValue, *my_args)
        return ret

    def get_computed_local_display_value(self, *args):
        """
        V.get_computed_local_display_value(Viewport) -> (int, int)
        C++: int *GetComputedLocalDisplayValue(Viewport *)
        Return the computed value in a specified coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedLocalDisplayValue, *my_args)
        return ret

    def get_computed_viewport_value(self, *args):
        """
        V.get_computed_viewport_value(Viewport) -> (int, int)
        C++: int *GetComputedViewportValue(Viewport *)
        Return the computed value in a specified coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedViewportValue, *my_args)
        return ret

    def get_computed_world_value(self, *args):
        """
        V.get_computed_world_value(Viewport) -> (float, float, float)
        C++: double *GetComputedWorldValue(Viewport *)
        Return the computed value in a specified coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComputedWorldValue, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('value',
    'GetValue'), ('coordinate_system', 'GetCoordinateSystem'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'coordinate_system', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Coordinate, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Coordinate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['coordinate_system'], ['value']),
            title='Edit Coordinate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Coordinate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

