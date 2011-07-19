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

from tvtk.tvtk_classes.property import Property


class RIBProperty(Property):
    """
    RIBProperty - RIP Property
    
    Superclass: Property
    
    RIBProperty is a subclass of Property that allows the user to
    specify named shaders for use with render_man. Both a surface shader
    and displacement shader can be specified. Parameters for the shaders
    can be declared and set.
    
    See Also:
    
    RIBExporter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRIBProperty, obj, update, **traits)
    
    displacement_shader = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the name of a displacement shader.
        """
    )
    def _displacement_shader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementShader,
                        self.displacement_shader)

    surface_shader = traits.String(r"plastic", enter_set=True, auto_set=False, help=\
        """
        Specify the name of a surface shader.
        """
    )
    def _surface_shader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSurfaceShader,
                        self.surface_shader)

    def _get_declarations(self):
        return self._vtk_obj.GetDeclarations()
    declarations = traits.Property(_get_declarations, help=\
        """
        Get variable declarations
        """
    )

    def _get_parameters(self):
        return self._vtk_obj.GetParameters()
    parameters = traits.Property(_get_parameters, help=\
        """
        Get parameters.
        """
    )

    def add_parameter(self, *args):
        """
        V.add_parameter(string, string)
        C++: void AddParameter(char *parameter, char *value)
        Specify parameter values for variables.
        """
        ret = self._wrap_call(self._vtk_obj.AddParameter, *args)
        return ret

    def add_variable(self, *args):
        """
        V.add_variable(string, string)
        C++: void AddVariable(char *variable, char *declaration)
        Specify declarations for variables..
        """
        ret = self._wrap_call(self._vtk_obj.AddVariable, *args)
        return ret

    def set_parameter(self, *args):
        """
        V.set_parameter(string, string)
        C++: void SetParameter(char *parameter, char *value)
        Specify parameter values for variables.
        """
        ret = self._wrap_call(self._vtk_obj.SetParameter, *args)
        return ret

    def set_variable(self, *args):
        """
        V.set_variable(string, string)
        C++: void SetVariable(char *variable, char *declaration)
        Specify declarations for variables..
        """
        ret = self._wrap_call(self._vtk_obj.SetVariable, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('frontface_culling',
    'GetFrontfaceCulling'), ('displacement_shader',
    'GetDisplacementShader'), ('surface_shader', 'GetSurfaceShader'),
    ('color', 'GetColor'), ('diffuse_color', 'GetDiffuseColor'),
    ('ambient_color', 'GetAmbientColor'), ('backface_culling',
    'GetBackfaceCulling'), ('debug', 'GetDebug'), ('lighting',
    'GetLighting'), ('specular_power', 'GetSpecularPower'), ('point_size',
    'GetPointSize'), ('diffuse', 'GetDiffuse'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_color', 'GetEdgeColor'),
    ('ambient', 'GetAmbient'), ('specular_color', 'GetSpecularColor'),
    ('shading', 'GetShading'), ('specular', 'GetSpecular'),
    ('edge_visibility', 'GetEdgeVisibility'), ('line_stipple_pattern',
    'GetLineStipplePattern'), ('reference_count', 'GetReferenceCount'),
    ('representation', 'GetRepresentation'),
    ('line_stipple_repeat_factor', 'GetLineStippleRepeatFactor'),
    ('line_width', 'GetLineWidth'), ('interpolation', 'GetInterpolation'))
    
    _full_traitnames_list_ = \
    (['backface_culling', 'debug', 'edge_visibility', 'frontface_culling',
    'global_warning_display', 'lighting', 'shading', 'interpolation',
    'representation', 'ambient', 'ambient_color', 'color', 'diffuse',
    'diffuse_color', 'displacement_shader', 'edge_color',
    'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
    'opacity', 'point_size', 'specular', 'specular_color',
    'specular_power', 'surface_shader'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RIBProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['backface_culling', 'edge_visibility',
            'frontface_culling', 'lighting', 'shading'], ['interpolation',
            'representation'], ['ambient', 'ambient_color', 'color', 'diffuse',
            'diffuse_color', 'displacement_shader', 'edge_color',
            'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
            'opacity', 'point_size', 'specular', 'specular_color',
            'specular_power', 'surface_shader']),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

