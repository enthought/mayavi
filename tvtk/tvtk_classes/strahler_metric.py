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

from tvtk.tvtk_classes.tree_algorithm import TreeAlgorithm


class StrahlerMetric(TreeAlgorithm):
    """
    StrahlerMetric - compute Strahler metric for a tree
    
    Superclass: TreeAlgorithm
    
    The Strahler metric is a value assigned to each vertex of a tree that
    characterizes the structural complexity of the sub-tree rooted at
    that node.  The metric originated in the study of river systems, but
    has been applied to other tree- structured systes,  Details of the
    metric and the rationale for using it in infovis can be found in:
    
    Tree Visualization and Navigation Clues for Information
    Visualization, I. Herman, M. Delest, and G. Melancon, Computer
    Graphics Forum, Vol 17(2), Blackwell, 1998.
    
    The input tree is copied to the output, but with a new array added to
    the output vertex data.
    
    Thanks:
    
    Thanks to David Duke from the University of Leeds for providing this
    implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStrahlerMetric, obj, update, **traits)
    
    normalize = tvtk_base.false_bool_trait(help=\
        """
        Set/get setting of normalize flag.  If this is set, the Strahler
        values are scaled into the range [0..1]. Default is for
        normalization to be OFF.
        """
    )
    def _normalize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalize,
                        self.normalize_)

    def _get_max_strahler(self):
        return self._vtk_obj.GetMaxStrahler()
    max_strahler = traits.Property(_get_max_strahler, help=\
        """
        Get the maximum strahler value for the tree.
        """
    )

    def set_metric_array_name(self, *args):
        """
        V.set_metric_array_name(string)
        C++: void SetMetricArrayName(char *)
        Set the name of the array in which the Strahler values will be
        stored within the output vertex data. Default is "Strahler"
        """
        ret = self._wrap_call(self._vtk_obj.SetMetricArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('normalize', 'GetNormalize'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'normalize',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StrahlerMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StrahlerMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['normalize'], [], []),
            title='Edit StrahlerMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StrahlerMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

