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

from tvtk.tvtk_classes.object import Object


class StructuredData(Object):
    """
    StructuredData - abstract class for topologically regular data
    
    Superclass: Object
    
    StructuredData is an abstract class that specifies an interface
    for topologically regular data. Regular data is data that can be
    accessed in rectangular fashion using an i-j-k index. A finite
    difference grid, a volume, or a pixmap are all considered regular.
    
    See Also:
    
    StructuredGrid UniformGrid RectilinearGrid
    RectilinearGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredData, obj, update, **traits)
    
    def get_cell_neighbors(self, *args):
        """
        V.get_cell_neighbors(int, IdList, IdList, [int, int, int])
        C++: static void GetCellNeighbors(IdType cellId,
            IdList *ptIds, IdList *cellIds, int dim[3])
        Get the cells using the points pt_ids, exclusive of the cell
        cell_id. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'vtkIdList', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetCellNeighbors, *my_args)
        return ret

    def get_cell_points(self, *args):
        """
        V.get_cell_points(int, IdList, int, [int, int, int])
        C++: static void GetCellPoints(IdType cellId, IdList *ptIds,
             int dataDescription, int dim[3])
        Get the points defining a cell. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'int', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetCellPoints, *my_args)
        return ret

    def get_data_description(self, *args):
        """
        V.get_data_description([int, int, int]) -> int
        C++: static int GetDataDescription(int dims[3])
        Returns the data description given the dimensions (eg.
        VTK_SINGLE_POINT, VTK_X_LINE, VTK_XY_PLANE etc.)
        """
        ret = self._wrap_call(self._vtk_obj.GetDataDescription, *args)
        return ret

    def get_data_dimension(self, *args):
        """
        V.get_data_dimension(int) -> int
        C++: static int GetDataDimension(int dataDescription)
        Return the topological dimension of the data (e.g., 0, 1, 2, or
        3d).
        """
        ret = self._wrap_call(self._vtk_obj.GetDataDimension, *args)
        return ret

    def get_point_cells(self, *args):
        """
        V.get_point_cells(int, IdList, [int, int, int])
        C++: static void GetPointCells(IdType ptId, IdList *cellIds,
             int dim[3])
        Get the cells using a point. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetPointCells, *my_args)
        return ret

    def compute_cell_id(self, *args):
        """
        V.compute_cell_id([int, int, int], [int, int, int]) -> int
        C++: static IdType ComputeCellId(int dim[3], int ijk[3])
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the cell id.  This
        method does not adjust for the beginning of the extent.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellId, *args)
        return ret

    def compute_cell_id_for_extent(self, *args):
        """
        V.compute_cell_id_for_extent([int, int, int, int, int, int], [int,
            int, int]) -> int
        C++: static IdType ComputeCellIdForExtent(int extent[6],
            int ijk[3])
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellIdForExtent, *args)
        return ret

    def compute_point_id(self, *args):
        """
        V.compute_point_id([int, int, int], [int, int, int]) -> int
        C++: static IdType ComputePointId(int dim[3], int ijk[3])
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the point id.  This
        method does not adjust for the beginning of the extent.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointId, *args)
        return ret

    def compute_point_id_for_extent(self, *args):
        """
        V.compute_point_id_for_extent([int, int, int, int, int, int], [int,
            int, int]) -> int
        C++: static IdType ComputePointIdForExtent(int extent[6],
            int ijk[3])
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointIdForExtent, *args)
        return ret

    def set_dimensions(self, *args):
        """
        V.set_dimensions([int, int, int], [int, int, int]) -> int
        C++: static int SetDimensions(int inDim[3], int dim[3])
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (in_dim) and the current dimensions
        (dim). The function returns the dimension of the dataset (_0-_3d).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
        """
        ret = self._wrap_call(self._vtk_obj.SetDimensions, *args)
        return ret

    def set_extent(self, *args):
        """
        V.set_extent([int, int, int, int, int, int], [int, int, int, int,
            int, int]) -> int
        C++: static int SetExtent(int inExt[6], int ext[6])
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (in_dim) and the current dimensions
        (dim). The function returns the dimension of the dataset (_0-_3d).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
        """
        ret = self._wrap_call(self._vtk_obj.SetExtent, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

