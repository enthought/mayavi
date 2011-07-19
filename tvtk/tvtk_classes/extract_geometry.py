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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ExtractGeometry(UnstructuredGridAlgorithm):
    """
    ExtractGeometry - extract cells that lie either entirely inside or
    outside of a specified implicit function
    
    Superclass: UnstructuredGridAlgorithm
    
    ExtractGeometry extracts from its input dataset all cells that are
    either completely inside or outside of a specified implicit function.
    Any type of dataset can be input to this filter. On output the filter
    generates an unstructured grid.
    
    To use this filter you must specify an implicit function. You must
    also specify whethter to extract cells lying inside or outside of the
    implicit function. (The inside of an implicit function is the
    negative values region.) An option exists to extract cells that are
    neither inside or outside (i.e., boundary).
    
    A more efficient version of this filter is available for PolyData
    input. See ExtractPolyDataGeometry.
    
    See Also:
    
    ExtractPolyDataGeometry GeometryFilter ExtractVOI
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractGeometry, obj, update, **traits)
    
    extract_boundary_cells = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether to extract cells that are partially
        inside. By default, extract_boundary_cells is off.
        """
    )
    def _extract_boundary_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractBoundaryCells,
                        self.extract_boundary_cells_)

    extract_only_boundary_cells = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether to extract cells that are partially
        inside. By default, extract_boundary_cells is off.
        """
    )
    def _extract_only_boundary_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractOnlyBoundaryCells,
                        self.extract_only_boundary_cells_)

    extract_inside = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether to extract cells that are inside of
        implicit function (_extract_inside == 1) or outside of implicit
        function (_extract_inside == 0).
        """
    )
    def _extract_inside_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractInside,
                        self.extract_inside_)

    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function for inside/outside checks.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('extract_boundary_cells', 'GetExtractBoundaryCells'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'),
    ('extract_only_boundary_cells', 'GetExtractOnlyBoundaryCells'),
    ('abort_execute', 'GetAbortExecute'), ('extract_inside',
    'GetExtractInside'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'extract_boundary_cells',
    'extract_inside', 'extract_only_boundary_cells',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractGeometry, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['extract_boundary_cells', 'extract_inside',
            'extract_only_boundary_cells'], [], []),
            title='Edit ExtractGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

