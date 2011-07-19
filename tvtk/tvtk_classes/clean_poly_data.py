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


class CleanPolyData(PolyDataAlgorithm):
    """
    CleanPolyData - merge duplicate points, and/or remove unused
    points and/or remove degenerate cells
    
    Superclass: PolyDataAlgorithm
    
    CleanPolyData is a filter that takes polygonal data as input and
    generates polygonal data as output. CleanPolyData can merge
    duplicate points (within specified tolerance and if enabled),
    eliminate points that are not used, and if enabled, transform
    degenerate cells into appropriate forms (for example, a triangle is
    converted into a line if two points of triangle are merged).
    
    Conversion of degenerate cells is controlled by the flags
    convert_lines_to_points, convert_polys_to_lines, convert_strips_to_polys which
    act cumulatively such that a degenerate strip may become a poly. The
    full set is Line with 1 points -> Vert (if convert_lines_to_points) Poly
    with 2 points -> Line (if convert_polys_to_lines) Poly with 1 points ->
    Vert (if convert_polys_to_lines && convert_lines_to_points) Strp with 3
    points -> Poly (if convert_strips_to_polys) Strp with 2 points -> Line
    (if convert_strips_to_polys && convert_polys_to_lines) Strp with 1 points
    -> Vert (if convert_strips_to_polys && convert_polys_to_lines
      && convert_lines_to_points)
    
    If tolerance is specified precisely=0.0, then CleanPolyData will
    use the MergePoints object to merge points (which is faster).
    Otherwise the slower IncrementalPointLocator is used.  Before
    inserting points into the point locator, this class calls a function
    operate_on_point which can be used (in subclasses) to further refine
    the cleaning process. See QuantizePolyDataPoints.
    
    Note that merging of points can be disabled. In this case, a point
    locator will not be used, and points that are not used by any cells
    will be eliminated, but never merged.
    
    Caveats:
    
    Merging points can alter topology, including introducing non-manifold
    forms. The tolerance should be chosen carefully to avoid these
    problems. Subclasses should handle operate_on_bounds as well as
    operate_on_point to ensure that the locator is correctly initialized
    (i.e. all modified points must lie inside modified bounds).
    
    See Also:
    
    QuantizePolyDataPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCleanPolyData, obj, update, **traits)
    
    convert_lines_to_points = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off conversion of degenerate lines to points. Default is
        On.
        """
    )
    def _convert_lines_to_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertLinesToPoints,
                        self.convert_lines_to_points_)

    convert_strips_to_polys = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off conversion of degenerate strips to polys. Default is
        On.
        """
    )
    def _convert_strips_to_polys_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertStripsToPolys,
                        self.convert_strips_to_polys_)

    tolerance_is_absolute = tvtk_base.false_bool_trait(help=\
        """
        By default tolerance_is_absolute is false and Tolerance is a
        fraction of Bounding box diagonal, if true, absolute_tolerance is
        used when adding points to locator (merging)
        """
    )
    def _tolerance_is_absolute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetToleranceIsAbsolute,
                        self.tolerance_is_absolute_)

    piece_invariant = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _piece_invariant_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPieceInvariant,
                        self.piece_invariant_)

    convert_polys_to_lines = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off conversion of degenerate polys to lines. Default is
        On.
        """
    )
    def _convert_polys_to_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertPolysToLines,
                        self.convert_polys_to_lines_)

    point_merging = tvtk_base.true_bool_trait(help=\
        """
        Set/Get a boolean value that controls whether point merging is
        performed. If on, a locator will be used, and points laying
        within the appropriate tolerance may be merged. If off, points
        are never merged. By default, merging is on.
        """
    )
    def _point_merging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointMerging,
                        self.point_merging_)

    absolute_tolerance = traits.Trait(1.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify tolerance in absolute terms. Default is 1.0.
        """
    )
    def _absolute_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbsoluteTolerance,
                        self.absolute_tolerance)

    tolerance = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify tolerance in terms of fraction of bounding box length.
        Default is 0.0.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set/Get a spatial locator for speeding the search process. By
        default an instance of MergePoints is used.
        """
    )

    def create_default_locator(self, *args):
        """
        V.create_default_locator(PolyData)
        C++: void CreateDefaultLocator(PolyData *input=0)
        Create default locator. Used to create one when none is
        specified.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateDefaultLocator, *my_args)
        return ret

    def operate_on_bounds(self, *args):
        """
        V.operate_on_bounds([float, float, float, float, float, float],
            [float, float, float, float, float, float])
        C++: virtual void OperateOnBounds(double in[6], double out[6])
        Perform operation on bounds
        """
        ret = self._wrap_call(self._vtk_obj.OperateOnBounds, *args)
        return ret

    def operate_on_point(self, *args):
        """
        V.operate_on_point([float, float, float], [float, float, float])
        C++: virtual void OperateOnPoint(double in[3], double out[3])
        Perform operation on a point
        """
        ret = self._wrap_call(self._vtk_obj.OperateOnPoint, *args)
        return ret

    def release_locator(self):
        """
        V.release_locator()
        C++: void ReleaseLocator()
        Release locator
        """
        ret = self._vtk_obj.ReleaseLocator()
        return ret
        

    _updateable_traits_ = \
    (('tolerance_is_absolute', 'GetToleranceIsAbsolute'),
    ('point_merging', 'GetPointMerging'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('piece_invariant', 'GetPieceInvariant'),
    ('progress_text', 'GetProgressText'), ('convert_strips_to_polys',
    'GetConvertStripsToPolys'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('convert_lines_to_points',
    'GetConvertLinesToPoints'), ('release_data_flag',
    'GetReleaseDataFlag'), ('absolute_tolerance', 'GetAbsoluteTolerance'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('tolerance', 'GetTolerance'), ('convert_polys_to_lines',
    'GetConvertPolysToLines'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'convert_lines_to_points',
    'convert_polys_to_lines', 'convert_strips_to_polys', 'debug',
    'global_warning_display', 'piece_invariant', 'point_merging',
    'release_data_flag', 'tolerance_is_absolute', 'absolute_tolerance',
    'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CleanPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CleanPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['convert_lines_to_points', 'convert_polys_to_lines',
            'convert_strips_to_polys', 'piece_invariant', 'point_merging',
            'tolerance_is_absolute'], [], ['absolute_tolerance', 'tolerance']),
            title='Edit CleanPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CleanPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

