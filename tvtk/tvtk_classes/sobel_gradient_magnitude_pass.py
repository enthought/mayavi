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

from tvtk.tvtk_classes.image_processing_pass import ImageProcessingPass


class SobelGradientMagnitudePass(ImageProcessingPass):
    """
    SobelGradientMagnitudePass - Implement a post-processing edge
    
    Superclass: ImageProcessingPass
    
    Detect the edges of the image renderered by its delegate.
    Edge-detection uses a Sobel high-pass filter (3x3 kernel).
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    The delegate is used once.
    
    Its delegate is usually set to a CameraPass or to a
    post-processing pass.
    
    This pass requires a open_gl context that supports texture objects
    (TO), framebuffer objects (FBO) and GLSL. If not, it will emit an
    error message and will render its delegate and return.
    
    Implementation:
    
    To compute the gradient magnitude, the x and y components of the
    gradient (Gx and Gy) have to be computed first. Each computation of
    Gx and Gy uses a separable filter. The first pass takes the image
    from the delegate as the single input texture. The first pass has two
    outputs, one for the first part of Gx, Gx1, result of a convolution
    with (-1 0 1), one for the first part of Gy, Gy1, result of a
    convolution with (1 2 1). The second pass has two inputs, Gx1 and
    Gy1. Kernel (1 2 1)^T is applied to Gx1 and kernel (-1 0 1)^T is
    applied to Gx2. It gives the values for Gx and Gy. Thoses values are
    then used to compute the magnitude of the gradient which is stored in
    the render target. The gradient computation happens per component
    (R,G,B). A is arbitrarly set to 1 (full opacity).
    
    \image html SobelGradientMagnitudePassFigure.png\image latex
    SobelGradientMagnitudePassFigure.eps
    
    See Also:
    
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSobelGradientMagnitudePass, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SobelGradientMagnitudePass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SobelGradientMagnitudePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SobelGradientMagnitudePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SobelGradientMagnitudePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

