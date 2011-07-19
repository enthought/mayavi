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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageAppend(ThreadedImageAlgorithm):
    """
    ImageAppend - Collects data from multiple inputs into one image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageAppend takes the components from multiple inputs and merges
    them into one output. The output images are append along the
    "_append_axis". Except for the append axis, all inputs must have the
    same extent. All inputs must have the same number of scalar
    components. A future extension might be to pad or clip inputs to have
    the same extent. The output has the same origin and spacing as the
    first input. The origin and spacing of all other inputs are ignored. 
    All inputs must have the same scalar type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageAppend, obj, update, **traits)
    
    preserve_extents = tvtk_base.false_bool_trait(help=\
        """
        By default "_preserve_extents" is off and the append axis is used.
        When "_preseve_extents" is on, the extent of the inputs is used to
        place the image in the output.  The whole extent of the output is
        the union of the input whole extents.  Any portion of the output
        not covered by the inputs is set to zero.  The origin and spacing
        is taken from the first input.
        """
    )
    def _preserve_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveExtents,
                        self.preserve_extents_)

    append_axis = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This axis is expanded to hold the multiple images. The default
        append_axis is the X axis. If you want to create a volue from a
        series of XY images, then you should set the append_axis to 2 (Z
        axis).
        """
    )
    def _append_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppendAxis,
                        self.append_axis)

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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int num)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get one input to this filter. This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use Algorithm::GetInputConnection(0, num).
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(int, DataObject)
        C++: void SetInput(int num, DataObject *input)
        V.set_input(DataObject)
        C++: void SetInput(DataObject *input)
        Set an Input of this filter.  This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use set_input_connection(), add_input_connection(), and
        replace_nth_input_connection() instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def _get_number_of_inputs(self):
        return self._vtk_obj.GetNumberOfInputs()
    number_of_inputs = traits.Property(_get_number_of_inputs, help=\
        """
        Get the number of inputs to this filter. This method is only for
        support of old-style pipeline connections.  When writing new code
        you should use Algorithm::GetNumberOfInputConnections(0).
        """
    )

    def replace_nth_input_connection(self, *args):
        """
        V.replace_nth_input_connection(int, AlgorithmOutput)
        C++: virtual void ReplaceNthInputConnection(int idx,
            AlgorithmOutput *input)
        Replace one of the input connections with a new input.  You can
        only replace input connections that you previously created with
        add_input_connection() or, in the case of the first input, with
        set_input_connection().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReplaceNthInputConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('append_axis', 'GetAppendAxis'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('preserve_extents', 'GetPreserveExtents'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'preserve_extents', 'release_data_flag', 'append_axis',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageAppend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageAppend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['preserve_extents'], [], ['append_axis',
            'number_of_threads']),
            title='Edit ImageAppend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageAppend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

