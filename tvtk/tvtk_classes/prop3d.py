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

from tvtk.tvtk_classes.prop import Prop


class Prop3D(Prop):
    """
    Prop3D - represents an 3d object for placement in a rendered scene 
    
    Superclass: Prop
    
    Prop3D is an abstract class used to represent an entity in a
    rendering scene (i.e., Prop3D is a Prop with an associated
    transformation matrix).  It handles functions related to the
    position, orientation and scaling. It combines these instance
    variables into one 4x4 transformation matrix as follows: [x y z 1] =
    [x y z 1] Translate(-origin) Scale(scale) Rot(y) Rot(x) Rot (z)
    Trans(origin) Trans(position). Both Actor and Volume are
    specializations of class Prop.  The constructor defaults to:
    origin(0,0,0) position=(0,0,0) orientation=(0,0,0), no user defined
    matrix or transform, and no texture map.
    
    See Also:
    
    Prop Actor Assembly Volume
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProp3D, obj, update, **traits)
    
    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the origin of the prop3d. This is the point about which
        all rotations take place.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    scale = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the scale of the actor. Scaling in performed
        independently on the X, Y and Z axis. A scale of zero is illegal
        and will be replaced with one.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    orientation = traits.Array(shape=(3,), value=(0.0, -0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Sets the orientation of the prop3d.  Orientation is specified as
        X,Y and Z rotations in that order, but they are performed as
        rotate_z, rotate_x, and finally rotate_y.
        """
    )
    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    def _get_user_matrix(self):
        return wrap_vtk(self._vtk_obj.GetUserMatrix())
    def _set_user_matrix(self, arg):
        old_val = self._get_user_matrix()
        self._wrap_call(self._vtk_obj.SetUserMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('user_matrix', old_val, arg)
    user_matrix = traits.Property(_get_user_matrix, _set_user_matrix, help=\
        """
        The user_matrix can be used in place of user_transform.
        """
    )

    def _get_user_transform(self):
        return wrap_vtk(self._vtk_obj.GetUserTransform())
    def _set_user_transform(self, arg):
        old_val = self._get_user_transform()
        self._wrap_call(self._vtk_obj.SetUserTransform,
                        deref_vtk(arg))
        self.trait_property_changed('user_transform', old_val, arg)
    user_transform = traits.Property(_get_user_transform, _set_user_transform, help=\
        """
        In addition to the instance variables such as position and
        orientation, you can add an additional transformation for your
        own use.  This transformation is concatenated with the actor's
        internal transformation, which you implicitly create through the
        use of set_position(), set_origin() and set_orientation().
        
        If the internal transformation is identity (i.e. if you don't set
        the Position, Origin, or Orientation) then the actors final
        transformation will be the user_transform, concatenated with the
        user_matrix if the user_matrix is present.
        """
    )

    position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get/Add the position of the prop3d in world coordinates.
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Get the center of the bounding box in world coordinates.
        """
    )

    def _get_is_identity(self):
        return self._vtk_obj.GetIsIdentity()
    is_identity = traits.Property(_get_is_identity, help=\
        """
        Is the matrix for this actor identity
        """
    )

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Get the length of the diagonal of the bounding box.
        """
    )

    def _get_orientation_wxyz(self):
        return self._vtk_obj.GetOrientationWXYZ()
    orientation_wxyz = traits.Property(_get_orientation_wxyz, help=\
        """
        Returns the WXYZ orientation of the prop3d.
        """
    )

    def _get_user_transform_matrix_m_time(self):
        return self._vtk_obj.GetUserTransformMatrixMTime()
    user_transform_matrix_m_time = traits.Property(_get_user_transform_matrix_m_time, help=\
        """
        Get the modified time of the user matrix or user transform.
        """
    )

    def _get_x_range(self):
        return self._vtk_obj.GetXRange()
    x_range = traits.Property(_get_x_range, help=\
        """
        Get the prop3d's x range in world coordinates.
        """
    )

    def _get_y_range(self):
        return self._vtk_obj.GetYRange()
    y_range = traits.Property(_get_y_range, help=\
        """
        Get the prop3d's y range in world coordinates.
        """
    )

    def _get_z_range(self):
        return self._vtk_obj.GetZRange()
    z_range = traits.Property(_get_z_range, help=\
        """
        Get the prop3d's z range in world coordinates.
        """
    )

    def add_orientation(self, *args):
        """
        V.add_orientation(float, float, float)
        C++: void AddOrientation(double, double, double)
        V.add_orientation([float, float, float])
        C++: void AddOrientation(double a[3])
        Add to the current orientation. See set_orientation and
        get_orientation for more details. This basically does a
        get_orientation, adds the passed in arguments, and then calls
        set_orientation.
        """
        ret = self._wrap_call(self._vtk_obj.AddOrientation, *args)
        return ret

    def add_position(self, *args):
        """
        V.add_position([float, float, float])
        C++: void AddPosition(double deltaPosition[3])
        V.add_position(float, float, float)
        C++: void AddPosition(double deltaX, double deltaY, double deltaZ)
        Set/Get/Add the position of the prop3d in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.AddPosition, *args)
        return ret

    def compute_matrix(self):
        """
        V.compute_matrix()
        C++: virtual void ComputeMatrix()
        Generate the matrix based on ivars
        """
        ret = self._vtk_obj.ComputeMatrix()
        return ret
        

    def rotate_wxyz(self, *args):
        """
        V.rotate_wxyz(float, float, float, float)
        C++: void RotateWXYZ(double, double, double, double)
        Rotate the prop3d in degrees about an arbitrary axis specified by
        the last three arguments. The axis is specified in world
        coordinates. To rotate an about its model axes, use rotate_x,
        rotate_y, rotate_z.
        """
        ret = self._wrap_call(self._vtk_obj.RotateWXYZ, *args)
        return ret

    def rotate_x(self, *args):
        """
        V.rotate_x(float)
        C++: void RotateX(double)
        Rotate the prop3d in degrees about the X axis using the right
        hand rule. The axis is the prop3d's X axis, which can change as
        other rotations are performed.  To rotate about the world X axis
        use rotate_wxyz (angle, 1, 0, 0). This rotation is applied before
        all others in the current transformation matrix.
        """
        ret = self._wrap_call(self._vtk_obj.RotateX, *args)
        return ret

    def rotate_y(self, *args):
        """
        V.rotate_y(float)
        C++: void RotateY(double)
        Rotate the prop3d in degrees about the Y axis using the right
        hand rule. The axis is the prop3d's Y axis, which can change as
        other rotations are performed.  To rotate about the world Y axis
        use rotate_wxyz (angle, 0, 1, 0). This rotation is applied before
        all others in the current transformation matrix.
        """
        ret = self._wrap_call(self._vtk_obj.RotateY, *args)
        return ret

    def rotate_z(self, *args):
        """
        V.rotate_z(float)
        C++: void RotateZ(double)
        Rotate the prop3d in degrees about the Z axis using the right
        hand rule. The axis is the prop3d's Z axis, which can change as
        other rotations are performed.  To rotate about the world Z axis
        use rotate_wxyz (angle, 0, 0, 1). This rotation is applied before
        all others in the current transformation matrix.
        """
        ret = self._wrap_call(self._vtk_obj.RotateZ, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'), ('orientation',
    'GetOrientation'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Prop3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Prop3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale']),
            title='Edit Prop3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Prop3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

