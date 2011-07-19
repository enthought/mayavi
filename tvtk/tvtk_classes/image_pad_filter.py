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


class ImagePadFilter(ThreadedImageAlgorithm):
    """
    ImagePadFilter - Super class for filters that fill in extra pixels.
    
    Superclass: ThreadedImageAlgorithm
    
    ImagePadFilter Changes the image extent of an image.  If the image
    extent is larger than the input image extent, the extra pixels are
    filled by an algorithm determined by the subclass. The image extent
    of the output has to be specified.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImagePadFilter, obj, update, **traits)
    
    output_number_of_scalar_components = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of output scalar components.
        """
    )
    def _output_number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputNumberOfScalarComponents,
                        self.output_number_of_scalar_components)

    output_whole_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        The image extent of the output has to be set explicitly.
        """
    )
    def _output_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputWholeExtent,
                        self.output_whole_extent)

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
            return super(ImagePadFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImagePadFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_threads',
            'output_number_of_scalar_components', 'output_whole_extent']),
            title='Edit ImagePadFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImagePadFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

