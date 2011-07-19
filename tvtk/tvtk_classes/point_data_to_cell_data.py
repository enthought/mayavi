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


class PointDataToCellData(DataSetAlgorithm):
    """
    PointDataToCellData - map point data to cell data
    
    Superclass: DataSetAlgorithm
    
    PointDataToCellData is a filter that transforms point data (i.e.,
    data specified per point) into cell data (i.e., data specified per
    cell). The method of transformation is based on averaging the data
    values of all points defining a particular cell. Optionally, the
    input point data can be passed through to the output as well.
    
    Caveats:
    
    This filter is an abstract filter, that is, the output is an abstract
    type (i.e., DataSet). Use the convenience methods (e.g.,
    get_poly_data_output(), get_structured_points_output(), etc.) to get the
    type of output you want.
    
    See Also:
    
    PointData CellData CellDataToPointData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointDataToCellData, obj, update, **traits)
    
    pass_point_data = tvtk_base.false_bool_trait(help=\
        """
        Control whether the input point data is to be passed to the
        output. If on, then the input point data is passed through to the
        output; otherwise, only generated point data is placed into the
        output.
        """
    )
    def _pass_point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPointData,
                        self.pass_point_data_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('pass_point_data',
    'GetPassPointData'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_point_data', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointDataToCellData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointDataToCellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pass_point_data'], [], []),
            title='Edit PointDataToCellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointDataToCellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

