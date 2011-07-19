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


class GeoTreeNodeCache(Object):
    """
    GeoTreeNodeCache - Manages a list of GeoTreeNodes.
    
    Superclass: Object
    
    GeoTreeNodeCache keeps track of a linked list of GeoTreeNodes,
    and has operations to move nodes to the front of the list and to
    delete data from the least used nodes. This is used to recover memory
    from nodes that store data that hasn't been used in a while.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTreeNodeCache, obj, update, **traits)
    
    cache_maximum_limit = traits.Int(500, enter_set=True, auto_set=False, help=\
        """
        The size of the cache of geospatial nodes. When the size reaches
        this limit, the list of non-empty nodes will be shortened to
        cache_minimum_limit.
        """
    )
    def _cache_maximum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheMaximumLimit,
                        self.cache_maximum_limit)

    cache_minimum_limit = traits.Int(250, enter_set=True, auto_set=False, help=\
        """
        The cache is reduced to this size when the maximum limit is
        reached.
        """
    )
    def _cache_minimum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheMinimumLimit,
                        self.cache_minimum_limit)

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        The current size of the list.
        """
    )

    def remove_node(self, *args):
        """
        V.remove_node(GeoTreeNode)
        C++: void RemoveNode(GeoTreeNode *node)
        Remove the node from the list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNode, *my_args)
        return ret

    def send_to_front(self, *args):
        """
        V.send_to_front(GeoTreeNode)
        C++: void SendToFront(GeoTreeNode *node)
        Send a node to the front of the list. Perform this whenever a
        node is accessed, so that the most recently accessed nodes' data
        are not deleted.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SendToFront, *my_args)
        return ret

    _updateable_traits_ = \
    (('cache_minimum_limit', 'GetCacheMinimumLimit'), ('reference_count',
    'GetReferenceCount'), ('cache_maximum_limit', 'GetCacheMaximumLimit'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cache_maximum_limit',
    'cache_minimum_limit'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTreeNodeCache, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTreeNodeCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cache_maximum_limit',
            'cache_minimum_limit']),
            title='Edit GeoTreeNodeCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTreeNodeCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

