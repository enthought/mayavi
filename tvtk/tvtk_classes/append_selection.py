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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class AppendSelection(SelectionAlgorithm):
    """
    AppendSelection - appends one or more selections together
    
    Superclass: SelectionAlgorithm
    
    AppendSelection is a filter that appends one of more selections
    into a single selection.  All selections must have the same content
    type unless append_by_union is false.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendSelection, obj, update, **traits)
    
    append_by_union = tvtk_base.true_bool_trait(help=\
        """
        When set to true, all the selections are combined together to
        form a single Selection output. When set to false, the output
        is a composite selection with input selections as the children of
        the composite selection. This allows for selections with
        different content types and properties. Default is true.
        """
    )
    def _append_by_union_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppendByUnion,
                        self.append_by_union_)

    user_managed_inputs = tvtk_base.false_bool_trait(help=\
        """
        user_managed_inputs allows the user to set inputs by number instead
        of using the add_input/_remove_input functions. Calls to
        set_number_of_inputs/_set_input_by_number should not be mixed with calls
        to add_input/_remove_input. By default, user_managed_inputs is false.
        """
    )
    def _user_managed_inputs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserManagedInputs,
                        self.user_managed_inputs_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> Selection
        C++: Selection *GetInput(int idx)
        V.get_input() -> Selection
        C++: Selection *GetInput()
        Get any input of this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(DataObject)
        C++: void SetInput(DataObject *obj)
        V.set_input(int, DataObject)
        C++: void SetInput(int index, DataObject *obj)
        Set an input of this algorithm. You should not override these
        methods because they are not the only way to connect a pipeline.
        Note that these methods support old-style pipeline connections.
        When writing new code you should use the more general
        Algorithm::SetInputConnection().  These methods transform the
        input index to the input port index, not an index of a connection
        within a single port.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def add_input(self, *args):
        """
        V.add_input(Selection)
        C++: void AddInput(Selection *)
        Add a dataset to the list of data to append. Should not be used
        when user_managed_inputs is true, use set_input_by_number instead.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def remove_input(self, *args):
        """
        V.remove_input(Selection)
        C++: void RemoveInput(Selection *)
        Remove a dataset from the list of data to append. Should not be
        used when user_managed_inputs is true, use set_input_by_number (NULL)
        instead.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def set_input_by_number(self, *args):
        """
        V.set_input_by_number(int, Selection)
        C++: void SetInputByNumber(int num, Selection *input)"""
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputByNumber, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def set_number_of_inputs(self, *args):
        """
        V.set_number_of_inputs(int)
        C++: void SetNumberOfInputs(int num)
        Directly set(allocate) number of inputs, should only be used when
        user_managed_inputs is true.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfInputs, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('append_by_union', 'GetAppendByUnion'), ('user_managed_inputs',
    'GetUserManagedInputs'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'append_by_union', 'debug',
    'global_warning_display', 'release_data_flag', 'user_managed_inputs',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendSelection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['append_by_union', 'user_managed_inputs'], [], []),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

