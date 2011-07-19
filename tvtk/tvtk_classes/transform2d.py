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


class Transform2D(Object):
    """
    Transform2D - describes linear transformations via a 3x3 matrix
    
    Superclass: Object
    
    A Transform2D can be used to describe the full range of linear
    (also known as affine) coordinate transformations in two dimensions,
    which are internally represented as a 3x3 homogeneous transformation
    matrix.  When you create a new Transform2D, it is always
    initialized to the identity transformation.
    
    This class performs all of its operations in a right handed
    coordinate system with right handed rotations. Some other graphics
    libraries use left handed coordinate systems and rotations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransform2D, obj, update, **traits)
    
    def _get_matrix(self):
        return wrap_vtk(self._vtk_obj.GetMatrix())
    def _set_matrix(self, arg):
        old_val = self._get_matrix()
        self._wrap_call(self._vtk_obj.SetMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('matrix', old_val, arg)
    matrix = traits.Property(_get_matrix, _set_matrix, help=\
        """
        Get the underlying 3x3 matrix.
        """
    )

    def get_inverse(self, *args):
        """
        V.get_inverse(Matrix3x3)
        C++: void GetInverse(Matrix3x3 *inverse)
        Return a matrix which is the inverse of the current
        transformation matrix.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInverse, *my_args)
        return ret

    def get_position(self, *args):
        """
        V.get_position([float, float])
        C++: void GetPosition(double pos[2])
        Return the position from the current transformation matrix as an
        array of two floating point numbers. This is simply returning the
        translation component of the 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.GetPosition, *args)
        return ret

    def get_transpose(self, *args):
        """
        V.get_transpose(Matrix3x3)
        C++: void GetTranspose(Matrix3x3 *transpose)
        Return a matrix which is the transpose of the current
        transformation matrix.  This is equivalent to the inverse if and
        only if the transformation is a pure rotation with no translation
        or scale.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTranspose, *my_args)
        return ret

    def identity(self):
        """
        V.identity()
        C++: void Identity()
        Set the transformation to the identity transformation.
        """
        ret = self._vtk_obj.Identity()
        return ret
        

    def inverse(self):
        """
        V.inverse()
        C++: void Inverse()
        Invert the transformation.
        """
        ret = self._vtk_obj.Inverse()
        return ret
        

    def inverse_transform_points(self, *args):
        """
        V.inverse_transform_points(Points2D, Points2D)
        C++: void InverseTransformPoints(Points2D *inPts,
            Points2D *outPts)
        Apply the transformation to a series of points, and append the
        results to out_pts.
        """
        my_args = deref_array(args, [('vtkPoints2D', 'vtkPoints2D')])
        ret = self._wrap_call(self._vtk_obj.InverseTransformPoints, *my_args)
        return ret

    def multiply_point(self, *args):
        """
        V.multiply_point((float, float, float), [float, float, float])
        C++: void MultiplyPoint(const double in[3], double out[3])
        Use this method only if you wish to compute the transformation in
        homogeneous (x,y,w) coordinates, otherwise use transform_point().
        This method calls this->_get_matrix()->_multiply_point().
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyPoint, *args)
        return ret

    def rotate(self, *args):
        """
        V.rotate(float)
        C++: void Rotate(double angle)
        Create a rotation matrix and concatenate it with the current
        transformation. The angle is in degrees.
        """
        ret = self._wrap_call(self._vtk_obj.Rotate, *args)
        return ret

    def scale(self, *args):
        """
        V.scale(float, float)
        C++: void Scale(double x, double y)
        V.scale((float, float))
        C++: void Scale(const double s[2])
        Create a scale matrix (i.e. set the diagonal elements to x, y)
        and concatenate it with the current transformation.
        """
        ret = self._wrap_call(self._vtk_obj.Scale, *args)
        return ret

    def transform_points(self, *args):
        """
        V.transform_points(Points2D, Points2D)
        C++: void TransformPoints(Points2D *inPts, Points2D *outPts)
        Apply the transformation to a series of points, and append the
        results to out_pts.
        """
        my_args = deref_array(args, [('vtkPoints2D', 'vtkPoints2D')])
        ret = self._wrap_call(self._vtk_obj.TransformPoints, *my_args)
        return ret

    def translate(self, *args):
        """
        V.translate(float, float)
        C++: void Translate(double x, double y)
        V.translate((float, float))
        C++: void Translate(const double x[2])
        Create a translation matrix and concatenate it with the current
        transformation.
        """
        ret = self._wrap_call(self._vtk_obj.Translate, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Transform2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Transform2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Transform2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Transform2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

