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

from tvtk.tvtk_classes.light import Light


class RIBLight(Light):
    """
    RIBLight - RIP Light
    
    Superclass: Light
    
    RIBLight is a subclass of Light that allows the user to specify
    light source shaders and shadow casting lights for use with
    render_man.
    
    See Also:
    
    RIBExporter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRIBLight, obj, update, **traits)
    
    shadows = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadows,
                        self.shadows_)

    _updateable_traits_ = \
    (('shadows', 'GetShadows'), ('specular_color', 'GetSpecularColor'),
    ('exponent', 'GetExponent'), ('color', 'GetColor'), ('debug',
    'GetDebug'), ('diffuse_color', 'GetDiffuseColor'), ('ambient_color',
    'GetAmbientColor'), ('cone_angle', 'GetConeAngle'), ('positional',
    'GetPositional'), ('switch', 'GetSwitch'), ('intensity',
    'GetIntensity'), ('light_type', 'GetLightType'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'),
    ('attenuation_values', 'GetAttenuationValues'), ('focal_point',
    'GetFocalPoint'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'positional', 'shadows',
    'switch', 'light_type', 'ambient_color', 'attenuation_values',
    'color', 'cone_angle', 'diffuse_color', 'exponent', 'focal_point',
    'intensity', 'position', 'specular_color'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RIBLight, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['positional', 'shadows', 'switch'], ['light_type'],
            ['ambient_color', 'attenuation_values', 'color', 'cone_angle',
            'diffuse_color', 'exponent', 'focal_point', 'intensity', 'position',
            'specular_color']),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

