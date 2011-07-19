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


class MaskPoints(PolyDataAlgorithm):
    """
    MaskPoints - selectively filter points
    
    Superclass: PolyDataAlgorithm
    
    MaskPoints is a filter that passes through points and point
    attributes from input dataset. (Other geometry is not passed
    through.) It is possible to mask every nth point, and to specify an
    initial offset to begin masking from. A special random mode feature
    enables random selection of points. The filter can also generate
    vertices (topological primitives) as well as points. This is useful
    because vertices are rendered while points are not.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMaskPoints, obj, update, **traits)
    
    generate_vertices = tvtk_base.false_bool_trait(help=\
        """
        Generate output polydata vertices as well as points. A useful
        convenience method because vertices are drawn (they are topology)
        while points are not (they are geometry). By default this method
        is off.
        """
    )
    def _generate_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertices,
                        self.generate_vertices_)

    single_vertex_per_cell = tvtk_base.false_bool_trait(help=\
        """
        When vertex generation is enabled, by default vertices are
        produced as multi-vertex cells (more than one per cell), if you
        wish to have a single vertex per cell, enable this flag.
        """
    )
    def _single_vertex_per_cell_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleVertexPerCell,
                        self.single_vertex_per_cell_)

    random_mode = tvtk_base.false_bool_trait(help=\
        """
        Special flag causes randomization of point selection. If this
        mode is on, statistically every nth point (i.e., on_ratio) will be
        displayed.
        """
    )
    def _random_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomMode,
                        self.random_mode_)

    on_ratio = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Turn on every nth point.
        """
    )
    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

    maximum_number_of_points = traits.Trait(2147483647, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Limit the number of points that can be passed through.
        """
    )
    def _maximum_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPoints,
                        self.maximum_number_of_points)

    offset = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Start with this point.
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    _updateable_traits_ = \
    (('random_mode', 'GetRandomMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('maximum_number_of_points', 'GetMaximumNumberOfPoints'),
    ('single_vertex_per_cell', 'GetSingleVertexPerCell'), ('debug',
    'GetDebug'), ('on_ratio', 'GetOnRatio'), ('generate_vertices',
    'GetGenerateVertices'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('offset', 'GetOffset'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_vertices',
    'global_warning_display', 'random_mode', 'release_data_flag',
    'single_vertex_per_cell', 'maximum_number_of_points', 'offset',
    'on_ratio', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MaskPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_vertices', 'random_mode',
            'single_vertex_per_cell'], [], ['maximum_number_of_points', 'offset',
            'on_ratio']),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

