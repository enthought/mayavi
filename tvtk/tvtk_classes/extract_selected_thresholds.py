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

from tvtk.tvtk_classes.extract_selection_base import ExtractSelectionBase


class ExtractSelectedThresholds(ExtractSelectionBase):
    """
    ExtractSelectedThresholds - extract a cells or points from a 
    
    Superclass: ExtractSelectionBase
    
    ExtractSelectedThresholds extracts all cells and points with
    attribute values that lie within a Selection's THRESHOLD contents.
    The selecion can specify to threshold a particular array within
    either the point or cell attribute data of the input. This is similar
    to Threshold but allows mutliple thresholds ranges. This filter
    adds a scalar array called OriginalCellIds that says what input
    cell produced each output cell. This is an example of a Pedigree ID
    which helps to trace back results.
    
    See Also:
    
    Selection ExtractSelection Threshold
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSelectedThresholds, obj, update, **traits)
    
    def evaluate_value(self, *args):
        """
        V.evaluate_value(DataArray, int, DataArray) -> int
        C++: static int EvaluateValue(DataArray *scalars, IdType id,
             DataArray *lims)
        V.evaluate_value(DataArray, int, int, DataArray) -> int
        C++: static int EvaluateValue(DataArray *array,
            int array_component_no, IdType id, DataArray *lims)
        Function for determining whether a value in a data array passes
        the threshold test(s) provided in lims.  Returns 1 if the value
        passes at least one of the threshold tests. If scalars is NULL,
        then the id itself is used as the scalar value.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', 'vtkDataArray'), ('vtkDataArray', 'int', 'int', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.EvaluateValue, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('preserve_topology',
    'GetPreserveTopology'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'preserve_topology', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSelectedThresholds, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['preserve_topology'], [], []),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

