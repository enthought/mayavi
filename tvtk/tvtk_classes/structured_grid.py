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

from tvtk.tvtk_classes.point_set import PointSet


class StructuredGrid(PointSet):
    """
    StructuredGrid - topologically regular array of data
    
    Superclass: PointSet
    
    StructuredGrid is a data object that is a concrete implementation
    of DataSet. StructuredGrid represents a geometric structure
    that is a topologically regular array of points. The topology is that
    of a cube that has been subdivided into a regular array of smaller
    cubes. Each point/cell can be addressed with i-j-k indices. Examples
    include finite difference grids.
    
    The order and number of points must match that specified by the
    dimensions of the grid. The point order increases in i fastest (from
    0<=i<dims[0]), then j (0<=j<dims[1]), then k (0<=k<dims[2]) where
    dims[] are the dimensions of the grid in the i-j-k topological
    directions. The number of points is dims[0]*dims[1]*dims[2]. The same
    is true for the cells of the grid. The order and number of cells must
    match that specified by the dimensions of the grid. The cell order
    increases in i fastest (from 0<=i<(dims[0]-1)), then j
    (0<=j<(dims[1]-1)), then k (0<=k<(dims[2]-1)) The number of cells is
    (dims[0]-1)*(dims[1]-1)*(dims[2]-1).
    
    A unusual feature of StructuredGrid is the ability to blank, or
    "turn-off" points and cells in the dataset. This is controlled by
    defining a "blanking array" whose values (0,1) specify whether a
    point should be blanked or not.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGrid, obj, update, **traits)
    
    def _get_point_visibility_array(self):
        return wrap_vtk(self._vtk_obj.GetPointVisibilityArray())
    def _set_point_visibility_array(self, arg):
        old_val = self._get_point_visibility_array()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetPointVisibilityArray,
                        my_arg[0])
        self.trait_property_changed('point_visibility_array', old_val, arg)
    point_visibility_array = traits.Property(_get_point_visibility_array, _set_point_visibility_array, help=\
        """
        Get the array that defines the blanking (visibility) of each
        point.
        """
    )

    def _get_cell_visibility_array(self):
        return wrap_vtk(self._vtk_obj.GetCellVisibilityArray())
    def _set_cell_visibility_array(self, arg):
        old_val = self._get_cell_visibility_array()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetCellVisibilityArray,
                        my_arg[0])
        self.trait_property_changed('cell_visibility_array', old_val, arg)
    cell_visibility_array = traits.Property(_get_cell_visibility_array, _set_cell_visibility_array, help=\
        """
        Get the array that defines the blanking (visibility) of each
        cell.
        """
    )

    dimensions = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        following methods are specific to structured grid
        """
    )
    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored  in the order (X, Y, Z).
        """
    )
    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    def _get_cell_blanking(self):
        return self._vtk_obj.GetCellBlanking()
    cell_blanking = traits.Property(_get_cell_blanking, help=\
        """
        Returns 1 if there is any visibility constraint on the cells, 0
        otherwise.
        """
    )

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Return the dimensionality of the data.
        """
    )

    def _get_point_blanking(self):
        return self._vtk_obj.GetPointBlanking()
    point_blanking = traits.Property(_get_point_blanking, help=\
        """
        Returns 1 if there is any visibility constraint on the points, 0
        otherwise.
        """
    )

    def blank_cell(self, *args):
        """
        V.blank_cell(int)
        C++: void BlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankCell, *args)
        return ret

    def blank_point(self, *args):
        """
        V.blank_point(int)
        C++: void BlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankPoint, *args)
        return ret

    def is_cell_visible(self, *args):
        """
        V.is_cell_visible(int) ->
        C++: unsigned char IsCellVisible(IdType cellId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsCellVisible, *args)
        return ret

    def is_point_visible(self, *args):
        """
        V.is_point_visible(int) ->
        C++: unsigned char IsPointVisible(IdType ptId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointVisible, *args)
        return ret

    def un_blank_cell(self, *args):
        """
        V.un_blank_cell(int)
        C++: void UnBlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankCell, *args)
        return ret

    def un_blank_point(self, *args):
        """
        V.un_blank_point(int)
        C++: void UnBlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankPoint, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('dimensions', 'GetDimensions'), ('whole_extent',
    'GetWholeExtent'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('extent', 'GetExtent'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('request_exact_extent', 'GetRequestExactExtent'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'dimensions', 'extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['dimensions', 'extent', 'maximum_number_of_pieces',
            'update_extent', 'update_ghost_level', 'update_number_of_pieces',
            'update_piece', 'whole_bounding_box', 'whole_extent']),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

