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

from tvtk.tvtk_classes.composite_data_set_algorithm import CompositeDataSetAlgorithm


class AppendCompositeDataLeaves(CompositeDataSetAlgorithm):
    """
    AppendCompositeDataLeaves - appends one or more composite datasets
    with the same structure together into a single output composite
    dataset
    
    Superclass: CompositeDataSetAlgorithm
    
    AppendCompositeDataLeaves is a filter that takes input composite
    datasets with the same structure: (1) the same number of entries and
    -- if any children are composites -- the same constraint holds from
    them; and (2) the same type of dataset at each position. It then
    creates an output dataset with the same structure whose leaves
    contain all the cells from the datasets at the corresponding leaves
    of the input datasets.
    
    Currently, only input polydata and unstructured grids are handled;
    other types of leaf datasets will be ignored and their positions in
    the output dataset will be NULL pointers. Point attributes (i.e.,
    scalars, vectors, normals, field data, etc.) are extracted and
    appended only if all datasets have the point attributes available.
    (For example, if one dataset has scalars but another does not,
    scalars will not be appended.)
    
    See Also:
    
    AppendPolyData AppendFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendCompositeDataLeaves, obj, update, **traits)
    
    append_field_data = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the field data of each dataset in the composite
        dataset is copied to the output. If append_field_data is non-zero,
        then field data arrays from all the inputs are added to the
        output. If there are duplicates, the array on the first input
        encountered is taken.
        """
    )
    def _append_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppendFieldData,
                        self.append_field_data_)

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
        V.get_input(int) -> CompositeDataSet
        C++: CompositeDataSet *GetInput(int idx)
        V.get_input() -> CompositeDataSet
        C++: CompositeDataSet *GetInput()
        Get any input of this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(DataObject)
        C++: void SetInput(DataObject *)
        V.set_input(int, DataObject)
        C++: void SetInput(int, DataObject *)
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

    def remove_input(self, *args):
        """
        V.remove_input(DataSet)
        C++: void RemoveInput(DataSet *in)
        Remove a dataset from the list of data to append.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    _updateable_traits_ = \
    (('append_field_data', 'GetAppendFieldData'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'append_field_data', 'debug',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendCompositeDataLeaves, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['append_field_data'], [], []),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

