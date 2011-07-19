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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class DIMACSGraphReader(GraphAlgorithm):
    """
    DIMACSGraphReader - reads Graph data from a DIMACS
    
    Superclass: GraphAlgorithm
    
    DIMACSGraphReader is a source object that reads Graph data
    files from a DIMACS format. DIMACS graphs are undirected. See webpage
    for format details.
     http://dimacs.rutgers.edu/Challenges/
     http://www.dis.uniroma1.it/~challenge9/format.shtml
    
    See Also:
    
    DIMACSGraphWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDIMACSGraphReader, obj, update, **traits)
    
    vertex_attribute_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Vertex attribute array name
        """
    )
    def _vertex_attribute_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexAttributeArrayName,
                        self.vertex_attribute_array_name)

    edge_attribute_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Edge attribute array name
        """
    )
    def _edge_attribute_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeAttributeArrayName,
                        self.edge_attribute_array_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        The DIMACS file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('file_name',
    'GetFileName'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('vertex_attribute_array_name', 'GetVertexAttributeArrayName'),
    ('edge_attribute_array_name', 'GetEdgeAttributeArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'edge_attribute_array_name', 'file_name',
    'progress_text', 'vertex_attribute_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DIMACSGraphReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['edge_attribute_array_name', 'file_name',
            'vertex_attribute_array_name']),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

