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

from tvtk.tvtk_classes.collection import Collection


class PropCollection(Collection):
    """
    PropCollection - a list of Props
    
    Superclass: Collection
    
    PropCollection represents and provides methods to manipulate a
    list of Props (i.e., Prop and subclasses). The list is unsorted
    and duplicate entries are not prevented.
    
    See Also:
    
    Prop Collection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPropCollection, obj, update, **traits)
    
    def _get_last_prop(self):
        return wrap_vtk(self._vtk_obj.GetLastProp())
    last_prop = traits.Property(_get_last_prop, help=\
        """
        Get the last Prop in the list.
        """
    )

    def _get_next_prop(self):
        return wrap_vtk(self._vtk_obj.GetNextProp())
    next_prop = traits.Property(_get_next_prop, help=\
        """
        Get the next Prop in the list.
        """
    )

    def _get_number_of_paths(self):
        return self._vtk_obj.GetNumberOfPaths()
    number_of_paths = traits.Property(_get_number_of_paths, help=\
        """
        Get the number of paths contained in this list. (Recall that a
        Prop can consist of multiple parts.) Used in picking and other
        activities to get the parts of composite entities like
        Assembly or PropAssembly.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PropCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PropCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PropCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PropCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

