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


class LightKit(Object):
    """
    LightKit - a simple but quality lighting kit
    
    Superclass: Object
    
    LightKit is designed to make general purpose lighting of vtk
    scenes simple, flexible, and attractive (or at least not horribly
    ugly without significant effort).  Use a light_kit when you want more
    control over your lighting than you can get with the default vtk
    light, which is a headlight located at the camera. (_head_lights are
    very simple to use, but they don't show the shape of objects very
    well, don't give a good sense of "up" and "down", and don't evenly
    light the object.)
    
    A light_kit consists of three lights, a key light, a fill light, and a
    headlight.  The main light is the key light.  It is usually
    positioned so that it appears like an overhead light (like the sun,
    or a ceiling light).  It is generally positioned to shine down on the
    scene from about a 45 degree angle vertically and at least a little
    offset side to side.  The key light usually at least about twice as
    bright as the total of all other lights in the scene to provide good
    modeling of object features.
    
    The other lights in the kit (the fill light, headlight, and a pair of
    back lights) are weaker sources that provide extra illumination to
    fill in the spots that the key light misses.  The fill light is
    usually positioned across from or opposite from the key light (though
    still on the same side of the object as the camera) in order to
    simulate diffuse reflections from other objects in the scene.  The
    headlight, always located at the position of the camera, reduces the
    contrast between areas lit by the key and fill light. The two back
    lights, one on the left of the object as seen from the observer and
    one on the right, fill on the high-contrast areas behind the object. 
    To enforce the relationship between the different lights, the
    intensity of the fill, back and headlights are set as a ratio to the
    key light brightness.  Thus, the brightness of all the lights in the
    scene can be changed by changing the key light intensity.
    
    All lights are directional lights (infinitely far away with no
    falloff).  Lights move with the camera.
    
    For simplicity, the position of lights in the light_kit can only be
    specified using angles: the elevation (latitude) and azimuth
    (longitude) of each light with respect to the camera, expressed in
    degrees.  (Lights always shine on the camera's lookat point.) For
    example, a light at (elevation=0, azimuth=0) is located at the camera
    (a headlight).  A light at (elevation=90, azimuth=0) is above the
    lookat point, shining down.  Negative azimuth values move the lights
    clockwise as seen above, positive values counter-clockwise.  So, a
    light at (elevation=45, azimuth=-20) is above and in front of the
    object and shining slightly from the left side.
    
    LightKit limits the colors that can be assigned to any light to
    those of incandescent sources such as light bulbs and sunlight.  It
    defines a special color spectrum called "warmth" from which light
    colors can be chosen, where 0 is cold blue, 0.5 is neutral white, and
    1 is deep sunset red.  Colors close to 0.5 are "cool whites" and "warm
    whites," respectively.
    
    Since colors far from white on the warmth scale appear less bright,
    key-to-fill and key-to-headlight ratios are skewed by key, fill, and
    headlight colors.  If the flag maintain_luminance is set, LightKit
    will attempt to compensate for these perceptual differences by
    increasing the brightness of more saturated colors.
    
    A light_kit is not explicitly part of the vtk pipeline.  Rather, it is
    a composite object that controls the behavior of lights using a
    unified user interface.  Every time a parameter of LightKit is
    adjusted, the properties of its lights are modified.
    
    Credits:
    
    LightKit was originally written and contributed to vtk by Michael
    Halle (mhalle@bwh.harvard.edu) at the Surgical Planning Lab, Brigham
    and Women's Hospital.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLightKit, obj, update, **traits)
    
    maintain_luminance = tvtk_base.false_bool_trait(help=\
        """
        If maintain_luminance is set, the light_kit will attempt to
        maintain the apparent intensity of lights based on their
        perceptual brightnesses. By default, maintain_luminance is off.
        """
    )
    def _maintain_luminance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaintainLuminance,
                        self.maintain_luminance_)

    fill_light_angle = traits.Array(shape=(2,), value=(-75.0, -10.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _fill_light_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillLightAngle,
                        self.fill_light_angle)

    head_light_warmth = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _head_light_warmth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeadLightWarmth,
                        self.head_light_warmth)

    back_light_warmth = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _back_light_warmth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackLightWarmth,
                        self.back_light_warmth)

    fill_light_elevation = traits.Float(-75.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _fill_light_elevation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillLightElevation,
                        self.fill_light_elevation)

    back_light_angle = traits.Array(shape=(2,), value=(0.0, 110.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _back_light_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackLightAngle,
                        self.back_light_angle)

    key_to_head_ratio = traits.Trait(3.0, traits.Range(0.5, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the key-to-headlight ratio.  Similar to the key-to-fill
        ratio, this ratio controls how bright the headlight light is
        compared to the key light: larger values correspond to a dimmer
        headlight light.  The headlight is special kind of fill light,
        lighting only the parts of the object that the camera can see. As
        such, a headlight tends to reduce the contrast of a scene.  It
        can be used to fill in "shadows" of the object missed by the key
        and fill lights.  The headlight should always be significantly
        dimmer than the key light:  ratios of 2 to 15 are typical.
        """
    )
    def _key_to_head_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyToHeadRatio,
                        self.key_to_head_ratio)

    key_to_fill_ratio = traits.Trait(3.0, traits.Range(0.5, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the key-to-fill ratio.  This ratio controls how bright
        the fill light is compared to the key light: larger values
        correspond to a dimmer fill light.  The purpose of the fill light
        is to light parts of the object not lit by the key light, while
        still maintaining constrast.  This type of lighting may
        correspond to indirect illumination from the key light, bounced
        off a wall, floor, or other object.  The fill light should never
        be brighter than the key light:  a good range for the key-to-fill
        ratio is between 2 and 10.
        """
    )
    def _key_to_fill_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyToFillRatio,
                        self.key_to_fill_ratio)

    fill_light_warmth = traits.Float(0.4, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _fill_light_warmth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillLightWarmth,
                        self.fill_light_warmth)

    key_light_intensity = traits.Float(0.75, enter_set=True, auto_set=False, help=\
        """
        Set/Get the intensity of the key light.  The key light is the
        brightest light in the scene.  The intensities of the other two
        lights are ratios of the key light's intensity.
        """
    )
    def _key_light_intensity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyLightIntensity,
                        self.key_light_intensity)

    back_light_azimuth = traits.Float(110.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _back_light_azimuth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackLightAzimuth,
                        self.back_light_azimuth)

    back_light_elevation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _back_light_elevation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackLightElevation,
                        self.back_light_elevation)

    fill_light_azimuth = traits.Float(-10.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _fill_light_azimuth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillLightAzimuth,
                        self.fill_light_azimuth)

    key_light_angle = traits.Array(shape=(2,), value=(50.0, 10.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get/Set the position of the key, fill, and back lights using
        angular methods.  Elevation corresponds to latitude, azimuth to
        longitude.  It is recommended that the key light always be on the
        viewer's side of the object and above the object, while the fill
        light generally lights the part of the object not lit by the fill
        light.  The headlight, which is always located at the viewer, can
        then be used to reduce the contrast in the image. There are a
        pair of back lights.  They are located at the same elevation and
        at opposing azimuths (ie, one to the left, and one to the right).
         They are generally set at the equator (elevation = 0), and at
        approximately 120 degrees (lighting from each side and behind).
        """
    )
    def _key_light_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyLightAngle,
                        self.key_light_angle)

    key_to_back_ratio = traits.Trait(3.5, traits.Range(0.5, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the key-to-back light ratio.  This ratio controls how
        bright the back lights are compared to the key light: larger
        values correspond to dimmer back lights.  The back lights fill in
        the remaining high-contrast regions behind the object. Values
        between 2 and 10 are good.
        """
    )
    def _key_to_back_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyToBackRatio,
                        self.key_to_back_ratio)

    key_light_azimuth = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _key_light_azimuth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyLightAzimuth,
                        self.key_light_azimuth)

    key_light_elevation = traits.Float(50.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _key_light_elevation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyLightElevation,
                        self.key_light_elevation)

    headlight_warmth = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        To maintain a deprecation API:
        """
    )
    def _headlight_warmth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeadlightWarmth,
                        self.headlight_warmth)

    key_light_warmth = traits.Float(0.6, enter_set=True, auto_set=False, help=\
        """
        Set the warmth of each the lights.  Warmth is a parameter that
        varies from 0 to 1, where 0 is "cold" (looks icy or lit by a very
        blue sky), 1 is "warm" (the red of a very red sunset, or the
        embers of a campfire), and 0.5 is a neutral white.  The warmth
        scale is non-linear. Warmth values close to 0.5 are subtly
        "warmer" or "cooler," much like a warmer tungsten incandescent
        bulb, a cooler halogen, or daylight (cooler still).  Moving
        further away from 0.5, colors become more quickly varying towards
        blues and reds.  With regards to aesthetics, extremes of warmth
        should be used sparingly.
        """
    )
    def _key_light_warmth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyLightWarmth,
                        self.key_light_warmth)

    def _get_back_light_color(self):
        return self._vtk_obj.GetBackLightColor()
    back_light_color = traits.Property(_get_back_light_color, help=\
        """
        Returns the floating-point RGB values of each of the light's
        color.
        """
    )

    def _get_fill_light_color(self):
        return self._vtk_obj.GetFillLightColor()
    fill_light_color = traits.Property(_get_fill_light_color, help=\
        """
        Returns the floating-point RGB values of each of the light's
        color.
        """
    )

    def _get_head_light_color(self):
        return self._vtk_obj.GetHeadLightColor()
    head_light_color = traits.Property(_get_head_light_color, help=\
        """
        Returns the floating-point RGB values of each of the light's
        color.
        """
    )

    def _get_key_light_color(self):
        return self._vtk_obj.GetKeyLightColor()
    key_light_color = traits.Property(_get_key_light_color, help=\
        """
        Returns the floating-point RGB values of each of the light's
        color.
        """
    )

    def get_short_string_from_sub_type(self, *args):
        """
        V.get_short_string_from_sub_type(int) -> string
        C++: static const char *GetShortStringFromSubType(int subtype)
        Helper method to go from a enum subtype to a string subtype The
        difference from get_string_from_sub_type is that it returns a shorter
        strings (usefull for GUI with minimun space)
        """
        ret = self._wrap_call(self._vtk_obj.GetShortStringFromSubType, *args)
        return ret

    def get_string_from_sub_type(self, *args):
        """
        V.get_string_from_sub_type(int) -> string
        C++: static const char *GetStringFromSubType(int type)
        Helper method to go from a enum subtype to a string subtype
        """
        ret = self._wrap_call(self._vtk_obj.GetStringFromSubType, *args)
        return ret

    def get_string_from_type(self, *args):
        """
        V.get_string_from_type(int) -> string
        C++: static const char *GetStringFromType(int type)
        Helper method to go from a enum type to a string type
        """
        ret = self._wrap_call(self._vtk_obj.GetStringFromType, *args)
        return ret

    def add_lights_to_renderer(self, *args):
        """
        V.add_lights_to_renderer(Renderer)
        C++: void AddLightsToRenderer(Renderer *renderer)
        Add lights to, or remove lights from, a renderer. Lights may be
        added to more than one renderer, if desired.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLightsToRenderer, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(LightKit)
        C++: void DeepCopy(LightKit *kit)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def remove_lights_from_renderer(self, *args):
        """
        V.remove_lights_from_renderer(Renderer)
        C++: void RemoveLightsFromRenderer(Renderer *renderer)
        Add lights to, or remove lights from, a renderer. Lights may be
        added to more than one renderer, if desired.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveLightsFromRenderer, *my_args)
        return ret

    def update(self):
        """
        V.update()
        C++: void Update()"""
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('head_light_warmth', 'GetHeadLightWarmth'), ('back_light_elevation',
    'GetBackLightElevation'), ('fill_light_angle', 'GetFillLightAngle'),
    ('back_light_angle', 'GetBackLightAngle'), ('fill_light_warmth',
    'GetFillLightWarmth'), ('key_to_fill_ratio', 'GetKeyToFillRatio'),
    ('key_light_intensity', 'GetKeyLightIntensity'),
    ('maintain_luminance', 'GetMaintainLuminance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('key_light_azimuth', 'GetKeyLightAzimuth'), ('key_to_head_ratio',
    'GetKeyToHeadRatio'), ('back_light_warmth', 'GetBackLightWarmth'),
    ('headlight_warmth', 'GetHeadlightWarmth'), ('back_light_azimuth',
    'GetBackLightAzimuth'), ('key_light_warmth', 'GetKeyLightWarmth'),
    ('debug', 'GetDebug'), ('fill_light_elevation',
    'GetFillLightElevation'), ('key_to_back_ratio', 'GetKeyToBackRatio'),
    ('key_light_elevation', 'GetKeyLightElevation'),
    ('fill_light_azimuth', 'GetFillLightAzimuth'), ('reference_count',
    'GetReferenceCount'), ('key_light_angle', 'GetKeyLightAngle'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maintain_luminance',
    'back_light_angle', 'back_light_azimuth', 'back_light_elevation',
    'back_light_warmth', 'fill_light_angle', 'fill_light_azimuth',
    'fill_light_elevation', 'fill_light_warmth', 'head_light_warmth',
    'headlight_warmth', 'key_light_angle', 'key_light_azimuth',
    'key_light_elevation', 'key_light_intensity', 'key_light_warmth',
    'key_to_back_ratio', 'key_to_fill_ratio', 'key_to_head_ratio'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LightKit, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LightKit properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['maintain_luminance'], [], ['back_light_angle',
            'back_light_azimuth', 'back_light_elevation', 'back_light_warmth',
            'fill_light_angle', 'fill_light_azimuth', 'fill_light_elevation',
            'fill_light_warmth', 'head_light_warmth', 'headlight_warmth',
            'key_light_angle', 'key_light_azimuth', 'key_light_elevation',
            'key_light_intensity', 'key_light_warmth', 'key_to_back_ratio',
            'key_to_fill_ratio', 'key_to_head_ratio']),
            title='Edit LightKit properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LightKit properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

