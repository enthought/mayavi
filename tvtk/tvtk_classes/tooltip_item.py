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

from tvtk.tvtk_classes.context_item import ContextItem


class TooltipItem(ContextItem):
    """
    TooltipItem - takes care of drawing 2d axes
    
    Superclass: ContextItem
    
    The TooltipItem is drawn in screen coordinates. It is used to
    display a tooltip on a scene, giving additional information about an
    element on the scene, such as in ChartXY. It takes care of
    ensuring that it draws itself within the bounds of the screen.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTooltipItem, obj, update, **traits)
    
    position = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    text = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Get/set the text of the item.
        """
    )
    def _text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetText,
                        self.text)

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    brush = traits.Property(_get_brush, help=\
        """
        Get a pointer to the Pen object.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get a pointer to the TextProperty object that controls the way
        the text is rendered.
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('visible', 'GetVisible'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('text',
    'GetText'), ('reference_count', 'GetReferenceCount'), ('position',
    'GetPosition'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'opacity', 'position', 'text',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TooltipItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TooltipItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['opacity', 'position', 'text', 'visible']),
            title='Edit TooltipItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TooltipItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

