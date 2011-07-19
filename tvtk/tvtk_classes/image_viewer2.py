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


class ImageViewer2(Object):
    """
    ImageViewer2 - Display a 2d image.
    
    Superclass: Object
    
    ImageViewer2 is a convenience class for displaying a 2d image.  It
    packages up the functionality found in RenderWindow, Renderer,
    ImageActor and ImageMapToWindowLevelColors into a single easy
    to use class.  This class also creates an image interactor style
    (vtk_interactor_style_image) that allows zooming and panning of images,
    and supports interactive window/level operations on the image. Note
    that ImageViewer2 is simply a wrapper around these classes.
    
    ImageViewer2 uses the 3d rendering and texture mapping engine to
    draw an image on a plane.  This allows for rapid rendering, zooming,
    and panning. The image is placed in the 3d scene at a depth based on
    the z-coordinate of the particular image slice. Each call to
    set_slice() changes the image data (slice) displayed AND changes the
    depth of the displayed slice in the 3d scene. This can be controlled
    by the auto_adjust_camera_clipping_range ivar of the interactor_style
    member.
    
    It is possible to mix images and geometry, using the methods:
    
    viewer->_set_input( my_image ); viewer->_get_renderer()->_add_actor( my_actor
    );
    
    This can be used to annotate an image with a poly_data of "edges" or
    or highlight sections of an image or display a 3d isosurface with a
    slice from the volume, etc. Any portions of your geometry that are in
    front of the displayed slice will be visible; any portions of your
    geometry that are behind the displayed slice will be obscured. A more
    general framework (with respect to viewing direction) for achieving
    this effect is provided by the ImagePlaneWidget .
    
    Note that pressing 'r' will reset the window/level and pressing
    shift+'r' or control+'r' will reset the camera.
    
    See Also:
    
    RenderWindow Renderer ImageActor
    ImageMapToWindowLevelColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageViewer2, obj, update, **traits)
    
    off_screen_rendering = tvtk_base.false_bool_trait(help=\
        """
        Create a window in memory instead of on the screen. This may not
        be supported for every type of window and on some windows you may
        need to invoke this prior to the first render.
        """
    )
    def _off_screen_rendering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffScreenRendering,
                        self.off_screen_rendering_)

    slice_orientation = traits.Trait('xy',
    tvtk_base.TraitRevPrefixMap({'xz': 1, 'yz': 0, 'xy': 2}), help=\
        """
        Set/get the slice orientation
        """
    )
    def _slice_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceOrientation,
                        self.slice_orientation_)

    z_slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        @deprecated Replaced by ImageViewer2::SetSlice() as of VTK
        5.0.
        """
    )
    def _z_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZSlice,
                        self.z_slice)

    slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current slice to display (depending on the
        orientation this can be in X, Y or Z).
        """
    )
    def _slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlice,
                        self.slice)

    color_level = traits.Float(127.5, enter_set=True, auto_set=False, help=\
        """
        Set window and level for mapping pixels to colors.
        """
    )
    def _color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorLevel,
                        self.color_level)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    color_window = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set window and level for mapping pixels to colors.
        """
    )
    def _color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorWindow,
                        self.color_window)

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the input image to the viewer.
        """
    )

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    image_actor = traits.Property(_get_image_actor, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetInteractorStyle())
    interactor_style = traits.Property(_get_interactor_style, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_slice_max(self):
        return self._vtk_obj.GetSliceMax()
    slice_max = traits.Property(_get_slice_max, help=\
        """
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def _get_slice_min(self):
        return self._vtk_obj.GetSliceMin()
    slice_min = traits.Property(_get_slice_min, help=\
        """
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def get_slice_range(self, *args):
        """
        V.get_slice_range([int, int])
        C++: virtual void GetSliceRange(int range[2])
        V.get_slice_range(int, int)
        C++: virtual void GetSliceRange(int &min, int &max)
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
        ret = self._wrap_call(self._vtk_obj.GetSliceRange, *args)
        return ret

    def _get_whole_z_max(self):
        return self._vtk_obj.GetWholeZMax()
    whole_z_max = traits.Property(_get_whole_z_max, help=\
        """
        @deprecated Replaced by ImageViewer2::GetSliceMax() as of VTK
        5.0.
        """
    )

    def _get_whole_z_min(self):
        return self._vtk_obj.GetWholeZMin()
    whole_z_min = traits.Property(_get_whole_z_min, help=\
        """
        @deprecated Replaced by ImageViewer2::GetSliceMin() as of VTK
        5.0.
        """
    )

    def _get_window_level(self):
        return wrap_vtk(self._vtk_obj.GetWindowLevel())
    window_level = traits.Property(_get_window_level, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_window_name(self):
        return self._vtk_obj.GetWindowName()
    window_name = traits.Property(_get_window_name, help=\
        """
        Get the name of rendering window.
        """
    )

    def render(self):
        """
        V.render()
        C++: virtual void Render(void)
        Render the resulting image.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def set_display_id(self):
        """
        V.set_display_id()
        C++: virtual void SetDisplayId(void *a)
        These are here when using a Tk window.
        """
        ret = self._vtk_obj.SetDisplayId()
        return ret
        

    def set_input_connection(self, *args):
        """
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *input)
        Set/Get the input image to the viewer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    def set_parent_id(self):
        """
        V.set_parent_id()
        C++: virtual void SetParentId(void *a)
        These are here when using a Tk window.
        """
        ret = self._vtk_obj.SetParentId()
        return ret
        

    def set_position(self, *args):
        """
        V.set_position(int, int)
        C++: virtual void SetPosition(int a, int b)
        V.set_position([int, int])
        C++: virtual void SetPosition(int a[2])
        Set/Get the position in screen coordinates of the rendering
        window.
        """
        ret = self._wrap_call(self._vtk_obj.SetPosition, *args)
        return ret

    def set_size(self, *args):
        """
        V.set_size(int, int)
        C++: virtual void SetSize(int a, int b)
        V.set_size([int, int])
        C++: virtual void SetSize(int a[2])
        Set/Get the size of the window in screen coordinates in pixels.
        """
        ret = self._wrap_call(self._vtk_obj.SetSize, *args)
        return ret

    def set_window_id(self):
        """
        V.set_window_id()
        C++: virtual void SetWindowId(void *a)
        These are here when using a Tk window.
        """
        ret = self._vtk_obj.SetWindowId()
        return ret
        

    def setup_interactor(self, *args):
        """
        V.setup_interactor(RenderWindowInteractor)
        C++: virtual void SetupInteractor(RenderWindowInteractor *)
        Attach an interactor for the internal render window.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetupInteractor, *my_args)
        return ret

    def update_display_extent(self):
        """
        V.update_display_extent()
        C++: virtual void UpdateDisplayExtent()
        Update the display extent manually so that the proper slice for
        the given orientation is displayed. It will also try to set a
        reasonable camera clipping range. This method is called
        automatically when the Input is changed, but most of the time the
        input of this class is likely to remain the same, i.e. connected
        to the output of a filter, or an image reader. When the input of
        this filter or reader itself is changed, an error message might
        be displayed since the current display extent is probably outside
        the new whole extent. Calling this method will ensure that the
        display extent is reset properly.
        """
        ret = self._vtk_obj.UpdateDisplayExtent()
        return ret
        

    _updateable_traits_ = \
    (('color_level', 'GetColorLevel'), ('slice', 'GetSlice'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('slice_orientation', 'GetSliceOrientation'), ('z_slice',
    'GetZSlice'), ('color_window', 'GetColorWindow'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'),
    ('off_screen_rendering', 'GetOffScreenRendering'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'off_screen_rendering',
    'slice_orientation', 'color_level', 'color_window', 'slice',
    'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageViewer2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['off_screen_rendering'], ['slice_orientation'],
            ['color_level', 'color_window', 'slice', 'z_slice']),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

