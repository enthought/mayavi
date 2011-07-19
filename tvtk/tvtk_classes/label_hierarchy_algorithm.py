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

from tvtk.tvtk_classes.algorithm import Algorithm


class LabelHierarchyAlgorithm(Algorithm):
    """
    LabelHierarchyAlgorithm - Superclass for algorithms that produce
    only label hierarchies as output
    
    Superclass: Algorithm
    
    LabelHierarchyAlgorithm is a convenience class to make writing
    algorithms easier. It is also designed to help transition old
    algorithms to the new pipeline architecture. There are some
    assumptions and defaults made by this class you should be aware of.
    This class defaults such that your filter will have one input port
    and one output port. If that is not the case simply change it with
    set_number_of_input_ports etc. See this class constructor for the
    default. This class also provides a fill_input_port_info method that by
    default says that all inputs will be data_objects. If that isn't the
    case then please override this method in your subclass. This class
    breaks out the downstream requests into separate functions such as
    request_data and request_information.  You should implement
    request_data( request, input_vec, output_vec) in subclasses.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelHierarchyAlgorithm, obj, update, **traits)
    
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
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

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    def _set_output(self, obj):
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)
    output = traits.Property(_get_output, _set_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> LabelHierarchy
        C++: LabelHierarchy *GetOutput()
        V.get_output(int) -> LabelHierarchy
        C++: LabelHierarchy *GetOutput(int)
        Get the output data object for a port on this algorithm.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def set_output(self, obj):
        """
        V.set_output(DataObject)
        C++: virtual void SetOutput(DataObject *d)
        Get the output data object for a port on this algorithm.
        """
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

    def get_label_hierarchy_input(self, *args):
        """
        V.get_label_hierarchy_input(int) -> LabelHierarchy
        C++: LabelHierarchy *GetLabelHierarchyInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetLabelHierarchyInput, *args)
        return wrap_vtk(ret)

    def add_input(self, *args):
        """
        V.add_input(DataObject)
        C++: void AddInput(DataObject *)
        V.add_input(int, DataObject)
        C++: void AddInput(int, DataObject *)
        Add an input of this algorithm.  Note that these methods support
        old-style pipeline connections.  When writing new code you should
        use the more general Algorithm::AddInputConnection().  See
        set_input() for details.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelHierarchyAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelHierarchyAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit LabelHierarchyAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelHierarchyAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

