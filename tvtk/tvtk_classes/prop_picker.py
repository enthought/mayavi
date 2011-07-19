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

from tvtk.tvtk_classes.abstract_prop_picker import AbstractPropPicker


class PropPicker(AbstractPropPicker):
    """
    PropPicker - pick an actor/prop using graphics hardware
    
    Superclass: AbstractPropPicker
    
    PropPicker is used to pick an actor/prop given a selection point
    (in display coordinates) and a renderer. This class uses graphics
    hardware/rendering system to pick rapidly (as compared to using ray
    casting as does CellPicker and PointPicker). This class
    determines the actor/prop and pick position in world coordinates;
    point and cell ids are not determined.
    
    See Also:
    
    Picker WorldPointPicker CellPicker PointPicker
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPropPicker, obj, update, **traits)
    
    def pick_prop(self, *args):
        """
        V.pick_prop(float, float, Renderer) -> int
        C++: int PickProp(double selectionX, double selectionY,
            Renderer *renderer)
        V.pick_prop(float, float, Renderer, PropCollection) -> int
        C++: int PickProp(double selectionX, double selectionY,
            Renderer *renderer, PropCollection *pickfrom)
        Perform the pick and set the picked_prop ivar. If something is
        picked, a 1 is returned, otherwise 0 is returned.  Use the
        get_view_prop() method to get the instance of Prop that was
        picked.  Props are picked from the renderers list of pickable
        Props.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PickProp, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PropPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], []),
            title='Edit PropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PropPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

