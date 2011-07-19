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

from tvtk.tvtk_classes.area_layout_strategy import AreaLayoutStrategy


class StackedTreeLayoutStrategy(AreaLayoutStrategy):
    """
    StackedTreeLayoutStrategy - lays out tree in stacked boxes or rings
    
    Superclass: AreaLayoutStrategy
    
    Performs a tree ring layout or "icicle" layout on a tree. This
    involves assigning a sector region to each vertex in the tree, and
    placing that information in a data array with four components per
    tuple representing (inner_radius, outer_radius, start_angle, end_angle).
    
    This class may be assigned as the layout strategy to AreaLayout.
    
    Thanks:
    
    Thanks to Jason Shepherd from Sandia National Laboratories for help
    developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStackedTreeLayoutStrategy, obj, update, **traits)
    
    reverse = tvtk_base.false_bool_trait(help=\
        """
        Define whether to reverse the order of the tree stacks from low
        to high.
        """
    )
    def _reverse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverse,
                        self.reverse_)

    use_rectangular_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Define whether or not rectangular coordinates are being used (as
        opposed to polar coordinates).
        """
    )
    def _use_rectangular_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRectangularCoordinates,
                        self.use_rectangular_coordinates_)

    ring_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Define the thickness of each of the tree rings.
        """
    )
    def _ring_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRingThickness,
                        self.ring_thickness)

    root_start_angle = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Define the start angle for the root node. NOTE: It is assumed
        that the root end angle is greater than the root start angle and
        subtends no more than 360 degrees.
        """
    )
    def _root_start_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRootStartAngle,
                        self.root_start_angle)

    interior_log_spacing_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The spacing of tree levels in the edge routing tree. Levels near
        zero give more space to levels near the root, while levels near
        one (the default) create evenly-spaced levels. Levels above one
        give more space to levels near the leaves.
        """
    )
    def _interior_log_spacing_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteriorLogSpacingValue,
                        self.interior_log_spacing_value)

    interior_radius = traits.Float(6.0, enter_set=True, auto_set=False, help=\
        """
        Define the tree ring's interior radius.
        """
    )
    def _interior_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteriorRadius,
                        self.interior_radius)

    root_end_angle = traits.Float(360.0, enter_set=True, auto_set=False, help=\
        """
        Define the end angle for the root node. NOTE: It is assumed that
        the root end angle is greater than the root start angle and
        subtends no more than 360 degrees.
        """
    )
    def _root_end_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRootEndAngle,
                        self.root_end_angle)

    _updateable_traits_ = \
    (('root_start_angle', 'GetRootStartAngle'), ('reverse', 'GetReverse'),
    ('interior_radius', 'GetInteriorRadius'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'),
    ('interior_log_spacing_value', 'GetInteriorLogSpacingValue'),
    ('ring_thickness', 'GetRingThickness'), ('reference_count',
    'GetReferenceCount'), ('root_end_angle', 'GetRootEndAngle'),
    ('use_rectangular_coordinates', 'GetUseRectangularCoordinates'),
    ('shrink_percentage', 'GetShrinkPercentage'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'reverse',
    'use_rectangular_coordinates', 'interior_log_spacing_value',
    'interior_radius', 'ring_thickness', 'root_end_angle',
    'root_start_angle', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StackedTreeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StackedTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['reverse', 'use_rectangular_coordinates'], [],
            ['interior_log_spacing_value', 'interior_radius', 'ring_thickness',
            'root_end_angle', 'root_start_angle', 'shrink_percentage']),
            title='Edit StackedTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StackedTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

