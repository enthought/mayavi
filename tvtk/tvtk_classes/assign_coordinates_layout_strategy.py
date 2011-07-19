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

from tvtk.tvtk_classes.graph_layout_strategy import GraphLayoutStrategy


class AssignCoordinatesLayoutStrategy(GraphLayoutStrategy):
    """
    AssignCoordinatesLayoutStrategy - uses array values to set vertex
    locations
    
    Superclass: GraphLayoutStrategy
    
    Uses AssignCoordinates to use values from arrays as the x, y, and
    z coordinates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssignCoordinatesLayoutStrategy, obj, update, **traits)
    
    x_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for the x coordinate values.
        """
    )
    def _x_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXCoordArrayName,
                        self.x_coord_array_name)

    y_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for the y coordinate values.
        """
    )
    def _y_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYCoordArrayName,
                        self.y_coord_array_name)

    z_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for the z coordinate values.
        """
    )
    def _z_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCoordArrayName,
                        self.z_coord_array_name)

    _updateable_traits_ = \
    (('x_coord_array_name', 'GetXCoordArrayName'), ('debug', 'GetDebug'),
    ('z_coord_array_name', 'GetZCoordArrayName'), ('y_coord_array_name',
    'GetYCoordArrayName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_weight_field',
    'GetEdgeWeightField'), ('reference_count', 'GetReferenceCount'),
    ('weight_edges', 'GetWeightEdges'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'edge_weight_field',
    'weight_edges', 'x_coord_array_name', 'y_coord_array_name',
    'z_coord_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AssignCoordinatesLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AssignCoordinatesLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['edge_weight_field', 'weight_edges',
            'x_coord_array_name', 'y_coord_array_name', 'z_coord_array_name']),
            title='Edit AssignCoordinatesLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AssignCoordinatesLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

