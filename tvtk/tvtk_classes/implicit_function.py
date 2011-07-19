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


class ImplicitFunction(Object):
    """
    ImplicitFunction - abstract interface for implicit functions
    
    Superclass: Object
    
    ImplicitFunction specifies an abstract interface for implicit
    functions. Implicit functions are real valued functions defined in 3d
    space, w = F(x,y,z). Two primitive operations are required: the
    ability to evaluate the function, and the function gradient at a
    given point. The implicit function divides space into three regions:
    on the surface (F(x,y,z)=w), outside of the surface (F(x,y,z)>c), and
    inside the surface (F(x,y,z)<c). (When c is zero, positive values are
    outside, negative values are inside, and zero is on the surface. Note
    also that the function gradient points from inside to outside.)
    
    Implicit functions are very powerful. It is possible to represent
    almost any type of geometry with the level sets w = const, especially
    if you use boolean combinations of implicit functions (see
    ImplicitBoolean).
    
    ImplicitFunction provides a mechanism to transform the implicit
    function(s) via a AbstractTransform.  This capability can be used
    to translate, orient, scale, or warp implicit functions.  For
    example, a sphere implicit function can be transformed into an
    oriented ellipse.
    
    Caveats:
    
    The transformation transforms a point into the space of the implicit
    function (i.e., the model space). Typically we want to transform the
    implicit model into world coordinates. In this case the inverse of
    the transformation is required.
    
    See Also:
    
    AbstractTransform Sphere Cylinder ImplicitBoolean
    Plane Planes Quadric ImplicitVolume SampleFunction
    Cutter ClipPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitFunction, obj, update, **traits)
    
    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set/Get a transformation to apply to input points before
        executing the implicit function.
        """
    )

    def evaluate_function(self, *args):
        """
        V.evaluate_function([float, float, float]) -> float
        C++: virtual double EvaluateFunction(double x[3])
        V.evaluate_function(float, float, float) -> float
        C++: double EvaluateFunction(double x, double y, double z)
        Evaluate function at position x-y-z and return value.  You should
        generally not call this method directly, you should use
        function_value() instead.  This method must be implemented by any
        derived class.
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateFunction, *args)
        return ret

    def evaluate_gradient(self, *args):
        """
        V.evaluate_gradient([float, float, float], [float, float, float])
        C++: virtual void EvaluateGradient(double x[3], double g[3])
        Evaluate function gradient at position x-y-z and pass back
        vector. You should generally not call this method directly, you
        should use function_gradient() instead.  This method must be
        implemented by any derived class.
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateGradient, *args)
        return ret

    def function_gradient(self, *args):
        """
        V.function_gradient((float, float, float), [float, float, float])
        C++: void FunctionGradient(const double x[3], double g[3])
        V.function_gradient((float, float, float)) -> (float, float, float)
        C++: double *FunctionGradient(const double x[3])
        V.function_gradient(float, float, float) -> (float, float, float)
        C++: double *FunctionGradient(double x, double y, double z)
        Evaluate function gradient at position x-y-z and pass back
        vector. Point x[3] is transformed through transform (if
        provided).
        """
        ret = self._wrap_call(self._vtk_obj.FunctionGradient, *args)
        return ret

    def function_value(self, *args):
        """
        V.function_value((float, float, float)) -> float
        C++: double FunctionValue(const double x[3])
        V.function_value(float, float, float) -> float
        C++: double FunctionValue(double x, double y, double z)
        Evaluate function at position x-y-z and return value. Point x[3]
        is transformed through transform (if provided).
        """
        ret = self._wrap_call(self._vtk_obj.FunctionValue, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

