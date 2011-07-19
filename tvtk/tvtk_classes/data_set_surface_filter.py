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


class DataSetSurfaceFilter(PolyDataAlgorithm):
    """
    DataSetSurfaceFilter - Extracts outer (polygonal) surface.
    
    Superclass: PolyDataAlgorithm
    
    DataSetSurfaceFilter is a faster version of Geometry filter,
    but it does not have an option to select bounds.  It may use more
    memory than GeometryFilter.  It only has one option: whether to
    use triangle strips when the input type is structured.
    
    See Also:
    
    GeometryFilter StructuredGridGeometryFilter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetSurfaceFilter, obj, update, **traits)
    
    use_strips = tvtk_base.false_bool_trait(help=\
        """
        When input is structured data, this flag will generate faces with
        triangle strips.  This should render faster and use less memory,
        but no cell data is copied.  By default, use_strips is Off.
        """
    )
    def _use_strips_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseStrips,
                        self.use_strips_)

    pass_through_cell_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for cell picking. The default is
        off to conserve memory. Note that pass_through_cell_ids will be
        ignored if use_strips is on, since in that case each tringle strip
        can represent more than on of the input cells.
        """
    )
    def _pass_through_cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughCellIds,
                        self.pass_through_cell_ids_)

    pass_through_point_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for cell picking. The default is
        off to conserve memory. Note that pass_through_cell_ids will be
        ignored if use_strips is on, since in that case each tringle strip
        can represent more than on of the input cells.
        """
    )
    def _pass_through_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughPointIds,
                        self.pass_through_point_ids_)

    original_point_ids_name = traits.String(r"vtkOriginalPointIds", enter_set=True, auto_set=False, help=\
        """
        If pass_through_cell_ids or pass_through_point_ids is on, then these
        ivars control the name given to the field in which the ids are
        written into.  If set to NULL, then OriginalCellIds or
        OriginalPointIds (the default) is used, respectively.
        """
    )
    def _original_point_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginalPointIdsName,
                        self.original_point_ids_name)

    nonlinear_subdivision_level = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        If the input is an unstructured grid with nonlinear faces, this
        parameter determines how many times the face is subdivided into
        linear faces.  If 0, the output is the equivalent of its linear
        couterpart (and the midpoints determining the nonlinear
        interpolation are discarded).  If 1 (the default), the nonlinear
        face is triangulated based on the midpoints.  If greater than 1,
        the triangulated pieces are recursively subdivided to reach the
        desired subdivision.  Setting the value to greater than 1 may
        cause some point data to not be passed even if no nonlinear faces
        exist.  This option has no effect if the input is not an
        unstructured grid.
        """
    )
    def _nonlinear_subdivision_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonlinearSubdivisionLevel,
                        self.nonlinear_subdivision_level)

    piece_invariant = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If piece_invariant is true, DataSetSurfaceFilter requests 1
        ghost level from input in order to remove internal surface that
        are between processes. False by default.
        """
    )
    def _piece_invariant_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPieceInvariant,
                        self.piece_invariant)

    original_cell_ids_name = traits.String(r"vtkOriginalCellIds", enter_set=True, auto_set=False, help=\
        """
        If pass_through_cell_ids or pass_through_point_ids is on, then these
        ivars control the name given to the field in which the ids are
        written into.  If set to NULL, then OriginalCellIds or
        OriginalPointIds (the default) is used, respectively.
        """
    )
    def _original_cell_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginalCellIdsName,
                        self.original_cell_ids_name)

    def data_set_execute(self, *args):
        """
        V.data_set_execute(DataSet, PolyData) -> int
        C++: virtual int DataSetExecute(DataSet *input,
            PolyData *output)
        Direct access methods that can be used to use the this class as
        an algorithm without using it as a filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DataSetExecute, *my_args)
        return ret

    def unstructured_grid_execute(self, *args):
        """
        V.unstructured_grid_execute(DataSet, PolyData) -> int
        C++: virtual int UnstructuredGridExecute(DataSet *input,
            PolyData *output)
        Direct access methods that can be used to use the this class as
        an algorithm without using it as a filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnstructuredGridExecute, *my_args)
        return ret

    _updateable_traits_ = \
    (('original_cell_ids_name', 'GetOriginalCellIdsName'), ('use_strips',
    'GetUseStrips'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('piece_invariant', 'GetPieceInvariant'),
    ('progress_text', 'GetProgressText'), ('pass_through_point_ids',
    'GetPassThroughPointIds'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('nonlinear_subdivision_level',
    'GetNonlinearSubdivisionLevel'), ('original_point_ids_name',
    'GetOriginalPointIdsName'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('pass_through_cell_ids',
    'GetPassThroughCellIds'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_through_cell_ids', 'pass_through_point_ids',
    'release_data_flag', 'use_strips', 'nonlinear_subdivision_level',
    'original_cell_ids_name', 'original_point_ids_name',
    'piece_invariant', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetSurfaceFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_through_cell_ids', 'pass_through_point_ids',
            'use_strips'], [], ['nonlinear_subdivision_level',
            'original_cell_ids_name', 'original_point_ids_name',
            'piece_invariant']),
            title='Edit DataSetSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

