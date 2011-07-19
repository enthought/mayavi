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


class ParametricFunctionSource(PolyDataAlgorithm):
    """
    ParametricFunctionSource - tessellate parametric functions
    
    Superclass: PolyDataAlgorithm
    
    This class tessellates parametric functions. The user must specify
    how many points in the parametric coordinate directions are required
    (i.e., the resolution), and the mode to use to generate scalars.
    
    Thanks:
    
    Andrew Maclean a.maclean@cas.edu.au for creating and contributing the
    class.
    
    See Also:
    
    ParametricFunction
    
    Implementation of parametrics for 1d lines: ParametricSpline
    
    Subclasses of ParametricFunction implementing non-orentable
    surfaces: ParametricBoy ParametricCrossCap
    ParametricFigure8Klein ParametricKlein ParametricMobius
    ParametricRoman
    
    Subclasses of ParametricFunction implementing orientable surfaces:
    ParametricConicSpiral ParametricDini ParametricEllipsoid
    ParametricEnneper ParametricRandomHills
    ParametricSuperEllipsoid ParametricSuperToroid
    ParametricTorus
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricFunctionSource, obj, update, **traits)
    
    generate_texture_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the generation of texture coordinates. This is off by
        default. Note that this is only applicable to parametric surfaces
        whose parametric dimension is 2. Note that texturing may fail in
        some cases.
        """
    )
    def _generate_texture_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTextureCoordinates,
                        self.generate_texture_coordinates_)

    scalar_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'distance': 12, 'none': 0, 'u0v0': 5, 'function_defined': 13, 'v0': 4, 'u0': 3, 'quadrant': 8, 'y': 10, 'u': 1, 'v': 2, 'phase': 7, 'x': 9, 'z': 11, 'modulus': 6}), help=\
        """
        Get/Set the mode used for the scalar data.  The options are:
        SCALAR_NONE, (default) scalars are not generated. SCALAR_U, the
        scalar is set to the u-value. SCALAR_V, the scalar is set to the
        v-value. SCALAR_U0, the scalar is set to 1 if u = (u_max -
        u_min)/2 = u_avg, 0 otherwise. SCALAR_V0, the scalar is set to 1
        if v = (v_max - v_min)/2 = v_avg, 0 otherwise. scalar__u0v0, the
        scalar is
          set to 1 if u == u_avg, 2 if v == v_avg, 3 if u = u_avg && v =
        v_avg, 0 otherwise. SCALAR_MODULUS, the scalar is set to
        (sqrt(u*u+v*v)), this is measured relative to (u_avg,v_avg).
        SCALAR_PHASE, the scalar is set to (atan2(v,u)) (in degrees, 0 to
        360), this is measured relative to (u_avg,v_avg).
        SCALAR_QUADRANT, the scalar is set to 1, 2, 3 or 4
          depending upon the quadrant of the point (u,v). SCALAR_X, the
        scalar is set to the x-value. SCALAR_Y, the scalar is set to the
        y-value. SCALAR_Z, the scalar is set to the z-value.
        SCALAR_DISTANCE, the scalar is set to (sqrt(x*x+y*y+z*z)). I.e.
        distance from the origin. SCALAR_FUNCTION_DEFINED, the scalar is
        set to the value returned from evaluate_scalar().
        """
    )
    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    def _get_parametric_function(self):
        return wrap_vtk(self._vtk_obj.GetParametricFunction())
    def _set_parametric_function(self, arg):
        old_val = self._get_parametric_function()
        self._wrap_call(self._vtk_obj.SetParametricFunction,
                        deref_vtk(arg))
        self.trait_property_changed('parametric_function', old_val, arg)
    parametric_function = traits.Property(_get_parametric_function, _set_parametric_function, help=\
        """
        Specify the parametric function to use to generate the
        tessellation.
        """
    )

    v_resolution = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of subdivisions / tessellations in the v
        parametric direction. Note that the number of tessellant points
        in the v direction is the VResolution + 1.
        """
    )
    def _v_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVResolution,
                        self.v_resolution)

    u_resolution = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of subdivisions / tessellations in the u
        parametric direction. Note that the number of tessellant points
        in the u direction is the UResolution + 1.
        """
    )
    def _u_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUResolution,
                        self.u_resolution)

    w_resolution = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of subdivisions / tessellations in the w
        parametric direction. Note that the number of tessellant points
        in the w direction is the WResolution + 1.
        """
    )
    def _w_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWResolution,
                        self.w_resolution)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('w_resolution', 'GetWResolution'), ('scalar_mode', 'GetScalarMode'),
    ('v_resolution', 'GetVResolution'), ('progress_text',
    'GetProgressText'), ('generate_texture_coordinates',
    'GetGenerateTextureCoordinates'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('u_resolution', 'GetUResolution'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_texture_coordinates',
    'global_warning_display', 'release_data_flag', 'scalar_mode',
    'progress_text', 'u_resolution', 'v_resolution', 'w_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricFunctionSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_texture_coordinates'], ['scalar_mode'],
            ['u_resolution', 'v_resolution', 'w_resolution']),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

