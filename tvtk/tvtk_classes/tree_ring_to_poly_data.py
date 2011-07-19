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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class TreeRingToPolyData(PolyDataAlgorithm):
    """
    TreeRingToPolyData - converts a tree to a polygonal data
    
    Superclass: PolyDataAlgorithm
    
    This algorithm requires that the TreeRingLayout filter has already
    been applied to the data in order to create the quadruple array
    (start angle, end angle, inner radius, outer radius) of bounds for
    each vertex of the tree.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeRingToPolyData, obj, update, **traits)
    
    shrink_percentage = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Define a shrink percentage for each of the sectors.
        """
    )
    def _shrink_percentage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkPercentage,
                        self.shrink_percentage)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_sectors_array_name(self, *args):
        """
        V.set_sectors_array_name(string)
        C++: virtual void SetSectorsArrayName(const char *name)
        The field containing quadruples of the form (start angle, end
        angle, inner radius, outer radius) representing the bounds of the
        rectangles for each vertex. This field may be added to the tree
        using TreeRingLayout. This array must be set.
        """
        ret = self._wrap_call(self._vtk_obj.SetSectorsArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('shrink_percentage',
    'GetShrinkPercentage'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeRingToPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeRingToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['shrink_percentage']),
            title='Edit TreeRingToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeRingToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

