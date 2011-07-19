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


class InitialValueProblemSolver(Object):
    """
    InitialValueProblemSolver - Integrate a set of ordinary
    
    Superclass: Object
    
    Given a FunctionSet which returns d_f_i(x_j, t)/dt given x_j and t,
    InitialValueProblemSolver computes the value of F_i at t+deltat.
    
    See Also:
    
    RungeKutta2 RungeKutta4
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInitialValueProblemSolver, obj, update, **traits)
    
    def _get_function_set(self):
        return wrap_vtk(self._vtk_obj.GetFunctionSet())
    def _set_function_set(self, arg):
        old_val = self._get_function_set()
        self._wrap_call(self._vtk_obj.SetFunctionSet,
                        deref_vtk(arg))
        self.trait_property_changed('function_set', old_val, arg)
    function_set = traits.Property(_get_function_set, _set_function_set, help=\
        """
        Set / get the dataset used for the implicit function evaluation.
        """
    )

    def is_adaptive(self):
        """
        V.is_adaptive() -> int
        C++: virtual int IsAdaptive()
        Returns 1 if the solver uses adaptive stepsize control, 0
        otherwise
        """
        ret = self._vtk_obj.IsAdaptive()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InitialValueProblemSolver, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

