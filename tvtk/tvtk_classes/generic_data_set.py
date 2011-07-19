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


class GenericDataSet(DataObject):
    """
    GenericDataSet - defines dataset interface
    
    Superclass: DataObject
    
    In VTK, spatial-temporal data is defined in terms of a dataset. The
    dataset consists of geometry (e.g., points), topology (e.g., cells),
    and attributes (e.g., scalars, vectors, etc.) GenericDataSet is an
    abstract class defining this abstraction.
    
    Since GenericDataSet provides a general interface to manipulate
    data, algorithms that process it tend to be slower than those
    specialized for a particular data type. For this reason, there are
    concrete, non-abstract subclasses that represent and provide access
    to data more efficiently. Note that filters to process this dataset
    type are currently found in the vtk/_generic_filtering/ subdirectory.
    
    Unlike the DataSet class, GenericDataSet provides a more
    flexible interface including support for iterators. GenericDataSet
    is also designed to interface VTK to external simulation packages
    without the penalty of copying memory (see
    vtk/_generic_filtering/_readme.html) for more information. Thus
    GenericDataSet plays a central role in the adaptor framework.
    
    Please note that this class introduces the concepts of "boundary
    cells". This refers to the boundaries of a cell (e.g., face of a
    tetrahedron) which may in turn be represented as a cell. Boundary
    cells are derivative topological features of cells, and are therefore
    never explicitly represented in the dataset. Often in visualization
    algorithms, looping over boundaries (edges or faces) is employed,
    while the actual dataset cells may not traversed. Thus there are
    methods to loop over these boundary cells.
    
    Finally, as a point of clarification, points are not the same as
    vertices. Vertices refer to points, and points specify a position is
    space. Vertices are a type of 0-D cell. Also, the concept of a
    DOFNode, which is where coefficients for higher-order cells are kept,
    is a new concept introduced by the adaptor framework (see
    GenericAdaptorCell for more information).
    
    See Also:
    
    GenericAdaptorCell DataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericDataSet, obj, update, **traits)
    
    def _get_tessellator(self):
        return wrap_vtk(self._vtk_obj.GetTessellator())
    def _set_tessellator(self, arg):
        old_val = self._get_tessellator()
        self._wrap_call(self._vtk_obj.SetTessellator,
                        deref_vtk(arg))
        self.trait_property_changed('tessellator', old_val, arg)
    tessellator = traits.Property(_get_tessellator, _set_tessellator, help=\
        """
        Set/Get a cell tessellator if cells must be tessellated during
        processing.
        \pre tessellator_exists: tessellator!=0
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float, float, float])
        C++: virtual void GetBounds(double bounds[6])
        Return the geometry bounding box in global coordinates in the
        form (xmin,xmax, ymin,ymax, zmin,zmax) in the `bounds' array.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_cell_dimension(self):
        return self._vtk_obj.GetCellDimension()
    cell_dimension = traits.Property(_get_cell_dimension, help=\
        """
        Return -1 if the dataset is explicitly defined by cells of
        varying dimensions or if there are no cells. If the dataset is
        explicitly defined by cells of a unique dimension, return this
        dimension.
        \post valid_range: (result>=-1) && (result<=3)
        """
    )

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
        \pre types_exist: types!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCellTypes, *my_args)
        return ret

    def get_center(self, *args):
        """
        V.get_center([float, float, float])
        C++: virtual void GetCenter(double center[3])
        Get the center of the bounding box in global coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenter, *args)
        return ret

    def _get_estimated_size(self):
        return self._vtk_obj.GetEstimatedSize()
    estimated_size = traits.Property(_get_estimated_size, help=\
        """
        Estimated size needed after tessellation (or special operation)
        """
    )

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Return the length of the diagonal of the bounding box.
        \post positive_result: result>=0
        """
    )

    def get_number_of_cells(self, *args):
        """
        V.get_number_of_cells(int) -> int
        C++: virtual IdType GetNumberOfCells(int dim=-1)
        Return the number of cells that explicitly define the dataset.
        See new_cell_iterator() for more details.
        \pre valid_dim_range: (dim>=-1) && (dim<=3)
        \post positive_result: result>=0
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfCells, *args)
        return ret

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of points composing the dataset. See
        new_point_iterator() for more details.
        \post positive_result: result>=0
        """
    )

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: virtual void ComputeBounds()
        Compute the geometry bounding box.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def find_point(self, *args):
        """
        V.find_point([float, float, float], GenericPointIterator)
        C++: virtual void FindPoint(double x[3],
            GenericPointIterator *p)
        Locate the closest point `p' to position `x' (global
        coordinates).
        \pre not_empty: get_number_of_points()>_0
        \pre p_exists: p!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindPoint, *my_args)
        return ret

    def new_boundary_iterator(self, *args):
        """
        V.new_boundary_iterator(int, int) -> GenericCellIterator
        C++: virtual GenericCellIterator *NewBoundaryIterator(
            int dim=-1, int exteriorOnly=0)
        Return an iterator to traverse cell boundaries of dimension `dim'
        (or all dimensions if -1) of the dataset.  If `exterior_only' is
        true, only the exterior cell boundaries of the dataset will be
        returned, otherwise it will return exterior and interior cell
        boundaries. The user is responsible for deleting the iterator.
        \pre valid_dim_range: (dim>=-1) && (dim<=2)
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.NewBoundaryIterator, *args)
        return wrap_vtk(ret)

    def new_cell_iterator(self, *args):
        """
        V.new_cell_iterator(int) -> GenericCellIterator
        C++: virtual GenericCellIterator *NewCellIterator(int dim=-1)
        Return an iterator to traverse cells of dimension `dim' (or all
        dimensions if -1) that explicitly define the dataset. For
        instance, it will return only tetrahedra if the mesh is defined
        by tetrahedra. If the mesh is composed of two parts, one with
        tetrahedra and another part with triangles, it will return both,
        but will not return the boundary edges and vertices of these
        cells. The user is responsible for deleting the iterator.
        \pre valid_dim_range: (dim>=-1) && (dim<=3)
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.NewCellIterator, *args)
        return wrap_vtk(ret)

    def new_point_iterator(self):
        """
        V.new_point_iterator() -> GenericPointIterator
        C++: virtual GenericPointIterator *NewPointIterator()
        Return an iterator to traverse the points composing the dataset;
        they can be points that define a cell (corner points) or isolated
        points. The user is responsible for deleting the iterator.
        \post result_exists: result!=0
        """
        ret = wrap_vtk(self._vtk_obj.NewPointIterator())
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
            return super(GenericDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit GenericDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

