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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class PlaneSource(PolyDataAlgorithm):
    """
    PlaneSource - create an array of quadrilaterals located in a plane
    
    Superclass: PolyDataAlgorithm
    
    PlaneSource creates an m x n array of quadrilaterals arranged as a
    regular tiling in a plane. The plane is defined by specifying an
    origin point, and then two other points that, together with the
    origin, define two axes for the plane. These axes do not have to be
    orthogonal - so you can create a parallelogram. (The axes must not be
    parallel.) The resolution of the plane (i.e., number of subdivisions)
    is controlled by the ivars XResolution and YResolution.
    
    By default, the plane is centered at the origin and perpendicular to
    the z-axis, with width and height of length 1 and resolutions set to
    1.
    
    There are three convenience methods that allow you to easily move the
    plane.  The first, set_normal(), allows you to specify the plane
    normal. The effect of this method is to rotate the plane around the
    center of the plane, aligning the plane normal with the specified
    normal. The rotation is about the axis defined by the cross product
    of the current normal with the new normal. The second, set_center(),
    translates the center of the plane to the specified center point. The
    third method, Push(), allows you to translate the plane along the
    plane normal by the distance specified. (Negative Push values
    translate the plane in the negative normal direction.)  Note that the
    set_normal(), set_center() and Push() methods modify the Origin,
    Point1, and/or Point2 instance variables.
    
    Caveats:
    
    The normal to the plane will point in the direction of the cross
    product of the first axis (Origin->Point1) with the second
    (Origin->Point2). This also affects the normals to the generated
    polygons.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlaneSource, obj, update, **traits)
    
    origin = traits.Array(shape=(3,), value=(-0.5, -0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    y_resolution = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the resolution of the plane along the second axes.
        """
    )
    def _y_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYResolution,
                        self.y_resolution)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the center of the plane. Works in conjunction with the
        plane normal to position the plane. Don't use this method to
        define the plane. Instead, use it to move the plane to a new
        center point.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the plane normal. Works in conjunction with the plane
        center to orient the plane. Don't use this method to define the
        plane. Instead, use it to rotate the plane around the current
        center point.
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    point1 = traits.Array(shape=(3,), value=(0.5, -0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify a point defining the first axis of the plane.
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(3,), value=(-0.5, 0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify a point defining the second axis of the plane.
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    x_resolution = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the resolution of the plane along the first axes.
        """
    )
    def _x_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXResolution,
                        self.x_resolution)

    def get_resolution(self, *args):
        """
        V.get_resolution(int, int)
        C++: void GetResolution(int &xR, int &yR)
        Set the number of x-y subdivisions in the plane.
        """
        ret = self._wrap_call(self._vtk_obj.GetResolution, *args)
        return ret

    def set_resolution(self, *args):
        """
        V.set_resolution(int, int)
        C++: void SetResolution(const int xR, const int yR)
        Set the number of x-y subdivisions in the plane.
        """
        ret = self._wrap_call(self._vtk_obj.SetResolution, *args)
        return ret

    def push(self, *args):
        """
        V.push(float)
        C++: void Push(double distance)
        Translate the plane in the direction of the normal by the
        distance specified.  Negative values move the plane in the
        opposite direction.
        """
        ret = self._wrap_call(self._vtk_obj.Push, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('center', 'GetCenter'), ('normal',
    'GetNormal'), ('x_resolution', 'GetXResolution'), ('progress_text',
    'GetProgressText'), ('y_resolution', 'GetYResolution'), ('point1',
    'GetPoint1'), ('point2', 'GetPoint2'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'normal', 'origin', 'point1', 'point2',
    'progress_text', 'x_resolution', 'y_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlaneSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'normal', 'origin', 'point1',
            'point2', 'x_resolution', 'y_resolution']),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

