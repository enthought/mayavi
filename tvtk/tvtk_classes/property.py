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

from tvtk.tvtk_classes.object import Object


class Property(Object):
    """
    Property - represent surface properties of a geometric object
    
    Superclass: Object
    
    Property is an object that represents lighting and other surface
    properties of a geometric object. The primary properties that can be
    set are colors (overall, ambient, diffuse, specular, and edge color);
    specular power; opacity of the object; the representation of the
    object (points, wireframe, or surface); and the shading method to be
    used (flat, Gouraud, and Phong). Also, some special graphics features
    like backface properties can be set and manipulated with this object.
    
    See Also:
    
    Actor PropertyDevice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProperty, obj, update, **traits)
    
    edge_visibility = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the visibility of edges. On some renderers it is
        possible to render the edges of geometric primitives separately
        from the interior.
        """
    )
    def _edge_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeVisibility,
                        self.edge_visibility_)

    lighting = tvtk_base.true_bool_trait(help=\
        """
        Set/Get lighting flag for an object. Initial value is true.
        """
    )
    def _lighting_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLighting,
                        self.lighting_)

    backface_culling = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off fast culling of polygons based on orientation of
        normal with respect to camera. If backface culling is on,
        polygons facing away from camera are not drawn.
        """
    )
    def _backface_culling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackfaceCulling,
                        self.backface_culling_)

    frontface_culling = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off fast culling of polygons based on orientation of
        normal with respect to camera. If frontface culling is on,
        polygons facing towards camera are not drawn.
        """
    )
    def _frontface_culling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrontfaceCulling,
                        self.frontface_culling_)

    shading = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable shading. When shading is enabled, the Material
        must be set.
        """
    )
    def _shading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShading,
                        self.shading_)

    representation = traits.Trait('surface',
    tvtk_base.TraitRevPrefixMap({'points': 0, 'wireframe': 1, 'surface': 2}), help=\
        """
        Control the surface geometry representation for the object.
        """
    )
    def _representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentation,
                        self.representation_)

    interpolation = traits.Trait('gouraud',
    tvtk_base.TraitRevPrefixMap({'flat': 0, 'phong': 2, 'gouraud': 1}), help=\
        """
        Set the shading interpolation method for an object.
        """
    )
    def _interpolation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolation,
                        self.interpolation_)

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    edge_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _edge_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeColor,
                        self.edge_color, True)

    specular_power = traits.Trait(1.0, traits.Range(0.0, 128.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the specular power.
        """
    )
    def _specular_power_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecularPower,
                        self.specular_power)

    point_size = traits.Trait(1.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the diameter of a point. The size is expressed in screen
        units. This is only implemented for open_gl. The default is 1.0.
        """
    )
    def _point_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointSize,
                        self.point_size)

    specular_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _specular_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecularColor,
                        self.specular_color, True)

    diffuse_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _diffuse_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuseColor,
                        self.diffuse_color, True)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        Set the color of the object. Has the side effect of setting the
        ambient diffuse and specular colors as well. This is basically a
        quick overall color setting method.
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, True)

    line_stipple_pattern = traits.Int(65535, enter_set=True, auto_set=False, help=\
        """
        Set/Get the stippling pattern of a Line, as a 16-bit binary
        pattern (1 = pixel on, 0 = pixel off). This is only implemented
        for open_gl. The default is 0x_ffff.
        """
    )
    def _line_stipple_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineStipplePattern,
                        self.line_stipple_pattern)

    line_stipple_repeat_factor = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the stippling repeat factor of a Line, which specifies
        how many times each bit in the pattern is to be repeated. This is
        only implemented for open_gl. The default is 1.
        """
    )
    def _line_stipple_repeat_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineStippleRepeatFactor,
                        self.line_stipple_repeat_factor)

    ambient_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _ambient_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbientColor,
                        self.ambient_color, True)

    specular = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the specular lighting coefficient.
        """
    )
    def _specular_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecular,
                        self.specular)

    def get_texture(self, *args):
        """
        V.get_texture(string) -> Texture
        C++: Texture *GetTexture(const char *name)
        V.get_texture(int) -> Texture
        C++: Texture *GetTexture(int unit)
        Set/Get the texture object to control rendering texture maps. 
        This will be a Texture object. A property does not need to
        have an associated texture map and multiple properties can share
        one texture. Textures must be assigned unique names.
        """
        ret = self._wrap_call(self._vtk_obj.GetTexture, *args)
        return wrap_vtk(ret)

    def set_texture(self, *args):
        """
        V.set_texture(string, Texture)
        C++: void SetTexture(const char *name, Texture *texture)
        V.set_texture(int, Texture)
        C++: void SetTexture(int unit, Texture *texture)
        Set/Get the texture object to control rendering texture maps. 
        This will be a Texture object. A property does not need to
        have an associated texture map and multiple properties can share
        one texture. Textures must be assigned unique names.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTexture, *my_args)
        return ret

    ambient = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ambient lighting coefficient.
        """
    )
    def _ambient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbient,
                        self.ambient)

    line_width = traits.Trait(1.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of a Line. The width is expressed in screen
        units. This is only implemented for open_gl. The default is 1.0.
        """
    )
    def _line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineWidth,
                        self.line_width)

    diffuse = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the diffuse lighting coefficient.
        """
    )
    def _diffuse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuse,
                        self.diffuse)

    def _get_material(self):
        return wrap_vtk(self._vtk_obj.GetMaterial())
    material = traits.Property(_get_material, help=\
        """
        Get the material representation used for shading. The material
        will be used only when shading is enabled.
        """
    )

    def _get_material_name(self):
        return self._vtk_obj.GetMaterialName()
    material_name = traits.Property(_get_material_name, help=\
        """
        Returns the name of the material currenly loaded, if any.
        """
    )

    def _get_number_of_textures(self):
        return self._vtk_obj.GetNumberOfTextures()
    number_of_textures = traits.Property(_get_number_of_textures, help=\
        """
        Returns the number of textures in this property.
        """
    )

    def _get_shader_program(self):
        return wrap_vtk(self._vtk_obj.GetShaderProgram())
    shader_program = traits.Property(_get_shader_program, help=\
        """
        Get the Shader program. If Material is not set/or not loaded
        properly, this will return null.
        """
    )

    def add_shader_variable(self, *args):
        """
        V.add_shader_variable(string, int)
        C++: void AddShaderVariable(const char *name, int v)
        V.add_shader_variable(string, float)
        C++: void AddShaderVariable(const char *name, double v)
        V.add_shader_variable(string, int, int)
        C++: void AddShaderVariable(const char *name, int v1, int v2)
        V.add_shader_variable(string, float, float)
        C++: void AddShaderVariable(const char *name, double v1,
            double v2)
        V.add_shader_variable(string, int, int, int)
        C++: void AddShaderVariable(const char *name, int v1, int v2,
            int v3)
        V.add_shader_variable(string, float, float, float)
        C++: void AddShaderVariable(const char *name, double v1,
            double v2, double v3)
        Methods to provide to add shader variables from tcl.
        """
        ret = self._wrap_call(self._vtk_obj.AddShaderVariable, *args)
        return ret

    def backface_render(self, *args):
        """
        V.backface_render(Actor, Renderer)
        C++: virtual void BackfaceRender(Actor *, Renderer *)
        This method renders the property as a backface property.
        two_sided_lighting must be turned off to see any backface
        properties. Note that only colors and opacity are used for
        backface properties. Other properties such as Representation,
        Culling are specified by the Property.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BackfaceRender, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Property)
        C++: void DeepCopy(Property *p)
        Assign one property to another.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def load_material(self, *args):
        """
        V.load_material(string)
        C++: void LoadMaterial(const char *name)
        V.load_material(XMLMaterial)
        C++: void LoadMaterial(XMLMaterial *)
        Load the material. The material can be the name of a built-on
        material or the filename for a VTK material XML description.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.LoadMaterial, *my_args)
        return ret

    def load_material_from_string(self, *args):
        """
        V.load_material_from_string(string)
        C++: void LoadMaterialFromString(const char *materialxml)
        Load the material given the contents of the material file.
        """
        ret = self._wrap_call(self._vtk_obj.LoadMaterialFromString, *args)
        return ret

    def post_render(self, *args):
        """
        V.post_render(Actor, Renderer)
        C++: virtual void PostRender(Actor *, Renderer *)
        This method is called after the actor has been rendered. Don't
        call this directly. This method cleans up any shaders allocated.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PostRender, *my_args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *win)
        Release any graphics resources that are being consumed by this
        property. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def remove_all_textures(self):
        """
        V.remove_all_textures()
        C++: void RemoveAllTextures()
        Remove all the textures.
        """
        ret = self._vtk_obj.RemoveAllTextures()
        return ret
        

    def remove_texture(self, *args):
        """
        V.remove_texture(int)
        C++: void RemoveTexture(int unit)
        V.remove_texture(string)
        C++: void RemoveTexture(const char *name)
        Set/Get the texture object to control rendering texture maps. 
        This will be a Texture object. A property does not need to
        have an associated texture map and multiple properties can share
        one texture. Textures must be assigned unique names.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveTexture, *args)
        return ret

    def render(self, *args):
        """
        V.render(Actor, Renderer)
        C++: virtual void Render(Actor *, Renderer *)
        This method causes the property to set up whatever is required
        for its instance variables. This is actually handled by a
        subclass of Property, which is created automatically. This
        method includes the invoking actor as an argument which can be
        used by property devices that require the actor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

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
            return super(Property, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Property properties', scrollable=True, resizable=True,
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
            title='Edit Property properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Property properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __getstate__(self):
        d = tvtk_base.TVTKBase.__getstate__(self)
        del d['color']
        return d
    
    def __setstate__(self, dict):
        tvtk_base.TVTKBase.__setstate__(self, dict)
        self.update_traits()

