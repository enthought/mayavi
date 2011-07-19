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

from tvtk.tvtk_classes.image_multiple_input_filter import ImageMultipleInputFilter


class ImageTwoInputFilter(ImageMultipleInputFilter):
    """
    ImageTwoInputFilter - Generic superclass for filters that have
    
    Superclass: ImageMultipleInputFilter
    
    ImageTwoInputFilter handles two inputs. It is just a subclass of
    ImageMultipleInputFilter with some methods that are specific to
    two inputs.  Although the inputs are labeled input1 and input2, they
    are stored in an array indexed starting at 0.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageTwoInputFilter, obj, update, **traits)
    
    def _get_input2(self):
        return wrap_vtk(self._vtk_obj.GetInput2())
    def _set_input2(self, arg):
        old_val = self._get_input2()
        self._wrap_call(self._vtk_obj.SetInput2,
                        deref_vtk(arg))
        self.trait_property_changed('input2', old_val, arg)
    input2 = traits.Property(_get_input2, _set_input2, help=\
        """
        Get the inputs to this filter.
        """
    )

    def _get_input1(self):
        return wrap_vtk(self._vtk_obj.GetInput1())
    def _set_input1(self, arg):
        old_val = self._get_input1()
        self._wrap_call(self._vtk_obj.SetInput1,
                        deref_vtk(arg))
        self.trait_property_changed('input1', old_val, arg)
    input1 = traits.Property(_get_input1, _set_input1, help=\
        """
        Get the inputs to this filter.
        """
    )

    _updateable_traits_ = \
    (('number_of_threads', 'GetNumberOfThreads'), ('bypass', 'GetBypass'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('input', 'GetInput'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bypass', 'debug', 'global_warning_display',
    'release_data_flag', 'input', 'number_of_threads', 'progress_text',
    'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageTwoInputFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageTwoInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bypass'], [], ['input', 'number_of_threads',
            'release_data_flag']),
            title='Edit ImageTwoInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageTwoInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

