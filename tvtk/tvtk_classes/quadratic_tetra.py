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

from tvtk.tvtk_classes.non_linear_cell import NonLinearCell


class QuadraticTetra(NonLinearCell):
    """
    QuadraticTetra - cell represents a parabolic, 10-node
    isoparametric tetrahedron
    
    Superclass: NonLinearCell
    
    QuadraticTetra is a concrete implementation of NonLinearCell to
    represent a three-dimensional, 10-node, isoparametric parabolic
    tetrahedron. The interpolation is the standard finite element,
    quadratic isoparametric shape function. The cell includes a mid-edge
    node on each of the size edges of the tetrahedron. The ordering of
    the ten points defining the cell is point ids (0-3,4-9) where ids 0-3
    are the four tetra vertices; and point ids 4-9 are the midedge nodes
    between (0,1), (1,2), (2,0), (0,3), (1,3), and (2,3).
    
    See Also:
    
    QuadraticEdge QuadraticTriangle QuadraticWedge
    QuadraticQuad QuadraticHexahedron QuadraticPyramid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadraticTetra, obj, update, **traits)
    
    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[30])
        @deprecated Replaced by QuadraticTetra::InterpolateDerivs as
        of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[10])
        @deprecated Replaced by QuadraticTetra::InterpolateFunctions
        as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuadraticTetra, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadraticTetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit QuadraticTetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadraticTetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

