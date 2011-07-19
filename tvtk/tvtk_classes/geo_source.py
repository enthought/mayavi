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


class GeoSource(Object):
    """
    GeoSource - A multi-resolution geographic data source
    
    Superclass: Object
    
    GeoSource is an abstract superclass for all multi-resolution data
    sources shown in a geographic view like GeoView or GeoView2D.
    GeoSource subclasses need to implement the fetch_root() method,
    which fills a GeoTreeNode with the low-res data at the root, and
    fetch_child(), which produces a refinement of a parent node. Other
    geovis classes such as GeoTerrain, GeoTerrain2D, and
    GeoAlignedImageSource use a GeoSource subclass to build their
    geometry or image caches which are stored in trees. The source itself
    does not maintain the tree, but simply provides a mechanism for
    generating refined tree nodes.
    
    Sources are multi-threaded. Each source may have one or more worker
    threads associated with it, which this superclass manages. It is
    essential that the fetch_child() method is thread-safe, since it may
    be called from multiple workers simultaneously.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoSource, obj, update, **traits)
    
    def get_requested_nodes(self, *args):
        """
        V.get_requested_nodes(GeoTreeNode) -> Collection
        C++: virtual Collection *GetRequestedNodes(
            GeoTreeNode *node)
        Non-blocking methods for to use from the main application. After
        calling request_children() for a certain node, get_requested_nodes()
        will after a certain period of time return a non-null pointer to
        a collection of four GeoTreeNode objects, which are the four
        children of the requested node. The collection is reference
        counted, so you need to eventually call Delete() on the returned
        collection pointer (if it is non-null).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetRequestedNodes, *my_args)
        return wrap_vtk(ret)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Return the projection transformation used by this source.
        """
    )

    def fetch_child(self, *args):
        """
        V.fetch_child(GeoTreeNode, int, GeoTreeNode) -> bool
        C++: virtual bool FetchChild(GeoTreeNode *node, int index,
            GeoTreeNode *child)
        Blocking access methods to be implemented in subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FetchChild, *my_args)
        return ret

    def fetch_root(self, *args):
        """
        V.fetch_root(GeoTreeNode) -> bool
        C++: virtual bool FetchRoot(GeoTreeNode *root)
        Blocking access methods to be implemented in subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FetchRoot, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int)
        C++: void Initialize(int numThreads=1)
        Spawn worker threads.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def request_children(self, *args):
        """
        V.request_children(GeoTreeNode)
        C++: virtual void RequestChildren(GeoTreeNode *node)
        Non-blocking methods for to use from the main application. After
        calling request_children() for a certain node, get_requested_nodes()
        will after a certain period of time return a non-null pointer to
        a collection of four GeoTreeNode objects, which are the four
        children of the requested node. The collection is reference
        counted, so you need to eventually call Delete() on the returned
        collection pointer (if it is non-null).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RequestChildren, *my_args)
        return ret

    def shut_down(self):
        """
        V.shut_down()
        C++: void ShutDown()
        Shut down the source. This terminates the thread and releases
        memory.
        """
        ret = self._vtk_obj.ShutDown()
        return ret
        

    def worker_thread(self):
        """
        V.worker_thread()
        C++: void WorkerThread()"""
        ret = self._vtk_obj.WorkerThread()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GeoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

