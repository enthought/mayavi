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

from tvtk.tvtk_classes.interactor_style import InteractorStyle


class InteractorStyleUnicam(InteractorStyle):
    """
    InteractorStyleUnicam - provides Unicam navigation style
    
    Superclass: InteractorStyle
    
    uni_cam is a camera interactor.  Here, just the primary features of
    the uni_cam technique are implemented.  uni_cam requires just one mouse
    button and supports context sensitive dollying, panning, and
    rotation.  (In this implementation, it uses the right mouse button,
    leaving the middle and left available for other functions.) For more
    information, see the paper at:
    
    
       ftp://ftp.cs.brown.edu/pub/papers/graphics/research/unicam.pdf
    
    The following is a brief description of the uni_cam Camera Controls. 
    You can perform 3 operations on the camera: rotate, pan, and dolly
    the camera. All operations are reached through the right mouse button
    & mouse movements.
    
    IMPORTANT: uni_cam assumes there is an axis that makes sense as a "up"
    vector for the world.  By default, this axis is defined to be the
    vector <0,0,1>.  You can set it explicitly for the data you are
    viewing with the '_set_world_up_vector(..)' method in C++, or similarly
    in Tcl/Tk (or other interpreted languages).
    
    1. ROTATE:
    
    Position the cursor over the point you wish to rotate around and
    press and release the left mouse button.  A 'focus dot' appears
    indicating the point that will be the center of rotation.  To rotate,
    press and hold the left mouse button and drag the mouse.. release the
    button to complete the rotation.
    
    Rotations can be done without placing a focus dot first by moving the
    mouse cursor to within 10% of the window border & pressing and
    holding the left button followed by dragging the mouse.  The last
    focus dot position will be re-used.
    
    2. PAN:
    
    Click and hold the left mouse button, and initially move the mouse
    left or right.  The point under the initial pick will pick correlate
    w/ the mouse tip-- (i.e., direct manipulation).
    
    3. DOLLY (+ PAN):
    
    Click and hold the left mouse button, and initially move the mouse up
    or down.  Moving the mouse down will dolly towards the picked point,
    and moving the mouse up will dolly away from it.  Dollying occurs
    relative to the picked point which simplifies the task of dollying
    towards a region of interest. Left and right mouse movements will pan
    the camera left and right.
    
    Caveats:
    
    (NOTE: This implementation of Unicam assumes a perspective camera. 
    It could be modified relatively easily to also support an
    orthographic projection.)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleUnicam, obj, update, **traits)
    
    world_up_vector = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _world_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldUpVector,
                        self.world_up_vector)

    def on_left_button_move(self):
        """
        V.on_left_button_move()
        C++: virtual void OnLeftButtonMove()
        Concrete implementation of event bindings
        """
        ret = self._vtk_obj.OnLeftButtonMove()
        return ret
        

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('world_up_vector',
    'GetWorldUpVector'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('pick_color', 'GetPickColor'),
    ('key_press_activation', 'GetKeyPressActivation'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('handle_observers',
    'GetHandleObservers'), ('reference_count', 'GetReferenceCount'),
    ('timer_duration', 'GetTimerDuration'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration', 'world_up_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleUnicam, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleUnicam properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'use_timers'], [],
            ['key_press_activation_value', 'mouse_wheel_motion_factor',
            'pick_color', 'priority', 'timer_duration', 'world_up_vector']),
            title='Edit InteractorStyleUnicam properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleUnicam properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

