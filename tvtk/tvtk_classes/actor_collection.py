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


class ActorCollection(PropCollection):
    """
    ActorCollection - a list of actors
    
    Superclass: PropCollection
    
    ActorCollection represents and provides methods to manipulate a
    list of actors (i.e., Actor and subclasses). The list is unsorted
    and duplicate entries are not prevented.
    
    See Also:
    
    Actor Collection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkActorCollection, obj, update, **traits)
    
    def _get_last_actor(self):
        return wrap_vtk(self._vtk_obj.GetLastActor())
    last_actor = traits.Property(_get_last_actor, help=\
        """
        Get the last actor in the list.
        """
    )

    def _get_last_item(self):
        return wrap_vtk(self._vtk_obj.GetLastItem())
    last_item = traits.Property(_get_last_item, help=\
        """
        Access routines that are provided for compatibility with previous
        version of VTK.  Please use the get_next_actor(), get_last_actor()
        variants where possible.
        """
    )

    def _get_next_actor(self):
        return wrap_vtk(self._vtk_obj.GetNextActor())
    next_actor = traits.Property(_get_next_actor, help=\
        """
        Get the next actor in the list.
        """
    )

    def _get_next_item(self):
        return wrap_vtk(self._vtk_obj.GetNextItem())
    next_item = traits.Property(_get_next_item, help=\
        """
        Access routines that are provided for compatibility with previous
        version of VTK.  Please use the get_next_actor(), get_last_actor()
        variants where possible.
        """
    )

    def apply_properties(self, *args):
        """
        V.apply_properties(Property)
        C++: void ApplyProperties(Property *p)
        Apply properties to all actors in this collection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyProperties, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ActorCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ActorCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ActorCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ActorCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

