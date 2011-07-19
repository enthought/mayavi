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

from tvtk.tvtk_classes.tree_map_layout_strategy import TreeMapLayoutStrategy


class SquarifyLayoutStrategy(TreeMapLayoutStrategy):
    """
    SquarifyLayoutStrategy - uses the squarify tree map layout
    algorithm
    
    Superclass: TreeMapLayoutStrategy
    
    SquarifyLayoutStrategy partitions the space for child vertices
    into regions that use all avaliable space and are as close to squares
    as possible. The algorithm also takes into account the relative
    vertex size.
    
    Thanks:
    
    The squarified tree map algorithm comes from: Bruls, D.M., C.
    Huizing, J.J. van Wijk. Squarified Treemaps. In: W. de Leeuw, R. van
    Liere (eds.), Data Visualization 2000, Proceedings of the joint
    Eurographics and IEEE TCVG Symposium on Visualization, 2000,
    Springer, Vienna, p. 33-42.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSquarifyLayoutStrategy, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('shrink_percentage', 'GetShrinkPercentage'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SquarifyLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SquarifyLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['shrink_percentage']),
            title='Edit SquarifyLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SquarifyLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

