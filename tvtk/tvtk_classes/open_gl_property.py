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


class OpenGLProperty(Property):
    """
    OpenGLProperty - open_gl property
    
    Superclass: Property
    
    OpenGLProperty is a concrete implementation of the abstract class
    Property. OpenGLProperty interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLProperty, obj, update, **traits)
    
    def _get_prop_program(self):
        return wrap_vtk(self._vtk_obj.GetPropProgram())
    def _set_prop_program(self, arg):
        old_val = self._get_prop_program()
        self._wrap_call(self._vtk_obj.SetPropProgram,
                        deref_vtk(arg))
        self.trait_property_changed('prop_program', old_val, arg)
    prop_program = traits.Property(_get_prop_program, _set_prop_program, help=\
        """
        Set/Get the shader program of the Prop. It can be set directly
        or by defining a Material.
        """
    )

    def _get_current_shader_program2(self):
        return wrap_vtk(self._vtk_obj.GetCurrentShaderProgram2())
    current_shader_program2 = traits.Property(_get_current_shader_program2, help=\
        """
        Get the ShaderProgram2 object in use.
        """
    )

    def _get_shader_device_adapter2(self):
        return wrap_vtk(self._vtk_obj.GetShaderDeviceAdapter2())
    shader_device_adapter2 = traits.Property(_get_shader_device_adapter2, help=\
        """
        Get the object that can pass vertex attribute to a
        ShaderProgram2.
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('frontface_culling',
    'GetFrontfaceCulling'), ('point_size', 'GetPointSize'),
    ('specular_color', 'GetSpecularColor'), ('color', 'GetColor'),
    ('diffuse_color', 'GetDiffuseColor'), ('ambient_color',
    'GetAmbientColor'), ('backface_culling', 'GetBackfaceCulling'),
    ('debug', 'GetDebug'), ('lighting', 'GetLighting'), ('specular_power',
    'GetSpecularPower'), ('shading', 'GetShading'), ('diffuse',
    'GetDiffuse'), ('edge_color', 'GetEdgeColor'), ('ambient',
    'GetAmbient'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('specular', 'GetSpecular'), ('edge_visibility', 'GetEdgeVisibility'),
    ('line_stipple_pattern', 'GetLineStipplePattern'), ('reference_count',
    'GetReferenceCount'), ('representation', 'GetRepresentation'),
    ('line_stipple_repeat_factor', 'GetLineStippleRepeatFactor'),
    ('line_width', 'GetLineWidth'), ('interpolation', 'GetInterpolation'))
    
    _full_traitnames_list_ = \
    (['backface_culling', 'debug', 'edge_visibility', 'frontface_culling',
    'global_warning_display', 'lighting', 'shading', 'interpolation',
    'representation', 'ambient', 'ambient_color', 'color', 'diffuse',
    'diffuse_color', 'edge_color', 'line_stipple_pattern',
    'line_stipple_repeat_factor', 'line_width', 'opacity', 'point_size',
    'specular', 'specular_color', 'specular_power'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['backface_culling', 'edge_visibility',
            'frontface_culling', 'lighting', 'shading'], ['interpolation',
            'representation'], ['ambient', 'ambient_color', 'color', 'diffuse',
            'diffuse_color', 'edge_color', 'line_stipple_pattern',
            'line_stipple_repeat_factor', 'line_width', 'opacity', 'point_size',
            'specular', 'specular_color', 'specular_power']),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

