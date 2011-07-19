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


class Light(Object):
    """
    Light - a virtual light for 3d rendering
    
    Superclass: Object
    
    Light is a virtual light for 3d rendering. It provides methods to
    locate and point the light, turn it on and off, and set its
    brightness and color. In addition to the basic infinite distance
    point light source attributes, you also can specify the light
    attenuation values and cone angle. These attributes are only used if
    the light is a positional light. The default is a directional light
    (e.g. infinite point light source).
    
    Lights have a type that describes how the light should move with
    respect to the camera.  A Headlight is always located at the current
    camera position and shines on the camera's focal point.  A
    camera_light also moves with the camera, but may not be coincident to
    it.  camera_lights are defined in a normalized coordinate space where
    the camera is located at (0, 0, 1), the camera is looking at (0, 0,
    0), and up is (0, 1, 0).  Finally, a scene_light is part of the scene
    itself and does not move with the camera. (Renderers are responsible
    for moving the light based on its type.)
    
    Lights have a transformation matrix that describes the space in which
    they are positioned.  A light's world space position and focal point
    are defined by their local position and focal point, transformed by
    their transformation matrix (if it exists).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLight, obj, update, **traits)
    
    positional = tvtk_base.false_bool_trait(help=\
        """
        Turn positional lighting on or off.
        """
    )
    def _positional_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositional,
                        self.positional_)

    switch = tvtk_base.true_bool_trait(help=\
        """
        Turn the light on or off.
        """
    )
    def _switch_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwitch,
                        self.switch_)

    light_type = traits.Trait('scene_light',
    tvtk_base.TraitRevPrefixMap({'camera_light': 2, 'headlight': 1, 'scene_light': 3}), help=\
        """
        Set/Get the type of the light. A scene_light is a light located in
        the world coordinate space.  A light is initially created as a
        scene light.
        
        A Headlight is always located at the camera and is pointed at the
        camera's focal point.  The renderer is free to modify the
        position and focal point of the camera at any time.
        
        A camera_light is also attached to the camera, but is not
        necessarily located at the camera's position.  camera_lights are
        defined in a coordinate space where the camera is located at (0,
        0, 1), looking towards (0, 0, 0) at a distance of 1, with up
        being (0, 1, 0).
        
        Note: Use set_light_type_to_scene_light, rather than set_light_type(_3),
        since the former clears the light's transform matrix.
        """
    )
    def _light_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLightType,
                        self.light_type_)

    exponent = traits.Trait(1.0, traits.Range(0.0, 128.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the exponent of the cosine used in positional lighting.
        """
    )
    def _exponent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponent,
                        self.exponent)

    diffuse_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _diffuse_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuseColor,
                        self.diffuse_color, True)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        Set/Get the color of the light. It is possible to set the
        ambient, diffuse and specular colors separately. The set_color()
        method sets the diffuse and specular colors to the same color
        (this is a feature to preserve backward compatbility.)
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, True)

    cone_angle = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the lighting cone angle of a positional light in degrees.
        This is the angle between the axis of the cone and a ray along
        the edge of the cone. A value of 180 indicates that you want no
        spot lighting effects just a positional light.
        """
    )
    def _cone_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConeAngle,
                        self.cone_angle)

    ambient_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _ambient_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbientColor,
                        self.ambient_color, True)

    intensity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the brightness of the light (from one to zero).
        """
    )
    def _intensity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntensity,
                        self.intensity)

    specular_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _specular_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecularColor,
                        self.specular_color, True)

    def _get_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetTransformMatrix())
    def _set_transform_matrix(self, arg):
        old_val = self._get_transform_matrix()
        self._wrap_call(self._vtk_obj.SetTransformMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('transform_matrix', old_val, arg)
    transform_matrix = traits.Property(_get_transform_matrix, _set_transform_matrix, help=\
        """
        Set/Get the light's transformation matrix.  If a matrix is set
        for a light, the light's parameters (position and focal point)
        are transformed by the matrix before being rendered.
        """
    )

    position = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    attenuation_values = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _attenuation_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttenuationValues,
                        self.attenuation_values)

    focal_point = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalPoint,
                        self.focal_point)

    def _get_transformed_focal_point(self):
        return self._vtk_obj.GetTransformedFocalPoint()
    transformed_focal_point = traits.Property(_get_transformed_focal_point, help=\
        """
        Get the focal point of the light, modified by the transformation
        matrix (if it exists).
        """
    )

    def _get_transformed_position(self):
        return self._vtk_obj.GetTransformedPosition()
    transformed_position = traits.Property(_get_transformed_position, help=\
        """
        Get the position of the light, modified by the transformation
        matrix (if it exists).
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(Light)
        C++: void DeepCopy(Light *light)
        Perform deep copy of this light.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def light_type_is_camera_light(self):
        """
        V.light_type_is_camera_light() -> int
        C++: int LightTypeIsCameraLight()
        Query the type of the light.
        """
        ret = self._vtk_obj.LightTypeIsCameraLight()
        return ret
        

    def light_type_is_headlight(self):
        """
        V.light_type_is_headlight() -> int
        C++: int LightTypeIsHeadlight()
        Query the type of the light.
        """
        ret = self._vtk_obj.LightTypeIsHeadlight()
        return ret
        

    def light_type_is_scene_light(self):
        """
        V.light_type_is_scene_light() -> int
        C++: int LightTypeIsSceneLight()
        Query the type of the light.
        """
        ret = self._vtk_obj.LightTypeIsSceneLight()
        return ret
        

    def render(self, *args):
        """
        V.render(Renderer, int)
        C++: virtual void Render(Renderer *, int)
        Abstract interface to renderer. Each concrete subclass of
        Light will load its data into the graphics system in response
        to this method invocation. The actual loading is performed by a
        LightDevice subclass, which will get created automatically.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def set_direction_angle(self, *args):
        """
        V.set_direction_angle(float, float)
        C++: void SetDirectionAngle(double elevation, double azimuth)
        V.set_direction_angle([float, float])
        C++: void SetDirectionAngle(double ang[2])
        Set the position and focal point of a light based on elevation
        and azimuth.  The light is moved so it is shining from the given
        angle. Angles are given in degrees.  If the light is a positional
        light, it is made directional instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetDirectionAngle, *args)
        return ret

    def shallow_clone(self):
        """
        V.shallow_clone() -> Light
        C++: virtual Light *ShallowClone()
        Create a new light object with the same light parameters than the
        current object (any ivar from the superclasses (vtk_object and
        ObjectBase), like reference counting, timestamp and observers
        are not copied). This is a shallow clone (_transform_matrix is
        referenced)
        """
        ret = wrap_vtk(self._vtk_obj.ShallowClone())
        return ret
        

    _updateable_traits_ = \
    (('specular_color', 'GetSpecularColor'), ('exponent', 'GetExponent'),
    ('color', 'GetColor'), ('diffuse_color', 'GetDiffuseColor'),
    ('ambient_color', 'GetAmbientColor'), ('cone_angle', 'GetConeAngle'),
    ('positional', 'GetPositional'), ('debug', 'GetDebug'), ('intensity',
    'GetIntensity'), ('light_type', 'GetLightType'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'),
    ('attenuation_values', 'GetAttenuationValues'), ('focal_point',
    'GetFocalPoint'), ('switch', 'GetSwitch'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'positional', 'switch',
    'light_type', 'ambient_color', 'attenuation_values', 'color',
    'cone_angle', 'diffuse_color', 'exponent', 'focal_point', 'intensity',
    'position', 'specular_color'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Light, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Light properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['positional', 'switch'], ['light_type'],
            ['ambient_color', 'attenuation_values', 'color', 'cone_angle',
            'diffuse_color', 'exponent', 'focal_point', 'intensity', 'position',
            'specular_color']),
            title='Edit Light properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Light properties', scrollable=True, resizable=True,
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

