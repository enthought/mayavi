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


class Matrix4x4(Object):
    """
    Matrix4x4 - represent and manipulate 4x4 transformation matrices
    
    Superclass: Object
    
    Matrix4x4 is a class to represent and manipulate 4x4 matrices.
    Specifically, it is designed to work on 4x4 transformation matrices
    found in 3d rendering using homogeneous coordinates [x y z w].
    
    See Also:
    
    Transform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMatrix4x4, obj, update, **traits)
    
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
        V.adjoint(Matrix4x4, Matrix4x4)
        C++: void Adjoint(Matrix4x4 *in, Matrix4x4 *out)
        V.adjoint((float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float),
            [float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: static void Adjoint(const double inElements[16],
            double outElements[16])
        Compute adjoint of the matrix and put it into out.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Adjoint, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Matrix4x4)
        C++: void DeepCopy(Matrix4x4 *source)
        V.deep_copy([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float,
            float], Matrix4x4)
        C++: static void DeepCopy(double Elements[16],
            Matrix4x4 *source)
        V.deep_copy([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float,
            float], (float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: static void DeepCopy(double Elements[16],
            const double newElements[16])
        V.deep_copy((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: void DeepCopy(const double Elements[16])
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
            float, float, float, float, float, float, float, float, float)
            ) -> float
        C++: static double Determinant(const double Elements[16])
        V.determinant(Matrix4x4) -> float
        C++: double Determinant(Matrix4x4 *in)
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
            float, float, float, float, float, float, float, float,
            float])
        C++: static void Identity(double Elements[16])
        Set equal to Identity matrix
        """
        ret = self._wrap_call(self._vtk_obj.Identity, *args)
        return ret

    def invert(self, *args):
        """
        V.invert(Matrix4x4, Matrix4x4)
        C++: static void Invert(Matrix4x4 *in, Matrix4x4 *out)
        V.invert()
        C++: void Invert()
        V.invert((float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float),
            [float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: static void Invert(const double inElements[16],
            double outElements[16])
        Matrix Inversion (adapted from Richard Carling in "Graphics
        Gems," Academic Press, 1990).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Invert, *my_args)
        return ret

    def multiply4x4(self, *args):
        """
        V.multiply4x4(Matrix4x4, Matrix4x4, Matrix4x4)
        C++: static void Multiply4x4(Matrix4x4 *a, Matrix4x4 *b,
            Matrix4x4 *c)
        V.multiply4x4((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            , (float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float),
            [float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: static void Multiply4x4(const double a[16],
            const double b[16], double c[16])
        Multiplies matrices a and b and stores the result in c.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Multiply4x4, *my_args)
        return ret

    def multiply_double_point(self, *args):
        """
        V.multiply_double_point((float, float, float, float)) -> (float,
            float, float, float)
        C++: double *MultiplyDoublePoint(const double in[4])
        For use in Java, Python or Tcl.  The default multiply_point() uses
        a single-precision point.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyDoublePoint, *args)
        return ret

    def multiply_float_point(self, *args):
        """
        V.multiply_float_point((float, float, float, float)) -> (float,
            float, float, float)
        C++: float *MultiplyFloatPoint(const float in[4])
        For use in Java, Python or Tcl.  The default multiply_point() uses
        a single-precision point.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyFloatPoint, *args)
        return ret

    def multiply_point(self, *args):
        """
        V.multiply_point((float, float, float, float), [float, float,
            float, float])
        C++: void MultiplyPoint(const double in[4], double out[4])
        V.multiply_point((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            , (float, float, float, float), [float, float, float, float])
        C++: static void MultiplyPoint(const double Elements[16],
            const double in[4], double out[4])
        V.multiply_point((float, float, float, float)) -> (float, float,
            float, float)
        C++: float *MultiplyPoint(const float in[4])
        Multiply a homogeneous coordinate by this matrix, i.e. out =
        A*in. The in[4] and out[4] can be the same array.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyPoint, *args)
        return ret

    def point_multiply(self, *args):
        """
        V.point_multiply((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            , (float, float, float, float), [float, float, float, float])
        C++: static void PointMultiply(const double Elements[16],
            const double in[4], double out[4])"""
        ret = self._wrap_call(self._vtk_obj.PointMultiply, *args)
        return ret

    def transpose(self, *args):
        """
        V.transpose(Matrix4x4, Matrix4x4)
        C++: static void Transpose(Matrix4x4 *in, Matrix4x4 *out)
        V.transpose()
        C++: void Transpose()
        V.transpose((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            , [float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: static void Transpose(const double inElements[16],
            double outElements[16])
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
            float, float, float, float, float, float, float, float])
        C++: static void Zero(double Elements[16])
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
            return super(Matrix4x4, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Matrix4x4 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Matrix4x4 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Matrix4x4 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __getstate__(self):
        d = tvtk_base.TVTKBase.__getstate__(self)
        obj = self._vtk_obj
        e = [obj.GetElement(i, j) for i in range(4) for j in range(4)]
        d['elements'] = e
        return d
    
    def __setstate__(self, dict):
        e = dict.pop('elements')
        tvtk_base.TVTKBase.__setstate__(self, dict)
        self._in_set = 1
        obj = self._vtk_obj
        [obj.SetElement(i, j, e[4*i+j]) for i in range(4) for j in range(4)]
        self._in_set = 0
        self.update_traits()
    
    def from_array(self, arr):
        '''Set the value of the matrix using the passed
        Numeric array or Python list.
        '''
        obj = self._vtk_obj
        [obj.SetElement(i, j, arr[i,j]) for i in range(4) for j in range(4)]
    
    def to_array(self):
        '''Return the object as a numpy array.'''
        obj = self._vtk_obj
        e = [obj.GetElement(i, j) for i in range(4) for j in range(4)]
        arr = array_handler.numpy.array(e, dtype=float)
        arr.shape = (4,4)
        return arr
    

