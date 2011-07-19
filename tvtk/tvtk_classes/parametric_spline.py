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

from tvtk.tvtk_classes.parametric_function import ParametricFunction


class ParametricSpline(ParametricFunction):
    """
    ParametricSpline - parametric function for 1d interpolating splines
    
    Superclass: ParametricFunction
    
    ParametricSpline is a parametric function for 1d interpolating
    splines. ParametricSpline maps the single parameter u into a 3d
    point (x,y,z) using three instances of interpolating splines.  This
    family of 1d splines is quaranteed to be parameterized in the
    interval [0,1].  Attempting to evaluate outside this interval will
    cause the parameter u to be clamped in the range [0,1].
    
    When constructed, this class creates instances of CardinalSpline
    for each of the x-y-z coordinates. The user may choose to replace
    these with their own instances of subclasses of Spline.
    
    Caveats:
    
    If you wish to tessellate the spline, use the class
    ParametricFunctionSource.
    
    See Also:
    
    Spline KochanekSpline CardinalSpline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricSpline, obj, update, **traits)
    
    parameterize_by_length = tvtk_base.true_bool_trait(help=\
        """
        Control whether the spline is parameterized by length or by point
        index. Default is by length.
        """
    )
    def _parameterize_by_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParameterizeByLength,
                        self.parameterize_by_length_)

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

    def _get_y_spline(self):
        return wrap_vtk(self._vtk_obj.GetYSpline())
    def _set_y_spline(self, arg):
        old_val = self._get_y_spline()
        self._wrap_call(self._vtk_obj.SetYSpline,
                        deref_vtk(arg))
        self.trait_property_changed('y_spline', old_val, arg)
    y_spline = traits.Property(_get_y_spline, _set_y_spline, help=\
        """
        By default, this class is constructed with three instances of
        CardinalSpline (for each of the x-y-z coordinate axes). The
        user may choose to create and assign their own instances of
        Spline.
        """
    )

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

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Specify the list of points defining the spline. Do this by
        specifying a Points array containing the points. Note that the
        order of the points in Points is the order that the splines
        will be fit.
        """
    )

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

    def _get_x_spline(self):
        return wrap_vtk(self._vtk_obj.GetXSpline())
    def _set_x_spline(self, arg):
        old_val = self._get_x_spline()
        self._wrap_call(self._vtk_obj.SetXSpline,
                        deref_vtk(arg))
        self.trait_property_changed('x_spline', old_val, arg)
    x_spline = traits.Property(_get_x_spline, _set_x_spline, help=\
        """
        By default, this class is constructed with three instances of
        CardinalSpline (for each of the x-y-z coordinate axes). The
        user may choose to create and assign their own instances of
        Spline.
        """
    )

    def _get_z_spline(self):
        return wrap_vtk(self._vtk_obj.GetZSpline())
    def _set_z_spline(self, arg):
        old_val = self._get_z_spline()
        self._wrap_call(self._vtk_obj.SetZSpline,
                        deref_vtk(arg))
        self.trait_property_changed('z_spline', old_val, arg)
    z_spline = traits.Property(_get_z_spline, _set_z_spline, help=\
        """
        By default, this class is constructed with three instances of
        CardinalSpline (for each of the x-y-z coordinate axes). The
        user may choose to create and assign their own instances of
        Spline.
        """
    )

    right_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The values of the derivative on the left and right sides. The
        value is used only if the left(right) constraint is type 1-3.
        """
    )
    def _right_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightValue,
                        self.right_value)

    def set_number_of_points(self, *args):
        """
        V.set_number_of_points(int)
        C++: void SetNumberOfPoints(IdType numPts)
        Another API to set the points. Set the number of points and then
        set the individual point coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfPoints, *args)
        return ret

    def set_point(self, *args):
        """
        V.set_point(int, float, float, float)
        C++: void SetPoint(IdType index, double x, double y, double z)
        Another API to set the points. Set the number of points and then
        set the individual point coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint, *args)
        return ret

    _updateable_traits_ = \
    (('closed', 'GetClosed'), ('clockwise_ordering',
    'GetClockwiseOrdering'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('parameterize_by_length',
    'GetParameterizeByLength'), ('debug', 'GetDebug'), ('left_value',
    'GetLeftValue'), ('left_constraint', 'GetLeftConstraint'), ('join_v',
    'GetJoinV'), ('join_u', 'GetJoinU'), ('derivatives_available',
    'GetDerivativesAvailable'), ('twist_v', 'GetTwistV'), ('twist_u',
    'GetTwistU'), ('right_constraint', 'GetRightConstraint'),
    ('minimum_u', 'GetMinimumU'), ('minimum_v', 'GetMinimumV'),
    ('minimum_w', 'GetMinimumW'), ('reference_count',
    'GetReferenceCount'), ('right_value', 'GetRightValue'), ('maximum_v',
    'GetMaximumV'), ('maximum_w', 'GetMaximumW'), ('maximum_u',
    'GetMaximumU'))
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'closed', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v',
    'parameterize_by_length', 'twist_u', 'twist_v', 'left_constraint',
    'left_value', 'maximum_u', 'maximum_v', 'maximum_w', 'minimum_u',
    'minimum_v', 'minimum_w', 'right_constraint', 'right_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricSpline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clockwise_ordering', 'closed',
            'derivatives_available', 'join_u', 'join_v', 'parameterize_by_length',
            'twist_u', 'twist_v'], [], ['left_constraint', 'left_value',
            'maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
            'minimum_w', 'right_constraint', 'right_value']),
            title='Edit ParametricSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

