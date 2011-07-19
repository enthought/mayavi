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


class GenericEdgeTable(Object):
    """
    GenericEdgeTable - keep track of edges (defined by pair of integer
    id's)
    
    Superclass: Object
    
    GenericEdgeTable is used to indicate the existance of and hold
    information about edges. Similar to EdgeTable, this class is more
    sophisticated in that it uses reference counting to keep track of
    when information about an edge should be deleted.
    
    GenericEdgeTable is a helper class used in the adaptor framework. 
    It is used during the tessellation process to hold information about
    the error metric on each edge. This avoids recomputing the error
    metric each time the same edge is visited.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericEdgeTable, obj, update, **traits)
    
    number_of_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the total number of components for the point-centered
        attributes.
        \pre positive_count: count>0
        """
    )
    def _number_of_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfComponents,
                        self.number_of_components)

    def check_edge(self, *args):
        """
        V.check_edge(int, int, int) -> int
        C++: int CheckEdge(IdType e1, IdType e2, IdType &ptId)
        Method to determine whether an edge is in the table (0 or 1), or
        not (-1). It returns whether the edge was split (1) or not (0),
        and the point id exists.
        """
        ret = self._wrap_call(self._vtk_obj.CheckEdge, *args)
        return ret

    def check_edge_reference_count(self, *args):
        """
        V.check_edge_reference_count(int, int) -> int
        C++: int CheckEdgeReferenceCount(IdType e1, IdType e2)
        Return the edge reference count.
        """
        ret = self._wrap_call(self._vtk_obj.CheckEdgeReferenceCount, *args)
        return ret

    def check_point(self, *args):
        """
        V.check_point(int) -> int
        C++: int CheckPoint(IdType ptId)
        Check if a point is already in the point table.
        """
        ret = self._wrap_call(self._vtk_obj.CheckPoint, *args)
        return ret

    def dump_table(self):
        """
        V.dump_table()
        C++: void DumpTable()
        For debugging purposes. It is particularly useful to dump the
        table and check that nothing is left after a complete iteration.
        load_factor should ideally be very low to be able to have a
        constant time access
        """
        ret = self._vtk_obj.DumpTable()
        return ret
        

    def increment_edge_reference_count(self, *args):
        """
        V.increment_edge_reference_count(int, int, int) -> int
        C++: int IncrementEdgeReferenceCount(IdType e1, IdType e2,
            IdType cellId)
        Method that increments the referencecount and returns it.
        """
        ret = self._wrap_call(self._vtk_obj.IncrementEdgeReferenceCount, *args)
        return ret

    def increment_point_reference_count(self, *args):
        """
        V.increment_point_reference_count(int)
        C++: void IncrementPointReferenceCount(IdType ptId)
        Increment the reference count for the indicated point.
        """
        ret = self._wrap_call(self._vtk_obj.IncrementPointReferenceCount, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int)
        C++: void Initialize(IdType start)
        To specify the starting point id. It will initialize last_point_id
        This is very sensitive the start point should be cautiously
        chosen
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def insert_edge(self, *args):
        """
        V.insert_edge(int, int, int, int, int)
        C++: void InsertEdge(IdType e1, IdType e2, IdType cellId,
             int ref, IdType &ptId)
        V.insert_edge(int, int, int, int)
        C++: void InsertEdge(IdType e1, IdType e2, IdType cellId,
             int ref=1)
        Split the edge with the indicated point id.
        """
        ret = self._wrap_call(self._vtk_obj.InsertEdge, *args)
        return ret

    def insert_point(self, *args):
        """
        V.insert_point(int, [float, float, float])
        C++: void InsertPoint(IdType ptId, double point[3])
        Insert point associated with an edge.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def load_factor(self):
        """
        V.load_factor()
        C++: void LoadFactor()
        For debugging purposes. It is particularly useful to dump the
        table and check that nothing is left after a complete iteration.
        load_factor should ideally be very low to be able to have a
        constant time access
        """
        ret = self._vtk_obj.LoadFactor()
        return ret
        

    def remove_edge(self, *args):
        """
        V.remove_edge(int, int) -> int
        C++: int RemoveEdge(IdType e1, IdType e2)
        Method to remove an edge from the table. The method returns the
        current reference count.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveEdge, *args)
        return ret

    def remove_point(self, *args):
        """
        V.remove_point(int)
        C++: void RemovePoint(IdType ptId)
        Remove a point from the point table.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('number_of_components', 'GetNumberOfComponents'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_components'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericEdgeTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_components']),
            title='Edit GenericEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericEdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

