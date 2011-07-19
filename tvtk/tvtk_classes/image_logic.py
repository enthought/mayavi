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


class ImageLogic(ThreadedImageAlgorithm):
    """
    ImageLogic - And, or, xor, nand, nor, not.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageLogic implements basic logic operations. set_operation is used
    to select the filter's behavior. The filter can take two or one
    input. Inputs must have the same type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageLogic, obj, update, **traits)
    
    operation = traits.Trait('and_',
    tvtk_base.TraitRevPrefixMap({'or_': 1, 'xor': 2, 'not_': 5, 'nand': 3, 'and_': 0, 'nor': 4}), help=\
        """
        Set/Get the Operation to perform.
        """
    )
    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    output_true_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set the value to use for true in the output.
        """
    )
    def _output_true_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputTrueValue,
                        self.output_true_value)

    def set_input1(self, *args):
        """
        V.set_input1(DataObject)
        C++: virtual void SetInput1(DataObject *input)
        Set the Input1 of this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1, *my_args)
        return ret

    def set_input2(self, *args):
        """
        V.set_input2(DataObject)
        C++: virtual void SetInput2(DataObject *input)
        Set the Input2 of this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('output_true_value',
    'GetOutputTrueValue'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('operation',
    'GetOperation'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'operation', 'number_of_threads',
    'output_true_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageLogic, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageLogic properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['operation'], ['number_of_threads',
            'output_true_value']),
            title='Edit ImageLogic properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageLogic properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

