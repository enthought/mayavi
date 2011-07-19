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

from tvtk.tvtk_classes.rendered_representation import RenderedRepresentation


class RenderedSurfaceRepresentation(RenderedRepresentation):
    """
    RenderedSurfaceRepresentation - Displays a geometric dataset as a
    surface.
    
    Superclass: RenderedRepresentation
    
    RenderedSurfaceRepresentation is used to show a geometric dataset
    in a view. The representation uses a GeometryFilter to convert the
    dataset to polygonal data (e.g. volumetric data is converted to its
    external surface). The representation may then be added to
    RenderView.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedSurfaceRepresentation, obj, update, **traits)
    
    cell_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _cell_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellColorArrayName,
                        self.cell_color_array_name)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('selection_type', 'GetSelectionType'), ('label_render_mode',
    'GetLabelRenderMode'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('selection_array_name',
    'GetSelectionArrayName'), ('cell_color_array_name',
    'GetCellColorArrayName'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('selectable', 'GetSelectable'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'cell_color_array_name',
    'label_render_mode', 'progress_text', 'selection_array_name',
    'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedSurfaceRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedSurfaceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['selectable'], [], ['cell_color_array_name',
            'label_render_mode', 'selection_array_name', 'selection_type']),
            title='Edit RenderedSurfaceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedSurfaceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

