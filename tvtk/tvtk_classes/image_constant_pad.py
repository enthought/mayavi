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


class ImageConstantPad(ImagePadFilter):
    """
    ImageConstantPad - Makes image larger by padding with constant.
    
    Superclass: ImagePadFilter
    
    ImageConstantPad changes the image extent of its input. Any pixels
    outside of the original image extent are filled with a constant value
    (default is 0.0).
    
    See Also:
    
    ImageWrapPad ImageMirrorPad
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageConstantPad, obj, update, **traits)
    
    constant = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the pad value.
        """
    )
    def _constant_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstant,
                        self.constant)

    _updateable_traits_ = \
    (('constant', 'GetConstant'), ('output_whole_extent',
    'GetOutputWholeExtent'), ('output_number_of_scalar_components',
    'GetOutputNumberOfScalarComponents'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'constant', 'number_of_threads',
    'output_number_of_scalar_components', 'output_whole_extent',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageConstantPad, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageConstantPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['constant', 'number_of_threads',
            'output_number_of_scalar_components', 'output_whole_extent']),
            title='Edit ImageConstantPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageConstantPad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

