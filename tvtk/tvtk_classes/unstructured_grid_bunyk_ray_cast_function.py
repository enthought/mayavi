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

from tvtk.tvtk_classes.unstructured_grid_volume_ray_cast_function import UnstructuredGridVolumeRayCastFunction


class UnstructuredGridBunykRayCastFunction(UnstructuredGridVolumeRayCastFunction):
    """
    UnstructuredGridBunykRayCastFunction - a superclass for ray
    casting functions
    
    Superclass: UnstructuredGridVolumeRayCastFunction
    
    UnstructuredGridBunykRayCastFunction is a concrete implementation
    of a ray cast function for unstructured grid data. This class was
    based on the paper "Simple, Fast, Robust Ray Casting of Irregular
    Grids" by Paul Bunyk, Arie Kaufmna, and Claudio Silva. This method is
    quite memory intensive (with extra explicit copies of the data) and
    therefore should not be used for very large data. This method assumes
    that the input data is composed entirely of tetras - use
    DataSetTriangleFilter before setting the input on the mapper.
    
    The basic idea of this method is as follows:
    
    1) Enumerate the triangles. At each triangle have space for some
       information that will be used during rendering. This includes
       which tetra the triangles belong to, the plane equation and the
       Barycentric coefficients.
    
    2) Keep a reference to all four triangles for each tetra.
    
    3) At the beginning of each render, do the precomputation. This
       includes creating an array of transformed points (in view
       coordinates) and computing the view dependent info per triangle
       (plane equations and barycentric coords in view space)
    
    4) Find all front facing boundary triangles (a triangle is on the
       boundary if it belongs to only one tetra). For each triangle, find
    all pixels in the image that intersect the triangle, and add this to
       the sorted (by depth) intersection list at each pixel.
    
    5) For each ray cast, traverse the intersection list. At each
       intersection, accumulate opacity and color contribution per tetra
       along the ray until you reach an exiting triangle (on the
       boundary).
    
    See Also:
    
    UnstructuredGridVolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridBunykRayCastFunction, obj, update, **traits)
    
    def _get_image_origin(self):
        return self._vtk_obj.GetImageOrigin()
    image_origin = traits.Property(_get_image_origin, help=\
        """
        Access to an internal structure for the templated method.
        """
    )

    def _get_image_viewport_size(self):
        return self._vtk_obj.GetImageViewportSize()
    image_viewport_size = traits.Property(_get_image_viewport_size, help=\
        """
        Access to an internal structure for the templated method.
        """
    )

    def _get_view_to_world_matrix(self):
        return wrap_vtk(self._vtk_obj.GetViewToWorldMatrix())
    view_to_world_matrix = traits.Property(_get_view_to_world_matrix, help=\
        """
        Access to an internal structure for the templated method.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridBunykRayCastFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridBunykRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit UnstructuredGridBunykRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridBunykRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

