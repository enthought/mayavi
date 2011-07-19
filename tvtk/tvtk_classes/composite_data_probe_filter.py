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

from tvtk.tvtk_classes.probe_filter import ProbeFilter


class CompositeDataProbeFilter(ProbeFilter):
    """
    CompositeDataProbeFilter - subclass of ProbeFilter which
    supports
    
    Superclass: ProbeFilter
    
    CompositeDataProbeFilter supports probing into multi-group
    datasets. It sequentially probes through each concrete dataset within
    the composite probing at only those locations at which there were no
    hits when probing earlier datasets. For Hierarchical datasets, this
    traversal through leaf datasets is done in reverse order of levels
    i.e. highest level first.
    
    When dealing with composite datasets, partial arrays are common i.e.
    data-arrays that are not available in all of the blocks. By default,
    this filter only passes those point and cell data-arrays that are
    available in all the blocks i.e. partial array are removed. When
    pass_partial_arrays is turned on, this behavior is changed to take a
    union of all arrays present thus partial arrays are passed as well.
    However, for composite dataset input, this filter still produces a
    non-composite output. For all those locations in a block of where a
    particular data array is missing, this filter uses Math::Nan() for
    double and float arrays, while 0 for all other types of arrays i.e
    int, char etc.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataProbeFilter, obj, update, **traits)
    
    pass_partial_arrays = tvtk_base.false_bool_trait(help=\
        """
        When dealing with composite datasets, partial arrays are common
        i.e. data-arrays that are not available in all of the blocks. By
        default, this filter only passes those point and cell data-arrays
        that are available in all the blocks i.e. partial array are
        removed.  When pass_partial_arrays is turned on, this behavior is
        changed to take a union of all arrays present thus partial arrays
        are passed as well. However, for composite dataset input, this
        filter still produces a non-composite output. For all those
        locations in a block of where a particular data array is missing,
        this filter uses Math::Nan() for double and float arrays,
        while 0 for all other types of arrays i.e int, char etc.
        """
    )
    def _pass_partial_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPartialArrays,
                        self.pass_partial_arrays_)

    _updateable_traits_ = \
    (('pass_partial_arrays', 'GetPassPartialArrays'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('spatial_match', 'GetSpatialMatch'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('valid_point_mask_array_name', 'GetValidPointMaskArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_partial_arrays', 'release_data_flag', 'spatial_match',
    'progress_text', 'valid_point_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeDataProbeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_partial_arrays', 'spatial_match'], [],
            ['valid_point_mask_array_name']),
            title='Edit CompositeDataProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

