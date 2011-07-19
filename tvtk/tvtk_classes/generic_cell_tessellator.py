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


class GenericCellTessellator(Object):
    """
    GenericCellTessellator - helper class to perform cell tessellation
    
    Superclass: Object
    
    GenericCellTessellator is a helper class to perform adaptive
    tessellation of particular cell topologies. The major purpose for
    this class is to transform higher-order cell types (e.g.,
    higher-order finite elements) into linear cells that can then be
    easily visualized by VTK. This class works in conjunction with the
    GenericDataSet and GenericAdaptorCell classes.
    
    This algorithm is based on edge subdivision. An error metric along
    each edge is evaluated, and if the error is greater than some
    tolerance, the edge is subdivided (as well as all connected 2d and 3d
    cells). The process repeats until the error metric is satisfied.
    
    A significant issue addressed by this algorithm is to insure face
    compatibility across neigboring cells. That is, diagonals due to face
    triangulation must match to insure that the mesh is compatible. The
    algorithm employs a precomputed table to accelerate the tessellation
    process. The table was generated with the help of
    OrderedTriangulator; the basic idea is that the choice of diagonal
    is made by considering the relative value of the point ids.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericCellTessellator, obj, update, **traits)
    
    def _get_error_metrics(self):
        return wrap_vtk(self._vtk_obj.GetErrorMetrics())
    def _set_error_metrics(self, arg):
        old_val = self._get_error_metrics()
        self._wrap_call(self._vtk_obj.SetErrorMetrics,
                        deref_vtk(arg))
        self.trait_property_changed('error_metrics', old_val, arg)
    error_metrics = traits.Property(_get_error_metrics, _set_error_metrics, help=\
        """
        Specify the list of error metrics used to decide if an edge has
        to be splitted or not. It is a collection of
        GenericSubdivisionErrorMetric-s.
        """
    )

    measurement = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If true, measure the quality of the fixed subdivision.
        """
    )
    def _measurement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMeasurement,
                        self.measurement)

    def init_error_metrics(self, *args):
        """
        V.init_error_metrics(GenericDataSet)
        C++: void InitErrorMetrics(GenericDataSet *ds)
        Init the error metric with the dataset. Should be called in each
        filter before any tessellation of any cell.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InitErrorMetrics, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(GenericDataSet)
        C++: virtual void Initialize(GenericDataSet *ds)
        Initialize the tessellator with a data set `ds'.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def tessellate(self, *args):
        """
        V.tessellate(GenericAdaptorCell, GenericAttributeCollection,
             DoubleArray, CellArray, PointData)
        C++: virtual void Tessellate(GenericAdaptorCell *cell,
            GenericAttributeCollection *att, DoubleArray *points,
            CellArray *cellArray, PointData *internalPd)
        Tessellate a 3d `cell'. The result is a set of smaller linear
        tetrahedra in `cell_array' with `points' and point data
        `internal_pd'.
        \pre cell_exists: cell!=0
        \pre valid_dimension: cell->_get_dimension()==_3
        \pre att_exists: att!=0
        \pre points_exists: points!=0
        \pre cell_array_exists: cell_array!=_0
        \pre internal_pd_exists: internal_pd!=_0
        """
        my_args = deref_array(args, [('vtkGenericAdaptorCell', 'vtkGenericAttributeCollection', 'vtkDoubleArray', 'vtkCellArray', 'vtkPointData')])
        ret = self._wrap_call(self._vtk_obj.Tessellate, *my_args)
        return ret

    def tessellate_face(self, *args):
        """
        V.tessellate_face(GenericAdaptorCell,
            GenericAttributeCollection, int, DoubleArray,
            CellArray, PointData)
        C++: virtual void TessellateFace(GenericAdaptorCell *cell,
            GenericAttributeCollection *att, IdType index,
            DoubleArray *points, CellArray *cellArray,
            PointData *internalPd)
        Tessellate a face of a 3d `cell'. The face is specified by the
        index value. The result is a set of smaller linear triangles in
        `cell_array' with `points' and point data `internal_pd'.
        \pre cell_exists: cell!=0
        \pre valid_dimension: cell->_get_dimension()==_3
        \pre valid_index_range: (index>=0) &&
            (index<cell->_get_number_of_boundaries(_2))
        \pre att_exists: att!=0
        \pre points_exists: points!=0
        \pre cell_array_exists: cell_array!=_0
        \pre internal_pd_exists: internal_pd!=_0
        """
        my_args = deref_array(args, [('vtkGenericAdaptorCell', 'vtkGenericAttributeCollection', 'int', 'vtkDoubleArray', 'vtkCellArray', 'vtkPointData')])
        ret = self._wrap_call(self._vtk_obj.TessellateFace, *my_args)
        return ret

    def triangulate(self, *args):
        """
        V.triangulate(GenericAdaptorCell,
            GenericAttributeCollection, DoubleArray, CellArray,
            PointData)
        C++: virtual void Triangulate(GenericAdaptorCell *cell,
            GenericAttributeCollection *att, DoubleArray *points,
            CellArray *cellArray, PointData *internalPd)
        Triangulate a 2d `cell'. The result is a set of smaller linear
        triangles in `cell_array' with `points' and point data
        `internal_pd'.
        \pre cell_exists: cell!=0
        \pre valid_dimension: cell->_get_dimension()==_2
        \pre att_exists: att!=0
        \pre points_exists: points!=0
        \pre cell_array_exists: cell_array!=_0
        \pre internal_pd_exists: internal_pd!=_0
        """
        my_args = deref_array(args, [('vtkGenericAdaptorCell', 'vtkGenericAttributeCollection', 'vtkDoubleArray', 'vtkCellArray', 'vtkPointData')])
        ret = self._wrap_call(self._vtk_obj.Triangulate, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('measurement',
    'GetMeasurement'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'measurement'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericCellTessellator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['measurement']),
            title='Edit GenericCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

