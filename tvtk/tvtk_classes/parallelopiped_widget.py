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


class ParallelopipedWidget(AbstractWidget):
    """
    ParallelopipedWidget - a widget to manipulate 3d parallelopipeds
    
    Superclass: AbstractWidget
    
    This widget was designed with the aim of visualizing / probing cuts
    on a skewed image data / structured grid.
    
    Interaction:
    
    The widget allows you to create a parallelopiped (defined by 8
    handles). The widget is initially placed by using the "_place_widget"
    method in the representation class. After the widget has been
    created, the following interactions may be used to manipulate it :
    1) Click on a handle and drag it around moves the handle in space,
       while keeping the same axis alignment of the parallelopiped
    2) Dragging a handle with the shift button pressed resizes the piped
       along an axis.
    3) Control-click on a handle creates a chair at that position. (A
       chair is a depression in the piped that allows you to visualize
       cuts in the volume).
    4) Clicking on a chair and dragging it around moves the chair within
       the piped.
    5) Shift-click on the piped enables you to translate it.
    
    Caveats:
    
    See Also:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelopipedWidget, obj, update, **traits)
    
    enable_chair_creation = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the creation of a chair on this widget. If off,
        chairs cannot be created.
        """
    )
    def _enable_chair_creation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableChairCreation,
                        self.enable_chair_creation_)

    def set_representation(self, *args):
        """
        V.set_representation(ParallelopipedRepresentation)
        C++: void SetRepresentation(ParallelopipedRepresentation *r)
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
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('enable_chair_creation', 'GetEnableChairCreation'), ('enabled',
    'GetEnabled'), ('manages_cursor', 'GetManagesCursor'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('key_press_activation',
    'GetKeyPressActivation'), ('process_events', 'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enable_chair_creation', 'enabled',
    'global_warning_display', 'key_press_activation', 'manages_cursor',
    'process_events', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelopipedWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelopipedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enable_chair_creation', 'enabled',
            'key_press_activation', 'manages_cursor', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit ParallelopipedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelopipedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

