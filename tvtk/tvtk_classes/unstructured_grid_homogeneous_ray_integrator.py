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

from tvtk.tvtk_classes.unstructured_grid_volume_ray_integrator import UnstructuredGridVolumeRayIntegrator


class UnstructuredGridHomogeneousRayIntegrator(UnstructuredGridVolumeRayIntegrator):
    """
    UnstructuredGridHomogeneousRayIntegrator - performs peicewise
    constant ray integration.
    
    Superclass: UnstructuredGridVolumeRayIntegrator
    
    UnstructuredGridHomogeneousRayIntegrator performs homogeneous ray
    integration.  This is a good method to use when volume rendering
    scalars that are defined on cells.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridHomogeneousRayIntegrator, obj, update, **traits)
    
    transfer_function_table_size = traits.Int(1024, enter_set=True, auto_set=False, help=\
        """
        For quick lookup, the transfer function is sampled into a table.
        This parameter sets how big of a table to use.  By default, 1024
        entries are used.
        """
    )
    def _transfer_function_table_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransferFunctionTableSize,
                        self.transfer_function_table_size)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('transfer_function_table_size', 'GetTransferFunctionTableSize'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'transfer_function_table_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridHomogeneousRayIntegrator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridHomogeneousRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['transfer_function_table_size']),
            title='Edit UnstructuredGridHomogeneousRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridHomogeneousRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

