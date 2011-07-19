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

from tvtk.tvtk_classes.image_stencil_source import ImageStencilSource


class ImplicitFunctionToImageStencil(ImageStencilSource):
    """
    ImplicitFunctionToImageStencil - clip an image with a function
    
    Superclass: ImageStencilSource
    
    ImplicitFunctionToImageStencil will convert a ImplicitFunction
    into a stencil that can be used with ImageStencil or with other
    classes that apply a stencil to an image.
    
    See Also:
    
    ImplicitFunction ImageStencil PolyDataToImageStencil
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitFunctionToImageStencil, obj, update, **traits)
    
    threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the threshold value for the implicit function.
        """
    )
    def _threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreshold,
                        self.threshold)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Specify the implicit function to convert into a stencil.
        """
    )

    _updateable_traits_ = \
    (('output_whole_extent', 'GetOutputWholeExtent'), ('output_spacing',
    'GetOutputSpacing'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('output_origin', 'GetOutputOrigin'),
    ('reference_count', 'GetReferenceCount'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('threshold', 'GetThreshold'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text', 'threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitFunctionToImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitFunctionToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['output_origin', 'output_spacing',
            'output_whole_extent', 'threshold']),
            title='Edit ImplicitFunctionToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitFunctionToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

