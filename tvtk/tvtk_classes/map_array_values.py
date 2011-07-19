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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class MapArrayValues(PassInputTypeAlgorithm):
    """
    MapArrayValues - Map values in an input array to different values
    in
    
    Superclass: PassInputTypeAlgorithm
    
    MapArrayValues allows you to associate certain values of an
    attribute array (on either a vertex, edge, point, or cell) with
    different values in a newly created attribute array.
    
    MapArrayValues manages an internal STL map of Variants that can
    be added to or cleared. When this filter executes, each "key" is
    searched for in the input array and the indices of the output array
    at which there were matches the set to the mapped "value".
    
    You can control whether the input array values are passed to the
    output before the mapping occurs (using pass_array) or, if not, what
    value to set the unmapped indices to (using fill_value).
    
    One application of this filter is to help address the dirty data
    problem. For example, using MapArrayValues you could associate the
    vertex values "Foo, John", "Foo, John.", and "John Foo" with a single
    entity.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMapArrayValues, obj, update, **traits)
    
    pass_array = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether to copy the data from the input array to the
        output array before the mapping occurs. If turned off, fill_value
        is used to initialize any unmapped array indices. Default is off.
        """
    )
    def _pass_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassArray,
                        self.pass_array_)

    input_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the input array. This must be set prior to
        execution.
        """
    )
    def _input_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputArrayName,
                        self.input_array_name)

    output_array_name = traits.String(r"ArrayMap", enter_set=True, auto_set=False, help=\
        """
        Set/Get the name of the output array. Default is "_array_map".
        """
    )
    def _output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputArrayName,
                        self.output_array_name)

    fill_value = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get whether to copy the data from the input array to the
        output array before the mapping occurs. If turned off, fill_value
        is used to initialize any unmapped array indices. Default is -1.
        """
    )
    def _fill_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillValue,
                        self.fill_value)

    field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get where the data is located that is being mapped. See
        field_type enumeration for possible values. Default is POINT_DATA.
        """
    )
    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    output_array_type = traits.Int(6, enter_set=True, auto_set=False, help=\
        """
        Set/Get the type of the output array. See SetGet.h for
        possible values. Default is VTK_INT.
        """
    )
    def _output_array_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputArrayType,
                        self.output_array_type)

    def _get_map_size(self):
        return self._vtk_obj.GetMapSize()
    map_size = traits.Property(_get_map_size, help=\
        """
        Get the size of the internal map.
        """
    )

    def add_to_map(self, *args):
        """
        V.add_to_map(Variant, Variant)
        C++: void AddToMap(Variant from, Variant to)
        V.add_to_map(int, int)
        C++: void AddToMap(int from, int to)
        V.add_to_map(int, string)
        C++: void AddToMap(int from, char *to)
        V.add_to_map(string, int)
        C++: void AddToMap(char *from, int to)
        V.add_to_map(string, string)
        C++: void AddToMap(char *from, char *to)
        Add to the internal STL map. "from" should be a value in the
        input array and "to" should be the new value it gets assigned in
        the output array.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddToMap, *my_args)
        return ret

    def clear_map(self):
        """
        V.clear_map()
        C++: void ClearMap()
        Clear the internal map.
        """
        ret = self._vtk_obj.ClearMap()
        return ret
        

    _updateable_traits_ = \
    (('output_array_name', 'GetOutputArrayName'), ('field_type',
    'GetFieldType'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('fill_value', 'GetFillValue'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('input_array_name',
    'GetInputArrayName'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('output_array_type', 'GetOutputArrayType'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('pass_array',
    'GetPassArray'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_array',
    'release_data_flag', 'field_type', 'fill_value', 'input_array_name',
    'output_array_name', 'output_array_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MapArrayValues, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MapArrayValues properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_array'], [], ['field_type', 'fill_value',
            'input_array_name', 'output_array_name', 'output_array_type']),
            title='Edit MapArrayValues properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MapArrayValues properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

