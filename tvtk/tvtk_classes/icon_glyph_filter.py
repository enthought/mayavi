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


class IconGlyphFilter(PolyDataAlgorithm):
    """
    IconGlyphFilter - Filter that generates a polydata consisting of
    
    Superclass: PolyDataAlgorithm
    
    IconGlyphFilter takes in a PointSet where each point
    corresponds to the center of an icon. Scalar integer data must also
    be set to give each point an icon index. This index is a zero based
    row major index into an image that contains a grid of icons (each
    icon is the same size). You must also specify 1) the size of the icon
    in the icon sheet (in pixels), 2) the size of the icon sheet (in
    pixels), and 3) the display size of each icon (again in display
    coordinates, or pixels).
    
    Various other parameters are used to control how this data is
    combined. If use_icon_size is true then the display_size is ignored. If
    pass_scalars is true, then the scalar index information is passed to
    the output. Also, there is an optional icon_scale array which, if
    use_icon_scaling is on, will scale each icon independently.
    
    See Also:
    
    PolyDataAlgorithm Glyph3D Glyph2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIconGlyphFilter, obj, update, **traits)
    
    pass_scalars = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to pass the scalar icon index to the output. By
        default this is not passed since it can affect color during the
        rendering process. Note that all other point data is passed to
        the output regardless of the value of this flag.
        """
    )
    def _pass_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassScalars,
                        self.pass_scalars_)

    use_icon_size = tvtk_base.true_bool_trait(help=\
        """
        Specify whether the Quad generated to place the icon on will be
        either the dimensions specified by icon_size or the display_size.
        """
    )
    def _use_icon_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseIconSize,
                        self.use_icon_size_)

    icon_scaling = traits.Trait('scaling_off',
    tvtk_base.TraitRevPrefixMap({'scaling_array': 1, 'scaling_off': 0}), help=\
        """
        Specify how to specify individual icons. By default, icon scaling
        is off, but if it is on, then the filter looks for an array named
        "_icon_scale" to control individual icon size.
        """
    )
    def _icon_scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconScaling,
                        self.icon_scaling_)

    gravity = traits.Trait('center_center',
    tvtk_base.TraitRevPrefixMap({'bottom_center': 8, 'bottom_right': 7, 'top_left': 3, 'bottom_left': 9, 'top_right': 1, 'top_center': 2, 'center_center': 5, 'center_right': 4, 'center_left': 6}), help=\
        """
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
    )
    def _gravity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGravity,
                        self.gravity_)

    icon_size = traits.Array(shape=(2,), value=(1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _icon_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconSize,
                        self.icon_size)

    icon_sheet_size = traits.Array(shape=(2,), value=(1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _icon_sheet_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconSheetSize,
                        self.icon_sheet_size)

    display_size = traits.Array(shape=(2,), value=(25, 25), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _display_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplaySize,
                        self.display_size)

    offset = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('use_icon_size', 'GetUseIconSize'), ('debug', 'GetDebug'),
    ('icon_sheet_size', 'GetIconSheetSize'), ('progress_text',
    'GetProgressText'), ('gravity', 'GetGravity'), ('pass_scalars',
    'GetPassScalars'), ('reference_count', 'GetReferenceCount'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('offset', 'GetOffset'), ('icon_size',
    'GetIconSize'), ('progress', 'GetProgress'), ('display_size',
    'GetDisplaySize'), ('icon_scaling', 'GetIconScaling'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_scalars',
    'release_data_flag', 'use_icon_size', 'gravity', 'icon_scaling',
    'display_size', 'icon_sheet_size', 'icon_size', 'offset',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IconGlyphFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IconGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_scalars', 'use_icon_size'], ['gravity',
            'icon_scaling'], ['display_size', 'icon_sheet_size', 'icon_size',
            'offset']),
            title='Edit IconGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IconGlyphFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

