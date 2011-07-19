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

from tvtk.tvtk_classes.interactor_observer import InteractorObserver


class XYPlotWidget(InteractorObserver):
    """
    XYPlotWidget - 2d widget for manipulating a XY plot
    
    Superclass: InteractorObserver
    
    This class provides support for interactively manipulating the
    position, size, and orientation of a XY Plot. It listens to Left
    mouse events and mouse movement. It will change the cursor shape
    based on its location. If the cursor is over an edge of thea XY plot
    it will change the cursor shape to a resize edge shape. If the
    position of a XY plot is moved to be close to the center of one of
    the four edges of the viewport, then the XY plot will change its
    orientation to align with that edge. This orientation is sticky in
    that it will stay that orientation until the position is moved close
    to another edge.
    
    See Also:
    
    InteractorObserver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXYPlotWidget, obj, update, **traits)
    
    def _get_xy_plot_actor(self):
        return wrap_vtk(self._vtk_obj.GetXYPlotActor())
    def _set_xy_plot_actor(self, arg):
        old_val = self._get_xy_plot_actor()
        self._wrap_call(self._vtk_obj.SetXYPlotActor,
                        deref_vtk(arg))
        self.trait_property_changed('xy_plot_actor', old_val, arg)
    xy_plot_actor = traits.Property(_get_xy_plot_actor, _set_xy_plot_actor, help=\
        """
        Get the XY plot used by this Widget. One is created
        automatically.
        """
    )

    _updateable_traits_ = \
    (('priority', 'GetPriority'), ('debug', 'GetDebug'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XYPlotWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XYPlotWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit XYPlotWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XYPlotWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

