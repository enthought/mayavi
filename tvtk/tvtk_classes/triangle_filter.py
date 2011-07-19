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


class TriangleFilter(PolyDataAlgorithm):
    """
    TriangleFilter - create triangle polygons from input polygons and
    triangle strips
    
    Superclass: PolyDataAlgorithm
    
    TriangleFilter generates triangles from input polygons and
    triangle strips. The filter also will pass through vertices and
    lines, if requested.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriangleFilter, obj, update, **traits)
    
    pass_lines = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off passing lines through filter.
        """
    )
    def _pass_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassLines,
                        self.pass_lines_)

    pass_verts = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off passing vertices through filter.
        """
    )
    def _pass_verts_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassVerts,
                        self.pass_verts_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('pass_verts', 'GetPassVerts'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('pass_lines',
    'GetPassLines'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_lines',
    'pass_verts', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TriangleFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_lines', 'pass_verts'], [], []),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

