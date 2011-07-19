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


class TransformInterpolator(Object):
    """
    TransformInterpolator - interpolate a series of transformation
    matrices
    
    Superclass: Object
    
    This class is used to interpolate a series of 4x4 transformation
    matrices. Position, scale and orientation (i.e., rotations) are
    interpolated separately, and can be interpolated linearly or with a
    spline function. Note that orientation is interpolated using
    quaternions via SLERP (spherical linear interpolation) or the special
    QuaternionSpline class.
    
    To use this class, specify at least two pairs of (t,transformation
    matrix) with the add_transform() method.  Then interpolated the
    transforms with the interpolate_transform(t,transform) method, where
    "t" must be in the range of (min,max) times specified by the
    add_transform() method.
    
    By default, spline interpolation is used for the interpolation of the
    transformation matrices. The position, scale and orientation of the
    matrices are interpolated with instances of the classes
    TupleInterpolator (position,scale) and QuaternionInterpolator
    (rotation). The user can override the interpolation behavior by
    gaining access to these separate interpolation classes.  These
    interpolator classes (vtk_tuple_interpolator and
    QuaternionInterpolator) can be modified to perform linear versus
    spline interpolation, and/or different spline basis functions can be
    specified.
    
    Caveats:
    
    The interpolator classes are initialized when the
    interpolate_transform() is called. Any changes to the interpolators,
    or additions to the list of transforms to be interpolated, causes a
    reinitialization of the interpolators the next time
    interpolate_transform() is invoked. Thus the best performance is
    obtained by 1) configuring the interpolators, 2) adding all the
    transforms, and 3) finally performing interpolation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformInterpolator, obj, update, **traits)
    
    interpolation_type = traits.Trait('spline',
    tvtk_base.TraitRevPrefixMap({'manual': 2, 'spline': 1, 'linear': 0}), help=\
        """
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the position, scale and orientation
        interpolators. Note that if the interpolation_type is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
    )
    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

    def _get_scale_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetScaleInterpolator())
    def _set_scale_interpolator(self, arg):
        old_val = self._get_scale_interpolator()
        self._wrap_call(self._vtk_obj.SetScaleInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('scale_interpolator', old_val, arg)
    scale_interpolator = traits.Property(_get_scale_interpolator, _set_scale_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the scale
        portion of the transformation matrix. Note that you can modify
        the behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances.
        """
    )

    def _get_rotation_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetRotationInterpolator())
    def _set_rotation_interpolator(self, arg):
        old_val = self._get_rotation_interpolator()
        self._wrap_call(self._vtk_obj.SetRotationInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('rotation_interpolator', old_val, arg)
    rotation_interpolator = traits.Property(_get_rotation_interpolator, _set_rotation_interpolator, help=\
        """
        Set/Get the tuple interpolator used to interpolate the
        orientation portion of the transformation matrix. Note that you
        can modify the behavior of the interpolator (linear vs spline
        interpolation; change spline basis) by manipulating the
        interpolator instances.
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
        portion of the transformation matrix. Note that you can modify
        the behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances.
        """
    )

    def _get_maximum_t(self):
        return self._vtk_obj.GetMaximumT()
    maximum_t = traits.Property(_get_maximum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned (corresponding to parameter t, usually thought
        of as time) are undefined if the list of transforms is empty.
        """
    )

    def _get_minimum_t(self):
        return self._vtk_obj.GetMinimumT()
    minimum_t = traits.Property(_get_minimum_t, help=\
        """
        Obtain some information about the interpolation range. The
        numbers returned (corresponding to parameter t, usually thought
        of as time) are undefined if the list of transforms is empty.
        """
    )

    def _get_number_of_transforms(self):
        return self._vtk_obj.GetNumberOfTransforms()
    number_of_transforms = traits.Property(_get_number_of_transforms, help=\
        """
        Return the number of transforms in the list of transforms.
        """
    )

    def add_transform(self, *args):
        """
        V.add_transform(float, Transform)
        C++: void AddTransform(double t, Transform *xform)
        V.add_transform(float, Matrix4x4)
        C++: void AddTransform(double t, Matrix4x4 *matrix)
        V.add_transform(float, Prop3D)
        C++: void AddTransform(double t, Prop3D *prop3D)
        Add another transform to the list of transformations defining the
        transform function. Note that using the same time t value more
        than once replaces the previous transform value at t. At least
        two transforms must be added to define a function. There are
        variants to this method depending on whether you are adding a
        Transform, Maxtirx4x4, and/or Prop3D.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddTransform, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Clear the list of transforms.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def interpolate_transform(self, *args):
        """
        V.interpolate_transform(float, Transform)
        C++: void InterpolateTransform(double t, Transform *xform)
        Interpolate the list of transforms and determine a new transform
        (i.e., fill in the transformation provided). If t is outside the
        range of (min,max) values, then t is clamped.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateTransform, *my_args)
        return ret

    def remove_transform(self, *args):
        """
        V.remove_transform(float)
        C++: void RemoveTransform(double t)
        Delete the transform at a particular parameter t. If there is no
        transform defined at location t, then the method does nothing.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveTransform, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('interpolation_type', 'GetInterpolationType'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interpolation_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['interpolation_type'], []),
            title='Edit TransformInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

