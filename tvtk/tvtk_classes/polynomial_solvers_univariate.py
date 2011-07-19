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


class PolynomialSolversUnivariate(Object):
    """
    PolynomialSolversUnivariate - polynomial solvers
    
    Superclass: Object
    
    PolynomialSolversUnivariate provides solvers for univariate
    polynomial equations with real coefficients. The Tartaglia-Cardan and
    Ferrari solvers work on polynomials of fixed degree 3 and 4,
    respectively. The Lin-Bairstow and Sturm solvers work on polynomials
    of arbitrary degree. The Sturm solver is the most robust solver but
    only reports roots within an interval and does not report
    multiplicities. The Lin-Bairstow solver reports multiplicities.
    
    For difficult polynomials, you may wish to use filter_roots to
    eliminate some of the roots reported by the Sturm solver. filter_roots
    evaluates the derivatives near each root to eliminate cases where a
    local minimum or maximum is close to zero.
    
    Thanks:
    
    Thanks to Philippe Pebay, Korben Rusek, David Thompson, and Maurice
    Rojas for implementing these solvers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolynomialSolversUnivariate, obj, update, **traits)
    
    division_tolerance = traits.Float(1e-08, enter_set=True, auto_set=False, help=\
        """
        Set/get the tolerance used when performing polynomial Euclidean
        division to find polynomial roots. This tolerance is used to
        decide whether the coefficient(s) of a polynomial remainder are
        close enough to zero to be neglected.
        """
    )
    def _division_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisionTolerance,
                        self.division_tolerance)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('division_tolerance', 'GetDivisionTolerance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'division_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolynomialSolversUnivariate, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['division_tolerance']),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

