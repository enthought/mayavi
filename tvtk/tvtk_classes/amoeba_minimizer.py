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


class AmoebaMinimizer(Object):
    """
    AmoebaMinimizer - nonlinear optimization with a simplex
    
    Superclass: Object
    
    AmoebaMinimizer will modify a set of parameters in order to find
    the minimum of a specified function.  The method used is commonly
    known as the amoeba method, it constructs an n-dimensional simplex in
    parameter space (i.e. a tetrahedron if the number or parameters is 3)
    and moves the vertices around parameter space until a local minimum
    is found.  The amoeba method is robust, reasonably efficient, but is
    not guaranteed to find the global minimum if several local minima
    exist.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAmoebaMinimizer, obj, update, **traits)
    
    def get_parameter_scale(self, *args):
        """
        V.get_parameter_scale(string) -> float
        C++: double GetParameterScale(const char *name)
        V.get_parameter_scale(int) -> float
        C++: double GetParameterScale(int i)
        Set the scale to use when modifying a parameter, i.e. the initial
        amount by which the parameter will be modified during the search
        for the minimum.  It is preferable to identify scalars by name
        rather than by number.
        """
        ret = self._wrap_call(self._vtk_obj.GetParameterScale, *args)
        return ret

    def set_parameter_scale(self, *args):
        """
        V.set_parameter_scale(string, float)
        C++: void SetParameterScale(const char *name, double scale)
        V.set_parameter_scale(int, float)
        C++: void SetParameterScale(int i, double scale)
        Set the scale to use when modifying a parameter, i.e. the initial
        amount by which the parameter will be modified during the search
        for the minimum.  It is preferable to identify scalars by name
        rather than by number.
        """
        ret = self._wrap_call(self._vtk_obj.SetParameterScale, *args)
        return ret

    def get_parameter_value(self, *args):
        """
        V.get_parameter_value(string) -> float
        C++: double GetParameterValue(const char *name)
        V.get_parameter_value(int) -> float
        C++: double GetParameterValue(int i)
        Get the value of a parameter at the current stage of the
        minimization. Call this method within the function that you are
        minimizing in order to get the current parameter values.  It is
        preferable to specify parameters by name rather than by index.
        """
        ret = self._wrap_call(self._vtk_obj.GetParameterValue, *args)
        return ret

    def set_parameter_value(self, *args):
        """
        V.set_parameter_value(string, float)
        C++: void SetParameterValue(const char *name, double value)
        V.set_parameter_value(int, float)
        C++: void SetParameterValue(int i, double value)
        Set the initial value for the specified parameter.  Calling this
        function for any parameter will reset the Iterations and the
        function_evaluations counts to zero.  You must also use
        set_parameter_scale() to specify the step size by which the
        parameter will be modified during the minimization.  It is
        preferable to specify parameters by name, rather than by number.
        """
        ret = self._wrap_call(self._vtk_obj.SetParameterValue, *args)
        return ret

    max_iterations = traits.Int(1000, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum number of iterations to try before giving up.
        """
    )
    def _max_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxIterations,
                        self.max_iterations)

    tolerance = traits.Float(0.0001, enter_set=True, auto_set=False, help=\
        """
        Specify the fractional tolerance to aim for during the
        minimization.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    function_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the function value resulting from the minimization.
        """
    )
    def _function_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunctionValue,
                        self.function_value)

    def _get_function_evaluations(self):
        return self._vtk_obj.GetFunctionEvaluations()
    function_evaluations = traits.Property(_get_function_evaluations, help=\
        """
        Return the number of times that the function has been evaluated.
        """
    )

    def _get_iterations(self):
        return self._vtk_obj.GetIterations()
    iterations = traits.Property(_get_iterations, help=\
        """
        Return the number of interations that have been performed.  This
        is not necessarily the same as the number of function
        evaluations.
        """
    )

    def _get_number_of_parameters(self):
        return self._vtk_obj.GetNumberOfParameters()
    number_of_parameters = traits.Property(_get_number_of_parameters, help=\
        """
        Get the number of parameters that have been set.
        """
    )

    def get_parameter_name(self, *args):
        """
        V.get_parameter_name(int) -> string
        C++: const char *GetParameterName(int i)
        For completeness, an unchecked method to get the name for
        particular parameter (the result will be NULL if no name was
        set).
        """
        ret = self._wrap_call(self._vtk_obj.GetParameterName, *args)
        return ret

    def evaluate_function(self):
        """
        V.evaluate_function()
        C++: void EvaluateFunction()
        Evaluate the function.  This is usually called internally by the
        minimization code, but it is provided here as a public method.
        """
        ret = self._vtk_obj.EvaluateFunction()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Initialize the minimizer.  This will reset the number of
        parameters to zero so that the minimizer can be reused.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def iterate(self):
        """
        V.iterate() -> int
        C++: virtual int Iterate()
        Perform one iteration of minimization.  Returns zero if the
        tolerance stopping criterion has been met.
        """
        ret = self._vtk_obj.Iterate()
        return ret
        

    def minimize(self):
        """
        V.minimize()
        C++: virtual void Minimize()
        Iterate until the minimum is found to within the specified
        tolerance, or until the max_iterations has been reached.
        """
        ret = self._vtk_obj.Minimize()
        return ret
        

    def set_function(self, *args):
        """
        V.set_function(function)
        C++: void SetFunction(void (*f)(void *) , void *arg)
        Specify the function to be minimized.  When this function is
        called, it must get the parameter values by calling
        get_parameter_value() for each parameter, and then must call
        set_function_value() to tell the minimizer what the result of the
        function evaluation was.  The number of function evaluations used
        for the minimization can be retrieved using
        get_function_evaluations().
        """
        ret = self._wrap_call(self._vtk_obj.SetFunction, *args)
        return ret

    _updateable_traits_ = \
    (('function_value', 'GetFunctionValue'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('tolerance',
    'GetTolerance'), ('max_iterations', 'GetMaxIterations'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'function_value',
    'max_iterations', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AmoebaMinimizer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AmoebaMinimizer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['function_value', 'max_iterations',
            'tolerance']),
            title='Edit AmoebaMinimizer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AmoebaMinimizer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

