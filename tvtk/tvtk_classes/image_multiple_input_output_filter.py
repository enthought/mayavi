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


class ImageMultipleInputOutputFilter(ImageMultipleInputFilter):
    """
    ImageMultipleInputOutputFilter - Generic filter that has N inputs.
    
    Superclass: ImageMultipleInputFilter
    
    ImageMultipleInputOutputFilter is a super class for filters that
    have any number of inputs. Streaming is not available in this class
    yet.
    
    See Also:
    
    ImageToImageFilter ImageInPlaceFilter ImageTwoInputFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMultipleInputOutputFilter, obj, update, **traits)
    
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
            return super(ImageMultipleInputOutputFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMultipleInputOutputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bypass'], [], ['input', 'number_of_threads',
            'release_data_flag']),
            title='Edit ImageMultipleInputOutputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMultipleInputOutputFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

