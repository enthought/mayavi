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

from tvtk.tvtk_classes.contour_line_interpolator import ContourLineInterpolator


class BezierContourLineInterpolator(ContourLineInterpolator):
    """
    BezierContourLineInterpolator - Interpolates supplied nodes with
    bezier line segments
    
    Superclass: ContourLineInterpolator
    
    The line interpolator interpolates supplied nodes (see
    interpolate_line) with bezier line segments. The finess of the curve
    may be controlled using set_maximum_curve_error and
    set_maximum_number_of_line_segments.
    
    See Also:
    
    ContourLineInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBezierContourLineInterpolator, obj, update, **traits)
    
    maximum_curve_error = traits.Trait(0.005, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        The difference between a line segment connecting two points and
        the curve connecting the same points. In the limit of the length
        of the curve dx -> 0, the two values will be the same. The
        smaller this number, the finer the bezier curve will be
        interpolated. Default is 0.005
        """
    )
    def _maximum_curve_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumCurveError,
                        self.maximum_curve_error)

    maximum_curve_line_segments = traits.Trait(100, traits.Range(1, 1000, enter_set=True, auto_set=False), help=\
        """
        Maximum number of bezier line segments between two nodes. Larger
        values create a finer interpolation. Default is 100.
        """
    )
    def _maximum_curve_line_segments_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumCurveLineSegments,
                        self.maximum_curve_line_segments)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_curve_error', 'GetMaximumCurveError'),
    ('maximum_curve_line_segments', 'GetMaximumCurveLineSegments'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maximum_curve_error',
    'maximum_curve_line_segments'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BezierContourLineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BezierContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['maximum_curve_error',
            'maximum_curve_line_segments']),
            title='Edit BezierContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BezierContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

