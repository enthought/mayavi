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


class Algorithm(Object):
    """
    Algorithm - Superclass for all sources, filters, and sinks in VTK.
    
    Superclass: Object
    
    Algorithm is the superclass for all sources, filters, and sinks in
    VTK.  It defines a generalized interface for executing data
    processing algorithms.  Pipeline connections are associated with
    input and output ports that are independent of the type of data
    passing through the connections.
    
    Instances may be used independently or within pipelines with a
    variety of architectures and update mechanisms.  Pipelines are
    controlled by instances of Executive.  Every Algorithm instance
    has an associated Executive when it is used in a pipeline.  The
    executive is responsible for data flow.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAlgorithm, obj, update, **traits)
    
    release_data_flag = tvtk_base.false_bool_trait(help=\
        """
        Turn release data flag on or off for all output ports.
        """
    )
    def _release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReleaseDataFlag,
                        self.release_data_flag_)

    abort_execute = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the abort_execute flag for the process object. Process
        objects may handle premature termination of execution in
        different ways.
        """
    )
    def _abort_execute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbortExecute,
                        self.abort_execute_)

    progress_text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the current text message associated with the progress state.
        This may be used by a calling process/GUI. Note: Because
        set_progress_text() is called from inside request_data() it does not
        modify the algorithm object. Algorithms are not allowed to modify
        themselves from inside request_data().
        """
    )
    def _progress_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgressText,
                        self.progress_text)

    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    def _set_information(self, arg):
        old_val = self._get_information()
        self._wrap_call(self._vtk_obj.SetInformation,
                        deref_vtk(arg))
        self.trait_property_changed('information', old_val, arg)
    information = traits.Property(_get_information, _set_information, help=\
        """
        Set/Get the information object associated with this algorithm.
        """
    )

    def _get_executive(self):
        return wrap_vtk(self._vtk_obj.GetExecutive())
    def _set_executive(self, arg):
        old_val = self._get_executive()
        self._wrap_call(self._vtk_obj.SetExecutive,
                        deref_vtk(arg))
        self.trait_property_changed('executive', old_val, arg)
    executive = traits.Property(_get_executive, _set_executive, help=\
        """
        Get this algorithm's executive.  If it has none, a default
        executive will be created.
        """
    )

    def _get_input_connection(self):
        if self._vtk_obj.GetTotalNumberOfInputConnections():
            return wrap_vtk(self._vtk_obj.GetInputConnection(0, 0))
        else:
            return None
    def _set_input_connection(self, obj):
        old_val = self._get_input_connection()
        self._wrap_call(self._vtk_obj.SetInputConnection, deref_vtk(obj))
        self.trait_property_changed('input_connection', old_val, obj)
    input_connection = traits.Property(_get_input_connection,
                                       _set_input_connection,
                                       help="The first input connection for this object, i.e. the result of `get_input_connection(0, 0)`.")
    
    def get_input_connection(self, *args):
        """
        V.get_input_connection(int, int) -> AlgorithmOutput
        C++: AlgorithmOutput *GetInputConnection(int port, int index)
        Get the algorithm output port connected to an input port.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputConnection, *args)
        return wrap_vtk(ret)

    def set_input_connection(self, *args):
        """
        V.set_input_connection(int, AlgorithmOutput)
        C++: virtual void SetInputConnection(int port,
            AlgorithmOutput *input)
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *input)
        Set the connection for the given input port index.  Each input
        port of a filter has a specific purpose.  A port may have zero or
        more connections and the required number is specified by each
        filter.  Setting the connection with this method removes all
        other connections from the port.  To add more than one connection
        use add_input_connection().
        
        The input for the connection is the output port of another
        filter, which is obtained with get_output_port().  Typical usage is
        
        
          filter_2->_set_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    progress = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the execution progress of a process object.
        """
    )
    def _progress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgress,
                        self.progress)

    def _get_error_code(self):
        return self._vtk_obj.GetErrorCode()
    error_code = traits.Property(_get_error_code, help=\
        """
        The error code contains a possible error that occured while
        reading or writing the file.
        """
    )

    def get_input_array_information(self, *args):
        """
        V.get_input_array_information(int) -> Information
        C++: Information *GetInputArrayInformation(int idx)
        Get the info object for the specified input array to this
        algorithm
        """
        ret = self._wrap_call(self._vtk_obj.GetInputArrayInformation, *args)
        return wrap_vtk(ret)

    def get_input_data_object(self, *args):
        """
        V.get_input_data_object(int, int) -> DataObject
        C++: DataObject *GetInputDataObject(int port, int connection)
        Get the data object that will contain the algorithm input for the
        given port and given connection.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputDataObject, *args)
        return wrap_vtk(ret)

    def get_input_port_information(self, *args):
        """
        V.get_input_port_information(int) -> Information
        C++: Information *GetInputPortInformation(int port)
        Get the information object associated with an input port.  There
        is one input port per kind of input to the algorithm.  Each input
        port tells executives what kind of data and downstream requests
        this algorithm can handle for that input.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputPortInformation, *args)
        return wrap_vtk(ret)

    def get_number_of_input_connections(self, *args):
        """
        V.get_number_of_input_connections(int) -> int
        C++: int GetNumberOfInputConnections(int port)
        Get the number of inputs currently connected to a port.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfInputConnections, *args)
        return ret

    def _get_number_of_input_ports(self):
        return self._vtk_obj.GetNumberOfInputPorts()
    number_of_input_ports = traits.Property(_get_number_of_input_ports, help=\
        """
        Get the number of input ports used by the algorithm.
        """
    )

    def _get_number_of_output_ports(self):
        return self._vtk_obj.GetNumberOfOutputPorts()
    number_of_output_ports = traits.Property(_get_number_of_output_ports, help=\
        """
        Get the number of output ports provided by the algorithm.
        """
    )

    def get_output_data_object(self, *args):
        """
        V.get_output_data_object(int) -> DataObject
        C++: DataObject *GetOutputDataObject(int port)
        Get the data object that will contain the algorithm output for
        the given port.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputDataObject, *args)
        return wrap_vtk(ret)

    def _get_output_port(self):
        if self._vtk_obj.GetNumberOfOutputPorts():
            return wrap_vtk(self._vtk_obj.GetOutputPort())
        else:
            return None
    output_port = traits.Property(_get_output_port, help=\
        """
        Get a proxy object corresponding to the given output port of this
        algorithm.  The proxy object can be passed to another algorithm's
        set_input_connection(), add_input_connection(), and
        remove_input_connection() methods to modify pipeline connectivity.
        """
    )

    def get_output_port_information(self, *args):
        """
        V.get_output_port_information(int) -> Information
        C++: Information *GetOutputPortInformation(int port)
        Get the information object associated with an output port.  There
        is one output port per output from the algorithm.  Each output
        port tells executives what kind of upstream requests this
        algorithm can handle for that output.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputPortInformation, *args)
        return wrap_vtk(ret)

    def _get_total_number_of_input_connections(self):
        return self._vtk_obj.GetTotalNumberOfInputConnections()
    total_number_of_input_connections = traits.Property(_get_total_number_of_input_connections, help=\
        """
        Get the total number of inputs for this algorithm
        """
    )

    def add_input_connection(self, *args):
        """
        V.add_input_connection(int, AlgorithmOutput)
        C++: virtual void AddInputConnection(int port,
            AlgorithmOutput *input)
        V.add_input_connection(AlgorithmOutput)
        C++: virtual void AddInputConnection(AlgorithmOutput *input)
        Add a connection to the given input port index.  See
        set_input_connection() for details on input connections.  This
        method is the complement to remove_input_connection() in that it
        adds only the connection specified without affecting other
        connections.  Typical usage is
        
        
          filter_2->_add_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInputConnection, *my_args)
        return ret

    def compute_priority(self):
        """
        V.compute_priority() -> float
        C++: virtual double ComputePriority()
        Returns the priority of the piece described by the current update
        extent. The priority is a number between 0.0 and 1.0 with 0
        meaning skippable (REQUEST_DATA not needed) and 1.0 meaning
        important.
        """
        ret = self._vtk_obj.ComputePriority()
        return ret
        

    def convert_total_input_to_port_connection(self, *args):
        """
        V.convert_total_input_to_port_connection(int, int, int)
        C++: void ConvertTotalInputToPortConnection(int ind, int &port,
            int &conn)
        Convenience routine to convert from a linear ordering of input
        connections to a port/connection pair.
        """
        ret = self._wrap_call(self._vtk_obj.ConvertTotalInputToPortConnection, *args)
        return ret

    def has_executive(self):
        """
        V.has_executive() -> int
        C++: int HasExecutive()
        Check whether this algorithm has an assigned executive.  This
        will NOT create a default executive.
        """
        ret = self._vtk_obj.HasExecutive()
        return ret
        

    def INPUT_ARRAYS_TO_PROCESS(self):
        """
        V.input__arrays__to__process() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *INPUT_ARRAYS_TO_PROCESS(
            )
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_ARRAYS_TO_PROCESS())
        return ret
        

    def INPUT_CONNECTION(self):
        """
        V.input__connection() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_CONNECTION()
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_CONNECTION())
        return ret
        

    def INPUT_IS_OPTIONAL(self):
        """
        V.input__is__optional() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_IS_OPTIONAL()
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_IS_OPTIONAL())
        return ret
        

    def INPUT_IS_REPEATABLE(self):
        """
        V.input__is__repeatable() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_IS_REPEATABLE()
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_IS_REPEATABLE())
        return ret
        

    def INPUT_PORT(self):
        """
        V.input__port() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_PORT()
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_PORT())
        return ret
        

    def INPUT_REQUIRED_DATA_TYPE(self):
        """
        V.input__required__data__type() -> InformationStringVectorKey
        C++: static InformationStringVectorKey *INPUT_REQUIRED_DATA_TYPE(
            )
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_REQUIRED_DATA_TYPE())
        return ret
        

    def INPUT_REQUIRED_FIELDS(self):
        """
        V.input__required__fields() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *INPUT_REQUIRED_FIELDS(
            )
        Keys used to specify input port requirements.
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_REQUIRED_FIELDS())
        return ret
        

    def modify_request(self, *args):
        """
        V.modify_request(Information, int) -> int
        C++: virtual int ModifyRequest(Information *request, int when)
        This method gives the algorithm a chance to modify the contents
        of a request before or after (specified in the when argument) it
        is forwarded. The default implementation is empty. Returns 1 on
        success, 0 on failure. When can be either
        Executive::BeforeForward or Executive::AfterForward.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ModifyRequest, *my_args)
        return ret

    def PRESERVES_ATTRIBUTES(self):
        """
        V.preserves__attributes() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_ATTRIBUTES()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_ATTRIBUTES())
        return ret
        

    def PRESERVES_BOUNDS(self):
        """
        V.preserves__bounds() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_BOUNDS()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_BOUNDS())
        return ret
        

    def PRESERVES_DATASET(self):
        """
        V.preserves__dataset() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_DATASET()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_DATASET())
        return ret
        

    def PRESERVES_GEOMETRY(self):
        """
        V.preserves__geometry() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_GEOMETRY()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_GEOMETRY())
        return ret
        

    def PRESERVES_RANGES(self):
        """
        V.preserves__ranges() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_RANGES()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_RANGES())
        return ret
        

    def PRESERVES_TOPOLOGY(self):
        """
        V.preserves__topology() -> InformationIntegerKey
        C++: static InformationIntegerKey *PRESERVES_TOPOLOGY()
        These are flags that can be set that let the pipeline keep
        accurate meta-information for compute_priority.
        """
        ret = wrap_vtk(self._vtk_obj.PRESERVES_TOPOLOGY())
        return ret
        

    def process_request(self, *args):
        """
        V.process_request(Information, Collection,
            InformationVector) -> int
        C++: int ProcessRequest(Information *request,
            Collection *inInfo, InformationVector *outInfo)
        Version of process_request() that is wrapped. This converts the
        collection to an array and calls the other version.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ProcessRequest, *my_args)
        return ret

    def remove_all_inputs(self):
        """
        V.remove_all_inputs()
        C++: void RemoveAllInputs()
        Remove all the input data.
        """
        old_val = self._get_input()
        ret = self._vtk_obj.RemoveAllInputs()
        self.trait_property_changed('input', old_val, self._get_input())
        return ret
        

    def remove_input_connection(self, *args):
        """
        V.remove_input_connection(int, AlgorithmOutput)
        C++: virtual void RemoveInputConnection(int port,
            AlgorithmOutput *input)
        Remove a connection from the given input port index.  See
        set_input_connection() for details on input connection.  This
        method is the complement to add_input_connection() in that it
        removes only the connection specified without affecting other
        connections.  Typical usage is
        
        
          filter_2->_remove_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInputConnection, *my_args)
        return ret

    def set_default_executive_prototype(self, *args):
        """
        V.set_default_executive_prototype(Executive)
        C++: static void SetDefaultExecutivePrototype(Executive *proto)
        If the default_executive_prototype is set, a copy of it is created
        in create_default_executive() using new_instance().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDefaultExecutivePrototype, *my_args)
        return ret

    def set_input_array_to_process(self, *args):
        """
        V.set_input_array_to_process(int, int, int, int, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, const char *name)
        V.set_input_array_to_process(int, int, int, int, int)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, int fieldAttributeType)
        V.set_input_array_to_process(int, Information)
        C++: virtual void SetInputArrayToProcess(int idx,
            Information *info)
        V.set_input_array_to_process(int, int, int, string, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, const char *fieldAssociation,
            const char *attributeTypeorName)
        Set the input data arrays that this algorithm will process.
        Specifically the idx array that this algorithm will process
        (starting from 0) is the array on port, connection with the
        specified association and name or attribute type (such as
        SCALARS). The field_association refers to which field in the data
        object the array is stored. See DataObject::FieldAssociations
        for detail.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputArrayToProcess, *my_args)
        return ret

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Bring this algorithm's outputs up-to-date.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    def update_extent_is_empty(self, *args):
        """
        V.update_extent_is_empty(DataObject) -> int
        C++: int UpdateExtentIsEmpty(DataObject *output)
        V.update_extent_is_empty(Information, int) -> int
        C++: int UpdateExtentIsEmpty(Information *pinfo,
            int extentType)
        This detects when the update_extent will generate no data This
        condition is satisfied when the update_extent has zero volume
        (0,-1,...) or the update_number_of_pieces is 0. The source uses this
        call to determine whether to call Execute.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateExtentIsEmpty, *my_args)
        return ret

    def update_information(self):
        """
        V.update_information()
        C++: virtual void UpdateInformation()
        Backward compatibility method to invoke update_information on
        executive.
        """
        ret = self._vtk_obj.UpdateInformation()
        return ret
        

    def update_progress(self, *args):
        """
        V.update_progress(float)
        C++: void UpdateProgress(double amount)
        Update the progress of the process object. If a progress_method
        exists, executes it.  Then set the Progress ivar to amount. The
        parameter amount should range between (0,1).
        """
        ret = self._wrap_call(self._vtk_obj.UpdateProgress, *args)
        return ret

    def update_whole_extent(self):
        """
        V.update_whole_extent()
        C++: virtual void UpdateWholeExtent()
        Bring this algorithm's outputs up-to-date.
        """
        ret = self._vtk_obj.UpdateWholeExtent()
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
            return super(Algorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

