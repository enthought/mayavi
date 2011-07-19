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

from tvtk.tvtk_classes.spline import Spline


class CardinalSpline(Spline):
    """
    CardinalSpline - computes an interpolating spline using a
    
    Superclass: Spline
    
    CardinalSpline is a concrete implementation of Spline using a
    Cardinal basis.
    
    See Also:
    
    Spline KochanekSpline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCardinalSpline, obj, update, **traits)
    
    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('left_value',
    'GetLeftValue'), ('left_constraint', 'GetLeftConstraint'),
    ('clamp_value', 'GetClampValue'), ('debug', 'GetDebug'),
    ('right_constraint', 'GetRightConstraint'), ('closed', 'GetClosed'),
    ('reference_count', 'GetReferenceCount'), ('right_value',
    'GetRightValue'))
    
    _full_traitnames_list_ = \
    (['clamp_value', 'closed', 'debug', 'global_warning_display',
    'left_constraint', 'left_value', 'right_constraint', 'right_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CardinalSpline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CardinalSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamp_value', 'closed'], [], ['left_constraint',
            'left_value', 'right_constraint', 'right_value']),
            title='Edit CardinalSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CardinalSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

