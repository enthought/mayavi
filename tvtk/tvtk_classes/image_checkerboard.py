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


class ImageCheckerboard(ThreadedImageAlgorithm):
    """
    ImageCheckerboard - show two images at once using a checkboard
    pattern
    
    Superclass: ThreadedImageAlgorithm
    
    ImageCheckerboard displays two images as one using a checkerboard
     pattern. This filter can be used to compare two images. The
     checkerboard pattern is controlled by the number_of_divisions
     ivar. This controls the number of checkerboard divisions in the
    whole
     extent of the image.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageCheckerboard, obj, update, **traits)
    
    number_of_divisions = traits.Array(shape=(3,), value=(2, 2, 2), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _number_of_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfDivisions,
                        self.number_of_divisions)

    def set_input1(self, *args):
        """
        V.set_input1(DataObject)
        C++: virtual void SetInput1(DataObject *in)
        Set the two inputs to this filter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1, *my_args)
        return ret

    def set_input2(self, *args):
        """
        V.set_input2(DataObject)
        C++: virtual void SetInput2(DataObject *in)
        Set the two inputs to this filter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_divisions', 'GetNumberOfDivisions'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_divisions', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageCheckerboard, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageCheckerboard properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_divisions', 'number_of_threads']),
            title='Edit ImageCheckerboard properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageCheckerboard properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

