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

from tvtk.tvtk_classes.context_item import ContextItem


class Axis(ContextItem):
    """
    Axis - takes care of drawing 2d axes
    
    Superclass: ContextItem
    
    The Axis is drawn in screen coordinates. It is usually one of the
    last elements of a chart to be drawn. It renders the axis label, tick
    marks and tick labels.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxis, obj, update, **traits)
    
    log_scale = traits.Bool(False, help=\
        """
        Get/set whether the axis should use a log scale, default is
        false.
        """
    )
    def _log_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogScale,
                        self.log_scale)

    labels_visible = traits.Bool(True, help=\
        """
        Get/set whether the axis labels should be visible.
        """
    )
    def _labels_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelsVisible,
                        self.labels_visible)

    precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Get/set the numerical precision to use, default is 2.
        """
    )
    def _precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrecision,
                        self.precision)

    notation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the numerical notation, standard, scientific or mixed (0,
        1, 2).
        """
    )
    def _notation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNotation,
                        self.notation)

    number_of_ticks = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the number of tick marks for this axis. Default is -1, which
        leads to automatic calculation of nicely spaced tick marks.
        """
    )
    def _number_of_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTicks,
                        self.number_of_ticks)

    title = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Get/set the title text of the axis.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_tick_labels(self):
        return wrap_vtk(self._vtk_obj.GetTickLabels())
    def _set_tick_labels(self, arg):
        old_val = self._get_tick_labels()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetTickLabels,
                        my_arg[0])
        self.trait_property_changed('tick_labels', old_val, arg)
    tick_labels = traits.Property(_get_tick_labels, _set_tick_labels, help=\
        """
        A string array containing the tick labels for the axis.
        """
    )

    grid_visible = traits.Bool(True, help=\
        """
        Get/set whether the axis grid lines should be drawn, default is
        true.
        """
    )
    def _grid_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridVisible,
                        self.grid_visible)

    maximum = traits.Float(6.66, enter_set=True, auto_set=False, help=\
        """
        Set the logical maximum value of the axis, in plot coordinates.
        """
    )
    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    point1 = traits.Array(shape=(2,), value=(0.0, 10.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set point 1 of the axis (in pixels), this is usually the origin.
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(2,), value=(0.0, 10.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set point 2 of the axis (in pixels), this is usually the
        terminus.
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    minimum = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the logical minimum value of the axis, in plot coordinates.
        """
    )
    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum)

    behavior = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the behavior of the axis (auto, fixed, custom). Default
        is 0 (auto).
        """
    )
    def _behavior_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBehavior,
                        self.behavior)

    position = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the position of the axis (LEFT, BOTTOM, RIGHT, TOP,
        PARALLEL).
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    def _get_tick_positions(self):
        return wrap_vtk(self._vtk_obj.GetTickPositions())
    def _set_tick_positions(self, arg):
        old_val = self._get_tick_positions()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetTickPositions,
                        my_arg[0])
        self.trait_property_changed('tick_positions', old_val, arg)
    tick_positions = traits.Property(_get_tick_positions, _set_tick_positions, help=\
        """
        An array with the positions of the tick marks along the axis
        line. The positions are specified in the plot coordinates of the
        axis.
        """
    )

    def _get_grid_pen(self):
        return wrap_vtk(self._vtk_obj.GetGridPen())
    grid_pen = traits.Property(_get_grid_pen, help=\
        """
        Get a pointer to the Pen object that controls the way this
        axis is drawn.
        """
    )

    def _get_label_properties(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperties())
    label_properties = traits.Property(_get_label_properties, help=\
        """
        Get the TextProperty that governs how the axis lables are
        displayed. Note that the alignment properties are not used.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get a pointer to the Pen object that controls the way this
        axis is drawn.
        """
    )

    def _get_tick_scene_positions(self):
        return wrap_vtk(self._vtk_obj.GetTickScenePositions())
    tick_scene_positions = traits.Property(_get_tick_scene_positions, help=\
        """
        An array with the positions of the tick marks along the axis
        line. The positions are specified in scene coordinates.
        """
    )

    def _get_title_properties(self):
        return wrap_vtk(self._vtk_obj.GetTitleProperties())
    title_properties = traits.Property(_get_title_properties, help=\
        """
        Get the TextProperty that governs how the axis title is
        displayed.
        """
    )

    def auto_scale(self):
        """
        V.auto_scale()
        C++: virtual void AutoScale()
        Use this function to autoscale the axes after setting the minimum
        and maximum values. This will cause the axes to select the nicest
        numbers that enclose the minimum and maximum values, and to
        select an appropriate number of tick marks.
        """
        ret = self._vtk_obj.AutoScale()
        return ret
        

    def recalculate_tick_spacing(self):
        """
        V.recalculate_tick_spacing()
        C++: virtual void RecalculateTickSpacing()
        Recalculate the spacing of the tick marks - typically useful to
        do after scaling the axis.
        """
        ret = self._vtk_obj.RecalculateTickSpacing()
        return ret
        

    def set_range(self, *args):
        """
        V.set_range(float, float)
        C++: virtual void SetRange(double minimum, double maximum)
        Get the logical range of the axis, in plot coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetRange, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('log_scale', 'GetLogScale'), ('notation',
    'GetNotation'), ('precision', 'GetPrecision'), ('number_of_ticks',
    'GetNumberOfTicks'), ('visible', 'GetVisible'), ('minimum',
    'GetMinimum'), ('grid_visible', 'GetGridVisible'), ('labels_visible',
    'GetLabelsVisible'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('title', 'GetTitle'), ('debug',
    'GetDebug'), ('maximum', 'GetMaximum'), ('point1', 'GetPoint1'),
    ('point2', 'GetPoint2'), ('behavior', 'GetBehavior'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'behavior', 'grid_visible',
    'labels_visible', 'log_scale', 'maximum', 'minimum', 'notation',
    'number_of_ticks', 'opacity', 'point1', 'point2', 'position',
    'precision', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Axis, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['behavior', 'grid_visible', 'labels_visible',
            'log_scale', 'maximum', 'minimum', 'notation', 'number_of_ticks',
            'opacity', 'point1', 'point2', 'position', 'precision', 'title',
            'visible']),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

