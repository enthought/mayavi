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

from tvtk.tvtk_classes.plot import Plot


class ControlPointsItem(Plot):
    """
    ControlPointsItem - Abstract class for control points items.
    
    Superclass: Plot
    
    ControlPointsItem provides control point painting and management
    for subclasses that provide points (typically control points of a
    transfer function)
    
    See Also:
    
    ScalarsToColorsItem PiecewiseControlPointsItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkControlPointsItem, obj, update, **traits)
    
    def deselect_all_points(self):
        """
        V.deselect_all_points()
        C++: void DeselectAllPoints()
        Unselect all the previously selected points
        """
        ret = self._vtk_obj.DeselectAllPoints()
        return ret
        

    def deselect_point(self, *args):
        """
        V.deselect_point(int)
        C++: void DeselectPoint(IdType pointId)
        Unselect a point by its ID
        """
        ret = self._wrap_call(self._vtk_obj.DeselectPoint, *args)
        return ret

    def select_point(self, *args):
        """
        V.select_point(int)
        C++: void SelectPoint(IdType pointId)
        Select a point by its ID
        """
        ret = self._wrap_call(self._vtk_obj.SelectPoint, *args)
        return ret

    def toggle_select_point(self, *args):
        """
        V.toggle_select_point(int)
        C++: void ToggleSelectPoint(IdType pointId)
        Toggle the selection of a point by its ID. If the point was
        selected then unselect it, otherwise select it.
        """
        ret = self._wrap_call(self._vtk_obj.ToggleSelectPoint, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('width', 'GetWidth'), ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'label', 'opacity',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ControlPointsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'opacity', 'use_index_for_x_series',
            'visible', 'width']),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

