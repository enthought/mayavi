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

from tvtk.tvtk_classes.data_object import DataObject


class PiecewiseFunction(DataObject):
    """
    PiecewiseFunction - Defines a 1d piecewise function.
    
    Superclass: DataObject
    
    Defines a piecewise function mapping. This mapping allows the
    addition of control points, and allows the user to control the
    function between the control points. A piecewise hermite curve is
    used between control points, based on the sharpness and midpoint
    parameters. A sharpness of 0 yields a piecewise linear function and a
    sharpness of 1 yields a piecewise constant function. The midpoint is
    the normalized distance between control points at which the curve
    reaches the median Y value. The midpoint and sharpness values
    specified when adding a node are used to control the transition to
    the next node (the last node's values are ignored) Outside the range
    of nodes, the values are 0 if Clamping is off, or the nearest node
    point if Clamping is on. Using the legacy methods for adding points 
    (which do not have Sharpness and Midpoint parameters) will default to
    Midpoint = 0.5 (halfway between the control points) and Sharpness =
    0.0 (linear).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPiecewiseFunction, obj, update, **traits)
    
    clamping = tvtk_base.true_bool_trait(help=\
        """
        When zero range clamping is Off, get_value() returns 0.0 when a
        value is requested outside of the points specified. When zero
        range clamping is On, get_value() returns the value at the value
        at the lowest point for a request below all points specified and
        returns the value at the highest point for a request above all
        points specified. On is the default.
        """
    )
    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    allow_duplicate_scalars = tvtk_base.false_bool_trait(help=\
        """
        Toggle whether to allow duplicate scalar values in the piecewise
        function (off by default).
        """
    )
    def _allow_duplicate_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowDuplicateScalars,
                        self.allow_duplicate_scalars_)

    def get_node_value(self, *args):
        """
        V.get_node_value(int, [float, float, float, float]) -> int
        C++: int GetNodeValue(int index, double val[4])
        For the node specified by index, set/get the location (X), value
        (Y), midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeValue, *args)
        return ret

    def set_node_value(self, *args):
        """
        V.set_node_value(int, [float, float, float, float]) -> int
        C++: int SetNodeValue(int index, double val[4])
        For the node specified by index, set/get the location (X), value
        (Y), midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.SetNodeValue, *args)
        return ret

    def _get_first_non_zero_value(self):
        return self._vtk_obj.GetFirstNonZeroValue()
    first_non_zero_value = traits.Property(_get_first_non_zero_value, help=\
        """
        Returns the first point location which precedes a non-zero
        segment of the function. Note that the value at this point may be
        zero.
        """
    )

    def _get_range(self):
        return self._vtk_obj.GetRange()
    range = traits.Property(_get_range, help=\
        """
        
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Get the number of points used to specify the function
        """
    )

    def _get_type(self):
        return self._vtk_obj.GetType()
    type = traits.Property(_get_type, help=\
        """
        Return the type of function: Function Types:
           0 : Constant        (No change in slope between end points)
           1 : non_decreasing   (Always increasing or zero slope)
           2 : non_increasing   (Always decreasing or zero slope)
           3 : Varied          (Contains both decreasing and increasing
        slopes)
        """
    )

    def get_value(self, *args):
        """
        V.get_value(float) -> float
        C++: double GetValue(double x)
        Returns the value of the function at the specified location using
        the specified interpolation.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def add_point(self, *args):
        """
        V.add_point(float, float) -> int
        C++: int AddPoint(double x, double y)
        V.add_point(float, float, float, float) -> int
        C++: int AddPoint(double x, double y, double midpoint,
            double sharpness)
        Add/Remove points to/from the function. If a duplicate point is
        added then the function value is changed at that location. Return
        the index of the point (0 based), or -1 on error.
        """
        ret = self._wrap_call(self._vtk_obj.AddPoint, *args)
        return ret

    def add_segment(self, *args):
        """
        V.add_segment(float, float, float, float)
        C++: void AddSegment(double x1, double y1, double x2, double y2)
        Add a line segment to the function. All points defined between
        the two points specified are removed from the function. This is a
        legacy method that does not allow the specification of the
        sharpness and midpoint values for the two nodes.
        """
        ret = self._wrap_call(self._vtk_obj.AddSegment, *args)
        return ret

    def adjust_range(self, *args):
        """
        V.adjust_range([float, float]) -> int
        C++: int AdjustRange(double range[2])
        Remove all points out of the new range, and make sure there is a
        point at each end of that range. Return 1 on success, 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.AdjustRange, *args)
        return ret

    def remove_all_points(self):
        """
        V.remove_all_points()
        C++: void RemoveAllPoints()
        Removes all points from the function.
        """
        ret = self._vtk_obj.RemoveAllPoints()
        return ret
        

    def remove_point(self, *args):
        """
        V.remove_point(float) -> int
        C++: int RemovePoint(double x)
        Add/Remove points to/from the function. If a duplicate point is
        added then the function value is changed at that location. Return
        the index of the point (0 based), or -1 on error.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('allow_duplicate_scalars', 'GetAllowDuplicateScalars'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('clamping', 'GetClamping'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('request_exact_extent',
    'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['allow_duplicate_scalars', 'clamping', 'debug',
    'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PiecewiseFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PiecewiseFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_duplicate_scalars', 'clamping',
            'global_release_data_flag', 'request_exact_extent'], [],
            ['maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
            'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
            'whole_extent']),
            title='Edit PiecewiseFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PiecewiseFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

