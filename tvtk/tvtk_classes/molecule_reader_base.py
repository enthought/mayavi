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


class MoleculeReaderBase(PolyDataAlgorithm):
    """
    MoleculeReaderBase - read Molecular Data files
    
    Superclass: PolyDataAlgorithm
    
    MoleculeReaderBase is a source object that reads Molecule files
    The file_name must be specified
    
    Thanks:
    
    Dr. Jean M. Favre who developed and contributed this class
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMoleculeReaderBase, obj, update, **traits)
    
    b_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _b_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBScale,
                        self.b_scale)

    hb_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _hb_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHBScale,
                        self.hb_scale)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_number_of_atoms(self):
        return self._vtk_obj.GetNumberOfAtoms()
    number_of_atoms = traits.Property(_get_number_of_atoms, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('hb_scale', 'GetHBScale'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('b_scale',
    'GetBScale'), ('file_name', 'GetFileName'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'b_scale', 'file_name', 'hb_scale',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MoleculeReaderBase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MoleculeReaderBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['b_scale', 'file_name', 'hb_scale']),
            title='Edit MoleculeReaderBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MoleculeReaderBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

