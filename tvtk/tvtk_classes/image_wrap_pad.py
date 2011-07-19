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

from tvtk.tvtk_classes.image_pad_filter import ImagePadFilter


class ImageWrapPad(ImagePadFilter):
    """
    ImageWrapPad - Makes an image larger by wrapping existing data.
    
    Superclass: ImagePadFilter
    
    ImageWrapPad performs a modulo operation on the output pixel index
    to determine the source input index.  The new image extent of the
    output has to be specified.  Input has to be the same scalar type as
    output.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageWrapPad, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('output_whole_extent', 'GetOutputWholeExtent'), ('number_of_threads',
    'GetNumberOfThreads'), ('output_number_of_scalar_components',
    'GetOutputNumberOfScalarComponents'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_threads',
    'output_number_of_scalar_components', 'output_whole_extent',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageWrapPad, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageWrapPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_threads',
            'output_number_of_scalar_components', 'output_whole_extent']),
            title='Edit ImageWrapPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageWrapPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

