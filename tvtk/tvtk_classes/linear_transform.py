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

from tvtk.tvtk_classes.homogeneous_transform import HomogeneousTransform


class LinearTransform(HomogeneousTransform):
    """
    LinearTransform - abstract superclass for linear transformations
    
    Superclass: HomogeneousTransform
    
    LinearTransform provides a generic interface for linear (affine or
    12 degree-of-freedom) geometric transformations.
    
    See Also:
    
    Transform IdentityTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLinearTransform, obj, update, **traits)
    
    def _get_linear_inverse(self):
        return wrap_vtk(self._vtk_obj.GetLinearInverse())
    linear_inverse = traits.Property(_get_linear_inverse, help=\
        """
        Just like get_inverse, but it includes a typecast to
        LinearTransform.
        """
    )

    def internal_transform_normal(self, *args):
        """
        V.internal_transform_normal((float, float, float), [float, float,
            float])
        C++: virtual void InternalTransformNormal(const double in[3],
            double out[3])
        This will calculate the transformation without calling Update.
        Meant for use only within other VTK classes.
        """
        ret = self._wrap_call(self._vtk_obj.InternalTransformNormal, *args)
        return ret

    def internal_transform_vector(self, *args):
        """
        V.internal_transform_vector((float, float, float), [float, float,
            float])
        C++: virtual void InternalTransformVector(const double in[3],
            double out[3])
        This will calculate the transformation without calling Update.
        Meant for use only within other VTK classes.
        """
        ret = self._wrap_call(self._vtk_obj.InternalTransformVector, *args)
        return ret

    def transform_double_normal(self, *args):
        """
        V.transform_double_normal(float, float, float) -> (float, float,
            float)
        C++: double *TransformDoubleNormal(double x, double y, double z)
        V.transform_double_normal((float, float, float)) -> (float, float,
            float)
        C++: double *TransformDoubleNormal(const double normal[3])
        Apply the transformation to a double-precision (x,y,z) normal.
        Use this if you are programming in python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformDoubleNormal, *args)
        return ret

    def transform_double_vector(self, *args):
        """
        V.transform_double_vector(float, float, float) -> (float, float,
            float)
        C++: double *TransformDoubleVector(double x, double y, double z)
        V.transform_double_vector((float, float, float)) -> (float, float,
            float)
        C++: double *TransformDoubleVector(const double vec[3])
        Apply the transformation to a double-precision (x,y,z) vector.
        Use this if you are programming in python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformDoubleVector, *args)
        return ret

    def transform_float_normal(self, *args):
        """
        V.transform_float_normal(float, float, float) -> (float, float,
            float)
        C++: float *TransformFloatNormal(float x, float y, float z)
        V.transform_float_normal((float, float, float)) -> (float, float,
            float)
        C++: float *TransformFloatNormal(const float normal[3])
        Apply the transformation to an (x,y,z) normal. Use this if you
        are programming in python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformFloatNormal, *args)
        return ret

    def transform_float_vector(self, *args):
        """
        V.transform_float_vector(float, float, float) -> (float, float,
            float)
        C++: float *TransformFloatVector(float x, float y, float z)
        V.transform_float_vector((float, float, float)) -> (float, float,
            float)
        C++: float *TransformFloatVector(const float vec[3])
        Apply the transformation to an (x,y,z) vector. Use this if you
        are programming in python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformFloatVector, *args)
        return ret

    def transform_normal(self, *args):
        """
        V.transform_normal((float, float, float), [float, float, float])
        C++: void TransformNormal(const double in[3], double out[3])
        V.transform_normal(float, float, float) -> (float, float, float)
        C++: double *TransformNormal(double x, double y, double z)
        V.transform_normal((float, float, float)) -> (float, float, float)
        C++: double *TransformNormal(const double normal[3])
        Apply the transformation to a double-precision normal. You can
        use the same array to store both the input and output.
        """
        ret = self._wrap_call(self._vtk_obj.TransformNormal, *args)
        return ret

    def transform_normals(self, *args):
        """
        V.transform_normals(DataArray, DataArray)
        C++: virtual void TransformNormals(DataArray *inNms,
            DataArray *outNms)
        Apply the transformation to a series of normals, and append the
        results to out_nms.
        """
        my_args = deref_array(args, [('vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.TransformNormals, *my_args)
        return ret

    def transform_vector(self, *args):
        """
        V.transform_vector(float, float, float) -> (float, float, float)
        C++: double *TransformVector(double x, double y, double z)
        V.transform_vector((float, float, float)) -> (float, float, float)
        C++: double *TransformVector(const double normal[3])
        V.transform_vector((float, float, float), [float, float, float])
        C++: void TransformVector(const double in[3], double out[3])
        Synonymous with transform_double_vector(x,y,z). Use this if you are
        programming in python, tcl or Java.
        """
        ret = self._wrap_call(self._vtk_obj.TransformVector, *args)
        return ret

    def transform_vectors(self, *args):
        """
        V.transform_vectors(DataArray, DataArray)
        C++: virtual void TransformVectors(DataArray *inVrs,
            DataArray *outVrs)
        Apply the transformation to a series of vectors, and append the
        results to out_vrs.
        """
        my_args = deref_array(args, [('vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.TransformVectors, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LinearTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LinearTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit LinearTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LinearTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

