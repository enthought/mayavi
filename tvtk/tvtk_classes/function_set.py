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


class FunctionSet(Object):
    """
    FunctionSet - Abstract interface for sets of functions
    
    Superclass: Object
    
    FunctionSet specifies an abstract interface for set of functions
    of the form F_i = F_i(x_j) where F (with i=1..m) are the functions
    and x (with j=1..n) are the independent variables. The only supported
    operation is the  function evaluation at x_j.
    
    See Also:
    
    ImplicitDataSet InterpolatedVelocityField
    InitialValueProblemSolver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFunctionSet, obj, update, **traits)
    
    def _get_number_of_functions(self):
        return self._vtk_obj.GetNumberOfFunctions()
    number_of_functions = traits.Property(_get_number_of_functions, help=\
        """
        Return the number of functions. Note that this is constant for a
        given type of set of functions and can not be changed at run
        time.
        """
    )

    def _get_number_of_independent_variables(self):
        return self._vtk_obj.GetNumberOfIndependentVariables()
    number_of_independent_variables = traits.Property(_get_number_of_independent_variables, help=\
        """
        Return the number of independent variables. Note that this is
        constant for a given type of set of functions and can not be
        changed at run time.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FunctionSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

