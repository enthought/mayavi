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


class QuaternionInterpolator(Object):
    """
    QuaternionInterpolator - interpolate a quaternion
    
    Superclass: Object
    
    This class is used to interpolate a series of quaternions
    representing the rotations of a 3d object.  The interpolation may be
    linear in form (using spherical linear interpolation SLERP), or via
    spline interpolation (using SQUAD). In either case the interpolation
    is specialized to quaternions since the interpolation occurs on the
    surface of the unit quaternion sphere.
    
    To use this class, specify at least two pairs of (t,q[4]) with the
    add_quaternion() method.  Next interpolate the tuples with the
    interpolate_quaternion(t,q[_4]) method, where "t" must be in the range
    of (t_min,t_max) parameter values specified by the add_quaternion()
    method (t is clamped otherwise), and q[4] is filled in by the method.
    
    There are several important background references. Ken Shoemake
    described the practical application of quaternions for the
    interpolation of rotation (K. Shoemake, "Animating rotation with quaternion
    curves", Computer Graphics (Siggraph '85) 19(3):245--254, 1985).
    Another fine reference (available on-line) is E. B. Dam, M. Koch, and
    M. Lillholm, Technical Report DIKU-TR-98/5, Dept. of Computer
    Science, University of Copenhagen, Denmark.
    
    Caveats:
    
    Note that for two or less quaternions, Slerp (linear) interpolation
    is performed even if spline interpolation is requested. Also, the
    tangents to the first and last segments of spline interpolation are
    (arbitrarily) defined by repeating the first and last quaternions.
    
    There are several methods particular to quaternions (norms, products,
    etc.) implemented interior to this class. These may be moved to a
    separate quaternion class at some point.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuaternionInterpolator, obj, update, **traits)
    
    interpolation_type = traits.Trait('spline',
    tvtk_base.TraitRevPrefixMap({'spline': 1, 'linear': 0}), help=\
        """
        Specify which type of function to use for interpolation. By
        default (_set_interpolation_function_to_spline()), cubic spline
        interpolation using a modifed Kochanek basis is employed.
        Otherwise, if set_interpolation_function_to_linear() is invoked,
        linear spherical interpolation is used between each pair of
        quaternions.
        """
    )
    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

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

    def _get_number_of_quaternions(self):
        return self._vtk_obj.GetNumberOfQuaternions()
    number_of_quaternions = traits.Property(_get_number_of_quaternions, help=\
        """
        Return the number of quaternions in the list of quaternions to be
        interpolated.
        """
    )

    def add_quaternion(self, *args):
        """
        V.add_quaternion(float, [float, float, float, float])
        C++: void AddQuaternion(double t, double q[4])
        Add another quaternion to the list of quaternions to be
        interpolated. Note that using the same time t value more than
        once replaces the previous quaternion at t.  At least one
        quaternions must be added to define an interpolation functios.
        """
        ret = self._wrap_call(self._vtk_obj.AddQuaternion, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Reset the class so that it contains no data; i.e., the array of
        (t,q[4]) information is discarded.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def interpolate_quaternion(self, *args):
        """
        V.interpolate_quaternion(float, [float, float, float, float])
        C++: void InterpolateQuaternion(double t, double q[4])
        Interpolate the list of quaternions and determine a new
        quaternion (i.e., fill in the quaternion provided). If t is
        outside the range of (min,max) values, then t is clamped to lie
        within the range.
        """
        ret = self._wrap_call(self._vtk_obj.InterpolateQuaternion, *args)
        return ret

    def remove_quaternion(self, *args):
        """
        V.remove_quaternion(float)
        C++: void RemoveQuaternion(double t)
        Delete the quaternion at a particular parameter t. If there is no
        quaternion tuple defined at t, then the method does nothing.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveQuaternion, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('interpolation_type', 'GetInterpolationType'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interpolation_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuaternionInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuaternionInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['interpolation_type'], []),
            title='Edit QuaternionInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuaternionInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

