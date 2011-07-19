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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class ImplicitDataSet(ImplicitFunction):
    """
    ImplicitDataSet - treat a dataset as if it were an implicit
    function
    
    Superclass: ImplicitFunction
    
    ImplicitDataSet treats any type of dataset as if it were an
    implicit function. This means it computes a function value and
    gradient. ImplicitDataSet is a concrete implementation of
    ImplicitFunction.
    
    ImplicitDataSet computes the function (at the point x) by
    performing cell interpolation. That is, it finds the cell containing
    x, and then uses the cell's interpolation functions to compute an
    interpolated scalar value at x. (A similar approach is used to find
    the gradient, if requested.) Points outside of the dataset are
    assigned the value of the ivar out_value, and the gradient value
    out_gradient.
    
    Caveats:
    
    Any type of dataset can be used as an implicit function as long as it
    has scalar data associated with it.
    
    See Also:
    
    ImplicitFunction ImplicitVolume ClipPolyData Cutter
    ImplicitWindowFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitDataSet, obj, update, **traits)
    
    out_value = traits.Float(-1e+299, enter_set=True, auto_set=False, help=\
        """
        Set / get the function value to use for points outside of the
        dataset.
        """
    )
    def _out_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutValue,
                        self.out_value)

    out_gradient = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _out_gradient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutGradient,
                        self.out_gradient)

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Set / get the dataset used for the implicit function evaluation.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('out_value', 'GetOutValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('out_gradient', 'GetOutGradient'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'out_gradient', 'out_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['out_gradient', 'out_value']),
            title='Edit ImplicitDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

