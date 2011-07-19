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

from tvtk.tvtk_classes.prop_collection import PropCollection


class Actor2DCollection(PropCollection):
    """
    Actor2DCollection -  a list of 2d actors
    
    Superclass: PropCollection
    
    Actor2DCollection is a subclass of Collection. 
    Actor2DCollection maintains a collection of Actor2D objects
    that is sorted by layer number, with lower layer numbers at the start
    of the list.  This allows the Actor2D objects to be rendered in
    the correct order.
    
    See Also:
    
    Actor2D Collection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkActor2DCollection, obj, update, **traits)
    
    def _get_last_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetLastActor2D())
    last_actor2d = traits.Property(_get_last_actor2d, help=\
        """
        Standard Collection methods
        """
    )

    def _get_last_item(self):
        return wrap_vtk(self._vtk_obj.GetLastItem())
    last_item = traits.Property(_get_last_item, help=\
        """
        Access routines that are provided for compatibility with previous
        version of VTK.  Please use the get_next_actor2d(),
        get_last_actor2d() variants where possible.
        """
    )

    def _get_next_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetNextActor2D())
    next_actor2d = traits.Property(_get_next_actor2d, help=\
        """
        Standard Collection methods
        """
    )

    def _get_next_item(self):
        return wrap_vtk(self._vtk_obj.GetNextItem())
    next_item = traits.Property(_get_next_item, help=\
        """
        Access routines that are provided for compatibility with previous
        version of VTK.  Please use the get_next_actor2d(),
        get_last_actor2d() variants where possible.
        """
    )

    def render_overlay(self, *args):
        """
        V.render_overlay(Viewport)
        C++: void RenderOverlay(Viewport *viewport)
        Sort and then render the collection of 2d actors.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderOverlay, *my_args)
        return ret

    def sort(self):
        """
        V.sort()
        C++: void Sort()
        Sorts the Actor2DCollection by layer number.  Smaller layer
        numbers are first.  Layer numbers can be any integer value.
        """
        ret = self._vtk_obj.Sort()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Actor2DCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Actor2DCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Actor2DCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Actor2DCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

