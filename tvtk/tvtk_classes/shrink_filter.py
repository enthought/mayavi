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


class ShrinkFilter(UnstructuredGridAlgorithm):
    """
    ShrinkFilter - shrink cells composing an arbitrary data set
    
    Superclass: UnstructuredGridAlgorithm
    
    ShrinkFilter shrinks cells composing an arbitrary data set towards
    their centroid. The centroid of a cell is computed as the average
    position of the cell points. Shrinking results in disconnecting the
    cells from one another. The output of this filter is of general
    dataset type UnstructuredGrid.
    
    Caveats:
    
    It is possible to turn cells inside out or cause self intersection in
    special cases.
    
    See Also:
    
    ShrinkPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShrinkFilter, obj, update, **traits)
    
    shrink_factor = traits.Trait(0.5, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Get/Set the fraction of shrink for each cell. The default is 0.5.
        """
    )
    def _shrink_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkFactor,
                        self.shrink_factor)

    _updateable_traits_ = \
    (('shrink_factor', 'GetShrinkFactor'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'shrink_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShrinkFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShrinkFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['shrink_factor']),
            title='Edit ShrinkFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShrinkFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

