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

from tvtk.tvtk_classes.clean_poly_data import CleanPolyData


class QuantizePolyDataPoints(CleanPolyData):
    """
    QuantizePolyDataPoints - quantizes x,y,z coordinates of points
    
    Superclass: CleanPolyData
    
    QuantizePolyDataPoints is a subclass of CleanPolyData and
    inherits the functionality of CleanPolyData with the addition that
    it quantizes the point coordinates before inserting into the point
    list. The user should set QFactor to a positive value (0.25 by
    default) and all {x,y,z} coordinates will be quantized to that grain
    size.
    
    A tolerance of zero is expected, though positive values may be used,
    the quantization will take place before the tolerance is applied.
    
    Caveats:
    
    Merging points can alter topology, including introducing non-manifold
    forms. Handling of degenerate cells is controlled by switches in
    CleanPolyData.
    
    See Also:
    
    CleanPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuantizePolyDataPoints, obj, update, **traits)
    
    q_factor = traits.Trait(0.25, traits.Range(1.0000000000000001e-05, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Specify quantization grain size. Default is 0.25
        """
    )
    def _q_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFactor,
                        self.q_factor)

    _updateable_traits_ = \
    (('point_merging', 'GetPointMerging'), ('piece_invariant',
    'GetPieceInvariant'), ('convert_strips_to_polys',
    'GetConvertStripsToPolys'), ('debug', 'GetDebug'),
    ('convert_lines_to_points', 'GetConvertLinesToPoints'),
    ('absolute_tolerance', 'GetAbsoluteTolerance'), ('q_factor',
    'GetQFactor'), ('tolerance_is_absolute', 'GetToleranceIsAbsolute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('tolerance', 'GetTolerance'), ('convert_polys_to_lines',
    'GetConvertPolysToLines'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'convert_lines_to_points',
    'convert_polys_to_lines', 'convert_strips_to_polys', 'debug',
    'global_warning_display', 'piece_invariant', 'point_merging',
    'release_data_flag', 'tolerance_is_absolute', 'absolute_tolerance',
    'progress_text', 'q_factor', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuantizePolyDataPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['convert_lines_to_points', 'convert_polys_to_lines',
            'convert_strips_to_polys', 'piece_invariant', 'point_merging',
            'tolerance_is_absolute'], [], ['absolute_tolerance', 'q_factor',
            'tolerance']),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

