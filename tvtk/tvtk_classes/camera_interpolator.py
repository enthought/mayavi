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


class CameraInterpolator(Object):
    """
    CameraInterpolator - interpolate a series of cameras to update a
    new camera
    
    Superclass: Object
    
    This class is used to interpolate a series of cameras to update a
    specified camera. Either linear interpolation or spline interpolation
    may be used. The instance variables currently interpolated include
    position, focal point, view up, view angle, parallel scale, and
    clipping range.
    
    To use this class, specify the type of interpolation to use, and add
    a series of cameras at various times "t" to the list of cameras from
    which to interpolate. Then to interpolate in between cameras, simply
    invoke the function interpolate_camera(t,camera) where "camera" is the
    camera to be updated with interpolated values. Note that "t" should
    be in the range (min,max) times specified with the add_camera()
    method. If outside this range, the interpolation is clamped. This
    class copies the camera information (as compared to referencing the
    cameras) so you do not need to keep separate instances of the camera
    around for each camera added to the list of cameras to interpolate.
    
    Caveats:
    
    The interpolator classes are initialized the first time
    interpolate_camera() is called. Any later changes to the
    interpolators, or additions to the list of cameras to be
    interpolated, causes a reinitialization of the interpolators the next
    time interpolate_camera() is invoked. Thus the best performance is
    obtained by 1) configuring the interpolators, 2) adding all the
    cameras, and 3) finally performing interpolation.
    
    Currently position, focal point and view up are interpolated to
    define the orientation of the camera. Quaternion interpolation may be
    added in the future as an alternative interpolation method for camera
    orientation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCameraInterpolator, obj, update, **traits)
    
    interpolation_type = traits.Trait('spline',
    tvtk_base.TraitRevPrefixMap({'manual': 2, 'spline': 1, 'linear': 0}), help=\
        """
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the interpolation_type is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
    )
    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

    def _get_focal_point_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetFocalPointInterpolator())
    def _set_focal_point_interpolator(self, arg):
        old_val = self._get_focal_point_interpolator()
        self._wrap_call(self._vtk_obj.SetFocalPointInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('focal_point_interpolator', old_val, arg)
    focal_point_interpolator = traits.Property(_get_focal_point_interpolator, _set_focal_point_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the focal
        point portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
    )

    def _get_position_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetPositionInterpolator())
    def _set_position_interpolator(self, arg):
        old_val = self._get_position_interpolator()
        self._wrap_call(self._vtk_obj.SetPositionInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('position_interpolator', old_val, arg)
    position_interpolator = traits.Property(_get_position_interpolator, _set_position_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the position
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
    )

    def _get_view_up_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetViewUpInterpolator())
    def _set_view_up_interpolator(self, arg):
        old_val = self._get_view_up_interpolator()
        self._wrap_call(self._vtk_obj.SetViewUpInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('view_up_interpolator', old_val, arg)
    view_up_interpolator = traits.Property(_get_view_up_interpolator, _set_view_up_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the view up
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
    )

    def _get_clipping_range_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetClippingRangeInterpolator())
    def _set_clipping_range_interpolator(self, arg):
        old_val = self._get_clipping_range_interpolator()
        self._wrap_call(self._vtk_obj.SetClippingRangeInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('clipping_range_interpolator', old_val, arg)
    clipping_range_interpolator = traits.Property(_get_clipping_range_interpolator, _set_clipping_range_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the clipping
        range portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
    )

    def _get_view_angle_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetViewAngleInterpolator())
    def _set_view_angle_interpolator(self, arg):
        old_val = self._get_view_angle_interpolator()
        self._wrap_call(self._vtk_obj.SetViewAngleInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('view_angle_interpolator', old_val, arg)
    view_angle_interpolator = traits.Property(_get_view_angle_interpolator, _set_view_angle_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the view angle
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
    )

    def _get_parallel_scale_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetParallelScaleInterpolator())
    def _set_parallel_scale_interpolator(self, arg):
        old_val = self._get_parallel_scale_interpolator()
        self._wrap_call(self._vtk_obj.SetParallelScaleInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('parallel_scale_interpolator', old_val, arg)
    parallel_scale_interpolator = traits.Property(_get_parallel_scale_interpolator, _set_parallel_scale_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the parallel
        scale portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
    )

    def _get_maximum_t(self):
        return self._vtk_obj.GetMaximumT()
    maximum_t = traits.Property(_get_maximum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned are undefined if the list of cameras is empty.
        """
    )

    def _get_minimum_t(self):
        return self._vtk_obj.GetMinimumT()
    minimum_t = traits.Property(_get_minimum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned are undefined if the list of cameras is empty.
        """
    )

    def _get_number_of_cameras(self):
        return self._vtk_obj.GetNumberOfCameras()
    number_of_cameras = traits.Property(_get_number_of_cameras, help=\
        """
        Return the number of cameras in the list of cameras.
        """
    )

    def add_camera(self, *args):
        """
        V.add_camera(float, Camera)
        C++: void AddCamera(double t, Camera *camera)
        Add another camera to the list of cameras defining the camera
        function. Note that using the same time t value more than once
        replaces the previous camera value at t. At least one camera must
        be added to define a function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddCamera, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Clear the list of cameras.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def interpolate_camera(self, *args):
        """
        V.interpolate_camera(float, Camera)
        C++: void InterpolateCamera(double t, Camera *camera)
        Interpolate the list of cameras and determine a new camera (i.e.,
        fill in the camera provided). If t is outside the range of
        (min,max) values, then t is clamped to lie within this range.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateCamera, *my_args)
        return ret

    def remove_camera(self, *args):
        """
        V.remove_camera(float)
        C++: void RemoveCamera(double t)
        Delete the camera at a particular parameter t. If there is no
        camera defined at location t, then the method does nothing.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveCamera, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('interpolation_type', 'GetInterpolationType'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interpolation_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CameraInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CameraInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['interpolation_type'], []),
            title='Edit CameraInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CameraInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

