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


class BiQuadraticQuadraticHexahedron(NonLinearCell):
    """
    BiQuadraticQuadraticHexahedron - cell represents a biquadratic, 
    
    Superclass: NonLinearCell
    
    BiQuadraticQuadraticHexahedron is a concrete implementation of
    NonLinearCell to represent a three-dimensional, 24-node
    isoparametric biquadratic hexahedron. The interpolation is the
    standard finite element, biquadratic-quadratic isoparametric shape
    function. The cell includes mid-edge and center-face nodes. The
    ordering of the 24 points defining the cell is point ids (0-7,8-19,
    20-23) where point ids 0-7 are the eight corner vertices of the cube;
    followed by twelve midedge nodes (8-19), nodes 20-23 are the
    center-face nodes. Note that these midedge nodes correspond lie on
    the edges defined by (0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7),
    (7,4), (0,4), (1,5), (2,6), (3,7). The center face nodes lieing in
    quad 22-(0,1,5,4), 21-(1,2,6,5), 23-(2,3,7,6) and 22-(3,0,4,7)
    
    
    
     top 
      7--14--6
      |      |
     15      13
      |      |
      4--12--5
    
      middle
     19--23--18
      |      |
     20      21
      |      |
     16--22--17
    
     bottom
      3--10--2
      |      |
     11      9 
      |      |
      0-- 8--1
      
     
    
    See Also:
    
    QuadraticEdge QuadraticTriangle QuadraticTetra
    QuadraticQuad QuadraticPyramid QuadraticWedge
    
    Thanks:
    
    Thanks to Soeren Gebbert  who developed this class and integrated it
    into VTK 5.0.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiQuadraticQuadraticHexahedron, obj, update, **traits)
    
    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[72])
        @deprecated Replaced by
        BiQuadraticQuadraticHexahedron::InterpolateDerivs as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[24])
        @deprecated Replaced by
        BiQuadraticQuadraticHexahedron::InterpolateFunctions as of VTK
        5.2
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
            return super(BiQuadraticQuadraticHexahedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BiQuadraticQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit BiQuadraticQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiQuadraticQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

