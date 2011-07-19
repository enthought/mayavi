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

from tvtk.tvtk_classes.border_representation import BorderRepresentation


class CameraRepresentation(BorderRepresentation):
    """
    CameraRepresentation - represent the CameraWidget
    
    Superclass: BorderRepresentation
    
    This class provides support for interactively saving a series of
    camera views into an interpolated path (using CameraInterpolator).
    The class typically works in conjunction with CameraWidget. To use
    this class simply specify the camera to interpolate and use the
    methods add_camera_to_path(), animate_path(), and initialize_path() to add
    a new camera view, animate the current views, and initialize the
    interpolation.
    
    See Also:
    
    CameraWidget CameraInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCameraRepresentation, obj, update, **traits)
    
    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Specify the camera to interpolate. This must be specified by the
        user.
        """
    )

    number_of_frames = traits.Trait(24, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of frames to generate when playback is initiated.
        """
    )
    def _number_of_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfFrames,
                        self.number_of_frames)

    def _get_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetInterpolator())
    def _set_interpolator(self, arg):
        old_val = self._get_interpolator()
        self._wrap_call(self._vtk_obj.SetInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('interpolator', old_val, arg)
    interpolator = traits.Property(_get_interpolator, _set_interpolator, help=\
        """
        Get the CameraInterpolator used to interpolate and save the
        sequence of camera views. If not defined, one is created
        automatically. Note that you can access this object to set the
        interpolation type (linear, spline) and other instance variables.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        By obtaining this property you can specify the properties of the
        representation.
        """
    )

    def add_camera_to_path(self):
        """
        V.add_camera_to_path()
        C++: void AddCameraToPath()
        These methods are used to create interpolated camera paths.  The
        add_camera_to_path() method adds the view defined by the current
        camera (via set_camera()) to the interpolated camera path.
        animate_path() interpolates number_of_frames along the current path.
        initialize_path() resets the interpolated path to its initial,
        empty configuration.
        """
        ret = self._vtk_obj.AddCameraToPath()
        return ret
        

    def animate_path(self, *args):
        """
        V.animate_path(RenderWindowInteractor)
        C++: void AnimatePath(RenderWindowInteractor *rwi)
        These methods are used to create interpolated camera paths.  The
        add_camera_to_path() method adds the view defined by the current
        camera (via set_camera()) to the interpolated camera path.
        animate_path() interpolates number_of_frames along the current path.
        initialize_path() resets the interpolated path to its initial,
        empty configuration.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AnimatePath, *my_args)
        return ret

    def initialize_path(self):
        """
        V.initialize_path()
        C++: void InitializePath()
        These methods are used to create interpolated camera paths.  The
        add_camera_to_path() method adds the view defined by the current
        camera (via set_camera()) to the interpolated camera path.
        animate_path() interpolates number_of_frames along the current path.
        initialize_path() resets the interpolated path to its initial,
        empty configuration.
        """
        ret = self._vtk_obj.InitializePath()
        return ret
        

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('handle_size', 'GetHandleSize'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('show_border', 'GetShowBorder'), ('moving', 'GetMoving'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('number_of_frames',
    'GetNumberOfFrames'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('position2',
    'GetPosition2'), ('proportional_resize', 'GetProportionalResize'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('maximum_size', 'GetMaximumSize'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'proportional_resize', 'use_bounds',
    'visibility', 'show_border', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'number_of_frames', 'place_factor', 'position',
    'position2', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CameraRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CameraRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['moving', 'need_to_render', 'proportional_resize',
            'use_bounds', 'visibility'], ['show_border'],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'number_of_frames', 'place_factor',
            'position', 'position2', 'render_time_multiplier', 'tolerance']),
            title='Edit CameraRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CameraRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

