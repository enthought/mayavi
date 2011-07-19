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

from tvtk.tvtk_classes.data_set_attributes import DataSetAttributes


class PointData(DataSetAttributes):
    """
    PointData - represent and manipulate point attribute data
    
    Superclass: DataSetAttributes
    
    PointData is a class that is used to represent and manipulate
    point attribute data (e.g., scalars, vectors, normals, texture
    coordinates, etc.) Most of the functionality is handled by
    DataSetAttributes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointData, obj, update, **traits)
    
    def null_point(self, *args):
        """
        V.null_point(int)
        C++: void NullPoint(IdType ptId)"""
        ret = self._wrap_call(self._vtk_obj.NullPoint, *args)
        return ret

    _updateable_traits_ = \
    (('copy_tensors', 'GetCopyTensors'), ('copy_vectors',
    'GetCopyVectors'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('copy_normals',
    'GetCopyNormals'), ('copy_global_ids', 'GetCopyGlobalIds'),
    ('copy_t_coords', 'GetCopyTCoords'), ('copy_scalars',
    'GetCopyScalars'), ('number_of_tuples', 'GetNumberOfTuples'),
    ('reference_count', 'GetReferenceCount'), ('copy_pedigree_ids',
    'GetCopyPedigreeIds'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'copy_global_ids',
    'copy_normals', 'copy_pedigree_ids', 'copy_scalars', 'copy_t_coords',
    'copy_tensors', 'copy_vectors', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['copy_global_ids', 'copy_normals',
            'copy_pedigree_ids', 'copy_scalars', 'copy_t_coords', 'copy_tensors',
            'copy_vectors', 'number_of_tuples']),
            title='Edit PointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

