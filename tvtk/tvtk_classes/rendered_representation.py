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

from tvtk.tvtk_classes.data_representation import DataRepresentation


class RenderedRepresentation(DataRepresentation):
    """
    RenderedRepresentation - 
    
    Superclass: DataRepresentation
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedRepresentation, obj, update, **traits)
    
    label_render_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the label render mode. RenderView::QT - Use Qt-based
        labeler with fitted labeling
          and unicode support. Requires VTK_USE_QT to be on.
        RenderView::FREETYPE - Use standard freetype text rendering.
        """
    )
    def _label_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelRenderMode,
                        self.label_render_mode)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('selection_type', 'GetSelectionType'), ('label_render_mode',
    'GetLabelRenderMode'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('selection_array_name', 'GetSelectionArrayName'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('selectable',
    'GetSelectable'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'label_render_mode',
    'progress_text', 'selection_array_name', 'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['selectable'], [], ['label_render_mode',
            'selection_array_name', 'selection_type']),
            title='Edit RenderedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

