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


class TexturedSphereSource(PolyDataAlgorithm):
    """
    TexturedSphereSource - create a sphere centered at the origin
    
    Superclass: PolyDataAlgorithm
    
    TexturedSphereSource creates a polygonal sphere of specified
    radius centered at the origin. The resolution (polygonal
    discretization) in both the latitude (phi) and longitude (theta)
    directions can be specified. It also is possible to create partial
    sphere by specifying maximum phi and theta angles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTexturedSphereSource, obj, update, **traits)
    
    theta = traits.Trait(0.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the maximum longitude angle.
        """
    )
    def _theta_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTheta,
                        self.theta)

    phi = traits.Trait(0.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Set the maximum latitude angle (0 is at north pole).
        """
    )
    def _phi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhi,
                        self.phi)

    radius = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set radius of sphere.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    theta_resolution = traits.Trait(8, traits.Range(4, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the longitude direction.
        """
    )
    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    phi_resolution = traits.Trait(8, traits.Range(4, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the latitude direction.
        """
    )
    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    _updateable_traits_ = \
    (('phi', 'GetPhi'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('theta_resolution', 'GetThetaResolution'),
    ('abort_execute', 'GetAbortExecute'), ('phi_resolution',
    'GetPhiResolution'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('progress', 'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('radius', 'GetRadius'), ('theta', 'GetTheta'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'phi', 'phi_resolution', 'progress_text',
    'radius', 'theta', 'theta_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TexturedSphereSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['phi', 'phi_resolution', 'radius', 'theta',
            'theta_resolution']),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

