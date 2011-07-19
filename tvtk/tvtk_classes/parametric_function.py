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


class ParametricFunction(Object):
    """
    ParametricFunction - abstract interface for parametric functions
    
    Superclass: Object
    
    ParametricFunction is an abstract interface for functions defined
    by parametric mapping i.e. f(u,v,w)->(x,y,z) where u_min <= u <
    u_max, v_min <= v < v_max, w_min <= w < w_max. (For notational
    convenience, we will write f(u)->x and assume that u means (u,v,w)
    and x means (x,y,z).)
    
    The interface contains the pure virtual function, Evaluate(), that
    generates a point and the derivatives at that point which are then
    used to construct the surface. A second pure virtual function,
    evaluate_scalar(), can be used to generate a scalar for the surface.
    Finally, the get_dimension() virtual function is used to differentiate
    1d, 2d, and 3d parametric functions. Since this abstract class
    defines a pure virtual API, its subclasses must implement the pure
    virtual functions get_dimension(), Evaluate() and evaluate_scalar().
    
    This class has also methods for defining a range of parametric values
    (u,v,w).
    
    Thanks:
    
    Andrew Maclean a.maclean@cas.edu.au for creating and contributing the
    class.
    
    See Also:
    
    ParametricFunctionSource - tessellates a parametric function
    
    Implementations of derived classes implementing non-orentable
    surfaces: ParametricBoy ParametricCrossCap
    ParametricFigure8Klein ParametricKlein ParametricMobius
    ParametricRoman
    
    Implementations of derived classes implementing orientable surfaces:
    ParametricConicSpiral ParametricDini ParametricEllipsoid
    ParametricEnneper ParametricRandomHills
    ParametricSuperEllipsoid ParametricSuperToroid
    ParametricTorus
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricFunction, obj, update, **traits)
    
    derivatives_available = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which determines whether derivatives are
        available from the parametric function (i.e., whether the
        Evaluate() method returns valid derivatives).
        """
    )
    def _derivatives_available_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDerivativesAvailable,
                        self.derivatives_available_)

    twist_u = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which joins the first triangle strip to the last
        one with a twist. join_u must also be set if this is set. Used
        when building some non-orientable surfaces.
        """
    )
    def _twist_u_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwistU,
                        self.twist_u_)

    twist_v = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which joins the ends of the triangle strips with
        a twist. join_v must also be set if this is set. Used when
        building some non-orientable surfaces.
        """
    )
    def _twist_v_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwistV,
                        self.twist_v_)

    join_u = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which joins the first triangle strip to the last
        one.
        """
    )
    def _join_u_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJoinU,
                        self.join_u_)

    join_v = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which joins the the ends of the triangle strips.
        """
    )
    def _join_v_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJoinV,
                        self.join_v_)

    clockwise_ordering = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag which determines the ordering of the the
        vertices forming the triangle strips. The ordering of the points
        being inserted into the triangle strip is important because it
        determines the direction of the normals for the lighting. If set,
        the ordering is clockwise, otherwise the ordering is
        anti-clockwise. Default is true (i.e. clockwise ordering).
        """
    )
    def _clockwise_ordering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClockwiseOrdering,
                        self.clockwise_ordering_)

    maximum_v = traits.Float(3.14159274101, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum v-value.
        """
    )
    def _maximum_v_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumV,
                        self.maximum_v)

    maximum_w = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum w-value.
        """
    )
    def _maximum_w_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumW,
                        self.maximum_w)

    minimum_v = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum v-value.
        """
    )
    def _minimum_v_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumV,
                        self.minimum_v)

    maximum_u = traits.Float(3.14159274101, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum u-value.
        """
    )
    def _maximum_u_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumU,
                        self.maximum_u)

    minimum_u = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum u-value.
        """
    )
    def _minimum_u_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumU,
                        self.minimum_u)

    minimum_w = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum w-value.
        """
    )
    def _minimum_w_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumW,
                        self.minimum_w)

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        
        """
    )

    def evaluate(self, *args):
        """
        V.evaluate([float, float, float], [float, float, float], [float,
            float, float, float, float, float, float, float, float])
        C++: virtual void Evaluate(double uvw[3], double Pt[3],
            double Duvw[9])
        Performs the mapping $f(uvw)->(Pt,Duvw)$f. This is a pure virtual
        function that must be instantiated in a derived class.
        
        uvw are the parameters, with u corresponding to uvw[0], v to
        uvw[1] and w to uvw[2] respectively. Pt is the returned Cartesian
        point, Duvw are the derivatives of this point with respect to u,
        v and w. Note that the first three values in Duvw are Du, the
        next three are Dv, and the final three are Dw. Du Dv Dw are the
        partial derivatives of the function at the point Pt with respect
        to u, v and w respectively.
        """
        ret = self._wrap_call(self._vtk_obj.Evaluate, *args)
        return ret

    def evaluate_scalar(self, *args):
        """
        V.evaluate_scalar([float, float, float], [float, float, float],
            [float, float, float, float, float, float, float, float,
            float]) -> float
        C++: virtual double EvaluateScalar(double uvw[3], double Pt[3],
            double Duvw[9])
        Calculate a user defined scalar using one or all of uvw, Pt,
        Duvw. This is a pure virtual function that must be instantiated
        in a derived class.
        
        uvw are the parameters with Pt being the the cartesian point,
        Duvw are the derivatives of this point with respect to u, v, and
        w. Pt, Duvw are obtained from Evaluate().
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateScalar, *args)
        return ret

    _updateable_traits_ = \
    (('clockwise_ordering', 'GetClockwiseOrdering'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('derivatives_available', 'GetDerivativesAvailable'),
    ('join_v', 'GetJoinV'), ('join_u', 'GetJoinU'), ('twist_v',
    'GetTwistV'), ('twist_u', 'GetTwistU'), ('minimum_u', 'GetMinimumU'),
    ('minimum_v', 'GetMinimumV'), ('minimum_w', 'GetMinimumW'),
    ('reference_count', 'GetReferenceCount'), ('maximum_v',
    'GetMaximumV'), ('maximum_w', 'GetMaximumW'), ('maximum_u',
    'GetMaximumU'))
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v', 'twist_u', 'twist_v',
    'maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
    'minimum_w'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clockwise_ordering', 'derivatives_available',
            'join_u', 'join_v', 'twist_u', 'twist_v'], [], ['maximum_u',
            'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w']),
            title='Edit ParametricFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

