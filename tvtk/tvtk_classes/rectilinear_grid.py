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

from tvtk.tvtk_classes.data_set import DataSet


class RectilinearGrid(DataSet):
    """
    RectilinearGrid - a dataset that is topologically regular with
    variable spacing in the three coordinate directions
    
    Superclass: DataSet
    
    RectilinearGrid is a data object that is a concrete implementation
    of DataSet. RectilinearGrid represents a geometric structure
    that is topologically regular with variable spacing in the three
    coordinate directions x-y-z.
    
    To define a RectilinearGrid, you must specify the dimensions of
    the data and provide three arrays of values specifying the
    coordinates along the x-y-z axes. The coordinate arrays are specified
    using three DataArray objects (one for x, one for y, one for z).
    
    Caveats:
    
    Make sure that the dimensions of the grid match the number of
    coordinates in the x-y-z directions. If not, unpredictable results
    (including program failure) may result. Also, you must supply
    coordinates in all three directions, even if the dataset topology is
    2d, 1d, or 0d.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectilinearGrid, obj, update, **traits)
    
    def _get_x_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetXCoordinates())
    def _set_x_coordinates(self, arg):
        old_val = self._get_x_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetXCoordinates,
                        my_arg[0])
        self.trait_property_changed('x_coordinates', old_val, arg)
    x_coordinates = traits.Property(_get_x_coordinates, _set_x_coordinates, help=\
        """
        Specify the grid coordinates in the x-direction.
        """
    )

    def _get_y_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetYCoordinates())
    def _set_y_coordinates(self, arg):
        old_val = self._get_y_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetYCoordinates,
                        my_arg[0])
        self.trait_property_changed('y_coordinates', old_val, arg)
    y_coordinates = traits.Property(_get_y_coordinates, _set_y_coordinates, help=\
        """
        Specify the grid coordinates in the y-direction.
        """
    )

    dimensions = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set dimensions of rectilinear grid dataset. This also sets the
        extent.
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

    def _get_z_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetZCoordinates())
    def _set_z_coordinates(self, arg):
        old_val = self._get_z_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetZCoordinates,
                        my_arg[0])
        self.trait_property_changed('z_coordinates', old_val, arg)
    z_coordinates = traits.Property(_get_z_coordinates, _set_z_coordinates, help=\
        """
        Specify the grid coordinates in the z-direction.
        """
    )

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Return the dimensionality of the data.
        """
    )

    def compute_cell_id(self, *args):
        """
        V.compute_cell_id([int, int, int]) -> int
        C++: IdType ComputeCellId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        cell id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellId, *args)
        return ret

    def compute_point_id(self, *args):
        """
        V.compute_point_id([int, int, int]) -> int
        C++: IdType ComputePointId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        point id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointId, *args)
        return ret

    def compute_structured_coordinates(self, *args):
        """
        V.compute_structured_coordinates([float, float, float], [int, int,
            int], [float, float, float]) -> int
        C++: int ComputeStructuredCoordinates(double x[3], int ijk[3],
            double pcoords[3])
        Convenience function computes the structured coordinates for a
        point x[3]. The cell is specified by the array ijk[3], and the
        parametric coordinates in the cell are specified with pcoords[3].
        The function returns a 0 if the point x is outside of the grid,
        and a 1 if inside the grid.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeStructuredCoordinates, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('dimensions', 'GetDimensions'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('update_extent', 'GetUpdateExtent'), ('debug', 'GetDebug'),
    ('extent', 'GetExtent'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'dimensions', 'extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectilinearGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['dimensions', 'extent', 'maximum_number_of_pieces',
            'update_extent', 'update_ghost_level', 'update_number_of_pieces',
            'update_piece', 'whole_bounding_box', 'whole_extent']),
            title='Edit RectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

