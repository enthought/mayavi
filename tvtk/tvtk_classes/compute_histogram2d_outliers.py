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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class ComputeHistogram2DOutliers(SelectionAlgorithm):
    """
    ComputeHistogram2DOutliers - compute the outliers in a set
    
    Superclass: SelectionAlgorithm
    
    This class takes a table and one or more ImageData histograms as
    input
     and computes the outliers in that data.  In general it does so by
     identifying histogram bins that are removed by a median (salt and
    pepper)
     filter and below a threshold.  This threshold is automatically
    identified
     to retrieve a number of outliers close to a user-determined value. 
    This
     value is set by calling set_preferred_number_of_outliers(int).
    
    
     The image data input can come either as a multiple ImageData via
    the
     repeatable INPUT_HISTOGRAM_IMAGE_DATA port, or as a single
     MultiBlockDataSet containing ImageData objects as blocks.  One
     or the other must be set, not both (or neither).
    
    
     The output can be retrieved as a set of row ids in a Selection or
     as a Table containing the actual outlier row data.
    
    See Also:
    
    
     ExtractHistogram2D PComputeHistogram2DOutliers
    
    Thanks:
    
    
     Developed by David Feng at Sandia National Laboratories
    ----------------------------------------------------------------------
        --------
    ----------------------------------------------------------------------
        --------
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkComputeHistogram2DOutliers, obj, update, **traits)
    
    preferred_number_of_outliers = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _preferred_number_of_outliers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreferredNumberOfOutliers,
                        self.preferred_number_of_outliers)

    def _get_output_table(self):
        return wrap_vtk(self._vtk_obj.GetOutputTable())
    output_table = traits.Property(_get_output_table, help=\
        """
        
        """
    )

    def set_input_histogram_image_data_connection(self, *args):
        """
        V.set_input_histogram_image_data_connection(AlgorithmOutput)
        C++: void SetInputHistogramImageDataConnection(
            AlgorithmOutput *cxn)
        Set the input histogram data as a (repeatable) ImageData
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputHistogramImageDataConnection, *my_args)
        return ret

    def set_input_histogram_multi_block_connection(self, *args):
        """
        V.set_input_histogram_multi_block_connection(AlgorithmOutput)
        C++: void SetInputHistogramMultiBlockConnection(
            AlgorithmOutput *cxn)
        Set the input histogram data as a MultiBlockData set
        containing multiple ImageData objects.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputHistogramMultiBlockConnection, *my_args)
        return ret

    def set_input_table_connection(self, *args):
        """
        V.set_input_table_connection(AlgorithmOutput)
        C++: void SetInputTableConnection(AlgorithmOutput *cxn)
        Set the source table data, from which data will be filtered.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputTableConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('preferred_number_of_outliers', 'GetPreferredNumberOfOutliers'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'preferred_number_of_outliers', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ComputeHistogram2DOutliers, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ComputeHistogram2DOutliers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['preferred_number_of_outliers']),
            title='Edit ComputeHistogram2DOutliers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ComputeHistogram2DOutliers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

