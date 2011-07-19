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


class SimpleImageToImageFilter(ImageAlgorithm):
    """
    SimpleImageToImageFilter - Generic image filter with one input.
    
    Superclass: ImageAlgorithm
    
    SimpleImageToImageFilter is a filter which aims to avoid much of
    the complexity associated with ImageAlgorithm (i.e. support for
    pieces, multi-threaded operation). If you need to write a simple
    image-image filter which operates on the whole input, use this as the
    superclass. The subclass has to provide only an execute method which
    takes input and output as arguments. Memory allocation is handled in
    SimpleImageToImageFilter. Also, you are guaranteed to have a valid
    input in the Execute(input, output) method. By default, this filter
    requests it's input's whole extent and copies the input's information
    (spacing, whole extent etc...) to the output. If the output's setup
    is different (for example, if it performs some sort of sub-sampling),
    execute_information has to be overwritten. As an example of how this
    can be done, you can look at ImageShrink3D::ExecuteInformation.
    For a complete example which uses templates to support generic data
    types, see SimpleImageToImageFilter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSimpleImageToImageFilter, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SimpleImageToImageFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SimpleImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SimpleImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SimpleImageToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

