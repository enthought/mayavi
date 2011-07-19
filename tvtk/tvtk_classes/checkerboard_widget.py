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

from tvtk.tvtk_classes.abstract_widget import AbstractWidget


class CheckerboardWidget(AbstractWidget):
    """
    CheckerboardWidget - interactively set the number of divisions in
    2d image checkerboard
    
    Superclass: AbstractWidget
    
    The CheckerboardWidget is used to interactively control an
    instance of ImageCheckerboard (and an associated ImageActor
    used to display the checkerboard). The user can adjust the number of
    divisions in each of the i-j directions in a 2d image. A frame
    appears around the ImageActor with sliders along each side of the
    frame. The user can interactively adjust the sliders to the desired
    number of checkerboard subdivisions.
    
    To use this widget, specify an instance of ImageCheckerboard and
    an instance of ImageActor. By default, the widget responds to the
    following events:
    
    If the slider bead is selected:
      left_button_press_event - select slider (if on slider)
      left_button_release_event - release slider
      mouse_move_event - move slider If the end caps or slider tube of a
    slider are selected:
      left_button_press_event - jump (or animate) to cap or point on tube; 
    It is possible to change these event bindings. Please refer to the
    documentation for SliderWidget for more information. Advanced
    users may directly access and manipulate the sliders by obtaining the
    instances of SliderWidget composing the Checkerboard widget.
    
    See Also:
    
    ImageCheckerboard ImageActor SliderWidget
    RectilinearWipeWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCheckerboardWidget, obj, update, **traits)
    
    def set_representation(self, *args):
        """
        V.set_representation(CheckerboardRepresentation)
        C++: void SetRepresentation(CheckerboardRepresentation *r)
        Specify an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop so it can be added to the renderer
        independent of the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentation, *my_args)
        return ret

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('enabled',
    'GetEnabled'), ('manages_cursor', 'GetManagesCursor'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('key_press_activation',
    'GetKeyPressActivation'), ('process_events', 'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CheckerboardWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CheckerboardWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority']),
            title='Edit CheckerboardWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CheckerboardWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

