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

from tvtk.tvtk_classes.picker import Picker


class CellPicker(Picker):
    """
    CellPicker - ray-cast cell picker for all kinds of prop3ds
    
    Superclass: Picker
    
    CellPicker will shoot a ray into a 3d scene and return information
    about the first object that the ray hits.  It works for all prop3ds.
    For Volume objects, it shoots a ray into the volume and returns
    the point where the ray intersects an isosurface of a chosen opacity.
    For ImageActor objects, it intersects the ray with the displayed
    slice. For Actor objects, it intersects the actor's polygons. If
    the object's mapper has clipping_planes, then it takes the clipping
    into account, and will return the Id of the clipping plane that was
    intersected. For all prop types, it returns point and cell
    information, plus the normal of the surface that was intersected at
    the pick position.  For volumes and images, it also returns (i,j,k)
    coordinates for the point and the cell that were picked.
    
    See Also:
    
    Picker PointPicker VolumePicker
    
    Thanks:
    
    This class was contributed to VTK by David Gobbi on behalf of Atamai
    Inc., as an enhancement to the original CellPicker.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellPicker, obj, update, **traits)
    
    pick_clipping_planes = tvtk_base.false_bool_trait(help=\
        """
        The pick_clipping_planes setting controls how clipping planes are
        handled by the pick.  If it is On, then the clipping planes
        become pickable objects, even though they are usually invisible. 
        This means that if the pick ray intersects a clipping plane
        before it hits anything else, the pick will stop at that clipping
        plane. The get_prop3d() and get_mapper() methods will return the
        prop3d and Mapper that the clipping plane belongs to.  The
        get_clipping_plane_id() method will return the index of the clipping
        plane so that you can retrieve it from the mapper, or -1 if no
        clipping plane was picked. The picking of ImageActors is not
        influenced by this setting, since they have no clipping planes.
        """
    )
    def _pick_clipping_planes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickClippingPlanes,
                        self.pick_clipping_planes_)

    use_volume_gradient_opacity = tvtk_base.false_bool_trait(help=\
        """
        Use the product of the scalar and gradient opacity functions when
        computing the opacity isovalue, instead of just using the scalar
        opacity. This parameter is only relevant to volume picking and is
        off by default.
        """
    )
    def _use_volume_gradient_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseVolumeGradientOpacity,
                        self.use_volume_gradient_opacity_)

    pick_texture_data = tvtk_base.false_bool_trait(help=\
        """
        If this is "On" and if the picked prop has a texture, then the
        data returned by get_data_set() will be the texture's data instead
        of the mapper's data.  The get_point_id(), get_cell_id(),
        get_p_coords() etc. will all return information for use with the
        texture's data.  If the picked prop does not have any texture,
        then get_data_set() will return the mapper's data instead and
        get_point_id() etc. will return information related to the mapper's
        data.  The default value of pick_texture_data is "Off".
        """
    )
    def _pick_texture_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickTextureData,
                        self.pick_texture_data_)

    volume_opacity_isovalue = traits.Float(0.05, enter_set=True, auto_set=False, help=\
        """
        Set the opacity isovalue to use for defining volume surfaces. 
        The pick will occur at the location along the pick ray where the
        opacity of the volume is equal to this isovalue.  If you want to
        do the pick based on an actual data isovalue rather than the
        opacity, then pass the data value through the scalar opacity
        function before using this method.
        """
    )
    def _volume_opacity_isovalue_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVolumeOpacityIsovalue,
                        self.volume_opacity_isovalue)

    def _get_cell_ijk(self):
        return self._vtk_obj.GetCellIJK()
    cell_ijk = traits.Property(_get_cell_ijk, help=\
        """
        
        """
    )

    def _get_cell_id(self):
        return self._vtk_obj.GetCellId()
    cell_id = traits.Property(_get_cell_id, help=\
        """
        Get the id of the picked cell. If cell_id = -1, nothing was
        picked.
        """
    )

    def _get_clipping_plane_id(self):
        return self._vtk_obj.GetClippingPlaneId()
    clipping_plane_id = traits.Property(_get_clipping_plane_id, help=\
        """
        Get the index of the clipping plane that was intersected during
        the pick.  This will be set regardless of whether
        pick_clipping_planes is On, all that is required is that the pick
        intersected a clipping plane of the prop3d that was picked.  The
        result will be -1 if the prop3d that was picked has no clipping
        planes, or if the ray didn't intersect the planes.
        """
    )

    def _get_mapper_normal(self):
        return self._vtk_obj.GetMapperNormal()
    mapper_normal = traits.Property(_get_mapper_normal, help=\
        """
        
        """
    )

    def _get_p_coords(self):
        return self._vtk_obj.GetPCoords()
    p_coords = traits.Property(_get_p_coords, help=\
        """
        
        """
    )

    def _get_pick_normal(self):
        return self._vtk_obj.GetPickNormal()
    pick_normal = traits.Property(_get_pick_normal, help=\
        """
        Return the normal of the picked surface at the pick_position.  If
        no surface was picked, then a vector pointing back at the camera
        is returned.
        """
    )

    def _get_point_ijk(self):
        return self._vtk_obj.GetPointIJK()
    point_ijk = traits.Property(_get_point_ijk, help=\
        """
        
        """
    )

    def _get_point_id(self):
        return self._vtk_obj.GetPointId()
    point_id = traits.Property(_get_point_id, help=\
        """
        Get the id of the picked point. If point_id = -1, nothing was
        picked. This point will be a member of any cell that is picked.
        """
    )

    def _get_sub_id(self):
        return self._vtk_obj.GetSubId()
    sub_id = traits.Property(_get_sub_id, help=\
        """
        Get the sub_id of the picked cell. This is useful, for example, if
        the data is made of triangle strips. If sub_id = -1, nothing was
        picked.
        """
    )

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    texture = traits.Property(_get_texture, help=\
        """
        Get the texture that was picked.  This will always be set if the
        picked prop has a texture, and will always be null otherwise.
        """
    )

    def add_locator(self, *args):
        """
        V.add_locator(AbstractCellLocator)
        C++: void AddLocator(AbstractCellLocator *locator)
        Add a locator for one of the data sets that will be included in
        the scene.  You must set up the locator with exactly the same
        data set that was input to the mapper of one or more of the
        actors in the scene.  As well, you must either build the locator
        before doing the pick, or you must turn on lazy_evaluation in the
        locator to make it build itself on the first pick.  Note that if
        you try to add the same locator to the picker twice, the second
        addition will be ignored.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLocator, *my_args)
        return ret

    def remove_all_locators(self):
        """
        V.remove_all_locators()
        C++: void RemoveAllLocators()
        Remove all locators associated with this picker.
        """
        ret = self._vtk_obj.RemoveAllLocators()
        return ret
        

    def remove_locator(self, *args):
        """
        V.remove_locator(AbstractCellLocator)
        C++: void RemoveLocator(AbstractCellLocator *locator)
        Remove a locator that was previously added.  If you try to remove
        a nonexistent locator, then nothing will happen and no errors
        will be raised.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveLocator, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_volume_gradient_opacity', 'GetUseVolumeGradientOpacity'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_texture_data', 'GetPickTextureData'), ('pick_from_list',
    'GetPickFromList'), ('debug', 'GetDebug'), ('volume_opacity_isovalue',
    'GetVolumeOpacityIsovalue'), ('reference_count', 'GetReferenceCount'),
    ('tolerance', 'GetTolerance'), ('pick_clipping_planes',
    'GetPickClippingPlanes'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_clipping_planes',
    'pick_from_list', 'pick_texture_data', 'use_volume_gradient_opacity',
    'tolerance', 'volume_opacity_isovalue'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_clipping_planes', 'pick_from_list',
            'pick_texture_data', 'use_volume_gradient_opacity'], [], ['tolerance',
            'volume_opacity_isovalue']),
            title='Edit CellPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

