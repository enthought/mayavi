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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class DataObjectToDataSetFilter(DataSetAlgorithm):
    """
    DataObjectToDataSetFilter - map field data to concrete dataset
    
    Superclass: DataSetAlgorithm
    
    DataObjectToDataSetFilter is an class that maps a data object
    (i.e., a field) into a concrete dataset, i.e., gives structure to the
    field by defining a geometry and topology.
    
    To use this filter you associate components in the input field data
    with portions of the output dataset. (A component is an array of
    values from the field.) For example, you would specify x-y-z points
    by assigning components from the field for the x, then y, then z
    values of the points. You may also have to specify component ranges
    (for each z-y-z) to make sure that the number of x, y, and z values
    is the same. Also, you may want to normalize the components which
    helps distribute the data uniformly. Once you've setup the filter to
    combine all the pieces of data into a specified dataset (the
    geometry, topology, point and cell data attributes), the various
    output methods (e.g., get_poly_data()) are used to retrieve the final
    product.
    
    This filter is often used in conjunction with
    FieldDataToAttributeDataFilter.  FieldDataToAttributeDataFilter
    takes field data and transforms it into attribute data (e.g., point
    and cell data attributes such as scalars and vectors).  To do this,
    use this filter which constructs a concrete dataset and passes the
    input data object field data to its output. and then use
    FieldDataToAttributeDataFilter to generate the attribute data
    associated with the dataset.
    
    Caveats:
    
    Make sure that the data you extract is consistent. That is, if you
    have N points, extract N x, y, and z components. Also, all the
    information necessary to define a dataset must be given. For example,
    PolyData requires points at a minimum; StructuredPoints
    requires setting the dimensions; StructuredGrid requires defining
    points and dimensions; UnstructuredGrid requires setting points;
    and RectilinearGrid requires that you define the x, y, and
    z-coordinate arrays (by specifying points) as well as the dimensions.
    
    If you wish to create a dataset of just points (i.e., unstructured
    points dataset), create PolyData consisting of points. There will
    be no cells in such a dataset.
    
    See Also:
    
    DataObject FieldData DataSet PolyData StructuredPoints
    StructuredGrid UnstructuredGrid RectilinearGrid
    DataSetAttributes DataArray
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectToDataSetFilter, obj, update, **traits)
    
    default_normalize = tvtk_base.false_bool_trait(help=\
        """
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., set_point_component).
        """
    )
    def _default_normalize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormalize,
                        self.default_normalize_)

    data_set_type = traits.Trait('poly_data',
    tvtk_base.TraitRevPrefixMap({'poly_data': 0, 'structured_points': 1, 'rectilinear_grid': 3, 'unstructured_grid': 4, 'structured_grid': 2}), help=\
        """
        Control what type of data is generated for output.
        """
    )
    def _data_set_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSetType,
                        self.data_set_type_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get the input to the filter.
        """
        ret = wrap_vtk(self._vtk_obj.GetInput())
        return ret
        

    def set_input(self, *args):
        """
        V.set_input(DataObject)
        C++: void SetInput(DataObject *)
        V.set_input(int, DataObject)
        C++: void SetInput(int, DataObject *)
        V.set_input(DataSet)
        C++: void SetInput(DataSet *)
        V.set_input(int, DataSet)
        C++: void SetInput(int, DataSet *)
        Set an input of this algorithm. You should not override these
        methods because they are not the only way to connect a pipeline.
        Note that these methods support old-style pipeline connections.
        When writing new code you should use the more general
        Algorithm::SetInputConnection().  These methods transform the
        input index to the input port index, not an index of a connection
        within a single port.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    spacing = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    dimensions = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    def _get_cell_connectivity_component_array_component(self):
        return self._vtk_obj.GetCellConnectivityComponentArrayComponent()
    cell_connectivity_component_array_component = traits.Property(_get_cell_connectivity_component_array_component, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_connectivity_component_array_name(self):
        return self._vtk_obj.GetCellConnectivityComponentArrayName()
    cell_connectivity_component_array_name = traits.Property(_get_cell_connectivity_component_array_name, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_connectivity_component_max_range(self):
        return self._vtk_obj.GetCellConnectivityComponentMaxRange()
    cell_connectivity_component_max_range = traits.Property(_get_cell_connectivity_component_max_range, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_connectivity_component_min_range(self):
        return self._vtk_obj.GetCellConnectivityComponentMinRange()
    cell_connectivity_component_min_range = traits.Property(_get_cell_connectivity_component_min_range, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_type_component_array_component(self):
        return self._vtk_obj.GetCellTypeComponentArrayComponent()
    cell_type_component_array_component = traits.Property(_get_cell_type_component_array_component, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_type_component_array_name(self):
        return self._vtk_obj.GetCellTypeComponentArrayName()
    cell_type_component_array_name = traits.Property(_get_cell_type_component_array_name, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_type_component_max_range(self):
        return self._vtk_obj.GetCellTypeComponentMaxRange()
    cell_type_component_max_range = traits.Property(_get_cell_type_component_max_range, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_cell_type_component_min_range(self):
        return self._vtk_obj.GetCellTypeComponentMinRange()
    cell_type_component_min_range = traits.Property(_get_cell_type_component_min_range, help=\
        """
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_lines_component_array_component(self):
        return self._vtk_obj.GetLinesComponentArrayComponent()
    lines_component_array_component = traits.Property(_get_lines_component_array_component, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_lines_component_array_name(self):
        return self._vtk_obj.GetLinesComponentArrayName()
    lines_component_array_name = traits.Property(_get_lines_component_array_name, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_lines_component_max_range(self):
        return self._vtk_obj.GetLinesComponentMaxRange()
    lines_component_max_range = traits.Property(_get_lines_component_max_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_lines_component_min_range(self):
        return self._vtk_obj.GetLinesComponentMinRange()
    lines_component_min_range = traits.Property(_get_lines_component_min_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def get_point_component_array_component(self, *args):
        """
        V.get_point_component_array_component(int) -> int
        C++: int GetPointComponentArrayComponent(int comp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponentArrayComponent, *args)
        return ret

    def get_point_component_array_name(self, *args):
        """
        V.get_point_component_array_name(int) -> string
        C++: const char *GetPointComponentArrayName(int comp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponentArrayName, *args)
        return ret

    def get_point_component_max_range(self, *args):
        """
        V.get_point_component_max_range(int) -> int
        C++: int GetPointComponentMaxRange(int comp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponentMaxRange, *args)
        return ret

    def get_point_component_min_range(self, *args):
        """
        V.get_point_component_min_range(int) -> int
        C++: int GetPointComponentMinRange(int comp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponentMinRange, *args)
        return ret

    def get_point_component_normailze_flag(self, *args):
        """
        V.get_point_component_normailze_flag(int) -> int
        C++: int GetPointComponentNormailzeFlag(int comp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponentNormailzeFlag, *args)
        return ret

    def _get_polys_component_array_component(self):
        return self._vtk_obj.GetPolysComponentArrayComponent()
    polys_component_array_component = traits.Property(_get_polys_component_array_component, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_polys_component_array_name(self):
        return self._vtk_obj.GetPolysComponentArrayName()
    polys_component_array_name = traits.Property(_get_polys_component_array_name, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_polys_component_max_range(self):
        return self._vtk_obj.GetPolysComponentMaxRange()
    polys_component_max_range = traits.Property(_get_polys_component_max_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_polys_component_min_range(self):
        return self._vtk_obj.GetPolysComponentMinRange()
    polys_component_min_range = traits.Property(_get_polys_component_min_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_strips_component_array_component(self):
        return self._vtk_obj.GetStripsComponentArrayComponent()
    strips_component_array_component = traits.Property(_get_strips_component_array_component, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_strips_component_array_name(self):
        return self._vtk_obj.GetStripsComponentArrayName()
    strips_component_array_name = traits.Property(_get_strips_component_array_name, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_strips_component_max_range(self):
        return self._vtk_obj.GetStripsComponentMaxRange()
    strips_component_max_range = traits.Property(_get_strips_component_max_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_strips_component_min_range(self):
        return self._vtk_obj.GetStripsComponentMinRange()
    strips_component_min_range = traits.Property(_get_strips_component_min_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_verts_component_array_component(self):
        return self._vtk_obj.GetVertsComponentArrayComponent()
    verts_component_array_component = traits.Property(_get_verts_component_array_component, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_verts_component_array_name(self):
        return self._vtk_obj.GetVertsComponentArrayName()
    verts_component_array_name = traits.Property(_get_verts_component_array_name, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_verts_component_max_range(self):
        return self._vtk_obj.GetVertsComponentMaxRange()
    verts_component_max_range = traits.Property(_get_verts_component_max_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def _get_verts_component_min_range(self):
        return self._vtk_obj.GetVertsComponentMinRange()
    verts_component_min_range = traits.Property(_get_verts_component_min_range, help=\
        """
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
    )

    def set_cell_connectivity_component(self, *args):
        """
        V.set_cell_connectivity_component(string, int, int, int)
        C++: void SetCellConnectivityComponent(char *arrayName,
            int arrayComp, int min, int max)
        V.set_cell_connectivity_component(string, int)
        C++: void SetCellConnectivityComponent(char *arrayName,
            int arrayComp)
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetCellConnectivityComponent, *args)
        return ret

    def set_cell_type_component(self, *args):
        """
        V.set_cell_type_component(string, int, int, int)
        C++: void SetCellTypeComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_cell_type_component(string, int)
        C++: void SetCellTypeComponent(char *arrayName, int arrayComp)
        Define cell types and cell connectivity when creating
        unstructured grid data.  These methods are similar to those for
        defining points, except that no normalization of the data is
        possible. Basically, you need to define an array of cell types
        (an integer value per cell), and another array consisting (for
        each cell) of a number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetCellTypeComponent, *args)
        return ret

    def set_dimensions_component(self, *args):
        """
        V.set_dimensions_component(string, int, int, int)
        C++: void SetDimensionsComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_dimensions_component(string, int)
        C++: void SetDimensionsComponent(char *arrayName, int arrayComp)"""
        ret = self._wrap_call(self._vtk_obj.SetDimensionsComponent, *args)
        return ret

    def set_lines_component(self, *args):
        """
        V.set_lines_component(string, int, int, int)
        C++: void SetLinesComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_lines_component(string, int)
        C++: void SetLinesComponent(char *arrayName, int arrayComp)
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetLinesComponent, *args)
        return ret

    def set_origin_component(self, *args):
        """
        V.set_origin_component(string, int, int, int)
        C++: void SetOriginComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_origin_component(string, int)
        C++: void SetOriginComponent(char *arrayName, int arrayComp)"""
        ret = self._wrap_call(self._vtk_obj.SetOriginComponent, *args)
        return ret

    def set_point_component(self, *args):
        """
        V.set_point_component(int, string, int, int, int, int)
        C++: void SetPointComponent(int comp, char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_point_component(int, string, int)
        C++: void SetPointComponent(int comp, char *arrayName,
            int arrayComp)
        Define the component of the field to be used for the x, y, and z
        values of the points. Note that the parameter comp must lie
        between (0,2) and refers to the x-y-z (i.e., 0,1,2) components of
        the points. To define the field component to use you can specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract. (This method should be used for PolyData,
        UnstructuredGrid, StructuredGrid, and RectilinearGrid.)
        A convenience method, set_point_component(),is also provided which
        does not require setting the (min,max) component range or the
        normalize flag (normalize is set to defaulat_normalize value).
        """
        ret = self._wrap_call(self._vtk_obj.SetPointComponent, *args)
        return ret

    def set_polys_component(self, *args):
        """
        V.set_polys_component(string, int, int, int)
        C++: void SetPolysComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_polys_component(string, int)
        C++: void SetPolysComponent(char *arrayName, int arrayComp)
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetPolysComponent, *args)
        return ret

    def set_spacing_component(self, *args):
        """
        V.set_spacing_component(string, int, int, int)
        C++: void SetSpacingComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_spacing_component(string, int)
        C++: void SetSpacingComponent(char *arrayName, int arrayComp)"""
        ret = self._wrap_call(self._vtk_obj.SetSpacingComponent, *args)
        return ret

    def set_strips_component(self, *args):
        """
        V.set_strips_component(string, int, int, int)
        C++: void SetStripsComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_strips_component(string, int)
        C++: void SetStripsComponent(char *arrayName, int arrayComp)
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetStripsComponent, *args)
        return ret

    def set_verts_component(self, *args):
        """
        V.set_verts_component(string, int, int, int)
        C++: void SetVertsComponent(char *arrayName, int arrayComp,
            int min, int max)
        V.set_verts_component(string, int)
        C++: void SetVertsComponent(char *arrayName, int arrayComp)
        Define cell connectivity when creating PolyData. You can
        define vertices, lines, polygons, and/or triangle strips via
        these methods. These methods are similar to those for defining
        points, except that no normalization of the data is possible.
        Basically, you need to define an array of values that (for each
        cell) includes the number of points per cell, and then the cell
        connectivity. (This is the vtk file format described in in the
        textbook or User's Guide.)
        """
        ret = self._wrap_call(self._vtk_obj.SetVertsComponent, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('dimensions', 'GetDimensions'),
    ('progress_text', 'GetProgressText'), ('spacing', 'GetSpacing'),
    ('default_normalize', 'GetDefaultNormalize'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('data_set_type', 'GetDataSetType'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'default_normalize',
    'global_warning_display', 'release_data_flag', 'data_set_type',
    'dimensions', 'origin', 'progress_text', 'spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectToDataSetFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['default_normalize'], ['data_set_type'],
            ['dimensions', 'origin', 'spacing']),
            title='Edit DataObjectToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectToDataSetFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

