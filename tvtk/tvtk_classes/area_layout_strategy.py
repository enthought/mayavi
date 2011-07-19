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

from tvtk.tvtk_classes.object import Object


class AreaLayoutStrategy(Object):
    """
    AreaLayoutStrategy - abstract superclass for all area layout
    strategies
    
    Superclass: Object
    
    All subclasses of this class perform a area layout on a tree. This
    involves assigning a region to each vertex in the tree, and placing
    that information in a data array with four components per tuple
    representing (inner_radius, outer_radius, start_angle, end_angle).
    
    Instances of subclasses of this class may be assigned as the layout
    strategy to AreaLayout
    
    Thanks:
    
    Thanks to Jason Shepherd from Sandia National Laboratories for help
    developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAreaLayoutStrategy, obj, update, **traits)
    
    shrink_percentage = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _shrink_percentage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkPercentage,
                        self.shrink_percentage)

    def find_vertex(self, *args):
        """
        V.find_vertex(Tree, DataArray, [float, float]) -> int
        C++: virtual IdType FindVertex(Tree *tree,
            DataArray *array, float pnt[2])
        Returns the vertex id that contains pnt (or -1 if no one contains
        it)
        """
        my_args = deref_array(args, [('vtkTree', 'vtkDataArray', ['float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.FindVertex, *my_args)
        return ret

    def layout(self, *args):
        """
        V.layout(Tree, DataArray, DataArray)
        C++: virtual void Layout(Tree *inputTree,
            DataArray *areaArray, DataArray *sizeArray)
        Perform the layout of the input tree, and store the sector bounds
        of each vertex as a tuple in a data array. For radial layout,
        this is (inner_radius, outer_radius, start_angle, end_angle). For
        rectangular layout, this is (xmin, xmax, ymin, ymax).
        
        The size_array may be NULL, or may contain the desired size of
        each vertex in the tree.
        """
        my_args = deref_array(args, [('vtkTree', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.Layout, *my_args)
        return ret

    def layout_edge_points(self, *args):
        """
        V.layout_edge_points(Tree, DataArray, DataArray, Tree)
        C++: virtual void LayoutEdgePoints(Tree *inputTree,
            DataArray *areaArray, DataArray *sizeArray,
            Tree *edgeLayoutTree)"""
        my_args = deref_array(args, [('vtkTree', 'vtkDataArray', 'vtkDataArray', 'vtkTree')])
        ret = self._wrap_call(self._vtk_obj.LayoutEdgePoints, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('shrink_percentage', 'GetShrinkPercentage'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AreaLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AreaLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['shrink_percentage']),
            title='Edit AreaLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AreaLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

