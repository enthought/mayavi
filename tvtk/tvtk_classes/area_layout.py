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

from tvtk.tvtk_classes.tree_algorithm import TreeAlgorithm


class AreaLayout(TreeAlgorithm):
    """
    AreaLayout - layout a Tree into a tree map
    
    Superclass: TreeAlgorithm
    
    AreaLayout assigns sector regions to each vertex in the tree,
    creating a tree ring.  The data is added as a data array with four
    components per tuple representing the location and size of the sector
    using the format (_start_angle, end_angle, inner_radius, outer_radius).
    
    This algorithm relies on a helper class to perform the actual layout.
    This helper class is a subclass of AreaLayoutStrategy.
    
    Thanks:
    
    Thanks to Jason Shepherd from Sandia National Laboratories for help
    developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAreaLayout, obj, update, **traits)
    
    edge_routing_points = tvtk_base.true_bool_trait(help=\
        """
        Whether to output a second output tree with vertex locations
        appropriate for routing bundled edges. Default is on.
        """
    )
    def _edge_routing_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeRoutingPoints,
                        self.edge_routing_points_)

    def _get_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetLayoutStrategy())
    def _set_layout_strategy(self, arg):
        old_val = self._get_layout_strategy()
        self._wrap_call(self._vtk_obj.SetLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('layout_strategy', old_val, arg)
    layout_strategy = traits.Property(_get_layout_strategy, _set_layout_strategy, help=\
        """
        The strategy to use when laying out the tree map.
        """
    )

    area_array_name = traits.String(r"area", enter_set=True, auto_set=False, help=\
        """
        The name for the array created for the area for each vertex. The
        rectangles are stored in a quadruple float array (start_angle,
        end_angle, inner_radius, outer_radius). For rectangular layouts,
        this is (minx, maxx, miny, maxy).
        """
    )
    def _area_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaArrayName,
                        self.area_array_name)

    def find_vertex(self, *args):
        """
        V.find_vertex([float, float]) -> int
        C++: IdType FindVertex(float pnt[2])
        Get the vertex whose area contains the point, or return -1 if no
        vertex area covers the point.
        """
        ret = self._wrap_call(self._vtk_obj.FindVertex, *args)
        return ret

    def set_size_array_name(self, *args):
        """
        V.set_size_array_name(string)
        C++: virtual void SetSizeArrayName(const char *name)
        The array name to use for retrieving the relative size of each
        vertex. If this array is not found, use constant size for each
        vertex.
        """
        ret = self._wrap_call(self._vtk_obj.SetSizeArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_routing_points', 'GetEdgeRoutingPoints'), ('area_array_name',
    'GetAreaArrayName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'edge_routing_points',
    'global_warning_display', 'release_data_flag', 'area_array_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AreaLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AreaLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['edge_routing_points'], [], ['area_array_name']),
            title='Edit AreaLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AreaLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

