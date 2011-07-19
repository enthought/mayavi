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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class DataObjectGenerator(DataObjectAlgorithm):
    """
    DataObjectGenerator - produces simple (composite or atomic) data 
    
    Superclass: DataObjectAlgorithm
    
    DataObjectGenerator parses a string and produces dataobjects from
    the dataobject template names it sees in the string. For example, if
    the string contains "ID1" the generator will create a ImageData.
    "UF1", "RG1", "SG1", "PD1", and "UG1" will produce UniformGrid,
    RectilinearGrid, StructuredGrid, PolyData and
    UnstructuredGrid respectively. "PD2" will produce an alternate
    PolyData. You can compose composite datasets from the atomic ones
    listed above by placing them within one of the two composite dataset
    identifiers
    - "MB{}" or "HB[]". "MB{ ID1 PD1 MB{} }" for example will create a
      MultiBlockDataSet consisting of three blocks: image data, poly
      data, multi-block (empty). Hierarchical Box data sets additionally
      require the notion of groups, declared within "()" braces, to
      specify AMR depth. "HB[ (UF1)(UF1)(UF1) ]" will create a
      HierarchicalBoxDataSet representing an octree that is three
      levels deep, in which the firstmost cell in each level is refined.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectGenerator, obj, update, **traits)
    
    program = traits.String(r"ID1", enter_set=True, auto_set=False, help=\
        """
        The string that will be parsed to specify a dataobject structure.
        """
    )
    def _program_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgram,
                        self.program)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('program', 'GetProgram'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'program', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectGenerator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['program']),
            title='Edit DataObjectGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

