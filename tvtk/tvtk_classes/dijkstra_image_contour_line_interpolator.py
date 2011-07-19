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

from tvtk.tvtk_classes.contour_line_interpolator import ContourLineInterpolator


class DijkstraImageContourLineInterpolator(ContourLineInterpolator):
    """
    DijkstraImageContourLineInterpolator - Contour interpolator for
    placing points on an image.
    
    Superclass: ContourLineInterpolator
    
    DijkstraImageContourLineInterpolator interpolates and places
    contour points on images. The class interpolates nodes by computing a
    graph lying on the image data. By graph, we mean that the line
    interpolating the two end points traverses along pixels so as to form
    a shortest path. A Dijkstra algorithm is used to compute the path.
    
    The class is meant to be used in conjunction with
    ImageActorPointPlacer. One reason for this coupling is a
    performance issue: both classes need to perform a cell pick, and
    coupling avoids multiple cell picks (cell picks are slow).  Another
    issue is that the interpolator may need to set the image input to its
    DijkstraImageGeodesicPath ivar.
    
    See Also:
    
    ContourWidget ContourLineInterpolator
    DijkstraImageGeodesicPath
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDijkstraImageContourLineInterpolator, obj, update, **traits)
    
    def _get_cost_image(self):
        return wrap_vtk(self._vtk_obj.GetCostImage())
    def _set_cost_image(self, arg):
        old_val = self._get_cost_image()
        self._wrap_call(self._vtk_obj.SetCostImage,
                        deref_vtk(arg))
        self.trait_property_changed('cost_image', old_val, arg)
    cost_image = traits.Property(_get_cost_image, _set_cost_image, help=\
        """
        Set the image data for the DijkstraImageGeodesicPath. If not
        set, the interpolator uses the image data input to the image
        actor. The image actor is obtained from the expected
        ImageActorPointPlacer.
        """
    )

    def _get_dijkstra_image_geodesic_path(self):
        return wrap_vtk(self._vtk_obj.GetDijkstraImageGeodesicPath())
    dijkstra_image_geodesic_path = traits.Property(_get_dijkstra_image_geodesic_path, help=\
        """
        access to the internal dijkstra path
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DijkstraImageContourLineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DijkstraImageContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DijkstraImageContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DijkstraImageContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

