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


class GroupLeafVertices(TreeAlgorithm):
    """
    GroupLeafVertices - Filter that expands a tree, categorizing leaf
    vertices
    
    Superclass: TreeAlgorithm
    
    Use set_input_array_to_process(_0, ...) to set the array to group on.
    Currently this array must be a StringArray.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGroupLeafVertices, obj, update, **traits)
    
    group_domain = traits.String(r"group_vertex", enter_set=True, auto_set=False, help=\
        """
        The name of the domain that non-leaf vertices will be assigned
        to. If the input graph already contains vertices in this domain:
        - If the ids for this domain are numeric, starts assignment with
          max id
        - If the ids for this domain are strings, starts assignment with "group
          X" where "X" is the max id. Default is "group_vertex".
        """
    )
    def _group_domain_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGroupDomain,
                        self.group_domain)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('group_domain',
    'GetGroupDomain'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'group_domain', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GroupLeafVertices, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GroupLeafVertices properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['group_domain']),
            title='Edit GroupLeafVertices properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GroupLeafVertices properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

