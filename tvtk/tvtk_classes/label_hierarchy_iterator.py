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


class LabelHierarchyIterator(Object):
    """
    LabelHierarchyIterator - iterator over LabelHierarchy
    
    Superclass: Object
    
    Abstract superclass for iterators over LabelHierarchy.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelHierarchyIterator, obj, update, **traits)
    
    all_bounds = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get whether all nodes in the hierarchy should be added to the
        traversed_bounds polydata or only those traversed. When non-zero,
        all nodes will be added. By default, all_bounds is 0.
        """
    )
    def _all_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllBounds,
                        self.all_bounds)

    def get_bounded_size(self, *args):
        """
        V.get_bounded_size([float, float])
        C++: virtual void GetBoundedSize(double sz[2])
        Retrieves the current label maximum width in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetBoundedSize, *args)
        return ret

    def _get_hierarchy(self):
        return wrap_vtk(self._vtk_obj.GetHierarchy())
    hierarchy = traits.Property(_get_hierarchy, help=\
        """
        Get the label hierarchy associated with the current label.
        """
    )

    def _get_label(self):
        return self._vtk_obj.GetLabel()
    label = traits.Property(_get_label, help=\
        """
        Retrieves the current label string.
        """
    )

    def _get_label_id(self):
        return self._vtk_obj.GetLabelId()
    label_id = traits.Property(_get_label_id, help=\
        """
        Retrieves the current label id.
        """
    )

    def get_node_geometry(self, *args):
        """
        V.get_node_geometry([float, float, float], float)
        C++: virtual void GetNodeGeometry(double ctr[3], double &size)
        Retrieve the coordinates of the center of the current hierarchy
        node and the size of the node. Nodes are n-cubes, so the size is
        the length of any edge of the cube. This is used by box_node().
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeGeometry, *args)
        return ret

    def _get_orientation(self):
        return self._vtk_obj.GetOrientation()
    orientation = traits.Property(_get_orientation, help=\
        """
        Retrieves the current label orientation.
        """
    )

    def get_point(self, *args):
        """
        V.get_point([float, float, float])
        C++: virtual void GetPoint(double x[3])
        Retrieves the current label location.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def get_size(self, *args):
        """
        V.get_size([float, float])
        C++: virtual void GetSize(double sz[2])
        Retrieves the current label size.
        """
        ret = self._wrap_call(self._vtk_obj.GetSize, *args)
        return ret

    def _get_type(self):
        return self._vtk_obj.GetType()
    type = traits.Property(_get_type, help=\
        """
        Retrieves the current label type.
        """
    )

    def _get_unicode_label(self):
        return self._vtk_obj.GetUnicodeLabel()
    unicode_label = traits.Property(_get_unicode_label, help=\
        """
        Retrieves the current label as a unicode string.
        """
    )

    def begin(self, *args):
        """
        V.begin(IdTypeArray)
        C++: virtual void Begin(IdTypeArray *)
        Initializes the iterator. last_labels is an array holding labels
        which should be traversed before any other labels in the
        hierarchy. This could include labels placed during a previous
        rendering or a label located under the mouse pointer. You may
        pass a null pointer.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.Begin, *my_args)
        return ret

    def box_all_nodes(self, *args):
        """
        V.box_all_nodes(PolyData)
        C++: virtual void BoxAllNodes(PolyData *)
        Add a representation for all existing octree nodes to the
        specified polydata. This is equivalent to setting
        traversed_bounds, iterating over the entire hierarchy, and then
        resetting traversed_bounds to its original value.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BoxAllNodes, *my_args)
        return ret

    def box_node(self):
        """
        V.box_node()
        C++: virtual void BoxNode()
        Add a representation to traversed_bounds for the current octree
        node. This should be called by subclasses inside Next(). Does
        nothing if traversed_bounds is NULL.
        """
        ret = self._vtk_obj.BoxNode()
        return ret
        

    def is_at_end(self):
        """
        V.is_at_end() -> bool
        C++: virtual bool IsAtEnd()
        Returns true if the iterator is at the end.
        """
        ret = self._vtk_obj.IsAtEnd()
        return ret
        

    def next(self):
        """
        V.next()
        C++: virtual void Next()
        Advance the iterator.
        """
        ret = self._vtk_obj.Next()
        return ret
        

    def set_traversed_bounds(self, *args):
        """
        V.set_traversed_bounds(PolyData)
        C++: virtual void SetTraversedBounds(PolyData *)
        Sets a polydata to fill with geometry representing the bounding
        boxes of the traversed octree nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTraversedBounds, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('all_bounds', 'GetAllBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'all_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelHierarchyIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelHierarchyIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['all_bounds']),
            title='Edit LabelHierarchyIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelHierarchyIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

