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


class CubicLine(NonLinearCell):
    """
    CubicLine - cell represents a cubic , isoparametric 1d line
    
    Superclass: NonLinearCell
    
    CubicLine is a concrete implementation of NonLinearCell to
    represent a 1d Cubic line. The Cubic Line is the 4 nodes
    isoparametric parabolic line . The interpolation is the standard
    finite element, cubic isoparametric shape function. The cell includes
    two mid-edge nodes. The ordering of the four points defining the cell
    is point ids (0,1,2,3) where id #2 and #3 are the mid-edge nodes.
    Please note that the parametric coordinates lie between -1 and 1 in
    accordance with most standard documentations.
    
    Thanks:
    
    This file has been developed by Oxalya - www.oxalya.com Copyright (c)
    EDF - www.edf.fr 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCubicLine, obj, update, **traits)
    
    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[4])
        @deprecated Replaced by CubicLine::InterpolateDerivs as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[4])
        @deprecated Replaced by CubicLine::InterpolateFunctions as of
        VTK 5.2
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
            return super(CubicLine, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CubicLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CubicLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CubicLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

