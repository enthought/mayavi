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

from tvtk.tvtk_classes.camera import Camera


class OpenGLCamera(Camera):
    """
    OpenGLCamera - open_gl camera
    
    Superclass: Camera
    
    OpenGLCamera is a concrete implementation of the abstract class
    Camera.  OpenGLCamera interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLCamera, obj, update, **traits)
    
    _updateable_traits_ = \
    (('head_tracked', 'GetHeadTracked'), ('view_plane_normal',
    'GetViewPlaneNormal'), ('window_center', 'GetWindowCenter'),
    ('clipping_range', 'GetClippingRange'), ('parallel_scale',
    'GetParallelScale'), ('view_up', 'GetViewUp'),
    ('use_horizontal_view_angle', 'GetUseHorizontalViewAngle'),
    ('focal_disk', 'GetFocalDisk'), ('debug', 'GetDebug'), ('view_shear',
    'GetViewShear'), ('view_angle', 'GetViewAngle'), ('focal_point',
    'GetFocalPoint'), ('distance', 'GetDistance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('eye_angle',
    'GetEyeAngle'), ('thickness', 'GetThickness'), ('left_eye',
    'GetLeftEye'), ('reference_count', 'GetReferenceCount'), ('position',
    'GetPosition'), ('parallel_projection', 'GetParallelProjection'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'parallel_projection',
    'use_horizontal_view_angle', 'clipping_range', 'distance',
    'eye_angle', 'focal_disk', 'focal_point', 'head_tracked', 'left_eye',
    'parallel_scale', 'position', 'thickness', 'view_angle',
    'view_plane_normal', 'view_shear', 'view_up', 'window_center'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLCamera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['parallel_projection', 'use_horizontal_view_angle'],
            [], ['clipping_range', 'distance', 'eye_angle', 'focal_disk',
            'focal_point', 'head_tracked', 'left_eye', 'parallel_scale',
            'position', 'thickness', 'view_angle', 'view_plane_normal',
            'view_shear', 'view_up', 'window_center']),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

