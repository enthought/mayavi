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

from tvtk.tvtk_classes.ray_cast_image_display_helper import RayCastImageDisplayHelper


class OpenGLRayCastImageDisplayHelper(RayCastImageDisplayHelper):
    """
    OpenGLRayCastImageDisplayHelper - open_gl subclass that draws the
    image to the screen
    
    Superclass: RayCastImageDisplayHelper
    
    This is the concrete implementation of a ray cast image display
    helper - a helper class responsible for drawing the image to the
    screen.
    
    See Also:
    
    RayCastImageDisplayHelper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRayCastImageDisplayHelper, obj, update, **traits)
    
    _updateable_traits_ = \
    (('pixel_scale', 'GetPixelScale'), ('reference_count',
    'GetReferenceCount'), ('pre_multiplied_colors',
    'GetPreMultipliedColors'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pre_multiplied_colors',
    'pixel_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLRayCastImageDisplayHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pre_multiplied_colors'], [], ['pixel_scale']),
            title='Edit OpenGLRayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

