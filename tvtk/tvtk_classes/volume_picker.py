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

from tvtk.tvtk_classes.cell_picker import CellPicker


class VolumePicker(CellPicker):
    """
    VolumePicker - ray-cast picker enhanced for volumes
    
    Superclass: CellPicker
    
    VolumePicker is a subclass of CellPicker.  It has one advantage
    over CellPicker for volumes: it will be able to correctly perform
    picking when cropping_planes are present.  This isn't possible for CellPicker since it
    doesn't link to the volume_rendering classes and hence cannot access
    information about the cropping_planes.
    
    See Also:
    
    Picker PointPicker CellPicker
    
    Thanks:
    
    This class was contributed to VTK by David Gobbi on behalf of Atamai
    Inc.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumePicker, obj, update, **traits)
    
    pick_cropping_planes = tvtk_base.false_bool_trait(help=\
        """
        Set whether to pick the cropping planes of props that have them.
        If this is set, then the pick will be done on the cropping planes
        rather than on the data. The get_cropping_plane_id() method will
        return the index of the cropping plane of the volume that was
        picked.  This setting is only relevant to the picking of volumes.
        """
    )
    def _pick_cropping_planes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickCroppingPlanes,
                        self.pick_cropping_planes_)

    def _get_cropping_plane_id(self):
        return self._vtk_obj.GetCroppingPlaneId()
    cropping_plane_id = traits.Property(_get_cropping_plane_id, help=\
        """
        Get the index of the cropping plane that the pick ray passed
        through on its way to the prop. This will be set regardless of
        whether pick_cropping_planes is on.  The crop planes are ordered as
        follows: xmin, xmax, ymin, ymax, zmin, zmax.  If the volume is
        not cropped, the value will bet set to -1.
        """
    )

    _updateable_traits_ = \
    (('use_volume_gradient_opacity', 'GetUseVolumeGradientOpacity'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_cropping_planes', 'GetPickCroppingPlanes'),
    ('pick_texture_data', 'GetPickTextureData'), ('pick_from_list',
    'GetPickFromList'), ('debug', 'GetDebug'), ('volume_opacity_isovalue',
    'GetVolumeOpacityIsovalue'), ('reference_count', 'GetReferenceCount'),
    ('tolerance', 'GetTolerance'), ('pick_clipping_planes',
    'GetPickClippingPlanes'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_clipping_planes',
    'pick_cropping_planes', 'pick_from_list', 'pick_texture_data',
    'use_volume_gradient_opacity', 'tolerance',
    'volume_opacity_isovalue'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumePicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_clipping_planes', 'pick_cropping_planes',
            'pick_from_list', 'pick_texture_data', 'use_volume_gradient_opacity'],
            [], ['tolerance', 'volume_opacity_isovalue']),
            title='Edit VolumePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumePicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

