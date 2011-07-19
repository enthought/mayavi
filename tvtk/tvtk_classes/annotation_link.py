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

from tvtk.tvtk_classes.annotation_layers_algorithm import AnnotationLayersAlgorithm


class AnnotationLink(AnnotationLayersAlgorithm):
    """
    AnnotationLink - An algorithm for linking annotations among objects
    
    Superclass: AnnotationLayersAlgorithm
    
    AnnotationLink is a simple source filter which outputs the
    AnnotationLayers object stored internally.  Multiple objects may
    share the same annotation link filter and connect it to an internal
    pipeline so that if one object changes the annotation set, it will be
    pulled into all the other objects when their pipelines update.
    
    The shared AnnotationLayers object (a collection of annotations)
    is shallow copied to output port 0.
    
    AnnotationLink can also store a set of domain maps. A domain map
    is simply a table associating values between domains. The domain of
    each column is defined by the array name of the column. The domain
    maps are sent to a multi-block dataset in output port 1.
    
    Output ports 0 and 1 can be set as input ports 0 and 1 to
    ConvertSelectionDomain, which can use the domain maps to convert
    the domains of selections in the AnnotationLayers to match a
    particular data object (set as port 2 on ConvertSelectionDomain).
    
    The shared AnnotationLayers object also stores a "current
    selection" normally interpreted as the interactive selection of an
    application. As a convenience, this selection is sent to output port
    2 so that it can be connected to pipelines requiring a Selection.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAnnotationLink, obj, update, **traits)
    
    def _get_annotation_layers(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLayers())
    def _set_annotation_layers(self, arg):
        old_val = self._get_annotation_layers()
        self._wrap_call(self._vtk_obj.SetAnnotationLayers,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_layers', old_val, arg)
    annotation_layers = traits.Property(_get_annotation_layers, _set_annotation_layers, help=\
        """
        The annotations to be shared.
        """
    )

    def _get_current_selection(self):
        return wrap_vtk(self._vtk_obj.GetCurrentSelection())
    def _set_current_selection(self, arg):
        old_val = self._get_current_selection()
        self._wrap_call(self._vtk_obj.SetCurrentSelection,
                        deref_vtk(arg))
        self.trait_property_changed('current_selection', old_val, arg)
    current_selection = traits.Property(_get_current_selection, _set_current_selection, help=\
        """
        Set or get the current selection in the annotation layers.
        """
    )

    def get_domain_map(self, *args):
        """
        V.get_domain_map(int) -> Table
        C++: Table *GetDomainMap(int i)
        The domain mappings.
        """
        ret = self._wrap_call(self._vtk_obj.GetDomainMap, *args)
        return wrap_vtk(ret)

    def _get_number_of_domain_maps(self):
        return self._vtk_obj.GetNumberOfDomainMaps()
    number_of_domain_maps = traits.Property(_get_number_of_domain_maps, help=\
        """
        The domain mappings.
        """
    )

    def add_domain_map(self, *args):
        """
        V.add_domain_map(Table)
        C++: void AddDomainMap(Table *map)
        The domain mappings.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDomainMap, *my_args)
        return ret

    def remove_all_domain_maps(self):
        """
        V.remove_all_domain_maps()
        C++: void RemoveAllDomainMaps()
        The domain mappings.
        """
        ret = self._vtk_obj.RemoveAllDomainMaps()
        return ret
        

    def remove_domain_map(self, *args):
        """
        V.remove_domain_map(Table)
        C++: void RemoveDomainMap(Table *map)
        The domain mappings.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveDomainMap, *my_args)
        return ret

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
            return super(AnnotationLink, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AnnotationLink properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AnnotationLink properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AnnotationLink properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

