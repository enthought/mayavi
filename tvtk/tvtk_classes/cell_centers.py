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


class CellCenters(PolyDataAlgorithm):
    """
    CellCenters - generate points at center of cells
    
    Superclass: PolyDataAlgorithm
    
    CellCenters is a filter that takes as input any dataset and
    generates on output points at the center of the cells in the dataset.
    These points can be used for placing glyphs (vtk_glyph3d) or labeling
    (vtk_labeled_data_mapper). (The center is the parametric center of the
    cell, not necessarily the geometric or bounding box center.) The cell
    attributes will be associated with the points on output.
    
    Caveats:
    
    You can choose to generate just points or points and vertex cells.
    Vertex cells are drawn during rendering; points are not. Use the ivar
    vertex_cells to generate cells.
    
    See Also:
    
    Glyph3D LabeledDataMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellCenters, obj, update, **traits)
    
    vertex_cells = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the generation of vertex cells. The default is
        Off.
        """
    )
    def _vertex_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexCells,
                        self.vertex_cells_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('vertex_cells',
    'GetVertexCells'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'vertex_cells', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellCenters, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellCenters properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['vertex_cells'], [], []),
            title='Edit CellCenters properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellCenters properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

