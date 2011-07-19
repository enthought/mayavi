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


class AbstractTransform(Object):
    """
    TransformConcatenationStack - Store a stack of concatenations.
    
    Superclass: Object
    
    A helper class (not derived from Object) to store a stack of
    concatenations.
    
    See Also:
    
    GeneralTransform WarpTransform HomogeneousTransform
    LinearTransform IdentityTransform TransformPolyDataFilter
    TransformFilter ImageReslice ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractTransform, obj, update, **traits)
    
    def _get_inverse(self):
        return wrap_vtk(self._vtk_obj.GetInverse())
    def _set_inverse(self, arg):
        old_val = self._get_inverse()
        self._wrap_call(self._vtk_obj.SetInverse,
                        deref_vtk(arg))
        self.trait_property_changed('inverse', old_val, arg)
    inverse = traits.Property(_get_inverse, _set_inverse, help=\
        """
        Get the inverse of this transform.  If you modify this transform,
        the returned inverse transform will automatically update.  If you
        want the inverse of a Transform, you might want to use
        get_linear_inverse() instead which will type cast the result from
        AbstractTransform to LinearTransform.
        """
    )

    def circuit_check(self, *args):
        """
        V.circuit_check(AbstractTransform) -> int
        C++: virtual int CircuitCheck(AbstractTransform *transform)
        Check for self-reference.  Will return true if concatenating with
        the specified transform, setting it to be our inverse, or setting
        it to be our input will create a circular reference. circuit_check
        is automatically called by set_input(), set_inverse(), and
        concatenate(vtk_x_transform *).  Avoid using this function, it is
        experimental.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CircuitCheck, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(AbstractTransform)
        C++: void DeepCopy(AbstractTransform *)
        Copy this transform from another of the same type.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def identity(self):
        """
        V.identity()
        C++: void Identity()
        @deprecated This method is deprecated in the base class.  It is
        still valid to use it on many of the specialized classes.
        """
        ret = self._vtk_obj.Identity()
        return ret
        

    def internal_transform_derivative(self, *args):
        """
        V.internal_transform_derivative((float, float, float), [float,
            float, float], [[float, float, float], [float, float, float],
            [float, float, float]])
        C++: virtual void InternalTransformDerivative(const double in[3],
            double out[3], double derivative[3][3])
        This will transform a point and, at the same time, calculate a
        3x3 Jacobian matrix that provides the partial derivatives of the
        transformation at that point.  This method does not call Update.
        Meant for use only within other VTK classes.
        """
        ret = self._wrap_call(self._vtk_obj.InternalTransformDerivative, *args)
        return ret

    def internal_transform_point(self, *args):
        """
        V.internal_transform_point((float, float, float), [float, float,
            float])
        C++: virtual void InternalTransformPoint(const double in[3],
            double out[3])
        This will calculate the transformation without calling Update.
        Meant for use only within other VTK classes.
        """
        ret = self._wrap_call(self._vtk_obj.InternalTransformPoint, *args)
        return ret

    def inverse(self):
        """
        V.inverse()
        C++: virtual void Inverse()
        Invert the transformation.
        """
        ret = self._vtk_obj.Inverse()
        return ret
        

    def make_transform(self):
        """
        V.make_transform() -> AbstractTransform
        C++: virtual AbstractTransform *MakeTransform()
        Make another transform of the same type.
        """
        ret = wrap_vtk(self._vtk_obj.MakeTransform())
        return ret
        

    def transform_double_normal_at_point(self, *args):
        """
        V.transform_double_normal_at_point((float, float, float), (float,
            float, float)) -> (float, float, float)
        C++: double *TransformDoubleNormalAtPoint(const double point[3],
            const double normal[3])
        Apply the transformation to a double-precision normal at the
        specified vertex.  If the transformation is a LinearTransform,
        you can use transform_double_normal() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformDoubleNormalAtPoint, *args)
        return ret

    def transform_double_point(self, *args):
        """
        V.transform_double_point(float, float, float) -> (float, float,
            float)
        C++: double *TransformDoublePoint(double x, double y, double z)
        V.transform_double_point((float, float, float)) -> (float, float,
            float)
        C++: double *TransformDoublePoint(const double point[3])
        Apply the transformation to a double-precision (x,y,z)
        coordinate. Use this if you are programming in Python, tcl or
        Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformDoublePoint, *args)
        return ret

    def transform_double_vector_at_point(self, *args):
        """
        V.transform_double_vector_at_point((float, float, float), (float,
            float, float)) -> (float, float, float)
        C++: double *TransformDoubleVectorAtPoint(const double point[3],
            const double vector[3])
        Apply the transformation to a double-precision vector at the
        specified vertex.  If the transformation is a LinearTransform,
        you can use transform_double_vector() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformDoubleVectorAtPoint, *args)
        return ret

    def transform_float_normal_at_point(self, *args):
        """
        V.transform_float_normal_at_point((float, float, float), (float,
            float, float)) -> (float, float, float)
        C++: float *TransformFloatNormalAtPoint(const float point[3],
            const float normal[3])
        Apply the transformation to a single-precision normal at the
        specified vertex.  If the transformation is a LinearTransform,
        you can use transform_float_normal() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformFloatNormalAtPoint, *args)
        return ret

    def transform_float_point(self, *args):
        """
        V.transform_float_point(float, float, float) -> (float, float,
            float)
        C++: float *TransformFloatPoint(float x, float y, float z)
        V.transform_float_point((float, float, float)) -> (float, float,
            float)
        C++: float *TransformFloatPoint(const float point[3])
        Apply the transformation to an (x,y,z) coordinate. Use this if
        you are programming in Python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformFloatPoint, *args)
        return ret

    def transform_float_vector_at_point(self, *args):
        """
        V.transform_float_vector_at_point((float, float, float), (float,
            float, float)) -> (float, float, float)
        C++: float *TransformFloatVectorAtPoint(const float point[3],
            const float vector[3])
        Apply the transformation to a single-precision vector at the
        specified vertex.  If the transformation is a LinearTransform,
        you can use transform_float_vector() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformFloatVectorAtPoint, *args)
        return ret

    def transform_normal_at_point(self, *args):
        """
        V.transform_normal_at_point((float, float, float), (float, float,
            float), [float, float, float])
        C++: void TransformNormalAtPoint(const double point[3],
            const double in[3], double out[3])
        V.transform_normal_at_point((float, float, float), (float, float,
            float)) -> (float, float, float)
        C++: double *TransformNormalAtPoint(const double point[3],
            const double normal[3])
        Apply the transformation to a normal at the specified vertex.  If
        the transformation is a LinearTransform, you can use
        transform_normal() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformNormalAtPoint, *args)
        return ret

    def transform_point(self, *args):
        """
        V.transform_point((float, float, float), [float, float, float])
        C++: void TransformPoint(const double in[3], double out[3])
        V.transform_point(float, float, float) -> (float, float, float)
        C++: double *TransformPoint(double x, double y, double z)
        V.transform_point((float, float, float)) -> (float, float, float)
        C++: double *TransformPoint(const double point[3])
        Apply the transformation to a double-precision coordinate. You
        can use the same array to store both the input and output point.
        """
        ret = self._wrap_call(self._vtk_obj.TransformPoint, *args)
        return ret

    def transform_points(self, *args):
        """
        V.transform_points(Points, Points)
        C++: virtual void TransformPoints(Points *inPts,
            Points *outPts)
        Apply the transformation to a series of points, and append the
        results to out_pts.
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.TransformPoints, *my_args)
        return ret

    def transform_points_normals_vectors(self, *args):
        """
        V.transform_points_normals_vectors(Points, Points,
            DataArray, DataArray, DataArray, DataArray)
        C++: virtual void TransformPointsNormalsVectors(Points *inPts,
            Points *outPts, DataArray *inNms, DataArray *outNms,
            DataArray *inVrs, DataArray *outVrs)
        Apply the transformation to a combination of points, normals and
        vectors.
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkPoints', 'vtkDataArray', 'vtkDataArray', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.TransformPointsNormalsVectors, *my_args)
        return ret

    def transform_vector_at_point(self, *args):
        """
        V.transform_vector_at_point((float, float, float), (float, float,
            float), [float, float, float])
        C++: void TransformVectorAtPoint(const double point[3],
            const double in[3], double out[3])
        V.transform_vector_at_point((float, float, float), (float, float,
            float)) -> (float, float, float)
        C++: double *TransformVectorAtPoint(const double point[3],
            const double vector[3])
        Apply the transformation to a vector at the specified vertex.  If
        the transformation is a LinearTransform, you can use
        transform_vector() instead.
        """
        ret = self._wrap_call(self._vtk_obj.TransformVectorAtPoint, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: void Update()
        Update the transform to account for any changes which have been
        made.  You do not have to call this method yourself, it is called
        automatically whenever the transform needs an update.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AbstractTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

