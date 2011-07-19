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


class AbstractPicker(Object):
    """
    AbstractPicker - define API for picking subclasses
    
    Superclass: Object
    
    AbstractPicker is an abstract superclass that defines a minimal
    API for its concrete subclasses. The minimum functionality of a
    picker is to return the x-y-z global coordinate position of a pick
    (the pick itself is defined in display coordinates).
    
    The API to this class is to invoke the Pick() method with a selection
    point (in display coordinates - pixels) and a renderer. Then get the
    resulting pick position in global coordinates with the
    get_pick_position() method.
    
    Picker fires events during the picking process.  These events are
    start_pick_event, pick_event, and end_pick_event which are invoked prior
    to picking, when something is picked, and after all picking
    candidates have been tested. Note that during the pick process the
    pick_event of Prop (and its subclasses such as Actor) is fired
    prior to the pick_event of Picker.
    
    Caveats:
    
    AbstractPicker and its subclasses will not pick props that are
    "unpickable" (see Prop) or are fully transparent (if transparency
    is a property of the Prop).
    
    There are two classes of pickers: those that pick using geometric
    methods (typically a ray cast); and those that use rendering
    hardware. Geometric methods return more information but are slower.
    Hardware methods are much faster and return minimal information.
    Examples of geometric pickers include Picker, CellPicker, and
    PointPicker. Examples of hardware pickers include
    WorldPointPicker and PropPicker.
    
    See Also:
    
    PropPicker uses hardware acceleration to pick an instance of
    Prop. (This means that 2d and 3d props can be picked, and it's
    relatively fast.) If you need to pick cells or points, you might wish
    to use CellPicker or PointPicker. WorldPointPicker is the
    fastest picker, returning an x-y-z coordinate value using the
    hardware z-buffer. Picker can be used to pick the bounding box of
    3d props.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractPicker, obj, update, **traits)
    
    pick_from_list = tvtk_base.false_bool_trait(help=\
        """
        Use these methods to control whether to limit the picking to this
        list (rather than renderer's actors). Make sure that the pick
        list contains actors that referred to by the picker's renderer.
        """
    )
    def _pick_from_list_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickFromList,
                        self.pick_from_list_)

    def _get_pick_list(self):
        return wrap_vtk(self._vtk_obj.GetPickList())
    pick_list = traits.Property(_get_pick_list, help=\
        """
        Return the list of actors in the pick_list.
        """
    )

    def _get_pick_position(self):
        return self._vtk_obj.GetPickPosition()
    pick_position = traits.Property(_get_pick_position, help=\
        """
        Return position in global coordinates of pick point.
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    renderer = traits.Property(_get_renderer, help=\
        """
        Get the renderer in which pick event occurred.
        """
    )

    def _get_selection_point(self):
        return self._vtk_obj.GetSelectionPoint()
    selection_point = traits.Property(_get_selection_point, help=\
        """
        Get the selection point in screen (pixel) coordinates. The third
        value is related to z-buffer depth. (Normally should be =0.)
        """
    )

    def add_pick_list(self, *args):
        """
        V.add_pick_list(Prop)
        C++: void AddPickList(Prop *)
        Add an actor to the pick list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPickList, *my_args)
        return ret

    def delete_pick_list(self, *args):
        """
        V.delete_pick_list(Prop)
        C++: void DeletePickList(Prop *)
        Delete an actor from the pick list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeletePickList, *my_args)
        return ret

    def initialize_pick_list(self):
        """
        V.initialize_pick_list()
        C++: void InitializePickList()
        Initialize list of actors in pick list.
        """
        ret = self._vtk_obj.InitializePickList()
        return ret
        

    def pick(self, *args):
        """
        V.pick(float, float, float, Renderer) -> int
        C++: virtual int Pick(double selectionX, double selectionY,
            double selectionZ, Renderer *renderer)
        V.pick([float, float, float], Renderer) -> int
        C++: int Pick(double selectionPt[3], Renderer *ren)
        Perform pick operation with selection point provided. Normally
        the first two values for the selection point are x-y pixel
        coordinate, and the third value is =0. Return non-zero if
        something was successfully picked.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Pick, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], []),
            title='Edit AbstractPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

