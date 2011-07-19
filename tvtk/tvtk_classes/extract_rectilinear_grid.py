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

from tvtk.tvtk_classes.rectilinear_grid_algorithm import RectilinearGridAlgorithm


class ExtractRectilinearGrid(RectilinearGridAlgorithm):
    """
    ExtractRectilinearGrid - Extract a sub grid (VOI) from the
    structured rectilinear dataset.
    
    Superclass: RectilinearGridAlgorithm
    
    ExtractRectilinearGrid rounds out the set of filters that extract
    a subgrid out of a larger structured data set.  RIght now, this
    filter only supports extracting a VOI.  In the future, it might
    support strides like the Extract grid filter.
    
    See Also:
    
    ExtractGrid ImageClip GeometryFilter ExtractGeometry
    ExtractVOI StructuredGridGeometryFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractRectilinearGrid, obj, update, **traits)
    
    include_boundary = tvtk_base.false_bool_trait(help=\
        """
        Control whether to enforce that the "boundary" of the grid is
        output in the subsampling process. (This ivar only has effect
        when the sample_rate in any direction is not equal to 1.) When
        this ivar include_boundary is on, the subsampling will always
        include the boundary of the grid even though the sample rate is
        not an even multiple of the grid dimensions. (By default
        include_boundary is off.)
        """
    )
    def _include_boundary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeBoundary,
                        self.include_boundary_)

    sample_rate = traits.Array(shape=(3,), value=(1, 1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _sample_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleRate,
                        self.sample_rate)

    voi = traits.Array(shape=(6,), value=(0, 2147483647, 0, 2147483647, 0, 2147483647), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _voi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVOI,
                        self.voi)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('include_boundary', 'GetIncludeBoundary'), ('progress_text',
    'GetProgressText'), ('voi', 'GetVOI'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('sample_rate',
    'GetSampleRate'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'include_boundary', 'release_data_flag', 'progress_text',
    'sample_rate', 'voi'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractRectilinearGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractRectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['include_boundary'], [], ['sample_rate', 'voi']),
            title='Edit ExtractRectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractRectilinearGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

