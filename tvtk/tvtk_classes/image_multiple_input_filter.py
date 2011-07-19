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

from tvtk.tvtk_classes.image_source import ImageSource


class ImageMultipleInputFilter(ImageSource):
    """
    ImageMultipleInputFilter - Generic filter that has N inputs.
    
    Superclass: ImageSource
    
    ImageMultipleInputFilter is a super class for filters that have
    any number of inputs. Streaming is not available in this class yet.
    
    See Also:
    
    ImageToImageFilter ImageInPlaceFilter ImageTwoInputFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMultipleInputFilter, obj, update, **traits)
    
    bypass = tvtk_base.false_bool_trait(help=\
        """
        Turning bypass on will cause the filter to turn off and simply
        pass the data from the first input (input0) through. It is
        implemented for consistency with ImageToImageFilter.
        """
    )
    def _bypass_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBypass,
                        self.bypass_)

    number_of_threads = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of threads to create when rendering
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    def get_input(self, *args):
        """
        V.get_input(int) -> ImageData
        C++: ImageData *GetInput(int num)
        V.get_input() -> ImageData
        C++: ImageData *GetInput()
        Get one input to this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(int, ImageData)
        C++: virtual void SetInput(int num, ImageData *input)
        Set an Input of this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def add_input(self, *args):
        """
        V.add_input(ImageData)
        C++: virtual void AddInput(ImageData *input)
        Adds an input to the first null position in the input list.
        Expands the list memory if necessary
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def remove_input(self, *args):
        """
        V.remove_input(ImageData)
        C++: virtual void RemoveInput(ImageData *input)
        Adds an input to the first null position in the input list.
        Expands the list memory if necessary
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def split_extent(self, *args):
        """
        V.split_extent([int, int, int, int, int, int], [int, int, int, int,
             int, int], int, int) -> int
        C++: virtual int SplitExtent(int splitExt[6], int startExt[6],
            int num, int total)
        Putting this here until I merge graphics and imaging streaming.
        """
        ret = self._wrap_call(self._vtk_obj.SplitExtent, *args)
        return ret

    _updateable_traits_ = \
    (('release_data_flag', 'GetReleaseDataFlag'), ('bypass', 'GetBypass'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'),
    ('reference_count', 'GetReferenceCount'), ('input', 'GetInput'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bypass', 'debug', 'global_warning_display',
    'release_data_flag', 'input', 'number_of_threads', 'progress_text',
    'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMultipleInputFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMultipleInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bypass'], [], ['input', 'number_of_threads',
            'release_data_flag']),
            title='Edit ImageMultipleInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMultipleInputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

