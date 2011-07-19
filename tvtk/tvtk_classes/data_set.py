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

from tvtk.tvtk_classes.data_object import DataObject


class DataSet(DataObject):
    """
    DataSet - abstract class to specify dataset behavior
    
    Superclass: DataObject
    
    DataSet is an abstract class that specifies an interface for
    dataset objects. DataSet also provides methods to provide
    informations about the data, such as center, bounding box, and
    representative length.
    
    In vtk a dataset consists of a structure (geometry and topology) and
    attribute data. The structure is defined implicitly or explicitly as
    a collection of cells. The geometry of the structure is contained in
    point coordinates plus the cell interpolation functions. The topology
    of the dataset structure is defined by cell types and how the cells
    share their defining points.
    
    Attribute data in vtk is either point data (data at points) or cell
    data (data at cells). Typically filters operate on point data, but
    some may operate on cell data, both cell and point data, either one,
    or none.
    
    See Also:
    
    PointSet StructuredPoints StructuredGrid UnstructuredGrid
    RectilinearGrid PolyData PointData CellData DataObject
    FieldData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSet, obj, update, **traits)
    
    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Return a pointer to the geometry bounding box in the form
        (xmin,xmax, ymin,ymax, zmin,zmax). THIS METHOD IS NOT THREAD
        SAFE.
        """
    )

    def get_cell(self, *args):
        """
        V.get_cell(int) -> Cell
        C++: virtual Cell *GetCell(IdType cellId)
        V.get_cell(int, GenericCell)
        C++: virtual void GetCell(IdType cellId, GenericCell *cell)
        Get cell with cell_id such that: 0 <= cell_id < number_of_cells. THIS
        METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCell, *my_args)
        return wrap_vtk(ret)

    def get_cell_bounds(self, *args):
        """
        V.get_cell_bounds(int, [float, float, float, float, float, float])
        C++: virtual void GetCellBounds(IdType cellId,
            double bounds[6])
        Get the bounds of the cell with cell_id such that:
            0 <= cell_id < number_of_cells. A subclass may be able to
        determine the bounds of cell without using an expensive get_cell()
        method. A default implementation is provided that actually uses a
        get_cell() call.  This is to ensure the method is available to all
        datasets.  Subclasses should override this method to provide an
        efficient implementation. THIS METHOD IS THREAD SAFE IF FIRST
        CALLED FROM A SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.GetCellBounds, *args)
        return ret

    def _get_cell_data(self):
        return wrap_vtk(self._vtk_obj.GetCellData())
    cell_data = traits.Property(_get_cell_data, help=\
        """
        Return a pointer to this dataset's cell data. THIS METHOD IS
        THREAD SAFE
        """
    )

    def get_cell_neighbors(self, *args):
        """
        V.get_cell_neighbors(int, IdList, IdList)
        C++: virtual void GetCellNeighbors(IdType cellId,
            IdList *ptIds, IdList *cellIds)
        Topological inquiry to get all cells using list of points
        exclusive of cell specified (e.g., cell_id). Note that the list
        consists of only cells that use ALL the points provided. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellNeighbors, *my_args)
        return ret

    def get_cell_points(self, *args):
        """
        V.get_cell_points(int, IdList)
        C++: virtual void GetCellPoints(IdType cellId,
            IdList *ptIds)
        Topological inquiry to get points defining cell. THIS METHOD IS
        THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND THE DATASET
        IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellPoints, *my_args)
        return ret

    def get_cell_type(self, *args):
        """
        V.get_cell_type(int) -> int
        C++: virtual int GetCellType(IdType cellId)
        Get type of cell with cell_id such that: 0 <= cell_id <
        number_of_cells. THIS METHOD IS THREAD SAFE IF FIRST CALLED FROM A
        SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.GetCellType, *args)
        return ret

    def get_cell_types(self, *args):
        """
        V.get_cell_types(CellTypes)
        C++: virtual void GetCellTypes(CellTypes *types)
        Get a list of types of cells in a dataset. The list consists of
        an array of types (not necessarily in any order), with a single
        entry per type. For example a dataset 5 triangles, 3 lines, and
        100 hexahedra would result a list of three entries, corresponding
        to the types VTK_TRIANGLE, VTK_LINE, and VTK_HEXAHEDRON. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCellTypes, *my_args)
        return ret

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Get the center of the bounding box. THIS METHOD IS NOT THREAD
        SAFE.
        """
    )

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Return the length of the diagonal of the bounding box. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
    )

    def _get_max_cell_size(self):
        return self._vtk_obj.GetMaxCellSize()
    max_cell_size = traits.Property(_get_max_cell_size, help=\
        """
        Convenience method returns largest cell size in dataset. This is
        generally used to allocate memory for supporting data structures.
        THIS METHOD IS THREAD SAFE
        """
    )

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        Determine the number of cells composing the dataset. THIS METHOD
        IS THREAD SAFE
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Determine the number of points composing the dataset. THIS METHOD
        IS THREAD SAFE
        """
    )

    def get_point(self, *args):
        """
        V.get_point(int) -> (float, float, float)
        C++: virtual double *GetPoint(IdType ptId)
        V.get_point(int, [float, float, float])
        C++: virtual void GetPoint(IdType id, double x[3])
        Get point coordinates with pt_id such that: 0 <= pt_id <
        number_of_points. THIS METHOD IS NOT THREAD SAFE.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def get_point_cells(self, *args):
        """
        V.get_point_cells(int, IdList)
        C++: virtual void GetPointCells(IdType ptId,
            IdList *cellIds)
        Topological inquiry to get cells using point. THIS METHOD IS
        THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND THE DATASET
        IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetPointCells, *my_args)
        return ret

    def _get_point_data(self):
        return wrap_vtk(self._vtk_obj.GetPointData())
    point_data = traits.Property(_get_point_data, help=\
        """
        Return a pointer to this dataset's point data. THIS METHOD IS
        THREAD SAFE
        """
    )

    def _get_scalar_range(self):
        return self._vtk_obj.GetScalarRange()
    scalar_range = traits.Property(_get_scalar_range, help=\
        """
        Convenience method to get the range of the scalar data (if there
        is any scalar data). Returns the (min/max) range of combined
        point and cell data. If there are no point or cell scalars the
        method will return (0,1). Note: Update needs to be called to
        create the scalars. THIS METHOD IS THREAD SAFE IF FIRST CALLED
        FROM A SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
    )

    def check_attributes(self):
        """
        V.check_attributes() -> int
        C++: int CheckAttributes()
        This method checks to see if the cell and point attributes match
        the geometry.  Many filters will crash if the number of tupples
        in an array is less than the number of points/cells. This method
        returns 1 if there is a mismatch, and 0 if everything is ok.  It
        prints an error if an array is too short, and a warning if an
        array is too long.
        """
        ret = self._vtk_obj.CheckAttributes()
        return ret
        

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: virtual void ComputeBounds()
        Compute the data bounding box from data points. THIS METHOD IS
        NOT THREAD SAFE.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def copy_attributes(self, *args):
        """
        V.copy_attributes(DataSet)
        C++: virtual void CopyAttributes(DataSet *ds)
        Copy the attributes associated with the specified dataset to this
        instance of DataSet. THIS METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAttributes, *my_args)
        return ret

    def copy_structure(self, *args):
        """
        V.copy_structure(DataSet)
        C++: virtual void CopyStructure(DataSet *ds)
        Copy the geometric and topological structure of an object. Note
        that the invoking object and the object pointed to by the
        parameter ds must be of the same type. THIS METHOD IS NOT THREAD
        SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def find_point(self, *args):
        """
        V.find_point(float, float, float) -> int
        C++: IdType FindPoint(double x, double y, double z)
        V.find_point([float, float, float]) -> int
        C++: virtual IdType FindPoint(double x[3])
        Locate the closest point to the global coordinate x. Return the
        point id. If point id < 0; then no point found. (This may arise
        when point is outside of dataset.) THIS METHOD IS THREAD SAFE IF
        FIRST CALLED FROM A SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.FindPoint, *args)
        return ret

    def generate_ghost_level_array(self):
        """
        V.generate_ghost_level_array()
        C++: virtual void GenerateGhostLevelArray()
        Normally called by pipeline executives or algoritgms only. This
        method computes the ghost arrays for a given dataset.
        """
        ret = self._vtk_obj.GenerateGhostLevelArray()
        return ret
        

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()
        Reclaim any extra memory used to store data. THIS METHOD IS NOT
        THREAD SAFE.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

