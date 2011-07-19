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

from tvtk.tvtk_classes.render_pass import RenderPass


class ImageProcessingPass(RenderPass):
    """
    ImageProcessingPass - Convenient class for post-processing passes.
    
    Superclass: RenderPass
    
    Abstract class with some convenient methods frequently used in
    subclasses.
    
    Implementation:
    
    See Also:
    
    RenderPass GaussianBlurPass SobelGradientMagnitudePass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageProcessingPass, obj, update, **traits)
    
    def _get_delegate_pass(self):
        return wrap_vtk(self._vtk_obj.GetDelegatePass())
    def _set_delegate_pass(self, arg):
        old_val = self._get_delegate_pass()
        self._wrap_call(self._vtk_obj.SetDelegatePass,
                        deref_vtk(arg))
        self.trait_property_changed('delegate_pass', old_val, arg)
    delegate_pass = traits.Property(_get_delegate_pass, _set_delegate_pass, help=\
        """
        Delegate for rendering the image to be processed. If it is NULL,
        nothing will be rendered and a warning will be emitted. It is
        usually set to a CameraPass or to a post-processing pass.
        Initial value is a NULL pointer.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageProcessingPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

