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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class StringToCategory(DataObjectAlgorithm):
    """
    StringToCategory - Creates a category array from a string array
    
    Superclass: DataObjectAlgorithm
    
    StringToCategory creates an integer array named "category" based
    on the values in a string array.  You may use this filter to create
    an array that you may use to color points/cells by the values in a
    string array.  Currently there is not support to color by a string
    array directly. The category values will range from zero to N-1,
    where N is the number of distinct strings in the string array.  Set
    the string array to process with set_input_array_to_process(_0,_0,_0,...). 
    The array may be in the point, cell, or field data of the data
    object.
    
    The list of unique strings, in the order they are mapped, can also be
    retrieved from output port 1. They are in a Table, stored in the
    "Strings" column as a StringArray.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStringToCategory, obj, update, **traits)
    
    category_array_name = traits.String(r"category", enter_set=True, auto_set=False, help=\
        """
        The name to give to the output IntArray of category values.
        """
    )
    def _category_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCategoryArrayName,
                        self.category_array_name)

    _updateable_traits_ = \
    (('category_array_name', 'GetCategoryArrayName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'category_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StringToCategory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StringToCategory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['category_array_name']),
            title='Edit StringToCategory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StringToCategory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

