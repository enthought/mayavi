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

from tvtk.tvtk_classes.generic_subdivision_error_metric import GenericSubdivisionErrorMetric


class GeometricErrorMetric(GenericSubdivisionErrorMetric):
    """
    GeometricErrorMetric - Objects that compute
    
    Superclass: GenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on a geometric criterium: the
    variation of the edge from a straight line.
    
    See Also:
    
    GenericCellTessellator GenericSubdivisionErrorMetric
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeometricErrorMetric, obj, update, **traits)
    
    absolute_geometric_tolerance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the geometric accuracy with a squared absolute value. This is
        the geometric object-based accuracy. Subdivision will be required
        if the square distance between the real point and the straight
        line passing through the vertices of the edge is greater than
        `value'. For instance 0.01 will give better result than 0.1.
        \pre positive_value: value>0
        """
    )
    def _absolute_geometric_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbsoluteGeometricTolerance,
                        self.absolute_geometric_tolerance)

    def _get_relative(self):
        return self._vtk_obj.GetRelative()
    relative = traits.Property(_get_relative, help=\
        """
        Return the type of output of get_error()
        """
    )

    def set_relative_geometric_tolerance(self, *args):
        """
        V.set_relative_geometric_tolerance(float, GenericDataSet)
        C++: void SetRelativeGeometricTolerance(double value,
            GenericDataSet *ds)
        Set the geometric accuracy with a value relative to the length of
        the bounding box of the dataset. Internally compute the absolute
        tolerance. For instance 0.01 will give better result than 0.1.
        \pre valid_range_value: value>0 && value<1
        \pre ds_exists: ds!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRelativeGeometricTolerance, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('absolute_geometric_tolerance', 'GetAbsoluteGeometricTolerance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'absolute_geometric_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeometricErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeometricErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['absolute_geometric_tolerance']),
            title='Edit GeometricErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeometricErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

