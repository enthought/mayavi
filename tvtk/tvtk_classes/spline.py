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


class Spline(Object):
    """
    Spline - spline abstract class for interpolating splines
    
    Superclass: Object
    
    Spline interpolates a set of data points (i.e., interpolation
    means that the spline passes through the points).  Spline is an
    abstract class: its subclasses CardinalSpline and
    KochenekSpline do the interpolation. Note that this spline maps
    the 1d parametric coordinate t into a single value x. Thus if you
    want to use the spline to interpolate points (i.e. x[3]), you have to
    create three splines for each of the x-y-z coordinates. Fortunately,
    the ParametricSpline class does this for you.
    
    Typically a spline is used by adding a sequence of parametric
    coordinate / data (t,x) values followed by use of an evaluation
    function (e.g., CardinalSpline::Evaluate()).  Since these splines
    are 1d, a point in this context is an independent / dependent
    variable pair.
    
    Splines can also be set up to be closed or open. Closed splines
    continue from the last point to the first point with continuous
    function and derivative values. (You don't need to duplicate the
    first point to close the spline, just set closed_on.)
    
    This implementation of splines does not use a normalized parametric
    coordinate. If the spline is open, then the parameter space is (t_min
    <= t <= t_max) where t_min and t_max are the minimum and maximum
    parametric values seen when performing add_point(). If the spline is
    closed, then the parameter space is (t_min <= t <= (t_max+_1)) where
    t_min and t_max are the minimum and maximum parametric values seen when
    performing add_point(). Note, however, that this behavior can be
    changed by explicitly setting the parametric_range(t_min,t_max). If set,
    the parameter space remains (t_min <= t <= t_max), except that
    additions of data with parametric values outside this range are
    clamped within this range.
    
    See Also:
    
    CardinalSpline KochenekSpline ParametricSpline
    ParametricFunctionSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpline, obj, update, **traits)
    
    closed = tvtk_base.false_bool_trait(help=\
        """
        Control whether the spline is open or closed. A closed spline
        forms a continuous loop: the first and last points are the same,
        and derivatives are continuous.
        """
    )
    def _closed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosed,
                        self.closed_)

    clamp_value = tvtk_base.false_bool_trait(help=\
        """
        Set/Get clamp_value. If On, results of the interpolation will be
        clamped to the min/max of the input data.
        """
    )
    def _clamp_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClampValue,
                        self.clamp_value_)

    right_constraint = traits.Trait(1, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        Set the type of constraint of the left(right) end points. Four
        constraints are available:
        
        0: the first derivative at left(right) most point is determined
        from the line defined from the first(last) two points.
        
        1: the first derivative at left(right) most point is set to
        Left(Right)Value.
        
        2: the second derivative at left(right) most point is set to
        Left(Right)Value.
        
        3: the second derivative at left(right)most points is
        Left(Right)Value times second derivative at first interior point.
        """
    )
    def _right_constraint_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightConstraint,
                        self.right_constraint)

    def get_parametric_range(self, *args):
        """
        V.get_parametric_range([float, float])
        C++: void GetParametricRange(double tRange[2])
        Set/Get the parametric range. If not set, the range is determined
        implicitly by keeping track of the (min,max) parameter values for
        t. If set, the add_point() method will clamp the t value to lie
        within the specified range.
        """
        ret = self._wrap_call(self._vtk_obj.GetParametricRange, *args)
        return ret

    def set_parametric_range(self, *args):
        """
        V.set_parametric_range(float, float)
        C++: void SetParametricRange(double tMin, double tMax)
        V.set_parametric_range([float, float])
        C++: void SetParametricRange(double tRange[2])
        Set/Get the parametric range. If not set, the range is determined
        implicitly by keeping track of the (min,max) parameter values for
        t. If set, the add_point() method will clamp the t value to lie
        within the specified range.
        """
        ret = self._wrap_call(self._vtk_obj.SetParametricRange, *args)
        return ret

    left_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The values of the derivative on the left and right sides. The
        value is used only if the left(right) constraint is type 1-3.
        """
    )
    def _left_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftValue,
                        self.left_value)

    left_constraint = traits.Trait(1, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        Set the type of constraint of the left(right) end points. Four
        constraints are available:
        
        0: the first derivative at left(right) most point is determined
        from the line defined from the first(last) two points.
        
        1: the first derivative at left(right) most point is set to
        Left(Right)Value.
        
        2: the second derivative at left(right) most point is set to
        Left(Right)Value.
        
        3: the second derivative at left(right)most points is
        Left(Right)Value times second derivative at first interior point.
        """
    )
    def _left_constraint_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftConstraint,
                        self.left_constraint)

    right_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The values of the derivative on the left and right sides. The
        value is used only if the left(right) constraint is type 1-3.
        """
    )
    def _right_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightValue,
                        self.right_value)

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of points inserted thus far.
        """
    )

    def add_point(self, *args):
        """
        V.add_point(float, float)
        C++: void AddPoint(double t, double x)
        Add a pair of points to be fit with the spline.
        """
        ret = self._wrap_call(self._vtk_obj.AddPoint, *args)
        return ret

    def compute(self):
        """
        V.compute()
        C++: virtual void Compute()
        Compute the coefficients for the spline.
        """
        ret = self._vtk_obj.Compute()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(Spline)
        C++: virtual void DeepCopy(Spline *s)
        Deep copy of spline data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def evaluate(self, *args):
        """
        V.evaluate(float) -> float
        C++: virtual double Evaluate(double t)
        Interpolate the value of the spline at parametric location of t.
        """
        ret = self._wrap_call(self._vtk_obj.Evaluate, *args)
        return ret

    def remove_all_points(self):
        """
        V.remove_all_points()
        C++: void RemoveAllPoints()
        Remove all points from the data.
        """
        ret = self._vtk_obj.RemoveAllPoints()
        return ret
        

    def remove_point(self, *args):
        """
        V.remove_point(float)
        C++: void RemovePoint(double t)
        Remove a point from the data to be fit with the spline.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('left_value',
    'GetLeftValue'), ('left_constraint', 'GetLeftConstraint'),
    ('clamp_value', 'GetClampValue'), ('debug', 'GetDebug'),
    ('right_constraint', 'GetRightConstraint'), ('closed', 'GetClosed'),
    ('reference_count', 'GetReferenceCount'), ('right_value',
    'GetRightValue'))
    
    _full_traitnames_list_ = \
    (['clamp_value', 'closed', 'debug', 'global_warning_display',
    'left_constraint', 'left_value', 'right_constraint', 'right_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Spline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Spline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamp_value', 'closed'], [], ['left_constraint',
            'left_value', 'right_constraint', 'right_value']),
            title='Edit Spline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Spline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

