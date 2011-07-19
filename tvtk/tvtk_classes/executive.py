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


class Executive(Object):
    """
    Executive - Superclass for all pipeline executives in VTK.
    
    Superclass: Object
    
    Executive is the superclass for all pipeline executives in VTK. A
    VTK executive is responsible for controlling one instance of
    Algorithm.  A pipeline consists of one or more executives that
    control data flow.  Every reader, source, writer, or data processing
    algorithm in the pipeline is implemented in an instance of
    Algorithm.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExecutive, obj, update, **traits)
    
    def get_output_data(self, *args):
        """
        V.get_output_data(int) -> DataObject
        C++: virtual DataObject *GetOutputData(int port)
        Get/Set the data object for an output port of the algorithm.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputData, *args)
        return wrap_vtk(ret)

    def set_output_data(self, *args):
        """
        V.set_output_data(int, DataObject, Information)
        C++: virtual void SetOutputData(int port, DataObject *,
            Information *info)
        V.set_output_data(int, DataObject)
        C++: virtual void SetOutputData(int port, DataObject *)
        Get/Set the data object for an output port of the algorithm.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetOutputData, *my_args)
        return ret

    def _get_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetAlgorithm())
    algorithm = traits.Property(_get_algorithm, help=\
        """
        Get the algorithm to which this executive has been assigned.
        """
    )

    def get_input_data(self, *args):
        """
        V.get_input_data(int, int) -> DataObject
        C++: virtual DataObject *GetInputData(int port, int connection)
        Get the data object for an input port of the algorithm.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputData, *args)
        return wrap_vtk(ret)

    def get_input_executive(self, *args):
        """
        V.get_input_executive(int, int) -> Executive
        C++: Executive *GetInputExecutive(int port, int connection)
        Get the executive managing the given input connection.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputExecutive, *args)
        return wrap_vtk(ret)

    def get_input_information(self, *args):
        """
        V.get_input_information(int, int) -> Information
        C++: Information *GetInputInformation(int port, int connection)
        V.get_input_information(int) -> InformationVector
        C++: InformationVector *GetInputInformation(int port)
        Get the pipeline information for the given input connection.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputInformation, *args)
        return wrap_vtk(ret)

    def get_number_of_input_connections(self, *args):
        """
        V.get_number_of_input_connections(int) -> int
        C++: int GetNumberOfInputConnections(int port)
        Get the number of input connections on the given port.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfInputConnections, *args)
        return ret

    def _get_number_of_input_ports(self):
        return self._vtk_obj.GetNumberOfInputPorts()
    number_of_input_ports = traits.Property(_get_number_of_input_ports, help=\
        """
        Get the number of input/output ports for the algorithm associated
        with this executive.  Returns 0 if no algorithm is set.
        """
    )

    def _get_number_of_output_ports(self):
        return self._vtk_obj.GetNumberOfOutputPorts()
    number_of_output_ports = traits.Property(_get_number_of_output_ports, help=\
        """
        Get the number of input/output ports for the algorithm associated
        with this executive.  Returns 0 if no algorithm is set.
        """
    )

    def _get_output_information(self):
        return wrap_vtk(self._vtk_obj.GetOutputInformation())
    output_information = traits.Property(_get_output_information, help=\
        """
        Get the pipeline information object for the given output port.
        """
    )

    def get_producer_port(self, *args):
        """
        V.get_producer_port(DataObject) -> AlgorithmOutput
        C++: virtual AlgorithmOutput *GetProducerPort(DataObject *)
        Get the output port that produces the given data object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetProducerPort, *my_args)
        return wrap_vtk(ret)

    def ALGORITHM_AFTER_FORWARD(self):
        """
        V.algorithm__after__forward() -> InformationIntegerKey
        C++: static InformationIntegerKey *ALGORITHM_AFTER_FORWARD()
        Keys to program Executive::ProcessRequest with the default
        behavior for unknown requests.
        """
        ret = wrap_vtk(self._vtk_obj.ALGORITHM_AFTER_FORWARD())
        return ret
        

    def ALGORITHM_BEFORE_FORWARD(self):
        """
        V.algorithm__before__forward() -> InformationIntegerKey
        C++: static InformationIntegerKey *ALGORITHM_BEFORE_FORWARD()
        Keys to program Executive::ProcessRequest with the default
        behavior for unknown requests.
        """
        ret = wrap_vtk(self._vtk_obj.ALGORITHM_BEFORE_FORWARD())
        return ret
        

    def ALGORITHM_DIRECTION(self):
        """
        V.algorithm__direction() -> InformationIntegerKey
        C++: static InformationIntegerKey *ALGORITHM_DIRECTION()
        Keys to program Executive::ProcessRequest with the default
        behavior for unknown requests.
        """
        ret = wrap_vtk(self._vtk_obj.ALGORITHM_DIRECTION())
        return ret
        

    def CONSUMERS(self):
        """
        V.consumers() -> InformationExecutivePortVectorKey
        C++: static InformationExecutivePortVectorKey *CONSUMERS()
        Information key to store the executive/port number pairs
        consuming an information object.
        """
        ret = wrap_vtk(self._vtk_obj.CONSUMERS())
        return ret
        

    def FORWARD_DIRECTION(self):
        """
        V.forward__direction() -> InformationIntegerKey
        C++: static InformationIntegerKey *FORWARD_DIRECTION()
        Keys to program Executive::ProcessRequest with the default
        behavior for unknown requests.
        """
        ret = wrap_vtk(self._vtk_obj.FORWARD_DIRECTION())
        return ret
        

    def FROM_OUTPUT_PORT(self):
        """
        V.from__output__port() -> InformationIntegerKey
        C++: static InformationIntegerKey *FROM_OUTPUT_PORT()
        Information key to store the output port number from which a
        request is made.
        """
        ret = wrap_vtk(self._vtk_obj.FROM_OUTPUT_PORT())
        return ret
        

    def KEYS_TO_COPY(self):
        """
        V.keys__to__copy() -> InformationKeyVectorKey
        C++: static InformationKeyVectorKey *KEYS_TO_COPY()
        Keys to program Executive::ProcessRequest with the default
        behavior for unknown requests.
        """
        ret = wrap_vtk(self._vtk_obj.KEYS_TO_COPY())
        return ret
        

    def PRODUCER(self):
        """
        V.producer() -> InformationExecutivePortKey
        C++: static InformationExecutivePortKey *PRODUCER()
        Information key to store the executive/port number producing an
        information object.
        """
        ret = wrap_vtk(self._vtk_obj.PRODUCER())
        return ret
        

    def set_shared_output_information(self, *args):
        """
        V.set_shared_output_information(InformationVector)
        C++: void SetSharedOutputInformation(
            InformationVector *outInfoVec)
        Set a pointer to an outside instance of input or output
        information vectors.  No references are held to the given
        vectors, and setting this does not change the executive object
        modification time.  This is a preliminary interface to use in
        implementing filters with internal pipelines, and may change
        without notice when a future interface is created.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSharedOutputInformation, *my_args)
        return ret

    def update(self, *args):
        """
        V.update() -> int
        C++: virtual int Update()
        V.update(int) -> int
        C++: virtual int Update(int port)
        Bring the algorithm's outputs up-to-date.  Returns 1 for success
        and 0 for failure.
        """
        ret = self._wrap_call(self._vtk_obj.Update, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Executive, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Executive properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Executive properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Executive properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

