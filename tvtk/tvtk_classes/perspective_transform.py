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


class PerspectiveTransform(HomogeneousTransform):
    """
    PerspectiveTransform - describes a 4x4 matrix transformation
    
    Superclass: HomogeneousTransform
    
    A PerspectiveTransform can be used to describe the full range of
    homogeneous transformations.  It was designed in particular to
    describe a camera-view of a scene. <P>The order in which you set up
    the display coordinates (via adjust_z_buffer() and adjust_viewport()),
    the projection (via Perspective(), Frustum(), or Ortho()) and the
    camera view (via setup_camera()) are important.  If the transform is
    in pre_multiply mode, which is the default, set the Viewport and
    ZBuffer first, then the projection, and finally the camera view. 
    Once the view is set up, the Translate and Rotate methods can be used
    to move the camera around in world coordinates.  If the Oblique() or
    Stereo() methods are used, they should be called just before
    setup_camera(). <P>In post_multiply mode, you must perform all
    transformations in the opposite order.  This is necessary, for
    example, if you already have a perspective transformation set up but
    must adjust the viewport.  Another example is if you have a view
    transformation, and wish to perform translations and rotations in the
    camera's coordinate system rather than in world coordinates. <P>The
    set_input and Concatenate methods can be used to create a
    transformation pipeline with PerspectiveTransform.  See
    Transform for more information on the transformation pipeline.
    
    See Also:
    
    GeneralTransform Transform Matrix4x4 Camera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPerspectiveTransform, obj, update, **traits)
    
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
        V.get_concatenated_transform(int) -> HomogeneousTransform
        C++: HomogeneousTransform *GetConcatenatedTransform(int i)"""
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

    def adjust_viewport(self, *args):
        """
        V.adjust_viewport(float, float, float, float, float, float, float,
            float)
        C++: void AdjustViewport(double oldXMin, double oldXMax,
            double oldYMin, double oldYMax, double newXMin,
            double newXMax, double newYMin, double newYMax)
        Perform an adjustment to the viewport coordinates.  By default
        Ortho, Frustum, and Perspective provide a window of
        ([-1,+1],[-1,+1]). In pre_multiply mode, you call this method
        before calling Ortho, Frustum, or Perspective.  In post_multiply
        mode you can call it after.  Note that if you must apply both
        adjust_z_buffer and adjust_viewport, it makes no difference which
        order you apply them in.
        """
        ret = self._wrap_call(self._vtk_obj.AdjustViewport, *args)
        return ret

    def adjust_z_buffer(self, *args):
        """
        V.adjust_z_buffer(float, float, float, float)
        C++: void AdjustZBuffer(double oldNearZ, double oldFarZ,
            double newNearZ, double newFarZ)
        Perform an adjustment to the Z-Buffer range that the near and far
        clipping planes map to.  By default Ortho, Frustum, and
        Perspective map the near clipping plane to -1 and the far
        clipping plane to +1. In pre_multiply mode, you call this method
        before calling Ortho, Frustum, or Perspective.  In post_multiply
        mode you can call it after.
        """
        ret = self._wrap_call(self._vtk_obj.AdjustZBuffer, *args)
        return ret

    def concatenate(self, *args):
        """
        V.concatenate(Matrix4x4)
        C++: void Concatenate(Matrix4x4 *matrix)
        V.concatenate((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float)
            )
        C++: void Concatenate(const double elements[16])
        V.concatenate(HomogeneousTransform)
        C++: void Concatenate(HomogeneousTransform *transform)
        Concatenates the matrix with the current transformation according
        to pre_multiply or post_multiply semantics.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Concatenate, *my_args)
        return ret

    def frustum(self, *args):
        """
        V.frustum(float, float, float, float, float, float)
        C++: void Frustum(double xmin, double xmax, double ymin,
            double ymax, double znear, double zfar)
        Create an perspective projection matrix and concatenate it by the
        current transformation.  The matrix maps a frustum with a back
        plane at -zfar and a front plane at -znear with extent
        [xmin,xmax],[ymin,ymax] to [-1,+1], [-1,+1], [+1,-1].
        """
        ret = self._wrap_call(self._vtk_obj.Frustum, *args)
        return ret

    def ortho(self, *args):
        """
        V.ortho(float, float, float, float, float, float)
        C++: void Ortho(double xmin, double xmax, double ymin,
            double ymax, double znear, double zfar)
        Create an orthogonal projection matrix and concatenate it by the
        current transformation.  The matrix maps [xmin,xmax],
        [ymin,ymax], [-znear,-zfar] to [-1,+1], [-1,+1], [+1,-1].
        """
        ret = self._wrap_call(self._vtk_obj.Ortho, *args)
        return ret

    def perspective(self, *args):
        """
        V.perspective(float, float, float, float)
        C++: void Perspective(double angle, double aspect, double znear,
            double zfar)
        Create a perspective projection matrix by specifying the view
        angle (this angle is in the y direction), the aspect ratio, and
        the near and far clipping range.  The projection matrix is
        concatenated with the current transformation.  This method works
        via Frustum.
        """
        ret = self._wrap_call(self._vtk_obj.Perspective, *args)
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

    def setup_camera(self, *args):
        """
        V.setup_camera((float, float, float), (float, float, float), (
            float, float, float))
        C++: void SetupCamera(const double position[3],
            const double focalpoint[3], const double viewup[3])
        V.setup_camera(float, float, float, float, float, float, float,
            float, float)
        C++: void SetupCamera(double p0, double p1, double p2, double fp0,
             double fp1, double fp2, double vup0, double vup1,
            double vup2)
        Set a view transformation matrix for the camera (this matrix does
        not contain any perspective) and concatenate it with the current
        transformation.
        """
        ret = self._wrap_call(self._vtk_obj.SetupCamera, *args)
        return ret

    def shear(self, *args):
        """
        V.shear(float, float, float)
        C++: void Shear(double dxdz, double dydz, double zplane)
        Create a shear transformation about a plane at distance z from
        the camera.  The values dxdz (i.e. dx/dz) and dydz specify the
        amount of shear in the x and y directions.  The 'zplane'
        specifies the distance from the camera to the plane at which the
        shear causes zero displacement.  Generally you want this plane to
        be the focal plane. This transformation can be used in
        combination with Ortho to create an oblique projection.  It can
        also be used in combination with Perspective to provide correct
        stereo views when the eye is at arbitrary but known positions
        relative to the center of a flat viewing screen.
        """
        ret = self._wrap_call(self._vtk_obj.Shear, *args)
        return ret

    def stereo(self, *args):
        """
        V.stereo(float, float)
        C++: void Stereo(double angle, double focaldistance)
        Create a stereo shear matrix and concatenate it with the current
        transformation.  This can be applied in conjunction with either a
        perspective transformation (via Frustum or Projection) or an
        orthographic projection.  You must specify the distance from the
        camera plane to the focal plane, and the angle between the
        distance vector and the eye.  The angle should be negative for
        the left eye, and positive for the right.  This method works via
        Oblique.
        """
        ret = self._wrap_call(self._vtk_obj.Stereo, *args)
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
            return super(PerspectiveTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PerspectiveTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PerspectiveTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PerspectiveTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

