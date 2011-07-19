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


class ContourLineInterpolator(Object):
    """
    ContourLineInterpolator - Defines API for interpolating/modifying
    nodes from a ContourRepresentation
    
    Superclass: Object
    
    ContourLineInterpolator is an abstract base class for
    interpolators that work are used by the contour representation class
    to interpolate and/or modify nodes in a contour. Subclasses must
    override the virtual method: interpolate_line. This is used by the
    contour representation to give the interpolator a chance to define an
    interpolation scheme between nodes. See
    BezierContourLineInterpolator for a concrete implementation.
    Subclasses may also override, update_node. This provides a way for the
    representation to give the interpolator a chance to modify the nodes,
    as the user constructs the contours. For instance a sticky contour
    widget may be implemented that moves nodes to nearby regions of high
    gradient, to be used in contour guided segmentation.
    
    See Also:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContourLineInterpolator, obj, update, **traits)
    
    def get_span(self, *args):
        """
        V.get_span(int, IntArray, ContourRepresentation)
        C++: virtual void GetSpan(int nodeIndex, IntArray *nodeIndices,
             ContourRepresentation *rep)
        Span of the interpolator. ie. the number of control points its
        supposed to interpolate given a node.
        
        The first argument is the current node_index. ie, you'd be trying
        to interpolate between nodes "node_index" and "node_index-_1",
        unless you're closing the contour in which case, you're trying to
        interpolate "node_index" and "Node=0".
        
        The node span is returned in a IntArray. The default node span
        is 1 (ie. node_indices is a 2 tuple (node_index, node_index-_1)).
        However, it need not always be 1. For instance, cubic spline
        interpolators, which have a span of 3 control points, it can be
        larger. See BezierContourLineInterpolator for instance.
        """
        my_args = deref_array(args, [('int', 'vtkIntArray', 'vtkContourRepresentation')])
        ret = self._wrap_call(self._vtk_obj.GetSpan, *my_args)
        return ret

    def interpolate_line(self, *args):
        """
        V.interpolate_line(Renderer, ContourRepresentation, int, int)
             -> int
        C++: virtual int InterpolateLine(Renderer *ren,
            ContourRepresentation *rep, int idx1, int idx2)
        Subclasses that wish to interpolate a line segment must implement
        this. For instance BezierContourLineInterpolator adds nodes
        between idx1 and idx2, that allow the contour to adhere to a
        bezier curve.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateLine, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContourLineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

