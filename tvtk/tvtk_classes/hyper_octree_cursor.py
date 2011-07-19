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


class HyperOctreeCursor(Object):
    """
    HyperOctreeCursor - Objects that can traverse hyperoctree nodes.
    
    Superclass: Object
    
    Objects that can traverse hyperoctree nodes. It is an abstract class.
    Cursors are created by the hyperoctree.
    
    See Also:
    
    DataObject FieldData HyperOctreeAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeCursor, obj, update, **traits)
    
    def _get_child_index(self):
        return self._vtk_obj.GetChildIndex()
    child_index = traits.Property(_get_child_index, help=\
        """
        Return the child number of the current node relative to its
        parent.
        \pre not_root: !_current_is_root().
        \post valid_range: result>=0 && result<_get_number_of_children()
        """
    )

    def _get_current_level(self):
        return self._vtk_obj.GetCurrentLevel()
    current_level = traits.Property(_get_current_level, help=\
        """
        Return the level of the node pointed by the cursor.
        \post positive_result: result>=0
        """
    )

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        Return the dimension of the tree.
        \post positive_result: result>0
        """
    )

    def get_index(self, *args):
        """
        V.get_index(int) -> int
        C++: virtual int GetIndex(int d)
        Return the index in dimension `d', as if the node was a cell of a
        uniform grid of 1<<_get_current_level() cells in each dimension.
        \pre valid_range: d>=0 && d<_get_dimension()
        \post valid_result: result>=0 && result<(_1<<_get_current_level())
        """
        ret = self._wrap_call(self._vtk_obj.GetIndex, *args)
        return ret

    def _get_leaf_id(self):
        return self._vtk_obj.GetLeafId()
    leaf_id = traits.Property(_get_leaf_id, help=\
        """
        Return the index of the current leaf in the data arrays.
        \pre is_leaf: current_is_leaf()
        """
    )

    def _get_number_of_children(self):
        return self._vtk_obj.GetNumberOfChildren()
    number_of_children = traits.Property(_get_number_of_children, help=\
        """
        Return the number of children for each node of the tree.
        \post positive_number: result>0
        """
    )

    def clone(self):
        """
        V.clone() -> HyperOctreeCursor
        C++: virtual HyperOctreeCursor *Clone()
        Create a copy of `this'.
        \post results_exists:result!=0
        \post same_tree: result->_same_tree(this)
        """
        ret = wrap_vtk(self._vtk_obj.Clone())
        return ret
        

    def current_is_leaf(self):
        """
        V.current_is_leaf() -> int
        C++: virtual int CurrentIsLeaf()
        Is the node pointed by the cursor a leaf?
        """
        ret = self._vtk_obj.CurrentIsLeaf()
        return ret
        

    def current_is_root(self):
        """
        V.current_is_root() -> int
        C++: virtual int CurrentIsRoot()
        Is the node pointed by the cursor the root?
        """
        ret = self._vtk_obj.CurrentIsRoot()
        return ret
        

    def current_is_terminal_node(self):
        """
        V.current_is_terminal_node() -> int
        C++: virtual int CurrentIsTerminalNode()"""
        ret = self._vtk_obj.CurrentIsTerminalNode()
        return ret
        

    def found(self):
        """
        V.found() -> int
        C++: virtual int Found()"""
        ret = self._vtk_obj.Found()
        return ret
        

    def is_equal(self, *args):
        """
        V.is_equal(HyperOctreeCursor) -> int
        C++: virtual int IsEqual(HyperOctreeCursor *other)
        Is `this' equal to `other'?
        \pre other_exists: other!=0
        \pre same_hyperoctree: this->_same_tree(other);
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsEqual, *my_args)
        return ret

    def same_tree(self, *args):
        """
        V.same_tree(HyperOctreeCursor) -> int
        C++: virtual int SameTree(HyperOctreeCursor *other)
        Are `this' and `other' pointing on the same hyperoctree?
        \pre other_exists: other!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SameTree, *my_args)
        return ret

    def to_child(self, *args):
        """
        V.to_child(int)
        C++: virtual void ToChild(int child)
        Move the cursor to child `child' of the current node.
        \pre not_leaf: !_current_is_leaf()
        \pre valid_child: child>=0 && child<this->_get_number_of_children()
        """
        ret = self._wrap_call(self._vtk_obj.ToChild, *args)
        return ret

    def to_parent(self):
        """
        V.to_parent()
        C++: virtual void ToParent()
        Move the cursor to the parent of the current node.
        \pre not_root: !_current_is_root()
        """
        ret = self._vtk_obj.ToParent()
        return ret
        

    def to_root(self):
        """
        V.to_root()
        C++: virtual void ToRoot()
        Move the cursor the root node.
        \pre can be root
        \post is_root: current_is_root()
        """
        ret = self._vtk_obj.ToRoot()
        return ret
        

    def to_same_node(self, *args):
        """
        V.to_same_node(HyperOctreeCursor)
        C++: virtual void ToSameNode(HyperOctreeCursor *other)
        Move the cursor to the same node pointed by `other'.
        \pre other_exists: other!=0
        \pre same_hyperoctree: this->_same_tree(other);
        \post equal: this->_is_equal(other)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToSameNode, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeCursor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit HyperOctreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

