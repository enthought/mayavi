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


class SelectVisiblePoints(PolyDataAlgorithm):
    """
    SelectVisiblePoints - extract points that are visible (based on
    z-buffer calculation)
    
    Superclass: PolyDataAlgorithm
    
    SelectVisiblePoints is a filter that selects points based on
    whether they are visible or not. Visibility is determined by
    accessing the z-buffer of a rendering window. (The position of each
    input point is converted into display coordinates, and then the
    z-value at that point is obtained. If within the user-specified
    tolerance, the point is considered visible.)
    
    Points that are visible (or if the ivar select_invisible is on,
    invisible points) are passed to the output. Associated data
    attributes are passed to the output as well.
    
    This filter also allows you to specify a rectangular window in
    display (pixel) coordinates in which the visible points must lie.
    This can be used as a sort of local "brushing" operation to select
    just data within a window.
    
    Caveats:
    
    You must carefully synchronize the execution of this filter. The
    filter refers to a renderer, which is modified every time a render
    occurs. Therefore, the filter is always out of date, and always
    executes. You may have to perform two rendering passes, or if you are
    using this filter in conjunction with LabeledDataMapper, things
    work out because 2d rendering occurs after the 3d rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectVisiblePoints, obj, update, **traits)
    
    selection_window = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which enables selection in a rectangular display
        region.
        """
    )
    def _selection_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionWindow,
                        self.selection_window_)

    select_invisible = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which enables inverse selection; i.e., invisible
        points are selected.
        """
    )
    def _select_invisible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectInvisible,
                        self.select_invisible_)

    selection = traits.Array(shape=(4,), value=(0, 1600, 0, 1600), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelection,
                        self.selection)

    tolerance = traits.Trait(0.01, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get a tolerance to use to determine whether a point is
        visible. A tolerance is usually required because the conversion
        from world space to display space during rendering introduces
        numerical round-off.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Specify the renderer in which the visibility computation is to be
        performed.
        """
    )

    _updateable_traits_ = \
    (('select_invisible', 'GetSelectInvisible'), ('selection',
    'GetSelection'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('selection_window',
    'GetSelectionWindow'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'select_invisible', 'selection_window',
    'progress_text', 'selection', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectVisiblePoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['select_invisible', 'selection_window'], [],
            ['selection', 'tolerance']),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

