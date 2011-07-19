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

from tvtk.tvtk_classes.unsigned_int_array import UnsignedIntArray


class TypeUInt32Array(UnsignedIntArray):
    """
    TypeUInt32Array - dynamic, self-adjusting array of TypeUInt32
    
    Superclass: UnsignedIntArray
    
    TypeUInt32Array is an array of values of type TypeUInt32.  It
    provides methods for insertion and retrieval of values and will
    automatically resize itself to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTypeUInt32Array, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('name', 'GetName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('number_of_tuples',
    'GetNumberOfTuples'), ('number_of_components',
    'GetNumberOfComponents'), ('component_name', 'GetComponentName'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'component_name', 'name',
    'number_of_components', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TypeUInt32Array, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TypeUInt32Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples']),
            title='Edit TypeUInt32Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TypeUInt32Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

