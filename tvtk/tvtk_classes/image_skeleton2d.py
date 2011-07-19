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

from tvtk.tvtk_classes.image_iterate_filter import ImageIterateFilter


class ImageSkeleton2D(ImageIterateFilter):
    """
    ImageSkeleton2D - Skeleton of 2d images.
    
    Superclass: ImageIterateFilter
    
    ImageSkeleton2D should leave only single pixel width lines of
    non-zero-valued pixels (values of 1 are not allowed). It works by
    erosion on a 3x3 neighborhood with special rules. The number of
    iterations determines how far the filter can erode. There are three
    pruning levels:
     prune == 0 will leave traces on all angles...
     prune == 1 will not leave traces on 135 degree angles, but will on
    90.
     prune == 2 does not leave traces on any angles leaving only closed
    loops. Prune defaults to zero. The output scalar type is the same as
    the input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSkeleton2D, obj, update, **traits)
    
    prune = tvtk_base.false_bool_trait(help=\
        """
        When prune is on, only closed loops are left unchanged.
        """
    )
    def _prune_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrune,
                        self.prune_)

    def set_number_of_iterations(self, *args):
        """
        V.set_number_of_iterations(int)
        C++: void SetNumberOfIterations(int num)
        Sets the number of cycles in the erosion.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfIterations, *args)
        return ret

    _updateable_traits_ = \
    (('prune', 'GetPrune'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'prune',
    'release_data_flag', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSkeleton2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSkeleton2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['prune'], [], ['number_of_threads']),
            title='Edit ImageSkeleton2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSkeleton2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

