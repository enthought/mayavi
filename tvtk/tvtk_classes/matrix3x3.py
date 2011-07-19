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


class Matrix3x3(Object):
    """
    Matrix3x3 - represent and manipulate 3x3 transformation matrices
    
    Superclass: Object
    
    Matrix3x3 is a class to represent and manipulate 3x3 matrices.
    Specifically, it is designed to work on 3x3 transformation matrices
    found in 2d rendering using homogeneous coordinates [x y w].
    
    See Also:
    
    Transform2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMatrix3x3, obj, update, **traits)
    
    def get_element(self, *args):
        """
        V.get_element(int, int) -> float
        C++: double GetElement(int i, int j)
        Returns the element i,j from the matrix.
        """
        ret = self._wrap_call(self._vtk_obj.GetElement, *args)
        return ret

    def set_element(self, *args):
        """
        V.set_element(int, int, float)
        C++: void SetElement(int i, int j, double value)
        Sets the element i,j in the matrix.
        """
        ret = self._wrap_call(self._vtk_obj.SetElement, *args)
        return ret

    def adjoint(self, *args):
        """
        V.adjoint(Matrix3x3, Matrix3x3)
        C++: void Adjoint(Matrix3x3 *in, Matrix3x3 *out)
        V.adjoint((float, float, float, float, float, float, float, float,
             float), [float, float, float, float, float, float, float,
            float, float])
        C++: static void Adjoint(const double inElements[9],
            double outElements[9])
        Compute adjoint of the matrix and put it into out.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Adjoint, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Matrix3x3)
        C++: void DeepCopy(Matrix3x3 *source)
        V.deep_copy([float, float, float, float, float, float, float,
            float, float], Matrix3x3)
        C++: static void DeepCopy(double Elements[9],
            Matrix3x3 *source)
        V.deep_copy([float, float, float, float, float, float, float,
            float, float], (float, float, float, float, float, float,
            float, float, float))
        C++: static void DeepCopy(double Elements[9],
            const double newElements[9])
        V.deep_copy((float, float, float, float, float, float, float,
            float, float))
        C++: void DeepCopy(const double Elements[9])
        Set the elements of the matrix to the same values as the elements
        of the source Matrix.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def determinant(self, *args):
        """
        V.determinant() -> float
        C++: double Determinant()
        V.determinant((float, float, float, float, float, float, float,
            float, float)) -> float
        C++: static double Determinant(const double Elements[9])
        V.determinant(Matrix3x3) -> float
        C++: double Determinant(Matrix3x3 *in)
        Compute the determinant of the matrix and return it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Determinant, *my_args)
        return ret

    def identity(self, *args):
        """
        V.identity()
        C++: void Identity()
        V.identity([float, float, float, float, float, float, float,
            float, float])
        C++: static void Identity(double Elements[9])
        Set equal to Identity matrix
        """
        ret = self._wrap_call(self._vtk_obj.Identity, *args)
        return ret

    def invert(self, *args):
        """
        V.invert(Matrix3x3, Matrix3x3)
        C++: static void Invert(Matrix3x3 *in, Matrix3x3 *out)
        V.invert()
        C++: void Invert()
        V.invert((float, float, float, float, float, float, float, float,
            float), [float, float, float, float, float, float, float,
            float, float])
        C++: static void Invert(const double inElements[9],
            double outElements[9])
        Matrix Inversion (adapted from Richard Carling in "Graphics
        Gems," Academic Press, 1990).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Invert, *my_args)
        return ret

    def is_identity(self):
        """
        V.is_identity() -> bool
        C++: bool IsIdentity()"""
        ret = self._vtk_obj.IsIdentity()
        return ret
        

    def multiply3x3(self, *args):
        """
        V.multiply3x3(Matrix3x3, Matrix3x3, Matrix3x3)
        C++: static void Multiply3x3(Matrix3x3 *a, Matrix3x3 *b,
            Matrix3x3 *c)
        V.multiply3x3((float, float, float, float, float, float, float,
            float, float), (float, float, float, float, float, float,
            float, float, float), [float, float, float, float, float,
            float, float, float, float])
        C++: static void Multiply3x3(const double a[9], const double b[9],
             double c[9])
        Multiplies matrices a and b and stores the result in c (c=a*b).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Multiply3x3, *my_args)
        return ret

    def multiply_point(self, *args):
        """
        V.multiply_point((float, float, float), [float, float, float])
        C++: void MultiplyPoint(const double in[3], double out[3])
        V.multiply_point((float, float, float, float, float, float, float,
            float, float), (float, float, float), [float, float, float])
        C++: static void MultiplyPoint(const double Elements[9],
            const double in[3], double out[3])
        Multiply a homogeneous coordinate by this matrix, i.e. out =
        A*in. The in[3] and out[3] can be the same array.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyPoint, *args)
        return ret

    def point_multiply(self, *args):
        """
        V.point_multiply((float, float, float, float, float, float, float,
            float, float), (float, float, float), [float, float, float])
        C++: static void PointMultiply(const double Elements[9],
            const double in[3], double out[3])"""
        ret = self._wrap_call(self._vtk_obj.PointMultiply, *args)
        return ret

    def transpose(self, *args):
        """
        V.transpose(Matrix3x3, Matrix3x3)
        C++: static void Transpose(Matrix3x3 *in, Matrix3x3 *out)
        V.transpose()
        C++: void Transpose()
        V.transpose((float, float, float, float, float, float, float,
            float, float), [float, float, float, float, float, float,
            float, float, float])
        C++: static void Transpose(const double inElements[9],
            double outElements[9])
        Transpose the matrix and put it into out.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Transpose, *my_args)
        return ret

    def zero(self, *args):
        """
        V.zero()
        C++: void Zero()
        V.zero([float, float, float, float, float, float, float, float,
            float])
        C++: static void Zero(double Elements[9])
        Set all of the elements to zero.
        """
        ret = self._wrap_call(self._vtk_obj.Zero, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Matrix3x3, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Matrix3x3 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Matrix3x3 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Matrix3x3 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

