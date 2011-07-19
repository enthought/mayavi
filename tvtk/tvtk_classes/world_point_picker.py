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

from tvtk.tvtk_classes.abstract_picker import AbstractPicker


class WorldPointPicker(AbstractPicker):
    """
    WorldPointPicker - find world x,y,z corresponding to display x,y,z
    
    Superclass: AbstractPicker
    
    WorldPointPicker is used to find the x,y,z world coordinate of a
    screen x,y,z. This picker cannot pick actors and/or mappers, it
    simply determines an x-y-z coordinate in world space. (It will always
    return a x-y-z, even if the selection point is not over a
    prop/actor.)
    
    Caveats:
    
    The pick_method() is not invoked, but start_pick_method() and
    end_pick_method() are.
    
    See Also:
    
    PropPicker Picker CellPicker PointPicker
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWorldPointPicker, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WorldPointPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WorldPointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], []),
            title='Edit WorldPointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WorldPointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

