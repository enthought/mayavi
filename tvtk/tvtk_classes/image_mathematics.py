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


class ImageMathematics(ThreadedImageAlgorithm):
    """
    ImageMathematics - Add, subtract, multiply, divide, invert, sin,
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMathematics implements basic mathematic operations
    set_operation is used to select the filters behavior.  The filter can
    take two or one input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMathematics, obj, update, **traits)
    
    divide_by_zero_to_c = tvtk_base.false_bool_trait(help=\
        """
        How to handle divide by zero. Default is 0.
        """
    )
    def _divide_by_zero_to_c_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivideByZeroToC,
                        self.divide_by_zero_to_c_)

    operation = traits.Trait('add',
    tvtk_base.TraitRevPrefixMap({'cos': 6, 'complex_multiply': 19, 'divide': 3, 'atan': 14, 'min': 12, 'max': 13, 'invert': 4, 'add_constant': 17, 'replace_c_by_k': 20, 'multiply_by_k': 16, 'atan2': 15, 'add': 0, 'square': 10, 'square_root': 11, 'exp': 7, 'conjugate': 18, 'multiply': 2, 'absolute_value': 9, 'subtract': 1, 'sin': 5, 'log': 8}), help=\
        """
        Set/Get the Operation to perform.
        """
    )
    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    constant_k = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        A constant used by some operations (typically multiplicative).
        Default is 1.
        """
    )
    def _constant_k_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstantK,
                        self.constant_k)

    constant_c = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        A constant used by some operations (typically additive). Default
        is 0.
        """
    )
    def _constant_c_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstantC,
                        self.constant_c)

    def set_input1(self, *args):
        """
        V.set_input1(DataObject)
        C++: virtual void SetInput1(DataObject *in)
        Set the two inputs to this filter. For some operations, the
        second input is not used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1, *my_args)
        return ret

    def set_input2(self, *args):
        """
        V.set_input2(DataObject)
        C++: virtual void SetInput2(DataObject *in)
        Set the two inputs to this filter. For some operations, the
        second input is not used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2, *my_args)
        return ret

    _updateable_traits_ = \
    (('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('progress_text', 'GetProgressText'), ('constant_k', 'GetConstantK'),
    ('reference_count', 'GetReferenceCount'), ('divide_by_zero_to_c',
    'GetDivideByZeroToC'), ('number_of_threads', 'GetNumberOfThreads'),
    ('constant_c', 'GetConstantC'), ('progress', 'GetProgress'),
    ('operation', 'GetOperation'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'divide_by_zero_to_c',
    'global_warning_display', 'release_data_flag', 'operation',
    'constant_c', 'constant_k', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMathematics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['divide_by_zero_to_c'], ['operation'], ['constant_c',
            'constant_k', 'number_of_threads']),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

