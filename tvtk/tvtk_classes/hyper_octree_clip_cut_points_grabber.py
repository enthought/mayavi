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

from tvtk.tvtk_classes.hyper_octree_points_grabber import HyperOctreePointsGrabber


class HyperOctreeClipCutPointsGrabber(HyperOctreePointsGrabber):
    """
    HyperOctreeClipCutPointsGrabber - A concrete implementation of
    
    Superclass: HyperOctreePointsGrabber
    
    See Also:
    
    HyperOctreeClipCut, HyperOctreeClipCutClipCutPointsGrabber,
    ClipHyperOctree, HyperOctreeClipCutCutter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeClipCutPointsGrabber, obj, update, **traits)
    
    def _get_polygon(self):
        return wrap_vtk(self._vtk_obj.GetPolygon())
    polygon = traits.Property(_get_polygon, help=\
        """
        Return the polygon.
        """
    )

    def _get_triangulator(self):
        return wrap_vtk(self._vtk_obj.GetTriangulator())
    triangulator = traits.Property(_get_triangulator, help=\
        """
        Return the ordered triangulator.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('dimension', 'GetDimension'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeClipCutPointsGrabber, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimension']),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

