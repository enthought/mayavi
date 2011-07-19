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


class GeoTreeNode(Object):
    """
    GeoTreeNode - Stores data for a patch of the globe.
    
    Superclass: Object
    
    A self-referential data structure for storing geometry or imagery for
    the geospatial views. The data is organized in a quadtree. Each node
    contains a pointer to its parent and owns references to its four
    child nodes. The ID of each node is unique in its level, and encodes
    the path from the root node in its bits.
    
    See Also:
    
    GeoView GeoView2D GeoTerrain
    GeoAlignedImageRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTreeNode, obj, update, **traits)
    
    def _get_older(self):
        return wrap_vtk(self._vtk_obj.GetOlder())
    def _set_older(self, arg):
        old_val = self._get_older()
        self._wrap_call(self._vtk_obj.SetOlder,
                        deref_vtk(arg))
        self.trait_property_changed('older', old_val, arg)
    older = traits.Property(_get_older, _set_older, help=\
        """
        Manage links to older and newer tree nodes. These are used to
        periodically delete unused patches.
        """
    )

    latitude_range = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _latitude_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeRange,
                        self.latitude_range)

    level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

    def _get_newer(self):
        return wrap_vtk(self._vtk_obj.GetNewer())
    def _set_newer(self, arg):
        old_val = self._get_newer()
        self._wrap_call(self._vtk_obj.SetNewer,
                        deref_vtk(arg))
        self.trait_property_changed('newer', old_val, arg)
    newer = traits.Property(_get_newer, _set_newer, help=\
        """
        Manage links to older and newer tree nodes. These are used to
        periodically delete unused patches.
        """
    )

    longitude_range = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _longitude_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeRange,
                        self.longitude_range)

    id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The id uniquely specified this node. For this implementation I am
        going to store the branch path in the bits.
        """
    )
    def _id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetId,
                        self.id)

    def get_child_tree_node(self, *args):
        """
        V.get_child_tree_node(int) -> GeoTreeNode
        C++: GeoTreeNode *GetChildTreeNode(int idx)
        Get the child as a GeoTreeNode. Subclasses also implement
        get_child() which returns the child as the appropriate subclass
        type.
        """
        ret = self._wrap_call(self._vtk_obj.GetChildTreeNode, *args)
        return wrap_vtk(ret)

    def _get_parent_tree_node(self):
        return wrap_vtk(self._vtk_obj.GetParentTreeNode())
    parent_tree_node = traits.Property(_get_parent_tree_node, help=\
        """
        Get the parent as a GeoTreeNode. Subclasses also implement
        get_parent() which returns the parent as the appropriate subclass
        type.
        """
    )

    def _get_which_child_are_you(self):
        return self._vtk_obj.GetWhichChildAreYou()
    which_child_are_you = traits.Property(_get_which_child_are_you, help=\
        """
        
        """
    )

    def create_children(self):
        """
        V.create_children() -> int
        C++: int CreateChildren()"""
        ret = self._vtk_obj.CreateChildren()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(GeoTreeNode)
        C++: virtual void DeepCopy(GeoTreeNode *src)
        Shallow and Deep copy. Deep copy performs a shallow copy of the
        Child nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def delete_data(self):
        """
        V.delete_data()
        C++: virtual void DeleteData()
        Deletes the data associated with the node to make this an "empty"
        node. This is performed when the node has been unused for a
        certain amount of time.
        """
        ret = self._vtk_obj.DeleteData()
        return ret
        

    def has_data(self):
        """
        V.has_data() -> bool
        C++: virtual bool HasData()
        Returns whether this node has valid data associated with it, or
        if it is an "empty" node.
        """
        ret = self._vtk_obj.HasData()
        return ret
        

    def is_descendant_of(self, *args):
        """
        V.is_descendant_of(GeoTreeNode) -> bool
        C++: bool IsDescendantOf(GeoTreeNode *elder)
        This method returns true if this node descends from the elder
        node.  The descision is made from the node ids, so the nodes do
        not have to be in the same tree!
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsDescendantOf, *my_args)
        return ret

    def set_child(self, *args):
        """
        V.set_child(GeoTreeNode, int)
        C++: void SetChild(GeoTreeNode *node, int idx)
        Get a child of this node. If one is set, then they all should
        set.  No not mix subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetChild, *my_args)
        return ret

    def set_parent(self, *args):
        """
        V.set_parent(GeoTreeNode)
        C++: void SetParent(GeoTreeNode *node)
        When we merge children to a lower resolution parent, we need this
        reference.  It is not referenced counted to avoid reference
        loops. A child should never exist when the parent is destructed
        anyway.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetParent, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(GeoTreeNode)
        C++: virtual void ShallowCopy(GeoTreeNode *src)
        Shallow and Deep copy. Deep copy performs a shallow copy of the
        Child nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('latitude_range', 'GetLatitudeRange'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('longitude_range', 'GetLongitudeRange'), ('level', 'GetLevel'),
    ('reference_count', 'GetReferenceCount'), ('id', 'GetId'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'id', 'latitude_range', 'level',
    'longitude_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTreeNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['id', 'latitude_range', 'level',
            'longitude_range']),
            title='Edit GeoTreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

