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

from tvtk.tvtk_classes.viewport import Viewport


class Renderer(Viewport):
    """
    Renderer - abstract specification for renderers
    
    Superclass: Viewport
    
    Renderer provides an abstract specification for renderers. A
    renderer is an object that controls the rendering process for
    objects. Rendering is the process of converting geometry, a
    specification for lights, and a camera view into an image.
    Renderer also performs coordinate transformation between world
    coordinates, view coordinates (the computer graphics rendering
    coordinate system), and display coordinates (the actual screen
    coordinates on the display device). Certain advanced rendering
    features such as two-sided lighting can also be controlled.
    
    See Also:
    
    RenderWindow Actor Camera Light Volume
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderer, obj, update, **traits)
    
    two_sided_lighting = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off two-sided lighting of surfaces. If two-sided lighting
        is off, then only the side of the surface facing the light(s)
        will be lit, and the other side dark. If two-sided lighting on,
        both sides of the surface will be lit.
        """
    )
    def _two_sided_lighting_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoSidedLighting,
                        self.two_sided_lighting_)

    draw = tvtk_base.true_bool_trait(help=\
        """
        When this flag is off, render commands are ignored.  It is used
        to either multiplex a RenderWindow or render only part of a
        RenderWindow. By default, Draw is on.
        """
    )
    def _draw_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDraw,
                        self.draw_)

    use_depth_peeling = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off rendering of translucent material with depth peeling
        technique. The render window must have alpha bits (ie call
        set_alpha_bit_planes(_1)) and no multisample buffer (ie call
        set_multi_samples(_0) ) to support depth peeling. If use_depth_peeling
        is on and the GPU supports it, depth peeling is used for
        rendering translucent materials. If use_depth_peeling is off, alpha
        blending is used. Initial value is off.
        """
    )
    def _use_depth_peeling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDepthPeeling,
                        self.use_depth_peeling_)

    light_follow_camera = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the automatic repositioning of lights as the camera
        moves. If light_follow_camera is on, lights that are designated as
        Headlights or camera_lights will be adjusted to move with this
        renderer's camera. If light_follow_camera is off, the lights will
        not be adjusted.
        
        (Note: In previous versions of vtk, this light-tracking
        functionality was part of the interactors, not the renderer. For
        backwards compatibility, the older, more limited interactor
        behavior is enabled by default. To disable this mode, turn the
        interactor's light_follow_camera flag OFF, and leave the renderer's
        light_follow_camera flag ON.)
        """
    )
    def _light_follow_camera_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLightFollowCamera,
                        self.light_follow_camera_)

    preserve_depth_buffer = tvtk_base.false_bool_trait(help=\
        """
        Normally a renderer is treated as transparent if Layer > 0. To
        treat a renderer at Layer 0 as transparent, set this flag to
        true.
        """
    )
    def _preserve_depth_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveDepthBuffer,
                        self.preserve_depth_buffer_)

    erase = tvtk_base.true_bool_trait(help=\
        """
        When this flag is off, the renderer will not erase the background
        or the Zbuffer.  It is used to have overlapping renderers. Both
        the render_window Erase and Render Erase must be on for the camera
        to clear the renderer.  By default, Erase is on.
        """
    )
    def _erase_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErase,
                        self.erase_)

    automatic_light_creation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off a flag which disables the automatic light creation
        capability. Normally in VTK if no lights are associated with the
        renderer, then a light is automatically created. However, in
        special circumstances this feature is undesirable, so the
        following boolean is provided to disable automatic light
        creation. (Turn automatic_light_creation off if you do not want
        lights to be created.)
        """
    )
    def _automatic_light_creation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticLightCreation,
                        self.automatic_light_creation_)

    textured_background = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether this viewport should have a textured background.
        Default is off.
        """
    )
    def _textured_background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTexturedBackground,
                        self.textured_background_)

    backing_store = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off using backing store. This may cause the re-rendering
        time to be slightly slower when the view changes. But it is much
        faster when the image has not changed, such as during an expose
        event.
        """
    )
    def _backing_store_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackingStore,
                        self.backing_store_)

    interactive = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off interactive status.  An interactive renderer is one
        that can receive events from an interactor.  Should only be set
        if there are multiple renderers in the same section of the
        viewport.
        """
    )
    def _interactive_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractive,
                        self.interactive_)

    layer = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the layer that this renderer belongs to.  This is only
        used if there are layered renderers.
        """
    )
    def _layer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayer,
                        self.layer)

    maximum_number_of_peels = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        In case of depth peeling, define the maximum number of peeling
        layers. Initial value is 4. A special value of 0 means no maximum
        limit. It has to be a positive value.
        """
    )
    def _maximum_number_of_peels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPeels,
                        self.maximum_number_of_peels)

    allocated_render_time = traits.Float(100.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the amount of time this renderer is allowed to spend
        rendering its scene. This is used by LODActor's.
        """
    )
    def _allocated_render_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllocatedRenderTime,
                        self.allocated_render_time)

    occlusion_ratio = traits.Trait(0.0, traits.Range(0.0, 0.5, enter_set=True, auto_set=False), help=\
        """
        In case of use of depth peeling technique for rendering
        translucent material, define the threshold under which the
        algorithm stops to iterate over peel layers. This is the ratio of
        the number of pixels that have been touched by the last layer
        over the total number of pixels of the viewport area. Initial
        value is 0.0, meaning rendering have to be exact. Greater values
        may speed-up the rendering with small impact on the quality.
        """
    )
    def _occlusion_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOcclusionRatio,
                        self.occlusion_ratio)

    def _get_pass_(self):
        return wrap_vtk(self._vtk_obj.GetPass())
    def _set_pass_(self, arg):
        old_val = self._get_pass_()
        self._wrap_call(self._vtk_obj.SetPass,
                        deref_vtk(arg))
        self.trait_property_changed('pass_', old_val, arg)
    pass_ = traits.Property(_get_pass_, _set_pass_, help=\
        """
        Set/Get a custom render pass. Initial value is NULL.
        """
    )

    near_clipping_plane_tolerance = traits.Trait(0.0, traits.Range(0.0, 0.98999999999999999, enter_set=True, auto_set=False), help=\
        """
        Specify tolerance for near clipping plane distance to the camera
        as a percentage of the far clipping plane distance. By default
        this will be set to 0.01 for 16 bit zbuffers and 0.001 for higher
        depth z buffers
        """
    )
    def _near_clipping_plane_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNearClippingPlaneTolerance,
                        self.near_clipping_plane_tolerance)

    def _get_background_texture(self):
        return wrap_vtk(self._vtk_obj.GetBackgroundTexture())
    def _set_background_texture(self, arg):
        old_val = self._get_background_texture()
        self._wrap_call(self._vtk_obj.SetBackgroundTexture,
                        deref_vtk(arg))
        self.trait_property_changed('background_texture', old_val, arg)
    background_texture = traits.Property(_get_background_texture, _set_background_texture, help=\
        """
        Set/Get the texture to be used for the background. If set and
        enabled this gets the priority over the gradient background.
        """
    )

    def _get_delegate(self):
        return wrap_vtk(self._vtk_obj.GetDelegate())
    def _set_delegate(self, arg):
        old_val = self._get_delegate()
        self._wrap_call(self._vtk_obj.SetDelegate,
                        deref_vtk(arg))
        self.trait_property_changed('delegate', old_val, arg)
    delegate = traits.Property(_get_delegate, _set_delegate, help=\
        """
        Set/Get a custom Render call. Allows to hook a Render call from
        an external project.It will be used in place of
        Renderer::Render() if it is not NULL and its Used ivar is set
        to true. Initial value is NULL.
        """
    )

    ambient = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _ambient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbient,
                        self.ambient)

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Specify the rendering window in which to draw. This is
        automatically set when the renderer is created by make_renderer. 
        The user probably shouldn't ever need to call this method.
        """
    )

    def _get_active_camera(self):
        return wrap_vtk(self._vtk_obj.GetActiveCamera())
    def _set_active_camera(self, arg):
        old_val = self._get_active_camera()
        self._wrap_call(self._vtk_obj.SetActiveCamera,
                        deref_vtk(arg))
        self.trait_property_changed('active_camera', old_val, arg)
    active_camera = traits.Property(_get_active_camera, _set_active_camera, help=\
        """
        Get the current camera. If there is not camera assigned to the
        renderer already, a new one is created automatically. This does
        *not* reset the camera.
        """
    )

    def _get_actors(self):
        return wrap_vtk(self._vtk_obj.GetActors())
    actors = traits.Property(_get_actors, help=\
        """
        Return any actors in this renderer.
        """
    )

    def _get_cullers(self):
        return wrap_vtk(self._vtk_obj.GetCullers())
    cullers = traits.Property(_get_cullers, help=\
        """
        Return the collection of cullers.
        """
    )

    def _get_last_render_time_in_seconds(self):
        return self._vtk_obj.GetLastRenderTimeInSeconds()
    last_render_time_in_seconds = traits.Property(_get_last_render_time_in_seconds, help=\
        """
        Get the time required, in seconds, for the last Render call.
        """
    )

    def _get_last_rendering_used_depth_peeling(self):
        return self._vtk_obj.GetLastRenderingUsedDepthPeeling()
    last_rendering_used_depth_peeling = traits.Property(_get_last_rendering_used_depth_peeling, help=\
        """
        Tells if the last call to
        device_render_translucent_polygonal_geometry() actually used depth
        peeling. Initial value is false.
        """
    )

    def _get_lights(self):
        return wrap_vtk(self._vtk_obj.GetLights())
    lights = traits.Property(_get_lights, help=\
        """
        Return the collection of lights.
        """
    )

    def _get_number_of_props_rendered(self):
        return self._vtk_obj.GetNumberOfPropsRendered()
    number_of_props_rendered = traits.Property(_get_number_of_props_rendered, help=\
        """
        Should be used internally only during a render Get the number of
        props that were rendered using a render_opaque_geometry or
        render_translucent_polygonal_geometry call. This is used to know if
        something is in the frame buffer.
        """
    )

    def _get_selector(self):
        return wrap_vtk(self._vtk_obj.GetSelector())
    selector = traits.Property(_get_selector, help=\
        """
        Get the current hardware selector. If the Selector is set, it
        implies the current render pass is for selection.
        Mappers/Properties may choose to behave differently when
        rendering for hardware selection.
        """
    )

    def _get_tiled_aspect_ratio(self):
        return self._vtk_obj.GetTiledAspectRatio()
    tiled_aspect_ratio = traits.Property(_get_tiled_aspect_ratio, help=\
        """
        Compute the aspect ratio of this renderer for the current tile.
        When tiled displays are used the aspect ratio of the renderer for
        a given tile may be diferent that the aspect ratio of the
        renderer when rendered in it entirity
        """
    )

    def _get_time_factor(self):
        return self._vtk_obj.GetTimeFactor()
    time_factor = traits.Property(_get_time_factor, help=\
        """
        Get the ratio between allocated time and actual render time.
        time_factor has been taken out of the render process. It is still
        computed in case someone finds it useful. It may be taken away in
        the future.
        """
    )

    def _get_volumes(self):
        return wrap_vtk(self._vtk_obj.GetVolumes())
    volumes = traits.Property(_get_volumes, help=\
        """
        Return the collection of volumes.
        """
    )

    def get_z(self, *args):
        """
        V.get_z(int, int) -> float
        C++: double GetZ(int x, int y)
        Given a pixel location, return the Z value. The z value is
        normalized (0,1) between the front and back clipping planes.
        """
        ret = self._wrap_call(self._vtk_obj.GetZ, *args)
        return ret

    def add_actor(self, *args):
        """
        V.add_actor(Prop)
        C++: void AddActor(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddActor, *my_args)
        return ret

    def add_culler(self, *args):
        """
        V.add_culler(Culler)
        C++: void AddCuller(Culler *)
        Add an culler to the list of cullers.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddCuller, *my_args)
        return ret

    def add_light(self, *args):
        """
        V.add_light(Light)
        C++: void AddLight(Light *)
        Add a light to the list of lights.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLight, *my_args)
        return ret

    def add_volume(self, *args):
        """
        V.add_volume(Prop)
        C++: void AddVolume(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddVolume, *my_args)
        return ret

    def clear(self):
        """
        V.clear()
        C++: virtual void Clear()
        Clear the image to the background color.
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def compute_visible_prop_bounds(self, *args):
        """
        V.compute_visible_prop_bounds([float, float, float, float, float,
            float])
        C++: void ComputeVisiblePropBounds(double bounds[6])
        V.compute_visible_prop_bounds() -> (float, float, float, float,
            float, float)
        C++: double *ComputeVisiblePropBounds()
        Compute the bounding box of all the visible props Used in
        reset_camera() and reset_camera_clipping_range()
        """
        ret = self._wrap_call(self._vtk_obj.ComputeVisiblePropBounds, *args)
        return ret

    def create_light(self):
        """
        V.create_light()
        C++: void CreateLight(void)
        Create and add a light to renderer.
        """
        ret = self._vtk_obj.CreateLight()
        return ret
        

    def device_render(self):
        """
        V.device_render()
        C++: virtual void DeviceRender()
        Create an image. Subclasses of Renderer must implement this
        method.
        """
        ret = self._vtk_obj.DeviceRender()
        return ret
        

    def device_render_translucent_polygonal_geometry(self):
        """
        V.device_render_translucent_polygonal_geometry()
        C++: virtual void DeviceRenderTranslucentPolygonalGeometry()
        Render translucent polygonal geometry. Default implementation
        just call update_translucent_polygonal_geometry(). Subclasses of
        Renderer that can deal with depth peeling must override this
        method. It updates boolean ivar last_rendering_used_depth_peeling.
        """
        ret = self._vtk_obj.DeviceRenderTranslucentPolygonalGeometry()
        return ret
        

    def is_active_camera_created(self):
        """
        V.is_active_camera_created() -> int
        C++: int IsActiveCameraCreated()
        This method returns 1 if the active_camera has already been set or
        automatically created by the renderer. It returns 0 if the
        active_camera does not yet exist.
        """
        ret = self._vtk_obj.IsActiveCameraCreated()
        return ret
        

    def make_camera(self):
        """
        V.make_camera() -> Camera
        C++: virtual Camera *MakeCamera()
        Create a new Camera sutible for use with this type of Renderer.
        For example, a MesaRenderer should create a MesaCamera in
        this function.   The default is to just call Camera::New.
        """
        ret = wrap_vtk(self._vtk_obj.MakeCamera())
        return ret
        

    def make_light(self):
        """
        V.make_light() -> Light
        C++: virtual Light *MakeLight()
        Create a new Light sutible for use with this type of Renderer.
        For example, a MesaRenderer should create a MesaLight in
        this function.   The default is to just call Light::New.
        """
        ret = wrap_vtk(self._vtk_obj.MakeLight())
        return ret
        

    def remove_actor(self, *args):
        """
        V.remove_actor(Prop)
        C++: void RemoveActor(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveActor, *my_args)
        return ret

    def remove_all_lights(self):
        """
        V.remove_all_lights()
        C++: void RemoveAllLights()
        Remove all lights from the list of lights.
        """
        ret = self._vtk_obj.RemoveAllLights()
        return ret
        

    def remove_culler(self, *args):
        """
        V.remove_culler(Culler)
        C++: void RemoveCuller(Culler *)
        Remove an actor from the list of cullers.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveCuller, *my_args)
        return ret

    def remove_light(self, *args):
        """
        V.remove_light(Light)
        C++: void RemoveLight(Light *)
        Remove a light from the list of lights.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveLight, *my_args)
        return ret

    def remove_volume(self, *args):
        """
        V.remove_volume(Prop)
        C++: void RemoveVolume(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveVolume, *my_args)
        return ret

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        CALLED BY RenderWindow ONLY. End-user pass your way and call
        RenderWindow::Render(). Create an image. This is a superclass
        method which will in turn call the device_render method of
        Subclasses of Renderer.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def reset_camera(self, *args):
        """
        V.reset_camera()
        C++: void ResetCamera()
        V.reset_camera([float, float, float, float, float, float])
        C++: void ResetCamera(double bounds[6])
        V.reset_camera(float, float, float, float, float, float)
        C++: void ResetCamera(double xmin, double xmax, double ymin,
            double ymax, double zmin, double zmax)
        Automatically set up the camera based on the visible actors. The
        camera will reposition itself to view the center point of the
        actors, and move along its initial view plane normal (i.e.,
        vector defined from camera position to focal point) so that all
        of the actors can be seen.
        """
        ret = self._wrap_call(self._vtk_obj.ResetCamera, *args)
        return ret

    def reset_camera_clipping_range(self, *args):
        """
        V.reset_camera_clipping_range()
        C++: void ResetCameraClippingRange()
        V.reset_camera_clipping_range([float, float, float, float, float,
            float])
        C++: void ResetCameraClippingRange(double bounds[6])
        V.reset_camera_clipping_range(float, float, float, float, float,
            float)
        C++: void ResetCameraClippingRange(double xmin, double xmax,
            double ymin, double ymax, double zmin, double zmax)
        Reset the camera clipping range based on the bounds of the
        visible actors. This ensures that no props are cut off
        """
        ret = self._wrap_call(self._vtk_obj.ResetCameraClippingRange, *args)
        return ret

    def set_light_collection(self, *args):
        """
        V.set_light_collection(LightCollection)
        C++: void SetLightCollection(LightCollection *lights)
        Set the collection of lights. We cannot name it set_lights because
        of test_set_get
        \pre lights_exist: lights!=0
        \post lights_set: lights==this->_get_lights()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLightCollection, *my_args)
        return ret

    def stereo_midpoint(self):
        """
        V.stereo_midpoint()
        C++: virtual void StereoMidpoint()
        Do anything necessary between rendering the left and right
        viewpoints in a stereo render. Doesn't do anything except in the
        derived IceTRenderer in para_view.
        """
        ret = self._vtk_obj.StereoMidpoint()
        return ret
        

    def transparent(self):
        """
        V.transparent() -> int
        C++: int Transparent()
        Returns a boolean indicating if this renderer is transparent.  It
        is transparent if it is not in the deepest layer of its render
        window.
        """
        ret = self._vtk_obj.Transparent()
        return ret
        

    def update_lights_geometry_to_follow_camera(self):
        """
        V.update_lights_geometry_to_follow_camera() -> int
        C++: virtual int UpdateLightsGeometryToFollowCamera(void)
        Ask the lights in the scene that are not in world space (for
        instance, Headlights or camera_lights that are attached to the
        camera) to update their geometry to match the active camera.
        """
        ret = self._vtk_obj.UpdateLightsGeometryToFollowCamera()
        return ret
        

    def visible_actor_count(self):
        """
        V.visible_actor_count() -> int
        C++: int VisibleActorCount()
        Returns the number of visible actors.
        """
        ret = self._vtk_obj.VisibleActorCount()
        return ret
        

    def visible_volume_count(self):
        """
        V.visible_volume_count() -> int
        C++: int VisibleVolumeCount()
        Returns the number of visible volumes.
        """
        ret = self._vtk_obj.VisibleVolumeCount()
        return ret
        

    _updateable_traits_ = \
    (('layer', 'GetLayer'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('maximum_number_of_peels',
    'GetMaximumNumberOfPeels'), ('two_sided_lighting',
    'GetTwoSidedLighting'), ('pixel_aspect', 'GetPixelAspect'),
    ('background', 'GetBackground'), ('draw', 'GetDraw'), ('view_point',
    'GetViewPoint'), ('background2', 'GetBackground2'), ('debug',
    'GetDebug'), ('erase', 'GetErase'), ('occlusion_ratio',
    'GetOcclusionRatio'), ('aspect', 'GetAspect'), ('ambient',
    'GetAmbient'), ('textured_background', 'GetTexturedBackground'),
    ('viewport', 'GetViewport'), ('preserve_depth_buffer',
    'GetPreserveDepthBuffer'), ('display_point', 'GetDisplayPoint'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('automatic_light_creation', 'GetAutomaticLightCreation'),
    ('near_clipping_plane_tolerance', 'GetNearClippingPlaneTolerance'),
    ('backing_store', 'GetBackingStore'), ('use_depth_peeling',
    'GetUseDepthPeeling'), ('world_point', 'GetWorldPoint'),
    ('light_follow_camera', 'GetLightFollowCamera'), ('reference_count',
    'GetReferenceCount'), ('gradient_background',
    'GetGradientBackground'), ('interactive', 'GetInteractive'))
    
    _full_traitnames_list_ = \
    (['automatic_light_creation', 'backing_store', 'debug', 'draw',
    'erase', 'global_warning_display', 'gradient_background',
    'interactive', 'light_follow_camera', 'preserve_depth_buffer',
    'textured_background', 'two_sided_lighting', 'use_depth_peeling',
    'allocated_render_time', 'ambient', 'aspect', 'background',
    'background2', 'display_point', 'layer', 'maximum_number_of_peels',
    'near_clipping_plane_tolerance', 'occlusion_ratio', 'pixel_aspect',
    'view_point', 'viewport', 'world_point'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Renderer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Renderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_light_creation', 'backing_store', 'draw',
            'erase', 'gradient_background', 'interactive', 'light_follow_camera',
            'preserve_depth_buffer', 'textured_background', 'two_sided_lighting',
            'use_depth_peeling'], [], ['allocated_render_time', 'ambient',
            'aspect', 'background', 'background2', 'display_point', 'layer',
            'maximum_number_of_peels', 'near_clipping_plane_tolerance',
            'occlusion_ratio', 'pixel_aspect', 'view_point', 'viewport',
            'world_point']),
            title='Edit Renderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Renderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

