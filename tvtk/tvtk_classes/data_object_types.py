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


class DataObjectTypes(Object):
    """
    DataObject - helper class to get VTK data object types as string
    and instantiate them
    
    Superclass: Object
    
    DataObjectTypes is a helper class that supports conversion between
    integer types defined in Type.h and string names as well as
    creation of data objects from either integer or string types. This
    class has to be updated every time a new data type is added to VTK.
    
    See Also:
    
    DataObject
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectTypes, obj, update, **traits)
    
    def get_class_name_from_type_id(self, *args):
        """
        V.get_class_name_from_type_id(int) -> string
        C++: static const char *GetClassNameFromTypeId(int typeId)
        Given an int (as defined in Type.h) identifier for a class
        return it's classname.
        """
        ret = self._wrap_call(self._vtk_obj.GetClassNameFromTypeId, *args)
        return ret

    def get_type_id_from_class_name(self, *args):
        """
        V.get_type_id_from_class_name(string) -> int
        C++: static int GetTypeIdFromClassName(const char *classname)
        Given a data object classname, return it's int identified (as
        defined in Type.h)
        """
        ret = self._wrap_call(self._vtk_obj.GetTypeIdFromClassName, *args)
        return ret

    def new_data_object(self, *args):
        """
        V.new_data_object(string) -> DataObject
        C++: static DataObject *NewDataObject(const char *classname)
        V.new_data_object(int) -> DataObject
        C++: static DataObject *NewDataObject(int typeId)
        Create (New) and return a data object of the given classname.
        """
        ret = self._wrap_call(self._vtk_obj.NewDataObject, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectTypes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DataObjectTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

