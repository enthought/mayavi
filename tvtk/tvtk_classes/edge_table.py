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


class EdgeTable(Object):
    """
    EdgeTable - keep track of edges (edge is pair of integer id's)
    
    Superclass: Object
    
    EdgeTable is a general object for keeping track of lists of edges.
    An edge is defined by the pair of point id's (p1,p2). Methods are
    available to insert edges, check if edges exist, and traverse the
    list of edges. Also, it's possible to associate attribute information
    with each edge. The attribute information may take the form of
    IdType id's, void* pointers, or points. To store attributes, make
    sure that init_edge_insertion() is invoked with the store_attributes
    flag set properly. If points are inserted, use the methods
    init_point_insertion() and insert_unique_point().
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEdgeTable, obj, update, **traits)
    
    def get_next_edge(self, *args):
        """
        V.get_next_edge(int, int) -> int
        C++: IdType GetNextEdge(IdType &p1, IdType &p2)
        Traverse list of edges in table. Return the edge as (p1,p2),
        where p1 and p2 are point id's. Method return value is <0 if list
        is exhausted; non-zero otherwise. The value of p1 is guaranteed
        to be <= p2.
        """
        ret = self._wrap_call(self._vtk_obj.GetNextEdge, *args)
        return ret

    def _get_number_of_edges(self):
        return self._vtk_obj.GetNumberOfEdges()
    number_of_edges = traits.Property(_get_number_of_edges, help=\
        """
        Return the number of edges that have been inserted thus far.
        """
    )

    def init_edge_insertion(self, *args):
        """
        V.init_edge_insertion(int, int) -> int
        C++: int InitEdgeInsertion(IdType numPoints,
            int storeAttributes=0)
        Initialize the edge insertion process. Provide an estimate of the
        number of points in a dataset (the maximum range value of p1 or
        p2).  The store_attributes variable controls whether attributes
        are to be stored with the edge, and what type of attributes. If
        store_attributes==_1, then attributes of IdType can be stored.
        If store_attributes==_2, then attributes of type void* can be
        stored. In either case, additional memory will be required by the
        data structure to store attribute data per each edge.  This
        method is used in conjunction with one of the three insert_edge()
        methods described below (don't mix the insert_edge()
        methods---make sure that the one used is consistent with the
        store_attributes flag set in init_edge_insertion()).
        """
        ret = self._wrap_call(self._vtk_obj.InitEdgeInsertion, *args)
        return ret

    def init_point_insertion(self, *args):
        """
        V.init_point_insertion(Points, int) -> int
        C++: int InitPointInsertion(Points *newPts, IdType estSize)
        Initialize the point insertion process. The new_pts is an object
        representing point coordinates into which incremental insertion
        methods place their data. The points are associated with the
        edge.
        """
        my_args = deref_array(args, [('vtkPoints', 'int')])
        ret = self._wrap_call(self._vtk_obj.InitPointInsertion, *my_args)
        return ret

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()
        Intialize traversal of edges in table.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Free memory and return to the initially instantiated state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_edge(self, *args):
        """
        V.insert_edge(int, int) -> int
        C++: IdType InsertEdge(IdType p1, IdType p2)
        V.insert_edge(int, int, int)
        C++: void InsertEdge(IdType p1, IdType p2,
            IdType attributeId)
        V.insert_edge(int, int, )
        C++: void InsertEdge(IdType p1, IdType p2, void *ptr)
        Insert the edge (p1,p2) into the table. It is the user's
        responsibility to check if the edge has already been inserted
        (use is_edge()). If the store_attributes flag in
        init_edge_insertion() has been set, then the method returns a
        unique integer id (i.e., the edge id) that can be used to set and
        get edge attributes. Otherwise, the method will return 1. Do not
        mix this method with the insert_edge() method that follows.
        """
        ret = self._wrap_call(self._vtk_obj.InsertEdge, *args)
        return ret

    def insert_unique_point(self, *args):
        """
        V.insert_unique_point(int, int, [float, float, float], int) -> int
        C++: int InsertUniquePoint(IdType p1, IdType p2,
            double x[3], IdType &ptId)
        Insert a unique point on the specified edge. Invoke this method
        only after init_point_insertion() has been called. Return 0 if
        point was already in the list, otherwise return 1.
        """
        ret = self._wrap_call(self._vtk_obj.InsertUniquePoint, *args)
        return ret

    def is_edge(self, *args):
        """
        V.is_edge(int, int) -> int
        C++: IdType IsEdge(IdType p1, IdType p2)
        Return an integer id for the edge, or an attribute id of the edge
        (p1,p2) if the edge has been previously defined (it depends upon
        which version of insert_edge() is being used); otherwise -1. The
        unique integer id can be used to set and retrieve attributes to
        the edge.
        """
        ret = self._wrap_call(self._vtk_obj.IsEdge, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the object and prepare for reinsertion of edges. Does not
        delete memory like the Initialize() method.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EdgeTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit EdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EdgeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

