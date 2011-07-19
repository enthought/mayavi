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


class Prop(Object):
    """
    Prop - abstract superclass for all actors, volumes and annotations
    
    Superclass: Object
    
    Prop is an abstract superclass for any objects that can exist in a
    rendered scene (either 2d or 3d). Instances of Prop may respond to
    various render methods (e.g., render_opaque_geometry()). Prop also
    defines the API for picking, LOD manipulation, and common instance
    variables that control visibility, picking, and dragging.
    
    See Also:
    
    Actor2D Actor Volume Prop3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProp, obj, update, **traits)
    
    dragable = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the value of the dragable instance variable. This
        determines if an Prop, once picked, can be dragged (translated)
        through space. This is typically done through an interactive
        mouse interface. This does not affect methods such as
        set_position, which will continue to work.  It is just intended to
        prevent some Prop'ss from being dragged from within a user
        interface. Initial value is true.
        """
    )
    def _dragable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDragable,
                        self.dragable_)

    pickable = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the pickable instance variable.  This determines if the
        Prop can be picked (typically using the mouse). Also see
        dragable. Initial value is true.
        """
    )
    def _pickable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickable,
                        self.pickable_)

    visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of this Prop. Initial value is true.
        """
    )
    def _visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVisibility,
                        self.visibility_)

    use_bounds = tvtk_base.true_bool_trait(help=\
        """
        In case the Visibility flag is true, tell if the bounds of this
        prop should be taken into account or ignored during the
        computation of other bounding boxes, like in
        Renderer::ResetCamera(). Initial value is true.
        """
    )
    def _use_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBounds,
                        self.use_bounds_)

    estimated_render_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS This method is
        used by, for example, the LODProp3D in order to initialize the
        estimated render time at start-up to some user defined value.
        """
    )
    def _estimated_render_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEstimatedRenderTime,
                        self.estimated_render_time)

    allocated_render_time = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS The renderer may
        use the allocated rendering time to determine how to render this
        actor. Therefore it might need the information provided in the
        viewport. A side effect of this method is to reset the
        estimated_render_time to 0.0. This way, each of the ways that this
        prop may be rendered can be timed and added together into this
        value.
        """
    )
    def _allocated_render_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllocatedRenderTime,
                        self.allocated_render_time)

    render_time_multiplier = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Get/Set the
        multiplier for the render time. This is used for culling and is a
        number between 0 and 1. It is used to create the allocated render
        time value.
        """
    )
    def _render_time_multiplier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderTimeMultiplier,
                        self.render_time_multiplier)

    def _get_property_keys(self):
        return wrap_vtk(self._vtk_obj.GetPropertyKeys())
    def _set_property_keys(self, arg):
        old_val = self._get_property_keys()
        self._wrap_call(self._vtk_obj.SetPropertyKeys,
                        deref_vtk(arg))
        self.trait_property_changed('property_keys', old_val, arg)
    property_keys = traits.Property(_get_property_keys, _set_property_keys, help=\
        """
        Set/Get property keys. Property keys can be digest by some
        rendering passes. For instance, the user may mark a prop as a
        shadow caster for a shadow mapping render pass. Keys are
        documented in render pass classes. Initial value is NULL.
        """
    )

    def get_actors(self, *args):
        """
        V.get_actors(PropCollection)
        C++: virtual void GetActors(PropCollection *)
        For some exporters and other other operations we must be able to
        collect all the actors or volumes. These methods are used in that
        process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetActors, *my_args)
        return ret

    def get_actors2d(self, *args):
        """
        V.get_actors2d(PropCollection)
        C++: virtual void GetActors2D(PropCollection *)
        For some exporters and other other operations we must be able to
        collect all the actors or volumes. These methods are used in that
        process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetActors2D, *my_args)
        return ret

    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Get the bounds for this Prop as (Xmin,Xmax,Ymin,Ymax,Zmin,Zmax).
        in world coordinates. NULL means that the bounds are not defined.
        """
    )

    def get_consumer(self, *args):
        """
        V.get_consumer(int) -> Object
        C++: Object *GetConsumer(int i)
        Add or remove or get or check a consumer,
        """
        ret = self._wrap_call(self._vtk_obj.GetConsumer, *args)
        return wrap_vtk(ret)

    def _get_matrix(self):
        return wrap_vtk(self._vtk_obj.GetMatrix())
    matrix = traits.Property(_get_matrix, help=\
        """
        These methods are used by subclasses to place a matrix (if any)
        in the prop prior to rendering. Generally used only for picking.
        See Prop3D for more information.
        """
    )

    def _get_next_path(self):
        return wrap_vtk(self._vtk_obj.GetNextPath())
    next_path = traits.Property(_get_next_path, help=\
        """
        Prop and its subclasses can be picked by subclasses of
        AbstractPicker (e.g., PropPicker). The following methods
        interface with the picking classes and return "pick paths". A
        pick path is a hierarchical, ordered list of props that form an
        assembly.  Most often, when a Prop is picked, its path
        consists of a single node (i.e., the prop). However, classes like
        Assembly and PropAssembly can return more than one path,
        each path being several layers deep. (See AssemblyPath for
        more information.)  To use these methods - first invoke
        init_path_traversal() followed by repeated calls to get_next_path().
        get_next_path() returns a NULL pointer when the list is exhausted.
        """
    )

    def _get_number_of_consumers(self):
        return self._vtk_obj.GetNumberOfConsumers()
    number_of_consumers = traits.Property(_get_number_of_consumers, help=\
        """
        Get the number of consumers
        """
    )

    def _get_number_of_paths(self):
        return self._vtk_obj.GetNumberOfPaths()
    number_of_paths = traits.Property(_get_number_of_paths, help=\
        """
        Prop and its subclasses can be picked by subclasses of
        AbstractPicker (e.g., PropPicker). The following methods
        interface with the picking classes and return "pick paths". A
        pick path is a hierarchical, ordered list of props that form an
        assembly.  Most often, when a Prop is picked, its path
        consists of a single node (i.e., the prop). However, classes like
        Assembly and PropAssembly can return more than one path,
        each path being several layers deep. (See AssemblyPath for
        more information.)  To use these methods - first invoke
        init_path_traversal() followed by repeated calls to get_next_path().
        get_next_path() returns a NULL pointer when the list is exhausted.
        """
    )

    def _get_redraw_m_time(self):
        return self._vtk_obj.GetRedrawMTime()
    redraw_m_time = traits.Property(_get_redraw_m_time, help=\
        """
        Return the mtime of anything that would cause the rendered image
        to appear differently. Usually this involves checking the mtime
        of the prop plus anything else it depends on such as properties,
        textures etc.
        """
    )

    def _get_supports_selection(self):
        return self._vtk_obj.GetSupportsSelection()
    supports_selection = traits.Property(_get_supports_selection, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Used by
        HardwareSelector to determine if the prop supports hardware
        selection.
        """
    )

    def get_volumes(self, *args):
        """
        V.get_volumes(PropCollection)
        C++: virtual void GetVolumes(PropCollection *)
        For some exporters and other other operations we must be able to
        collect all the actors or volumes. These methods are used in that
        process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetVolumes, *my_args)
        return ret

    def add_consumer(self, *args):
        """
        V.add_consumer(Object)
        C++: void AddConsumer(Object *c)
        Add or remove or get or check a consumer,
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddConsumer, *my_args)
        return ret

    def add_estimated_render_time(self, *args):
        """
        V.add_estimated_render_time(float, Viewport)
        C++: virtual void AddEstimatedRenderTime(double t,
            Viewport *vp)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS This method is
        intended to allow the renderer to add to the estimated_render_time
        in props that require information that the renderer has in order
        to do this. For example, props that are rendered with a ray
        casting method do not know themselves how long it took for them
        to render. We don't want to cause a this->Modified() when we set
        this value since it is not really a modification to the object.
        (For example, we don't want to rebuild matrices at every render
        because the estimated render time is changing)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddEstimatedRenderTime, *my_args)
        return ret

    def build_paths(self, *args):
        """
        V.build_paths(AssemblyPaths, AssemblyPath)
        C++: virtual void BuildPaths(AssemblyPaths *paths,
            AssemblyPath *path)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Used to
        construct assembly paths and perform part traversal.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildPaths, *my_args)
        return ret

    def has_keys(self, *args):
        """
        V.has_keys(Information) -> bool
        C++: virtual bool HasKeys(Information *requiredKeys)
        Tells if the prop has all the required keys.
        \pre keys_can_be_null: required_keys==_0 || required_keys!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasKeys, *my_args)
        return ret

    def has_translucent_polygonal_geometry(self):
        """
        V.has_translucent_polygonal_geometry() -> int
        C++: virtual int HasTranslucentPolygonalGeometry()
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS Does this prop
        have some translucent polygonal geometry? This method is called
        during the rendering process to know if there is some translucent
        polygonal geometry. A simple prop that has some translucent
        polygonal geometry will return true. A composite prop (like
        Assembly) that has at least one sub-prop that has some
        translucent polygonal geometry will return true. Default
        implementation return false.
        """
        ret = self._vtk_obj.HasTranslucentPolygonalGeometry()
        return ret
        

    def init_path_traversal(self):
        """
        V.init_path_traversal()
        C++: virtual void InitPathTraversal()
        Prop and its subclasses can be picked by subclasses of
        AbstractPicker (e.g., PropPicker). The following methods
        interface with the picking classes and return "pick paths". A
        pick path is a hierarchical, ordered list of props that form an
        assembly.  Most often, when a Prop is picked, its path
        consists of a single node (i.e., the prop). However, classes like
        Assembly and PropAssembly can return more than one path,
        each path being several layers deep. (See AssemblyPath for
        more information.)  To use these methods - first invoke
        init_path_traversal() followed by repeated calls to get_next_path().
        get_next_path() returns a NULL pointer when the list is exhausted.
        """
        ret = self._vtk_obj.InitPathTraversal()
        return ret
        

    def is_consumer(self, *args):
        """
        V.is_consumer(Object) -> int
        C++: int IsConsumer(Object *c)
        Add or remove or get or check a consumer,
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsConsumer, *my_args)
        return ret

    def pick(self):
        """
        V.pick()
        C++: virtual void Pick()
        Method fires pick_event if the prop is picked.
        """
        ret = self._vtk_obj.Pick()
        return ret
        

    def poke_matrix(self, *args):
        """
        V.poke_matrix(Matrix4x4)
        C++: virtual void PokeMatrix(Matrix4x4 *matrix)
        These methods are used by subclasses to place a matrix (if any)
        in the prop prior to rendering. Generally used only for picking.
        See Prop3D for more information.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PokeMatrix, *my_args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Release
        any graphics resources that are being consumed by this actor. The
        parameter window could be used to determine which graphic
        resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def remove_consumer(self, *args):
        """
        V.remove_consumer(Object)
        C++: void RemoveConsumer(Object *c)
        Add or remove or get or check a consumer,
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveConsumer, *my_args)
        return ret

    def render_filtered_opaque_geometry(self, *args):
        """
        V.render_filtered_opaque_geometry(Viewport, Information)
            -> bool
        C++: virtual bool RenderFilteredOpaqueGeometry(Viewport *v,
            Information *requiredKeys)
        Render the opaque geometry only if the prop has all the
        required_keys. This is recursive for composite props like
        Assembly. An implementation is provided in Prop but each
        composite prop must override it. It returns if the rendering was
        performed.
        \pre v_exists: v!=0
        \pre keys_can_be_null: required_keys==_0 || required_keys!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderFilteredOpaqueGeometry, *my_args)
        return ret

    def render_filtered_overlay(self, *args):
        """
        V.render_filtered_overlay(Viewport, Information) -> bool
        C++: virtual bool RenderFilteredOverlay(Viewport *v,
            Information *requiredKeys)
        Render in the overlay of the viewport only if the prop has all
        the required_keys. This is recursive for composite props like
        Assembly. An implementation is provided in Prop but each
        composite prop must override it. It returns if the rendering was
        performed.
        \pre v_exists: v!=0
        \pre keys_can_be_null: required_keys==_0 || required_keys!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderFilteredOverlay, *my_args)
        return ret

    def render_filtered_translucent_polygonal_geometry(self, *args):
        """
        V.render_filtered_translucent_polygonal_geometry(Viewport,
            Information) -> bool
        C++: virtual bool RenderFilteredTranslucentPolygonalGeometry(
            Viewport *v, Information *requiredKeys)
        Render the translucent polygonal geometry only if the prop has
        all the required_keys. This is recursive for composite props like
        Assembly. An implementation is provided in Prop but each
        composite prop must override it. It returns if the rendering was
        performed.
        \pre v_exists: v!=0
        \pre keys_can_be_null: required_keys==_0 || required_keys!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderFilteredTranslucentPolygonalGeometry, *my_args)
        return ret

    def render_filtered_volumetric_geometry(self, *args):
        """
        V.render_filtered_volumetric_geometry(Viewport, Information)
            -> bool
        C++: virtual bool RenderFilteredVolumetricGeometry(Viewport *v,
             Information *requiredKeys)
        Render the volumetric geometry only if the prop has all the
        required_keys. This is recursive for composite props like
        Assembly. An implementation is provided in Prop but each
        composite prop must override it. It returns if the rendering was
        performed.
        \pre v_exists: v!=0
        \pre keys_can_be_null: required_keys==_0 || required_keys!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderFilteredVolumetricGeometry, *my_args)
        return ret

    def render_opaque_geometry(self, *args):
        """
        V.render_opaque_geometry(Viewport) -> int
        C++: virtual int RenderOpaqueGeometry(Viewport *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS All concrete
        subclasses must be able to render themselves. There are four key
        render methods in vtk and they correspond to four different
        points in the rendering cycle. Any given prop may implement one
        or more of these methods. The first method is intended for
        rendering all opaque geometry. The second method is intended for
        rendering all translucent polygonal geometry. The third one is
        intended for rendering all translucent volumetric geometry. Most
        of the volume rendering mappers draw their results during this
        thrid method. The last method is to render any 2d annotation or
        overlays. Each of these methods return an integer value
        indicating whether or not this render method was applied to this
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderOpaqueGeometry, *my_args)
        return ret

    def render_overlay(self, *args):
        """
        V.render_overlay(Viewport) -> int
        C++: virtual int RenderOverlay(Viewport *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS All concrete
        subclasses must be able to render themselves. There are four key
        render methods in vtk and they correspond to four different
        points in the rendering cycle. Any given prop may implement one
        or more of these methods. The first method is intended for
        rendering all opaque geometry. The second method is intended for
        rendering all translucent polygonal geometry. The third one is
        intended for rendering all translucent volumetric geometry. Most
        of the volume rendering mappers draw their results during this
        thrid method. The last method is to render any 2d annotation or
        overlays. Each of these methods return an integer value
        indicating whether or not this render method was applied to this
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderOverlay, *my_args)
        return ret

    def render_translucent_polygonal_geometry(self, *args):
        """
        V.render_translucent_polygonal_geometry(Viewport) -> int
        C++: virtual int RenderTranslucentPolygonalGeometry(Viewport *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS All concrete
        subclasses must be able to render themselves. There are four key
        render methods in vtk and they correspond to four different
        points in the rendering cycle. Any given prop may implement one
        or more of these methods. The first method is intended for
        rendering all opaque geometry. The second method is intended for
        rendering all translucent polygonal geometry. The third one is
        intended for rendering all translucent volumetric geometry. Most
        of the volume rendering mappers draw their results during this
        thrid method. The last method is to render any 2d annotation or
        overlays. Each of these methods return an integer value
        indicating whether or not this render method was applied to this
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentPolygonalGeometry, *my_args)
        return ret

    def render_volumetric_geometry(self, *args):
        """
        V.render_volumetric_geometry(Viewport) -> int
        C++: virtual int RenderVolumetricGeometry(Viewport *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS All concrete
        subclasses must be able to render themselves. There are four key
        render methods in vtk and they correspond to four different
        points in the rendering cycle. Any given prop may implement one
        or more of these methods. The first method is intended for
        rendering all opaque geometry. The second method is intended for
        rendering all translucent polygonal geometry. The third one is
        intended for rendering all translucent volumetric geometry. Most
        of the volume rendering mappers draw their results during this
        thrid method. The last method is to render any 2d annotation or
        overlays. Each of these methods return an integer value
        indicating whether or not this render method was applied to this
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderVolumetricGeometry, *my_args)
        return ret

    def restore_estimated_render_time(self):
        """
        V.restore_estimated_render_time()
        C++: virtual void RestoreEstimatedRenderTime()
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THESE METHODS OUTSIDE OF THE RENDERING PROCESS When the
        estimated_render_time is first set to 0.0 (in the
        set_allocated_render_time method) the old value is saved. This
        method is used to restore that old value should the render be
        aborted.
        """
        ret = self._vtk_obj.RestoreEstimatedRenderTime()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Prop)
        C++: virtual void ShallowCopy(Prop *prop)
        Shallow copy of this Prop.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('reference_count', 'GetReferenceCount'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Prop, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Prop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time',
            'render_time_multiplier']),
            title='Edit Prop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Prop properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

