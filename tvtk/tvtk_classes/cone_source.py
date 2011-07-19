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


class ConeSource(PolyDataAlgorithm):
    """
    ConeSource - generate polygonal cone 
    
    Superclass: PolyDataAlgorithm
    
    ConeSource creates a cone centered at a specified point and
    pointing in a specified direction. (By default, the center is the
    origin and the direction is the x-axis.) Depending upon the
    resolution of this object, different representations are created. If
    resolution=0 a line is created; if resolution=1, a single triangle is
    created; if resolution=2, two crossed triangles are created. For
    resolution > 2, a 3d cone (with resolution number of sides) is
    created. It also is possible to control whether the bottom of the
    cone is capped with a (resolution-sided) polygon, and to specify the
    height and radius of the cone.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConeSource, obj, update, **traits)
    
    capping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off whether to cap the base of the cone with a polygon.
        """
    )
    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    direction = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction)

    angle = traits.Float(26.5650511771, enter_set=True, auto_set=False, help=\
        """
        Set the angle of the cone. This is the angle between the axis of
        the cone and a generatrix. Warning: this is not the aperture! The
        aperture is twice this angle. As a side effect, the angle plus
        height sets the base radius of the cone. Angle is expressed in
        degrees.
        """
    )
    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    height = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the height of the cone. This is the height along the cone in
        its specified direction.
        """
    )
    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    radius = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the base radius of the cone.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    resolution = traits.Trait(6, traits.Range(0, 512, enter_set=True, auto_set=False), help=\
        """
        Set the number of facets used to represent the cone.
        """
    )
    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    _updateable_traits_ = \
    (('direction', 'GetDirection'), ('angle', 'GetAngle'), ('center',
    'GetCenter'), ('progress_text', 'GetProgressText'), ('height',
    'GetHeight'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('radius', 'GetRadius'), ('release_data_flag',
    'GetReleaseDataFlag'), ('capping', 'GetCapping'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('resolution',
    'GetResolution'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'release_data_flag', 'angle', 'center', 'direction', 'height',
    'progress_text', 'radius', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConeSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['capping'], [], ['angle', 'center', 'direction',
            'height', 'radius', 'resolution']),
            title='Edit ConeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

