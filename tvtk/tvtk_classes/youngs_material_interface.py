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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class YoungsMaterialInterface(MultiBlockDataSetAlgorithm):
    """
    YoungsMaterialInterface - reconstructs material interfaces
    
    Superclass: MultiBlockDataSetAlgorithm
    
    Reconstructs material interfaces from a mesh containing mixed cells
    (where several materials are mixed) this implementation is based on
    the youngs algorithm, generalized to arbitrary cell types and works
    on both 2d and 3d meshes. the main advantage of the youngs algorithm
    is it guarantees the material volume correctness. for 2d meshes, the
    axis_symetric flag allows to switch between a pure 2d (plannar)
    algorithm and an axis symetric 2d algorithm handling volumes of
    revolution.
    
    Thanks:
    
    This file is part of the generalized Youngs material interface
    reconstruction algorithm contributed by
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Implementation by Thierry Carrard (thierry.carrard@cea.fr)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkYoungsMaterialInterface, obj, update, **traits)
    
    use_fraction_as_distance = tvtk_base.false_bool_trait(help=\
        """
        when use_fraction_as_distance is true, the volume fraction is
        interpreted as the distance of the cutting plane from the origin.
        in axis symetric mode, 2d meshes are understood as volumes of
        revolution.
        """
    )
    def _use_fraction_as_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFractionAsDistance,
                        self.use_fraction_as_distance_)

    onion_peel = tvtk_base.false_bool_trait(help=\
        """
        Set/Get onion_peel flag. if this flag is on, the normal vector of
        the first material (which depends on material ordering) is used
        for all materials.
        """
    )
    def _onion_peel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnionPeel,
                        self.onion_peel_)

    fill_material = tvtk_base.false_bool_trait(help=\
        """
        When fill_material is set to 1, the volume containing material is
        output and not only the interface surface.
        """
    )
    def _fill_material_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillMaterial,
                        self.fill_material_)

    inverse_normal = tvtk_base.false_bool_trait(help=\
        """
        Set/Get wether the normal vector has to be flipped.
        """
    )
    def _inverse_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseNormal,
                        self.inverse_normal_)

    two_materials_optimization = tvtk_base.false_bool_trait(help=\
        """
        Triggers some additional optimizations for cells containing only
        two materials. This option might produce different result than
        expected if the sum of volume fractions is not 1.
        """
    )
    def _two_materials_optimization_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoMaterialsOptimization,
                        self.two_materials_optimization_)

    reverse_material_order = tvtk_base.false_bool_trait(help=\
        """
        If this flag is on, material order in reversed. Otherwise,
        materials are sorted in ascending order depending on the given
        ordering array.
        """
    )
    def _reverse_material_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseMaterialOrder,
                        self.reverse_material_order_)

    axis_symetric = tvtk_base.false_bool_trait(help=\
        """
        Turns on/off axis_symetric computation of 2d interfaces. in axis
        symetric mode, 2d meshes are understood as volumes of revolution.
        """
    )
    def _axis_symetric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisSymetric,
                        self.axis_symetric_)

    volume_fraction_range = traits.Array(shape=(2,), value=(0.01, 0.98999999999999999), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _volume_fraction_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVolumeFractionRange,
                        self.volume_fraction_range)

    number_of_materials = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets/Gets the number of materials.
        """
    )
    def _number_of_materials_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfMaterials,
                        self.number_of_materials)

    def remove_all_materials(self):
        """
        V.remove_all_materials()
        C++: virtual void RemoveAllMaterials()
        Removes all meterials previously added.
        """
        ret = self._vtk_obj.RemoveAllMaterials()
        return ret
        

    def set_material_arrays(self, *args):
        """
        V.set_material_arrays(int, string, string, string)
        C++: virtual void SetMaterialArrays(int i,
            const char *volumeFraction, const char *interfaceNormal,
            const char *materialOrdering)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialArrays, *args)
        return ret

    def set_material_normal_array(self, *args):
        """
        V.set_material_normal_array(int, string)
        C++: virtual void SetMaterialNormalArray(int i,
            const char *normal)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialNormalArray, *args)
        return ret

    def set_material_ordering_array(self, *args):
        """
        V.set_material_ordering_array(int, string)
        C++: virtual void SetMaterialOrderingArray(int i,
            const char *ordering)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialOrderingArray, *args)
        return ret

    def set_material_volume_fraction_array(self, *args):
        """
        V.set_material_volume_fraction_array(int, string)
        C++: virtual void SetMaterialVolumeFractionArray(int i,
            const char *volume)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialVolumeFractionArray, *args)
        return ret

    _updateable_traits_ = \
    (('number_of_materials', 'GetNumberOfMaterials'), ('inverse_normal',
    'GetInverseNormal'), ('debug', 'GetDebug'), ('reverse_material_order',
    'GetReverseMaterialOrder'), ('two_materials_optimization',
    'GetTwoMaterialsOptimization'), ('volume_fraction_range',
    'GetVolumeFractionRange'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_fraction_as_distance',
    'GetUseFractionAsDistance'), ('axis_symetric', 'GetAxisSymetric'),
    ('progress_text', 'GetProgressText'), ('onion_peel', 'GetOnionPeel'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('fill_material', 'GetFillMaterial'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'axis_symetric', 'debug', 'fill_material',
    'global_warning_display', 'inverse_normal', 'onion_peel',
    'release_data_flag', 'reverse_material_order',
    'two_materials_optimization', 'use_fraction_as_distance',
    'number_of_materials', 'progress_text', 'volume_fraction_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(YoungsMaterialInterface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['axis_symetric', 'fill_material', 'inverse_normal',
            'onion_peel', 'reverse_material_order', 'two_materials_optimization',
            'use_fraction_as_distance'], [], ['number_of_materials',
            'volume_fraction_range']),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

