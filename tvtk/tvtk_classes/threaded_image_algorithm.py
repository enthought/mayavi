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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ThreadedImageAlgorithm(ImageAlgorithm):
    """
    ThreadedImageAlgorithm - Generic filter that has one input..
    
    Superclass: ImageAlgorithm
    
    ThreadedImageAlgorithm is a filter superclass that hides much of
    the pipeline  complexity. It handles breaking the pipeline execution
    into smaller extents so that the ImageData limits are observed. It
    also provides support for multithreading. If you don't need any of
    this functionality, consider using SimpleImageToImageAlgorithm
    instead.
    
    See also:
    
    SimpleImageToImageAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThreadedImageAlgorithm, obj, update, **traits)
    
    number_of_threads = traits.Trait(2, traits.Range(1, 32, enter_set=True, auto_set=False), help=\
        """
        Get/Set the number of threads to create when rendering
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

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
            ImageData *outData, int extent[6], int threadId)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ThreadedExecute, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThreadedImageAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_threads']),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

