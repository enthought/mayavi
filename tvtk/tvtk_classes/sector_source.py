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


class SectorSource(PolyDataAlgorithm):
    """
    SectorSource - create a sector of a disk
    
    Superclass: PolyDataAlgorithm
    
    SectorSource creates a sector of a polygonal disk. The disk has
    zero height. The user can specify the inner and outer radius of the
    disk, the z-coordinate, and the radial and circumferential resolution
    of the polygonal representation.
    
    See Also:
    
    LinearExtrusionFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSectorSource, obj, update, **traits)
    
    outer_radius = traits.Trait(2.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify outer radius of the sector.
        """
    )
    def _outer_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOuterRadius,
                        self.outer_radius)

    radial_resolution = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in radius direction.
        """
    )
    def _radial_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialResolution,
                        self.radial_resolution)

    z_coord = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the z coordinate of the sector.
        """
    )
    def _z_coord_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCoord,
                        self.z_coord)

    inner_radius = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify inner radius of the sector.
        """
    )
    def _inner_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInnerRadius,
                        self.inner_radius)

    end_angle = traits.Trait(90.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the end angle of the sector.
        """
    )
    def _end_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndAngle,
                        self.end_angle)

    circumferential_resolution = traits.Trait(6, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in circumferential direction.
        """
    )
    def _circumferential_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCircumferentialResolution,
                        self.circumferential_resolution)

    start_angle = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the start angle of the sector.
        """
    )
    def _start_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartAngle,
                        self.start_angle)

    _updateable_traits_ = \
    (('inner_radius', 'GetInnerRadius'), ('start_angle', 'GetStartAngle'),
    ('debug', 'GetDebug'), ('progress_text', 'GetProgressText'),
    ('end_angle', 'GetEndAngle'), ('z_coord', 'GetZCoord'),
    ('circumferential_resolution', 'GetCircumferentialResolution'),
    ('outer_radius', 'GetOuterRadius'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('radial_resolution', 'GetRadialResolution'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'circumferential_resolution', 'end_angle',
    'inner_radius', 'outer_radius', 'progress_text', 'radial_resolution',
    'start_angle', 'z_coord'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SectorSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['circumferential_resolution', 'end_angle',
            'inner_radius', 'outer_radius', 'radial_resolution', 'start_angle',
            'z_coord']),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

