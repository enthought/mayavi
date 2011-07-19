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

from tvtk.tvtk_classes.plot import Plot


class PlotParallelCoordinates(Plot):
    """
    PlotParallelCoordinates - Class for drawing a parallel coordinate
    
    Superclass: Plot
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotParallelCoordinates, obj, update, **traits)
    
    scalar_visibility = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
    )
    def _scalar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarVisibility,
                        self.scalar_visibility_)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify a lookup table for the mapper to use.
        """
    )

    def _get_color_array_name(self):
        return self._vtk_obj.GetColorArrayName()
    color_array_name = traits.Property(_get_color_array_name, help=\
        """
        Get the array name to color by.
        """
    )

    def create_default_lookup_table(self):
        """
        V.create_default_lookup_table()
        C++: virtual void CreateDefaultLookupTable()
        Create default lookup table. Generally used to create one when
        none is available with the scalar data.
        """
        ret = self._vtk_obj.CreateDefaultLookupTable()
        return ret
        

    def reset_selection_range(self):
        """
        V.reset_selection_range() -> bool
        C++: bool ResetSelectionRange()
        Reset the selection criteria for the chart.
        """
        ret = self._vtk_obj.ResetSelectionRange()
        return ret
        

    def select_color_array(self, *args):
        """
        V.select_color_array(int)
        C++: void SelectColorArray(IdType arrayNum)
        V.select_color_array(string)
        C++: void SelectColorArray(const StdString &arrayName)
        When scalar_mode is set to use_point_field_data or use_cell_field_data,
        you can specify which array to use for coloring using these
        methods. The lookup table will decide how to convert vectors to
        colors.
        """
        ret = self._wrap_call(self._vtk_obj.SelectColorArray, *args)
        return ret

    def set_input(self, *args):
        """
        V.set_input(Table)
        C++: virtual void SetInput(Table *table)
        V.set_input(Table, string, string)
        C++: virtual void SetInput(Table *table, const StdString &,
            const StdString &)
        This is a convenience function to set the input table.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def set_selection_range(self, *args):
        """
        V.set_selection_range(int, float, float) -> bool
        C++: bool SetSelectionRange(int Axis, float low, float high)
        Set the selection criteria on the given axis in normalized space
        (0.0 - 1.0).
        """
        ret = self._wrap_call(self._vtk_obj.SetSelectionRange, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('scalar_visibility', 'GetScalarVisibility'), ('width', 'GetWidth'),
    ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scalar_visibility', 'label',
    'opacity', 'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotParallelCoordinates, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scalar_visibility'], [], ['label', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit PlotParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

