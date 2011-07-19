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


class PlotHistogram2D(Plot):
    """
    TwoDHistogramItem - 2d histogram item.
    
    Superclass: Plot
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotHistogram2D, obj, update, **traits)
    
    def _get_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetTransferFunction())
    def _set_transfer_function(self, arg):
        old_val = self._get_transfer_function()
        self._wrap_call(self._vtk_obj.SetTransferFunction,
                        deref_vtk(arg))
        self.trait_property_changed('transfer_function', old_val, arg)
    transfer_function = traits.Property(_get_transfer_function, _set_transfer_function, help=\
        """
        Get the color transfer function that is used to generate the
        histogram.
        """
    )

    def _get_input_image_data(self):
        return wrap_vtk(self._vtk_obj.GetInputImageData())
    input_image_data = traits.Property(_get_input_image_data, help=\
        """
        Get the input table used by the plot.
        """
    )

    def set_input(self, *args):
        """
        V.set_input(ImageData, int)
        C++: virtual void SetInput(ImageData *data, IdType z=0)
        V.set_input(Table)
        C++: virtual void SetInput(Table *)
        V.set_input(Table, string, string)
        C++: virtual void SetInput(Table *, const StdString &,
            const StdString &)
        Set the input, we are expecting a ImageData with just one
        component, this would normally be a float or a double. It will be
        passed to the other functions as a double to generate a color.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('width', 'GetWidth'), ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'label', 'opacity',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'opacity', 'use_index_for_x_series',
            'visible', 'width']),
            title='Edit PlotHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

