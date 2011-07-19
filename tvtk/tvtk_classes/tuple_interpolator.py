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


class TupleInterpolator(Object):
    """
    TupleInterpolator - interpolate a tuple of arbitray size
    
    Superclass: Object
    
    This class is used to interpolate a tuple which may have an arbitrary
    number of components (but at least one component). The interpolation
    may be linear in form, or via a subclasses of Spline.
    
    To use this class, begin by specifying the number of components of
    the tuple and the interpolation function to use. Then specify at
    least one pair of (t,tuple) with the add_tuple() method.  Next
    interpolate the tuples with the interpolate_tuple(t,tuple) method,
    where "t" must be in the range of (t_min,t_max) parameter values
    specified by the add_tuple() method (if not then t is clamped), and
    tuple[] is filled in by the method (make sure that tuple [] is long
    enough to hold the interpolated data).
    
    You can control the type of interpolation to use. By default, the
    interpolation is based on a Kochanek spline. However, other types of
    splines can be specified. You can also set the interpolation method
    to linear, in which case the specified spline has no effect on the
    interpolation.
    
    Caveats:
    
    Setting the number of components or changing the type of
    interpolation causes the list of tuples to be reset, so any data
    inserted up to that point is lost. Bisection methods are used to
    speed up the search for the interpolation interval.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTupleInterpolator, obj, update, **traits)
    
    interpolation_type = traits.Trait('spline',
    tvtk_base.TraitRevPrefixMap({'spline': 1, 'linear': 0}), help=\
        """
        Specify which type of function to use for interpolation. By
        default spline interpolation (_set_interpolation_function_to_spline())
        is used (i.e., a Kochanek spline) and the interpolating_spline
        instance variable is used to birth the actual interpolation
        splines via a combination of new_instance() and deep_copy(). You
        may also choose to use linear interpolation by invoking
        set_interpolation_function_to_linear(). Note that changing the type
        of interpolation causes previously inserted data to be discarded.
        """
    )
    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

    def _get_interpolating_spline(self):
        return wrap_vtk(self._vtk_obj.GetInterpolatingSpline())
    def _set_interpolating_spline(self, arg):
        old_val = self._get_interpolating_spline()
        self._wrap_call(self._vtk_obj.SetInterpolatingSpline,
                        deref_vtk(arg))
        self.trait_property_changed('interpolating_spline', old_val, arg)
    interpolating_spline = traits.Property(_get_interpolating_spline, _set_interpolating_spline, help=\
        """
        If the interpolation_type is set to spline, then this method
        applies. By default Kochanek interpolation is used, but you can
        specify any instance of Spline to use. Note that the actual
        interpolating splines are created by invoking new_instance()
        followed by deep_copy() on the interpolating spline specified
        here, for each tuple component to interpolate.
        """
    )

    number_of_components = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of tuple components to interpolate. Note that
        setting this value discards any previously inserted data.
        """
    )
    def _number_of_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfComponents,
                        self.number_of_components)

    def _get_maximum_t(self):
        return self._vtk_obj.GetMaximumT()
    maximum_t = traits.Property(_get_maximum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned (corresponding to parameter t, usually thought
        of as time) are undefined if the list of transforms is empty.
        This is a convenience method for interpolation.
        """
    )

    def _get_minimum_t(self):
        return self._vtk_obj.GetMinimumT()
    minimum_t = traits.Property(_get_minimum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned (corresponding to parameter t, usually thought
        of as time) are undefined if the list of transforms is empty.
        This is a convenience method for interpolation.
        """
    )

    def _get_number_of_tuples(self):
        return self._vtk_obj.GetNumberOfTuples()
    number_of_tuples = traits.Property(_get_number_of_tuples, help=\
        """
        Return the number of tuples in the list of tuples to be
        interpolated.
        """
    )

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Reset the class so that it contains no (t,tuple) information.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def remove_tuple(self, *args):
        """
        V.remove_tuple(float)
        C++: void RemoveTuple(double t)
        Delete the tuple at a particular parameter t. If there is no
        tuple defined at t, then the method does nothing.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveTuple, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('interpolation_type', 'GetInterpolationType'),
    ('number_of_components', 'GetNumberOfComponents'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interpolation_type',
    'number_of_components'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TupleInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TupleInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['interpolation_type'], ['number_of_components']),
            title='Edit TupleInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TupleInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

