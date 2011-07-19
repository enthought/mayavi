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


class ImageDataStreamer(ImageAlgorithm):
    """
    ImageDataStreamer - Initiates streaming on image data.
    
    Superclass: ImageAlgorithm
    
    To satisfy a request, this filter calls update on its input many
    times with smaller update extents.  All processing up stream streams
    smaller pieces.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDataStreamer, obj, update, **traits)
    
    def _get_extent_translator(self):
        return wrap_vtk(self._vtk_obj.GetExtentTranslator())
    def _set_extent_translator(self, arg):
        old_val = self._get_extent_translator()
        self._wrap_call(self._vtk_obj.SetExtentTranslator,
                        deref_vtk(arg))
        self.trait_property_changed('extent_translator', old_val, arg)
    extent_translator = traits.Property(_get_extent_translator, _set_extent_translator, help=\
        """
        Get the extent translator that will be used to split the requests
        """
    )

    number_of_stream_divisions = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Set how many pieces to divide the input into. void
        set_number_of_stream_divisions(int num); int
        get_number_of_stream_divisions();
        """
    )
    def _number_of_stream_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfStreamDivisions,
                        self.number_of_stream_divisions)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_stream_divisions', 'GetNumberOfStreamDivisions'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_stream_divisions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDataStreamer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_stream_divisions']),
            title='Edit ImageDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

