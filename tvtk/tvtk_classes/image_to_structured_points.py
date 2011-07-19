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


class ImageToStructuredPoints(ImageAlgorithm):
    """
    ImageToStructuredPoints - Attaches image pipeline to VTK. 
    
    Superclass: ImageAlgorithm
    
    ImageToStructuredPoints changes an image cache format to a
    structured points dataset.  It takes an Input plus an optional
    vector_input. The vector_input converts the RGB scalar components of
    the vector_input to vector pointdata attributes. This filter will try
    to reference count the data but in some cases it must make a copy.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageToStructuredPoints, obj, update, **traits)
    
    def _get_vector_input(self):
        return wrap_vtk(self._vtk_obj.GetVectorInput())
    def _set_vector_input(self, arg):
        old_val = self._get_vector_input()
        self._wrap_call(self._vtk_obj.SetVectorInput,
                        deref_vtk(arg))
        self.trait_property_changed('vector_input', old_val, arg)
    vector_input = traits.Property(_get_vector_input, _set_vector_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    def _get_structured_points_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredPointsOutput())
    structured_points_output = traits.Property(_get_structured_points_output, help=\
        """
        Get the output of the filter.
        """
    )

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
            return super(ImageToStructuredPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageToStructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ImageToStructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageToStructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

