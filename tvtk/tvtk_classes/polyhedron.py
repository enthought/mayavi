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

from tvtk.tvtk_classes.cell3d import Cell3D


class Polyhedron(Cell3D):
    """
    Polyhedron - a 3d cell defined by a set of polygonal faces
    
    Superclass: Cell3D
    
    Polyhedron is a concrete implementation that represents a 3d cell
    defined by a set of polygonal faces. The polyhedron should be
    watertight, non-self-intersecting and manifold (each edge is used
    twice).
    
    Interpolation functions and weights are defined / computed using the
    method of Mean Value Coordinates (MVC). See the VTK class
    MeanValueCoordinatesInterpolator for more information.
    
    The class assumes that the polyhedron is non-convex. However, the
    polygonal faces should be planar. Non-planar polygonal faces will
    definitely cause problems, especially in severely warped situations.
    
    See Also:
    
    Cell3D ConvecPointSet MeanValueCoordinatesInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyhedron, obj, update, **traits)
    
    def _get_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetPolyData())
    poly_data = traits.Property(_get_poly_data, help=\
        """
        Construct polydata if no one exist, then return this->_poly_data
        """
    )

    def is_inside(self, *args):
        """
        V.is_inside([float, float, float], float) -> int
        C++: int IsInside(double x[3], double tolerance)"""
        ret = self._wrap_call(self._vtk_obj.IsInside, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('merge_tolerance', 'GetMergeTolerance'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Polyhedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['merge_tolerance']),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

