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


class TreeBFSIterator(Object):
    """
    TreeBFSIterator - breadth first search iterator through a Tree
    
    Superclass: Object
    
    TreeBFSIterator performs a breadth first search of a tree.
    
    After setting up the iterator, the normal mode of operation is to set
    up a while(iter->_has_next())loop, with the statement IdType vertex
    = iter->Next()inside the loop.
    
    Thanks:
    
    Thanks to David Doria for submitting this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeBFSIterator, obj, update, **traits)
    
    mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the visit mode of the iterator.  Mode can be
          DISCOVER (0): Order by discovery time
          FINISH   (1): Order by finish time Default is DISCOVER. Use
        DISCOVER for top-down algorithms where parents need to be
        processed before children. Use FINISH for bottom-up algorithms
        where children need to be processed before parents.
        """
    )
    def _mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMode,
                        self.mode)

    start_vertex = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The start vertex of the seedgeh. The tree iterator will only
        iterate over the subtree rooted at vertex. If not set (or set to
        a negative value), starts at the root of the tree.
        """
    )
    def _start_vertex_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartVertex,
                        self.start_vertex)

    def has_next(self):
        """
        V.has_next() -> bool
        C++: bool HasNext()
        Return true when all vertices have been visited.
        """
        ret = self._vtk_obj.HasNext()
        return ret
        

    def next(self):
        """
        V.next() -> int
        C++: IdType Next()
        The next vertex visited in the graph.
        """
        ret = self._vtk_obj.Next()
        return ret
        

    def set_tree(self, *args):
        """
        V.set_tree(Tree)
        C++: void SetTree(Tree *graph)
        Set the graph to iterate over.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTree, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('mode',
    'GetMode'), ('start_vertex', 'GetStartVertex'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'mode', 'start_vertex'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeBFSIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeBFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['mode', 'start_vertex']),
            title='Edit TreeBFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeBFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

