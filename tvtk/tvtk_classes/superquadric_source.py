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


class SuperquadricSource(PolyDataAlgorithm):
    """
    SuperquadricSource - create a polygonal superquadric centered 
    
    Superclass: PolyDataAlgorithm
    
    SuperquadricSource creates a superquadric (represented by
    polygons) of specified size centered at the origin. The resolution
    (polygonal discretization) in both the latitude (phi) and longitude
    (theta) directions can be specified. Roundness parameters
    (_phi_roundness and theta_roundness) control the shape of the
    superquadric.  The Toroidal boolean controls whether a toroidal
    superquadric is produced.  If so, the Thickness parameter controls
    the thickness of the toroid:  0 is the thinnest allowable toroid, and
    1 has a minimum sized hole.  The Scale parameters allow the
    superquadric to be scaled in x, y, and z (normal vectors are
    correctly generated in any case).  The Size parameter controls size
    of the superquadric.
    
    This code is based on "Rigid physically based superquadrics", A. H.
    Barr, in "Graphics Gems III", David Kirk, ed., Academic Press, 1992.
    
    Caveats:
    
    Resolution means the number of latitude or longitude lines for a
    complete superquadric. The resolution parameters are rounded to the
    nearest 4 in phi and 8 in theta.
    
    Texture coordinates are not equally distributed around all
    superquadrics.
    
    The Size and Thickness parameters control coefficients of
    superquadric generation, and may do not exactly describe the size of
    the superquadric.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSuperquadricSource, obj, update, **traits)
    
    toroidal = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
        """
    )
    def _toroidal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetToroidal,
                        self.toroidal_)

    scale = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    theta_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
    )
    def _theta_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaRoundness,
                        self.theta_roundness)

    phi_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set the number of points in the latitude direction. Initial value
        is 16.
        """
    )
    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    thickness = traits.Trait(0.3333, traits.Range(0.0001, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
    )
    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

    theta_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set the number of points in the longitude direction. Initial
        value is 16.
        """
    )
    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    phi_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
    )
    def _phi_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiRoundness,
                        self.phi_roundness)

    size = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric isotropic size. Initial value is 0.5;
        """
    )
    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    _updateable_traits_ = \
    (('scale', 'GetScale'), ('center', 'GetCenter'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('phi_roundness', 'GetPhiRoundness'), ('debug', 'GetDebug'),
    ('progress_text', 'GetProgressText'), ('thickness', 'GetThickness'),
    ('theta_resolution', 'GetThetaResolution'), ('abort_execute',
    'GetAbortExecute'), ('phi_resolution', 'GetPhiResolution'),
    ('toroidal', 'GetToroidal'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('theta_roundness', 'GetThetaRoundness'),
    ('size', 'GetSize'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'toroidal', 'center', 'phi_resolution',
    'phi_roundness', 'progress_text', 'scale', 'size', 'theta_resolution',
    'theta_roundness', 'thickness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SuperquadricSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['toroidal'], [], ['center', 'phi_resolution',
            'phi_roundness', 'scale', 'size', 'theta_resolution',
            'theta_roundness', 'thickness']),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

