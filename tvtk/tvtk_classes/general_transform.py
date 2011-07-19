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

from tvtk.tvtk_classes.abstract_transform import AbstractTransform


class GeneralTransform(AbstractTransform):
    """
    GeneralTransform - allows operations on any transforms
    
    Superclass: AbstractTransform
    
    GeneralTransform is like Transform and PerspectiveTransform,
    but it will work with any AbstractTransform as input.  It is not
    as efficient as the other two, however, because arbitrary
    transformations cannot be concatenated by matrix multiplication.
    Transform concatenation is simulated by passing each input point
    through each transform in turn.
    
    See Also:
    
    Transform PerspectiveTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeneralTransform, obj, update, **traits)
    
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
        V.get_concatenated_transform(int) -> AbstractTransform
        C++: AbstractTransform *GetConcatenatedTransform(int i)"""
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

    def concatenate(self, *args):
        """
        V.concatenate(Matrix4x4)
        C++: void Concatenate(Matrix4x4 *matrix)
        V.concatenate((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: void Concatenate(const double elements[16])
        V.concatenate(AbstractTransform)
        C++: void Concatenate(AbstractTransform *transform)
        Concatenates the matrix with the current transformation according
        to pre_multiply or post_multiply semantics.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Concatenate, *my_args)
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
            return super(GeneralTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeneralTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GeneralTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeneralTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

