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

from tvtk.tvtk_classes.extract_selection_base import ExtractSelectionBase


class ExtractSelection(ExtractSelectionBase):
    """
    ExtractSelection - extract a subset from a DataSet.
    
    Superclass: ExtractSelectionBase
    
    ExtractSelection extracts some subset of cells and points from its
    input dataset. The dataset is given on its first input port. The
    subset is described by the contents of the Selection on its second
    input port. Depending on the content of the Selection, this will
    use either a ExtractSelectedIds, ExtractSelectedFrustum
    ExtractSelectedLocations or a ExtractSelectedThreshold to
    perform the extraction.
    
    See Also:
    
    Selection ExtractSelectedIds ExtractSelectedFrustum
    ExtractSelectedLocations ExtractSelectedThresholds
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSelection, obj, update, **traits)
    
    use_probe_for_locations = tvtk_base.false_bool_trait(help=\
        """
        When On, ProbeSelectedLocations is used for extracting
        selections of content type Selection::LOCATIONS. Default is
        off and then ExtractSelectedLocations is used.
        """
    )
    def _use_probe_for_locations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseProbeForLocations,
                        self.use_probe_for_locations_)

    show_bounds = tvtk_base.false_bool_trait(help=\
        """
        When On, this returns an unstructured grid that outlines
        selection area. Off is the default. Applicable only to Frustum
        selection extraction.
        """
    )
    def _show_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowBounds,
                        self.show_bounds_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('preserve_topology',
    'GetPreserveTopology'), ('use_probe_for_locations',
    'GetUseProbeForLocations'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('show_bounds', 'GetShowBounds'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'preserve_topology', 'release_data_flag', 'show_bounds',
    'use_probe_for_locations', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSelection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['preserve_topology', 'show_bounds',
            'use_probe_for_locations'], [], []),
            title='Edit ExtractSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

