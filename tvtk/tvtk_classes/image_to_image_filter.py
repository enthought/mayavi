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


class ImageToImageFilter(ImageSource):
    """
    ImageToImageFilter - Generic filter that has one input of type
    ImageData
    
    Superclass: ImageSource
    
    ImageToImageFilter is a filter superclass that hides much of the
    pipeline  complexity. It handles breaking the pipeline execution into
    smaller extents so that the ImageData limits are observed. It also
    provides support for multithreading. If you don't need any of this
    functionality, consider using SimpleImageToImageFilter instead.
    
    Warning:
    
    This used to be the parent class for most imaging filter in VTK4.x,
    now this role has been replaced by ImageAlgorithm. You should
    consider using ImageAlgorithm instead, when writing filter for
    VTK5 and above. This class was kept to ensure full backward
    compatibility.
    
    See also:
    
    SimpleImageToImageFilter ImageSpatialFilter ImageAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageToImageFilter, obj, update, **traits)
    
    bypass = tvtk_base.false_bool_trait(help=\
        """
        Obsolete feature - do not use.
        """
    )
    def _bypass_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBypass,
                        self.bypass_)

    number_of_threads = traits.Trait(2, traits.Range(1, 32, enter_set=True, auto_set=False), help=\
        """
        Get/Set the number of threads to create when rendering
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the Input of a filter.
        """
    )

    input_memory_limit = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _input_memory_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputMemoryLimit,
                        self.input_memory_limit)

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

    def threaded_execute(self, *args):
        """
        V.threaded_execute(ImageData, ImageData, [int, int, int, int,
             int, int], int)
        C++: virtual void ThreadedExecute(ImageData *inData,
            ImageData *outData, int extent[6], int threadId)
        If the subclass does not define an Execute method, then the task
        will be broken up, multiple threads will be spawned, and each
        thread will call this method. It is public so that the thread
        functions can call this method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ThreadedExecute, *my_args)
        return ret

    _updateable_traits_ = \
    (('release_data_flag', 'GetReleaseDataFlag'), ('bypass', 'GetBypass'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('input_memory_limit',
    'GetInputMemoryLimit'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bypass', 'debug', 'global_warning_display',
    'release_data_flag', 'input_memory_limit', 'number_of_threads',
    'progress_text', 'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageToImageFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bypass'], [], ['input_memory_limit',
            'number_of_threads', 'release_data_flag']),
            title='Edit ImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

