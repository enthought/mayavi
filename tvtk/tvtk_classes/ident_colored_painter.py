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

from tvtk.tvtk_classes.poly_data_painter import PolyDataPainter


class IdentColoredPainter(PolyDataPainter):
    """
    IdentColoredPainter - DEPRECATED A PolyDataPainter that colors
    each polygon
    
    Superclass: PolyDataPainter
    
    DEPRECATED. Refer to HardwareSelectionPolyDataPainter instead.
    This painter will color each polygon in a color that encodes an
    integer. Doing so allows us to determine what polygon is behind each
    pixel on the screen.
    
    See Also:
    
    VisibleCellSelection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIdentColoredPainter, obj, update, **traits)
    
    def get_actor_from_id(self, *args):
        """
        V.get_actor_from_id(int) -> Prop
        C++: Prop *GetActorFromId(IdType id)"""
        ret = self._wrap_call(self._vtk_obj.GetActorFromId, *args)
        return wrap_vtk(ret)

    def color_by_actor_id(self, *args):
        """
        V.color_by_actor_id(Prop)
        C++: void ColorByActorId(Prop *ActorId)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ColorByActorId, *my_args)
        return ret

    def color_by_constant(self, *args):
        """
        V.color_by_constant(int)
        C++: void ColorByConstant(unsigned int constant)"""
        ret = self._wrap_call(self._vtk_obj.ColorByConstant, *args)
        return ret

    def color_by_increasing_ident(self, *args):
        """
        V.color_by_increasing_ident(int)
        C++: void ColorByIncreasingIdent(unsigned int plane)"""
        ret = self._wrap_call(self._vtk_obj.ColorByIncreasingIdent, *args)
        return ret

    def color_by_vertex(self):
        """
        V.color_by_vertex()
        C++: void ColorByVertex()"""
        ret = self._vtk_obj.ColorByVertex()
        return ret
        

    def reset_current_id(self):
        """
        V.reset_current_id()
        C++: void ResetCurrentId()"""
        ret = self._vtk_obj.ResetCurrentId()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IdentColoredPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IdentColoredPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit IdentColoredPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IdentColoredPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

