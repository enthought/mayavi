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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class CastToConcrete(DataSetAlgorithm):
    """
    CastToConcrete - works around type-checking limitations
    
    Superclass: DataSetAlgorithm
    
    CastToConcrete is a filter that works around type-checking
    limitations in the filter classes. Some filters generate abstract
    types on output, and cannot be connected to the input of filters
    requiring a concrete input type. For example, ElevationFilter
    generates DataSet for output, and cannot be connected to
    Decimate, because Decimate requires PolyData as input. This
    is true even though (in this example) the input to ElevationFilter
    is of type PolyData, and you know the output of ElevationFilter
    is the same type as its input.
    
    CastToConcrete performs run-time checking to insure that output
    type is of the right type. An error message will result if you try to
    cast an input type improperly. Otherwise, the filter performs the
    appropriate cast and returns the data.
    
    Caveats:
    
    You must specify the input before you can get the output. Otherwise
    an error results.
    
    See Also:
    
    DataSetAlgorithm PointSetToPointSetFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCastToConcrete, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CastToConcrete, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CastToConcrete properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CastToConcrete properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CastToConcrete properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

