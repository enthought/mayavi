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


class TubeFilter(PolyDataAlgorithm):
    """
    TubeFilter - filter that generates tubes around lines
    
    Superclass: PolyDataAlgorithm
    
    TubeFilter is a filter that generates a tube around each input
    line. The tubes are made up of triangle strips and rotate around the
    tube with the rotation of the line normals. (If no normals are
    present, they are computed automatically.) The radius of the tube can
    be set to vary with scalar or vector value. If the radius varies with
    scalar value the radius is linearly adjusted. If the radius varies
    with vector value, a mass flux preserving variation is used. The
    number of sides for the tube also can be specified. You can also
    specify which of the sides are visible. This is useful for generating
    interesting striping effects. Other options include the ability to
    cap the tube and generate texture coordinates. Texture coordinates
    can be used with an associated texture map to create interesting
    effects such as marking the tube with stripes corresponding to length
    or time.
    
    This filter is typically used to create thick or dramatic lines.
    Another common use is to combine this filter with StreamLine to
    generate streamtubes.
    
    Caveats:
    
    The number of tube sides must be greater than 3. If you wish to use
    fewer sides (i.e., a ribbon), use RibbonFilter.
    
    The input line must not have duplicate points, or normals at points
    that are parallel to the incoming/outgoing line segments. (Duplicate
    points can be removed with CleanPolyData.) If a line does not meet
    this criteria, then that line is not tubed.
    
    See Also:
    
    RibbonFilter StreamLine
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTubeFilter, obj, update, **traits)
    
    use_default_normal = tvtk_base.false_bool_trait(help=\
        """
        Set a boolean to control whether to use default normals.
        default_normal_on is set.
        """
    )
    def _use_default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDefaultNormal,
                        self.use_default_normal_)

    sides_share_vertices = tvtk_base.true_bool_trait(help=\
        """
        Set a boolean to control whether tube sides should share
        vertices. This creates independent strips, with constant normals
        so the tube is always faceted in appearance.
        """
    )
    def _sides_share_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSidesShareVertices,
                        self.sides_share_vertices_)

    capping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off whether to cap the ends with polygons.
        """
    )
    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    vary_radius = traits.Trait('vary_radius_off',
    tvtk_base.TraitRevPrefixMap({'vary_radius_by_scalar': 1, 'vary_radius_off': 0, 'vary_radius_by_vector': 2, 'vary_radius_by_absolute_scalar': 3}), help=\
        """
        Turn on/off the variation of tube radius with scalar value.
        """
    )
    def _vary_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVaryRadius,
                        self.vary_radius_)

    generate_t_coords = traits.Trait('off',
    tvtk_base.TraitRevPrefixMap({'use_scalars': 3, 'use_length': 2, 'off': 0, 'normalized_length': 1}), help=\
        """
        Control whether and how texture coordinates are produced. This is
        useful for striping the tube with length textures, etc. If you
        use scalars to create the texture, the scalars are assumed to be
        monotonically increasing (or decreasing).
        """
    )
    def _generate_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTCoords,
                        self.generate_t_coords_)

    on_ratio = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control the striping of the tubes. If on_ratio is greater than 1,
        then every nth tube side is turned on, beginning with the Offset
        side.
        """
    )
    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

    offset = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control the striping of the tubes. The offset sets the first tube
        side that is visible. Offset is generally used with on_ratio to
        create nifty striping effects.
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    number_of_sides = traits.Trait(3, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of sides for the tube. At a minimum, number of
        sides is 3.
        """
    )
    def _number_of_sides_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSides,
                        self.number_of_sides)

    default_normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormal,
                        self.default_normal)

    radius = traits.Trait(0.5, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the minimum tube radius (minimum because the tube radius may
        vary).
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    radius_factor = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum tube radius in terms of a multiple of the minimum
        radius.
        """
    )
    def _radius_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadiusFactor,
                        self.radius_factor)

    texture_length = traits.Trait(1.0, traits.Range(9.9999999999999995e-07, 2147483647.0, enter_set=True, auto_set=False), help=\
        """
        Control the conversion of units during the texture coordinates
        calculation. The texture_length indicates what length (whether
        calculated from scalars or length) is mapped to the [0,1) texture
        space.
        """
    )
    def _texture_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureLength,
                        self.texture_length)

    _updateable_traits_ = \
    (('generate_t_coords', 'GetGenerateTCoords'), ('radius_factor',
    'GetRadiusFactor'), ('capping', 'GetCapping'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('default_normal', 'GetDefaultNormal'), ('number_of_sides',
    'GetNumberOfSides'), ('progress_text', 'GetProgressText'),
    ('texture_length', 'GetTextureLength'), ('debug', 'GetDebug'),
    ('on_ratio', 'GetOnRatio'), ('radius', 'GetRadius'),
    ('sides_share_vertices', 'GetSidesShareVertices'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('offset', 'GetOffset'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('vary_radius', 'GetVaryRadius'), ('use_default_normal',
    'GetUseDefaultNormal'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'release_data_flag', 'sides_share_vertices', 'use_default_normal',
    'generate_t_coords', 'vary_radius', 'default_normal',
    'number_of_sides', 'offset', 'on_ratio', 'progress_text', 'radius',
    'radius_factor', 'texture_length'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TubeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['capping', 'sides_share_vertices',
            'use_default_normal'], ['generate_t_coords', 'vary_radius'],
            ['default_normal', 'number_of_sides', 'offset', 'on_ratio', 'radius',
            'radius_factor', 'texture_length']),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

