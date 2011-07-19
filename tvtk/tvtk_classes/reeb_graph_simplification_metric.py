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

from tvtk.tvtk_classes.object import Object


class ReebGraphSimplificationMetric(Object):
    """
    ReebGraphSimplificationMetric - abstract class for custom Reeb
    graph
    
    Superclass: Object
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReebGraphSimplificationMetric, obj, update, **traits)
    
    lower_bound = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the lowest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the compute_metric call to make sure the
        returned value of compute_metric call is indeed between 0 and 1.
        """
    )
    def _lower_bound_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerBound,
                        self.lower_bound)

    upper_bound = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the highest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the compute_metric call to make sure the
        returned value of compute_metric call is indeed between 0 and 1.
        """
    )
    def _upper_bound_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperBound,
                        self.upper_bound)

    def compute_metric(self, *args):
        """
        V.compute_metric(DataSet, DataArray, int, AbstractArray,
            int) -> float
        C++: virtual double ComputeMetric(DataSet *mesh,
            DataArray *field, IdType startCriticalPoint,
            AbstractArray *vertexList, IdType endCriticalPoint)
        Function to implement in your simplification metric algorithm.
        Given the input mesh and the Ids of the vertices living on the
        Reeb graph arc to consider for removal, you should return a value
        between 0 and 1 (the smallest the more likely the arc will be
        removed, depending on the user-defined simplification threshold).
        """
        my_args = deref_array(args, [('vtkDataSet', 'vtkDataArray', 'int', 'vtkAbstractArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.ComputeMetric, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('lower_bound',
    'GetLowerBound'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('upper_bound', 'GetUpperBound'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'lower_bound', 'upper_bound'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReebGraphSimplificationMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['lower_bound', 'upper_bound']),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

