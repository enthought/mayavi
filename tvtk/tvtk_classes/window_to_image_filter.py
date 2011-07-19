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

from tvtk.tvtk_classes.algorithm import Algorithm


class WindowToImageFilter(Algorithm):
    """
    WindowToImageFilter - Use a Window as input to image pipeline
    
    Superclass: Algorithm
    
    WindowToImageFilter provides methods needed to read the data in a
    Window and use it as input to the imaging pipeline. This is useful
    for saving an image to a file for example. The window can be read as
    either RGB or RGBA pixels;  in addition, the depth buffer can also be
    read.   RGB and RGBA pixels are of type unsigned char, while Z-Buffer
    data is returned as floats.  Use this filter to convert render_windows
    or image_windows to an image format.
    
    Caveats:
    
    A Window doesn't behave like other parts of the VTK pipeline: its
    modification time doesn't get updated when an image is rendered.  As
    a result, naive use of WindowToImageFilter will produce an image
    of the first image that the window rendered, but which is never
    updated on subsequent window updates.  This behavior is unexpected
    and in general undesirable.
    
    To force an update of the output image, call WindowToImageFilter's
    Modified method after rendering to the window.
    
    In VTK versions 4 and later, this filter is part of the canonical way
    to output an image of a window to a file (replacing the obsolete
    save_image_as_ppm method for RenderWindows that existed in 3.2 and
    earlier).  Connect this filter to the output of the window, and
    filter's output to a writer such as PNGWriter.
    
    Reading back alpha planes is dependent on the correct operation of
    the render window's get_rgba_char_pixel_data method, which in turn is
    dependent on the configuration of the window's alpha planes.  As of
    VTK 4.4+, machine-independent behavior is not automatically assured
    because of these dependencies.
    
    See Also:
    
    Window RenderLargeImage
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindowToImageFilter, obj, update, **traits)
    
    should_rerender = tvtk_base.true_bool_trait(help=\
        """
        Set/get whether to re-render the input window. Initial value is
        true. (This option makes no difference if Magnification > 1.)
        """
    )
    def _should_rerender_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShouldRerender,
                        self.should_rerender_)

    read_front_buffer = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that determines which buffer to read from. The
        default is to read from the front buffer.
        """
    )
    def _read_front_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadFrontBuffer,
                        self.read_front_buffer_)

    fix_boundary = tvtk_base.false_bool_trait(help=\
        """
        When this->Magnification > 1, this class render the full image in
        tiles. Sometimes that results in artificial artifacts at internal
        tile seams. To overcome this issue, set this flag to true.
        """
    )
    def _fix_boundary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixBoundary,
                        self.fix_boundary_)

    input_buffer_type = traits.Trait('rgb',
    tvtk_base.TraitRevPrefixMap({'rgb': 3, 'z_buffer': 5, 'rgba': 4}), help=\
        """
        Set/get the window buffer from which data will be read.  Choices
        include VTK_RGB (read the color image from the window), VTK_RGBA
        (same, but include the alpha channel), and VTK_ZBUFFER (depth
        buffer, returned as a float array). Initial value is VTK_RGB.
        """
    )
    def _input_buffer_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputBufferType,
                        self.input_buffer_type_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Returns which renderer is being used as the source for the pixel
        data. Initial value is 0.
        """
    )

    magnification = traits.Trait(1, traits.Range(1, 2048, enter_set=True, auto_set=False), help=\
        """
        The magnification of the current render window. Initial value is
        1.
        """
    )
    def _magnification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMagnification,
                        self.magnification)

    viewport = traits.Array(shape=(4,), value=(0.0, 0.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _viewport_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewport,
                        self.viewport)

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> ImageData
        C++: ImageData *GetOutput()
        Get the output data object for a port on this algorithm.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    _updateable_traits_ = \
    (('read_front_buffer', 'GetReadFrontBuffer'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('should_rerender', 'GetShouldRerender'), ('input_buffer_type',
    'GetInputBufferType'), ('fix_boundary', 'GetFixBoundary'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('magnification', 'GetMagnification'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('viewport', 'GetViewport'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'fix_boundary', 'global_warning_display',
    'read_front_buffer', 'release_data_flag', 'should_rerender',
    'input_buffer_type', 'magnification', 'progress_text', 'viewport'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WindowToImageFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WindowToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['fix_boundary', 'read_front_buffer',
            'should_rerender'], ['input_buffer_type'], ['magnification',
            'viewport']),
            title='Edit WindowToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WindowToImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

