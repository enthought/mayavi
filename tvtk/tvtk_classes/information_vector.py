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


class InformationVector(Object):
    """
    InformationVector - Store zero or more Information instances.
    
    Superclass: Object
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationVector, obj, update, **traits)
    
    number_of_information_objects = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of information objects in the vector.  Setting
        the number to larger than the current number will create empty
        Information instances.  Setting the number to smaller than the
        current number will remove entries from higher indices.
        """
    )
    def _number_of_information_objects_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfInformationObjects,
                        self.number_of_information_objects)

    def get_information_object(self, *args):
        """
        V.get_information_object(int) -> Information
        C++: Information *GetInformationObject(int index)
        Get/Set the Information instance stored at the given index in
        the vector.  The vector will automatically expand to include the
        index given if necessary.  Missing entries in-between will be
        filled with empty Information instances.
        """
        ret = self._wrap_call(self._vtk_obj.GetInformationObject, *args)
        return wrap_vtk(ret)

    def set_information_object(self, *args):
        """
        V.set_information_object(int, Information)
        C++: void SetInformationObject(int index, Information *info)
        Get/Set the Information instance stored at the given index in
        the vector.  The vector will automatically expand to include the
        index given if necessary.  Missing entries in-between will be
        filled with empty Information instances.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInformationObject, *my_args)
        return ret

    def append(self, *args):
        """
        V.append(Information)
        C++: void Append(Information *info)
        Append/Remove an information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def copy(self, *args):
        """
        V.copy(InformationVector, int)
        C++: void Copy(InformationVector *from, int deep=0)
        Copy all information entries from the given Information
        instance.  Any previously existing entries are removed.  If
        deep==1, a deep copy of the information structure is performed
        (new instances of any contained Information and
        InformationVector objects are created).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Copy, *my_args)
        return ret

    def remove(self, *args):
        """
        V.remove(Information)
        C++: void Remove(Information *info)
        Append/Remove an information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Remove, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('number_of_information_objects', 'GetNumberOfInformationObjects'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_information_objects'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationVector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationVector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_information_objects']),
            title='Edit InformationVector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationVector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

