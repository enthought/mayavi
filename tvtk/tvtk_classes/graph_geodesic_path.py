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

from tvtk.tvtk_classes.geodesic_path import GeodesicPath


class GraphGeodesicPath(GeodesicPath):
    """
    GraphGeodesicPath - Abstract base for classes that generate a
    geodesic path on a graph (mesh).
    
    Superclass: GeodesicPath
    
    Serves as a base class for algorithms that trace a geodesic on a
    polygonal dataset treating it as a graph. ie points connecting the
    vertices of the graph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphGeodesicPath, obj, update, **traits)
    
    end_vertex = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The vertex at the end of the shortest path
        """
    )
    def _end_vertex_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndVertex,
                        self.end_vertex)

    start_vertex = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The vertex at the start of the shortest path
        """
    )
    def _start_vertex_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartVertex,
                        self.start_vertex)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('end_vertex', 'GetEndVertex'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('start_vertex', 'GetStartVertex'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'end_vertex', 'progress_text', 'start_vertex'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphGeodesicPath, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['end_vertex', 'start_vertex']),
            title='Edit GraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

