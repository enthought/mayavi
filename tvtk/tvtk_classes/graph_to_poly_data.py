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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class GraphToPolyData(PolyDataAlgorithm):
    """
    GraphToPolyData - convert a Graph to PolyData
    
    Superclass: PolyDataAlgorithm
    
    Converts a Graph to a PolyData.  This assumes that the points
    of the graph have already been filled (perhaps by GraphLayout),
    and coverts all the edge of the graph into lines in the polydata. The
    vertex data is passed along to the point data, and the edge data is
    passed along to the cell data.
    
    Only the owned graph edges (i.e. edges with ghost level 0) are copied
    into the PolyData.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphToPolyData, obj, update, **traits)
    
    edge_glyph_output = tvtk_base.false_bool_trait(help=\
        """
        Create a second output containing points and orientation vectors
        for drawing arrows or other glyphs on edges.  This output should
        be set as the first input to Glyph3D to place glyphs on the
        edges. GlyphSource2D's VTK_EDGEARROW_GLYPH provides a good
        glyph for drawing arrows. Default value is off.
        """
    )
    def _edge_glyph_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeGlyphOutput,
                        self.edge_glyph_output_)

    edge_glyph_position = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The position of the glyph point along the edge. 0 puts a glyph
        point at the source of each edge. 1 puts a glyph point at the
        target of each edge. An intermediate value will place the glyph
        point between the source and target. The default value is 1.
        """
    )
    def _edge_glyph_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeGlyphPosition,
                        self.edge_glyph_position)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_glyph_output', 'GetEdgeGlyphOutput'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('progress', 'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('edge_glyph_position', 'GetEdgeGlyphPosition'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'edge_glyph_output',
    'global_warning_display', 'release_data_flag', 'edge_glyph_position',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphToPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['edge_glyph_output'], [], ['edge_glyph_position']),
            title='Edit GraphToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

