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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ImageToPolyDataFilter(PolyDataAlgorithm):
    """
    ImageToPolyDataFilter - generate linear primitives (vtk_poly_data)
    from an image
    
    Superclass: PolyDataAlgorithm
    
    ImageToPolyDataFilter converts raster data (i.e., an image) into
    polygonal data (i.e., quads or n-sided polygons), with each polygon
    assigned a constant color. This is useful for writers that generate
    vector formats (i.e., CGM or post_script). To use this filter, you
    specify how to quantize the color (or whether to use an image with a
    lookup table), and what style the output should be. The output is
    always polygons, but the choice is n x m quads (where n and m define
    the input image dimensions) "Pixelize" option; arbitrary polygons
    "Polygonalize" option; or variable number of quads of constant color
    generated along scan lines "_run_length" option.
    
    The algorithm quantizes color in order to create coherent regions
    that the polygons can represent with good compression. By default,
    the input image is quantized to 256 colors using a 3-3-2 bits for
    red-green-blue. However, you can also supply a single component image
    and a lookup table, with the single component assumed to be an index
    into the table.  (Note: a quantized image can be generated with the
    filter ImageQuantizeRGBToIndex.) The number of colors on output is
    equal to the number of colors in the input lookup table (or 256 if
    the built in linear ramp is used).
    
    The output of the filter is polygons with a single color per polygon
    cell. If the output style is set to "Polygonalize", the polygons may
    have an large number of points (bounded by something like 2*(n+m));
    and the polygon may not be convex which may cause rendering problems
    on some systems (use TriangleFilter). Otherwise, each polygon will
    have four vertices. The output also contains scalar data defining RGB
    color in unsigned char form.
    
    Caveats:
    
    The input linear lookup table must be of the form of 3-component
    unsigned char.
    
    This filter defines constant cell colors. If you have a plotting
    device that supports Gouraud shading (linear interpolation of color),
    then superior algorithms are available for generating polygons from
    images.
    
    Note that many plotting devices/formats support only a limited number
    of colors.
    
    See Also:
    
    CGMWriter ImageQuantizeRGBToIndex TriangleFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageToPolyDataFilter, obj, update, **traits)
    
    decimation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off whether the final polygons should be decimated.
        whether to smooth boundaries.
        """
    )
    def _decimation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDecimation,
                        self.decimation_)

    smoothing = tvtk_base.true_bool_trait(help=\
        """
        If the output style is set to polygonalize, then you can control
        whether to smooth boundaries.
        """
    )
    def _smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSmoothing,
                        self.smoothing_)

    color_mode = traits.Trait('linear256',
    tvtk_base.TraitRevPrefixMap({'linear256': 1, 'lut': 0}), help=\
        """
        Specify how to quantize color.
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    output_style = traits.Trait('polygonalize',
    tvtk_base.TraitRevPrefixMap({'run_length': 2, 'polygonalize': 1, 'pixelize': 0}), help=\
        """
        Specify how to create the output. Pixelize means converting the
        image to quad polygons with a constant color per quad.
        Polygonalize means merging colors together into polygonal
        regions, and then smoothing the regions (if smoothing is turned
        on). run_length means creating quad polygons that may encompass
        several pixels on a scan line. The default behavior is
        Polygonalize.
        """
    )
    def _output_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputStyle,
                        self.output_style_)

    sub_image_size = traits.Trait(250, traits.Range(10, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the size (n by n pixels) of the largest region to
        polygonalize. When the output_style is set to
        VTK_STYLE_POLYGONALIZE, large amounts of memory are used. In
        order to process large images, the image is broken into pieces
        that are at most Size pixels in width and height.
        """
    )
    def _sub_image_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubImageSize,
                        self.sub_image_size)

    number_of_smoothing_iterations = traits.Trait(40, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of smoothing iterations to smooth polygons.
        (Only in effect if output style is Polygonalize and smoothing is
        on.)
        """
    )
    def _number_of_smoothing_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSmoothingIterations,
                        self.number_of_smoothing_iterations)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set/Get the LookupTable to use. The lookup table is used when
        the color mode is set to LUT and a single component scalar is
        input.
        """
    )

    decimation_error = traits.Trait(1.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the error to use for decimation (if decimation is on).
        The error is an absolute number--the image spacing and dimensions
        are used to create points so the error should be consistent with
        the image size.
        """
    )
    def _decimation_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDecimationError,
                        self.decimation_error)

    error = traits.Trait(100, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the error value between two colors where the colors are
        considered the same. Only use this if the color mode uses the
        default 256 table.
        """
    )
    def _error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetError,
                        self.error)

    _updateable_traits_ = \
    (('color_mode', 'GetColorMode'), ('decimation', 'GetDecimation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('sub_image_size', 'GetSubImageSize'),
    ('number_of_smoothing_iterations', 'GetNumberOfSmoothingIterations'),
    ('progress_text', 'GetProgressText'), ('smoothing', 'GetSmoothing'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('error', 'GetError'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('decimation_error', 'GetDecimationError'), ('output_style',
    'GetOutputStyle'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'decimation', 'global_warning_display',
    'release_data_flag', 'smoothing', 'color_mode', 'output_style',
    'decimation_error', 'error', 'number_of_smoothing_iterations',
    'progress_text', 'sub_image_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageToPolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageToPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['decimation', 'smoothing'], ['color_mode',
            'output_style'], ['decimation_error', 'error',
            'number_of_smoothing_iterations', 'sub_image_size']),
            title='Edit ImageToPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageToPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

