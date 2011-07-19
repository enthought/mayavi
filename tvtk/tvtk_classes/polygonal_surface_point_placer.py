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

from tvtk.tvtk_classes.poly_data_point_placer import PolyDataPointPlacer


class PolygonalSurfacePointPlacer(PolyDataPointPlacer):
    """
    - Place points on the surface of polygonal data.
    
    Superclass: PolyDataPointPlacer
    
    PolygonalSurfacePointPlacer places points on polygonal data and is
    meant to be used in conjunction with
    PolygonalSurfaceContourLineInterpolator.
    
    Usage:
    
    Caveats:
    
    You should have computed cell normals for the input polydata if you
    are specifying a distance offset.
    
    See Also:
    
    PointPlacer PolyDataNormals
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolygonalSurfacePointPlacer, obj, update, **traits)
    
    distance_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Height offset at which points may be placed on the polygonal
        surface. If you specify a non-zero value here, be sure to compute
        cell normals on your input polygonal data (easily done with
        PolyDataNormals).
        """
    )
    def _distance_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceOffset,
                        self.distance_offset)

    def _get_cell_picker(self):
        return wrap_vtk(self._vtk_obj.GetCellPicker())
    cell_picker = traits.Property(_get_cell_picker, help=\
        """
        Get the Prop picker.
        """
    )

    def _get_polys(self):
        return wrap_vtk(self._vtk_obj.GetPolys())
    polys = traits.Property(_get_polys, help=\
        """
        Be sure to add polydata on which you wish to place points to this
        list or they will not be considered for placement.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('distance_offset', 'GetDistanceOffset'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pixel_tolerance', 'GetPixelTolerance'), ('reference_count',
    'GetReferenceCount'), ('world_tolerance', 'GetWorldTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'distance_offset',
    'pixel_tolerance', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolygonalSurfacePointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolygonalSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['distance_offset', 'pixel_tolerance',
            'world_tolerance']),
            title='Edit PolygonalSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolygonalSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

