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


class GenericVertexAttributeMapping(Object):
    """
    GenericVertexAttributeMapping - stores mapping for data arrays to
    
    Superclass: Object
    
    GenericVertexAttributeMapping stores mapping between data arrays
    and generic vertex attributes. It is used by PainterPolyDataMapper
    to pass the mappings to the painter which rendering the attributes.
    
    Thanks:
    
    Support for generic vertex attributes in VTK was contributed in
    collaboration with Stephane Ploix at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericVertexAttributeMapping, obj, update, **traits)
    
    def get_array_name(self, *args):
        """
        V.get_array_name(int) -> string
        C++: const char *GetArrayName(unsigned int index)
        Get the array name at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayName, *args)
        return ret

    def get_attribute_name(self, *args):
        """
        V.get_attribute_name(int) -> string
        C++: const char *GetAttributeName(unsigned int index)
        Get the attribute name at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeName, *args)
        return ret

    def get_component(self, *args):
        """
        V.get_component(int) -> int
        C++: int GetComponent(unsigned int index)
        Get the component no. at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetComponent, *args)
        return ret

    def get_field_association(self, *args):
        """
        V.get_field_association(int) -> int
        C++: int GetFieldAssociation(unsigned int index)
        Get the field association at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldAssociation, *args)
        return ret

    def _get_number_of_mappings(self):
        return self._vtk_obj.GetNumberOfMappings()
    number_of_mappings = traits.Property(_get_number_of_mappings, help=\
        """
        Get number of mapppings.
        """
    )

    def get_texture_unit(self, *args):
        """
        V.get_texture_unit(int) -> int
        C++: int GetTextureUnit(unsigned int index)
        Get the component no. at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetTextureUnit, *args)
        return ret

    def add_mapping(self, *args):
        """
        V.add_mapping(string, string, int, int)
        C++: void AddMapping(const char *attributeName,
            const char *arrayName, int fieldAssociation, int component)
        V.add_mapping(int, string, int, int)
        C++: void AddMapping(int unit, const char *arrayName,
            int fieldAssociation, int component)
        Select a data array from the point/cell data and map it to a
        generic vertex attribute. Note that indices change when a mapping
        is added/removed.
        """
        ret = self._wrap_call(self._vtk_obj.AddMapping, *args)
        return ret

    def remove_all_mappings(self):
        """
        V.remove_all_mappings()
        C++: void RemoveAllMappings()
        Remove all mappings.
        """
        ret = self._vtk_obj.RemoveAllMappings()
        return ret
        

    def remove_mapping(self, *args):
        """
        V.remove_mapping(string) -> bool
        C++: bool RemoveMapping(const char *attributeName)
        Remove a vertex attribute mapping.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveMapping, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericVertexAttributeMapping, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericVertexAttributeMapping properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GenericVertexAttributeMapping properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericVertexAttributeMapping properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

