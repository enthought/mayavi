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

from tvtk.tvtk_classes.prop3d import Prop3D


class ImageActor(Prop3D):
    """
    ImageActor - draw an image (data & properties) in a rendered 3d
    scene
    
    Superclass: Prop3D
    
    ImageActor is used to render an image in a 3d scene.  The image is
    placed at the origin of the image, and its size is controlled by the
    image dimensions and image spacing. The orientation of the image is
    orthogonal to one of the x-y-z axes depending on which plane the
    image is defined in. ImageActor duplicates the functionality of
    combinations of other VTK classes in a convenient, single class.
    
    Caveats:
    
    ImageData requires the image to be of type unsigned char. Use a
    filter like ImageShiftScale to convert to unsigned char (the
    method to use is set_output_type_to_unsigned_char()).
    
    See Also:
    
    ImageData Prop ImageShiftScale
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageActor, obj, update, **traits)
    
    interpolate = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off linear interpolation of the image when rendering.
        """
    )
    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the image data input for the image actor.
        """
    )

    z_slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )
    def _z_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZSlice,
                        self.z_slice)

    display_extent = traits.Array(shape=(6,), value=(-1, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        The image extent is generally set explicitly, but if not set it
        will be determined from the input image data.
        """
    )
    def _display_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayExtent,
                        self.display_extent)

    def get_display_bounds(self, *args):
        """
        V.get_display_bounds([float, float, float, float, float, float])
        C++: void GetDisplayBounds(double bounds[6])
        Get the bounds of the data that is displayed by this image actor.
         If the transformation matrix for this actor is the identity
        matrix, this will return the same value as get_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.GetDisplayBounds, *args)
        return ret

    def _get_slice_number(self):
        return self._vtk_obj.GetSliceNumber()
    slice_number = traits.Property(_get_slice_number, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_slice_number_max(self):
        return self._vtk_obj.GetSliceNumberMax()
    slice_number_max = traits.Property(_get_slice_number_max, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_slice_number_min(self):
        return self._vtk_obj.GetSliceNumberMin()
    slice_number_min = traits.Property(_get_slice_number_min, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_whole_z_max(self):
        return self._vtk_obj.GetWholeZMax()
    whole_z_max = traits.Property(_get_whole_z_max, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def _get_whole_z_min(self):
        return self._vtk_obj.GetWholeZMin()
    whole_z_min = traits.Property(_get_whole_z_min, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def render(self, *args):
        """
        V.render(Renderer)
        C++: virtual void Render(Renderer *)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Support the
        standard render methods.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('origin', 'GetOrigin'), ('scale',
    'GetScale'), ('orientation', 'GetOrientation'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('z_slice', 'GetZSlice'),
    ('interpolate', 'GetInterpolate'), ('reference_count',
    'GetReferenceCount'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('visibility', 'GetVisibility'),
    ('display_extent', 'GetDisplayExtent'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'interpolate',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'display_extent', 'estimated_render_time', 'opacity', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale', 'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['interpolate', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'display_extent', 'estimated_render_time',
            'opacity', 'orientation', 'origin', 'position',
            'render_time_multiplier', 'scale', 'z_slice']),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

