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

from tvtk.tvtk_classes.linear_transform import LinearTransform


class Transform(LinearTransform):
    """
    Transform - describes linear transformations via a 4x4 matrix
    
    Superclass: LinearTransform
    
    A Transform can be used to describe the full range of linear (also
    known as affine) coordinate transformations in three dimensions,
    which are internally represented as a 4x4 homogeneous transformation
    matrix.  When you create a new Transform, it is always initialized
    to the identity transformation. <P>The set_input() method allows you
    to set another transform, instead of the identity transform, to be
    the base transformation. There is a pipeline mechanism to ensure that
    when the input is modified, the current transformation will be
    updated accordingly. This pipeline mechanism is also supported by the
    Concatenate() method. <P>Most of the methods for manipulating this
    transformation, e.g. Translate, Rotate, and Concatenate, can operate
    in either pre_multiply (the default) or post_multiply mode.  In
    pre_multiply mode, the translation, concatenation, etc. will occur
    before any transformations which are represented by the current
    matrix.  In post_multiply mode, the additional transformation will
    occur after any transformations represented by the current matrix.
    <P>This class performs all of its operations in a right handed
    coordinate system with right handed rotations. Some other graphics
    libraries use left handed coordinate systems and rotations.
    
    See Also:
    
    PerspectiveTransform GeneralTransform Matrix4x4
    TransformCollection TransformFilter TransformPolyDataFilter
    ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransform, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the input for this transformation.  This will be used as the
        base transformation if it is set.  This method allows you to
        build a transform pipeline: if the input is modified, then this
        transformation will automatically update accordingly.  Note that
        the inverse_flag, controlled via Inverse(), determines whether
        this transformation will use the Input or the inverse of the
        Input.
        """
    )

    def get_concatenated_transform(self, *args):
        """
        V.get_concatenated_transform(int) -> LinearTransform
        C++: LinearTransform *GetConcatenatedTransform(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetConcatenatedTransform, *args)
        return wrap_vtk(ret)

    def _get_inverse_flag(self):
        return self._vtk_obj.GetInverseFlag()
    inverse_flag = traits.Property(_get_inverse_flag, help=\
        """
        Get the inverse flag of the transformation.  This controls
        whether it is the Input or the inverse of the Input that is used
        as the base transformation.  The inverse_flag is flipped every
        time Inverse() is called.  The inverse_flag is off when a
        transform is first created.
        """
    )

    def _get_number_of_concatenated_transforms(self):
        return self._vtk_obj.GetNumberOfConcatenatedTransforms()
    number_of_concatenated_transforms = traits.Property(_get_number_of_concatenated_transforms, help=\
        """
        Get the total number of transformations that are linked into this
        one via Concatenate() operations or via set_input().
        """
    )

    def _get_orientation(self):
        return self._vtk_obj.GetOrientation()
    orientation = traits.Property(_get_orientation, help=\
        """
        Get the x, y, z orientation angles from the transformation matrix
        as an array of three floating point values.
        """
    )

    def _get_orientation_wxyz(self):
        return self._vtk_obj.GetOrientationWXYZ()
    orientation_wxyz = traits.Property(_get_orientation_wxyz, help=\
        """
        Return the wxyz angle+axis representing the current orientation.
        The angle is in degrees and the axis is a unit vector.
        """
    )

    def _get_position(self):
        return self._vtk_obj.GetPosition()
    position = traits.Property(_get_position, help=\
        """
        Return the position from the current transformation matrix as an
        array of three floating point numbers. This is simply returning
        the translation component of the 4x4 matrix.
        """
    )

    def _get_scale(self):
        return self._vtk_obj.GetScale()
    scale = traits.Property(_get_scale, help=\
        """
        Return the scale factors of the current transformation matrix as
        an array of three float numbers.  These scale factors are not
        necessarily about the x, y, and z axes unless unless the scale
        transformation was applied before any rotations.
        """
    )

    def get_transpose(self, *args):
        """
        V.get_transpose(Matrix4x4)
        C++: void GetTranspose(Matrix4x4 *transpose)
        Return a matrix which is the transpose of the current
        transformation matrix.  This is equivalent to the inverse if and
        only if the transformation is a pure rotation with no translation
        or scale.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTranspose, *my_args)
        return ret

    def concatenate(self, *args):
        """
        V.concatenate(Matrix4x4)
        C++: void Concatenate(Matrix4x4 *matrix)
        V.concatenate((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: void Concatenate(const double elements[16])
        V.concatenate(LinearTransform)
        C++: void Concatenate(LinearTransform *transform)
        Concatenates the matrix with the current transformation according
        to pre_multiply or post_multiply semantics.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Concatenate, *my_args)
        return ret

    def multiply_point(self, *args):
        """
        V.multiply_point((float, float, float, float), [float, float,
            float, float])
        C++: void MultiplyPoint(const double in[4], double out[4])
        Use this method only if you wish to compute the transformation in
        homogeneous (x,y,z,w) coordinates, otherwise use
        transform_point(). This method calls
        this->_get_matrix()->_multiply_point().
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyPoint, *args)
        return ret

    def pop(self):
        """
        V.pop()
        C++: void Pop()
        Deletes the transformation on the top of the stack and sets the
        top to the next transformation on the stack.
        """
        ret = self._vtk_obj.Pop()
        return ret
        

    def post_multiply(self):
        """
        V.post_multiply()
        C++: void PostMultiply()
        Sets the internal state of the transform to post_multiply. All
        subsequent operations will occur after those already represented
        in the current transformation.  In homogeneous matrix notation, M
        = A*M where M is the current transformation matrix and A is the
        applied matrix. The default is pre_multiply.
        """
        ret = self._vtk_obj.PostMultiply()
        return ret
        

    def pre_multiply(self):
        """
        V.pre_multiply()
        C++: void PreMultiply()
        Sets the internal state of the transform to pre_multiply. All
        subsequent operations will occur before those already represented
        in the current transformation.  In homogeneous matrix notation, M
        = M*A where M is the current transformation matrix and A is the
        applied matrix. The default is pre_multiply.
        """
        ret = self._vtk_obj.PreMultiply()
        return ret
        

    def push(self):
        """
        V.push()
        C++: void Push()
        Pushes the current transformation onto the transformation stack.
        """
        ret = self._vtk_obj.Push()
        return ret
        

    def rotate_wxyz(self, *args):
        """
        V.rotate_wxyz(float, float, float, float)
        C++: void RotateWXYZ(double angle, double x, double y, double z)
        V.rotate_wxyz(float, (float, float, float))
        C++: void RotateWXYZ(double angle, const double axis[3])
        Create a rotation matrix and concatenate it with the current
        transformation according to pre_multiply or post_multiply
        semantics. The angle is in degrees, and (x,y,z) specifies the
        axis that the rotation will be performed around.
        """
        ret = self._wrap_call(self._vtk_obj.RotateWXYZ, *args)
        return ret

    def rotate_x(self, *args):
        """
        V.rotate_x(float)
        C++: void RotateX(double angle)
        Create a rotation matrix about the X, Y, or Z axis and
        concatenate it with the current transformation according to
        pre_multiply or post_multiply semantics.  The angle is expressed in
        degrees.
        """
        ret = self._wrap_call(self._vtk_obj.RotateX, *args)
        return ret

    def rotate_y(self, *args):
        """
        V.rotate_y(float)
        C++: void RotateY(double angle)
        Create a rotation matrix about the X, Y, or Z axis and
        concatenate it with the current transformation according to
        pre_multiply or post_multiply semantics.  The angle is expressed in
        degrees.
        """
        ret = self._wrap_call(self._vtk_obj.RotateY, *args)
        return ret

    def rotate_z(self, *args):
        """
        V.rotate_z(float)
        C++: void RotateZ(double angle)
        Create a rotation matrix about the X, Y, or Z axis and
        concatenate it with the current transformation according to
        pre_multiply or post_multiply semantics.  The angle is expressed in
        degrees.
        """
        ret = self._wrap_call(self._vtk_obj.RotateZ, *args)
        return ret

    def scale(self, *args):
        """
        V.scale(float, float, float)
        C++: void Scale(double x, double y, double z)
        V.scale((float, float, float))
        C++: void Scale(const double s[3])
        Create a scale matrix (i.e. set the diagonal elements to x, y, z)
        and concatenate it with the current transformation according to
        pre_multiply or post_multiply semantics.
        """
        ret = self._wrap_call(self._vtk_obj.Scale, *args)
        return ret

    def set_matrix(self, *args):
        """
        V.set_matrix(Matrix4x4)
        C++: void SetMatrix(Matrix4x4 *matrix)
        V.set_matrix((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: void SetMatrix(const double elements[16])
        Set the current matrix directly.  This actually calls Identity(),
        followed by Concatenate(matrix).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMatrix, *my_args)
        return ret

    def translate(self, *args):
        """
        V.translate(float, float, float)
        C++: void Translate(double x, double y, double z)
        V.translate((float, float, float))
        C++: void Translate(const double x[3])
        Create a translation matrix and concatenate it with the current
        transformation according to pre_multiply or post_multiply
        semantics.
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
            return super(Transform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Transform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Transform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Transform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

