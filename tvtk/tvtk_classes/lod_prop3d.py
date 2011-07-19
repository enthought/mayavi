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

from tvtk.tvtk_classes.prop3d import Prop3D


class LODProp3D(Prop3D):
    """
    LODProp3D - level of detail 3d prop
    
    Superclass: Prop3D
    
    LODProp3D is a class to support level of detail rendering for
    prop3d. Any number of mapper/property/texture items can be added to
    this object. Render time will be measured, and will be used to select
    a LOD based on the allocated_render_time of this prop3d. Depending on
    the type of the mapper/property, a Actor or a Volume will be
    created behind the scenes.
    
    See Also:
    
    Prop3D Actor Volume LODActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLODProp3D, obj, update, **traits)
    
    automatic_lod_selection = tvtk_base.true_bool_trait(help=\
        """
        Turn on / off automatic selection of LOD. This is on by default.
        If it is off, then the selected_lodid is rendered regardless of
        rendering time or desired update rate.
        """
    )
    def _automatic_lod_selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticLODSelection,
                        self.automatic_lod_selection_)

    automatic_pick_lod_selection = tvtk_base.true_bool_trait(help=\
        """
        Turn on / off automatic selection of picking LOD. This is on by
        default. If it is off, then the selected_lodid is rendered
        regardless of rendering time or desired update rate.
        """
    )
    def _automatic_pick_lod_selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticPickLODSelection,
                        self.automatic_pick_lod_selection_)

    selected_pick_lodid = traits.Int(1000, enter_set=True, auto_set=False, help=\
        """
        Set the id of the LOD that is to be used for picking when 
        automatic LOD pick selection is turned off.
        """
    )
    def _selected_pick_lodid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedPickLODID,
                        self.selected_pick_lodid)

    def get_lod_mapper(self, *args):
        """
        V.get_lod_mapper(int) -> AbstractMapper3D
        C++: AbstractMapper3D *GetLODMapper(int id)
        Get the LODMapper as an AbstractMapper3D.  It is the user's
        respondibility to safe down cast this to a Mapper or
        VolumeMapper as appropriate.
        """
        ret = self._wrap_call(self._vtk_obj.GetLODMapper, *args)
        return wrap_vtk(ret)

    def set_lod_mapper(self, *args):
        """
        V.set_lod_mapper(int, Mapper)
        C++: void SetLODMapper(int id, Mapper *m)
        V.set_lod_mapper(int, AbstractVolumeMapper)
        C++: void SetLODMapper(int id, AbstractVolumeMapper *m)
        Methods to set / get the mapper of an LOD. Since the LOD could be
        a volume or an actor, you have to pass in the pointer to the
        mapper to get it. The returned mapper will be NULL if the id is
        not valid, or the mapper is of the wrong type for the
        corresponding prop3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLODMapper, *my_args)
        return ret

    def get_lod_level(self, *args):
        """
        V.get_lod_level(int) -> float
        C++: double GetLODLevel(int id)
        Set the level of a particular LOD. When a LOD is selected for
        rendering because it has the largest render time that fits within
        the allocated time, all LOD are then checked to see if any one
        can render faster but has a lower (more resolution/better) level.
        This quantity is a double to ensure that a level can be inserted
        between 2 and 3.
        """
        ret = self._wrap_call(self._vtk_obj.GetLODLevel, *args)
        return ret

    def set_lod_level(self, *args):
        """
        V.set_lod_level(int, float)
        C++: void SetLODLevel(int id, double level)
        Set the level of a particular LOD. When a LOD is selected for
        rendering because it has the largest render time that fits within
        the allocated time, all LOD are then checked to see if any one
        can render faster but has a lower (more resolution/better) level.
        This quantity is a double to ensure that a level can be inserted
        between 2 and 3.
        """
        ret = self._wrap_call(self._vtk_obj.SetLODLevel, *args)
        return ret

    selected_lodid = traits.Int(1000, enter_set=True, auto_set=False, help=\
        """
        Set the id of the LOD that is to be drawn when automatic LOD
        selection is turned off.
        """
    )
    def _selected_lodid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedLODID,
                        self.selected_lodid)

    def _get_automatic_lod_selection_max_value(self):
        return self._vtk_obj.GetAutomaticLODSelectionMaxValue()
    automatic_lod_selection_max_value = traits.Property(_get_automatic_lod_selection_max_value, help=\
        """
        Turn on / off automatic selection of LOD. This is on by default.
        If it is off, then the selected_lodid is rendered regardless of
        rendering time or desired update rate.
        """
    )

    def _get_automatic_lod_selection_min_value(self):
        return self._vtk_obj.GetAutomaticLODSelectionMinValue()
    automatic_lod_selection_min_value = traits.Property(_get_automatic_lod_selection_min_value, help=\
        """
        Turn on / off automatic selection of LOD. This is on by default.
        If it is off, then the selected_lodid is rendered regardless of
        rendering time or desired update rate.
        """
    )

    def _get_automatic_pick_lod_selection_max_value(self):
        return self._vtk_obj.GetAutomaticPickLODSelectionMaxValue()
    automatic_pick_lod_selection_max_value = traits.Property(_get_automatic_pick_lod_selection_max_value, help=\
        """
        Turn on / off automatic selection of picking LOD. This is on by
        default. If it is off, then the selected_lodid is rendered
        regardless of rendering time or desired update rate.
        """
    )

    def _get_automatic_pick_lod_selection_min_value(self):
        return self._vtk_obj.GetAutomaticPickLODSelectionMinValue()
    automatic_pick_lod_selection_min_value = traits.Property(_get_automatic_pick_lod_selection_min_value, help=\
        """
        Turn on / off automatic selection of picking LOD. This is on by
        default. If it is off, then the selected_lodid is rendered
        regardless of rendering time or desired update rate.
        """
    )

    def _get_current_index(self):
        return self._vtk_obj.GetCurrentIndex()
    current_index = traits.Property(_get_current_index, help=\
        """
        Get the current index, used to determine the ID of the next LOD
        that is added.  Useful for guessing what IDs have been used (with
        number_of_lo_ds, without depending on the constructor initialization
        to 1000.
        """
    )

    def get_lod_estimated_render_time(self, *args):
        """
        V.get_lod_estimated_render_time(int) -> float
        C++: double GetLODEstimatedRenderTime(int id)
        Access method that can be used to find out the estimated render
        time (the thing used to select an LOD) for a given LOD ID or
        index. Value is returned in seconds.
        """
        ret = self._wrap_call(self._vtk_obj.GetLODEstimatedRenderTime, *args)
        return ret

    def get_lod_index_estimated_render_time(self, *args):
        """
        V.get_lod_index_estimated_render_time(int) -> float
        C++: double GetLODIndexEstimatedRenderTime(int index)
        Access method that can be used to find out the estimated render
        time (the thing used to select an LOD) for a given LOD ID or
        index. Value is returned in seconds.
        """
        ret = self._wrap_call(self._vtk_obj.GetLODIndexEstimatedRenderTime, *args)
        return ret

    def get_lod_index_level(self, *args):
        """
        V.get_lod_index_level(int) -> float
        C++: double GetLODIndexLevel(int index)
        Set the level of a particular LOD. When a LOD is selected for
        rendering because it has the largest render time that fits within
        the allocated time, all LOD are then checked to see if any one
        can render faster but has a lower (more resolution/better) level.
        This quantity is a double to ensure that a level can be inserted
        between 2 and 3.
        """
        ret = self._wrap_call(self._vtk_obj.GetLODIndexLevel, *args)
        return ret

    def _get_last_rendered_lodid(self):
        return self._vtk_obj.GetLastRenderedLODID()
    last_rendered_lodid = traits.Property(_get_last_rendered_lodid, help=\
        """
        Get the ID of the previously (during the last render) selected
        LOD index
        """
    )

    def _get_number_of_lo_ds(self):
        return self._vtk_obj.GetNumberOfLODs()
    number_of_lo_ds = traits.Property(_get_number_of_lo_ds, help=\
        """
        Get the current number of LODs.
        """
    )

    def _get_pick_lodid(self):
        return self._vtk_obj.GetPickLODID()
    pick_lodid = traits.Property(_get_pick_lodid, help=\
        """
        Get the ID of the appropriate pick LOD index
        """
    )

    def add_lod(self, *args):
        """
        V.add_lod(Mapper, Property, Property, Texture, float)
            -> int
        C++: int AddLOD(Mapper *m, Property *p, Property *back,
            Texture *t, double time)
        V.add_lod(Mapper, Property, Texture, float) -> int
        C++: int AddLOD(Mapper *m, Property *p, Texture *t,
            double time)
        V.add_lod(Mapper, Property, Property, float) -> int
        C++: int AddLOD(Mapper *m, Property *p, Property *back,
            double time)
        V.add_lod(Mapper, Property, float) -> int
        C++: int AddLOD(Mapper *m, Property *p, double time)
        V.add_lod(Mapper, Texture, float) -> int
        C++: int AddLOD(Mapper *m, Texture *t, double time)
        V.add_lod(Mapper, float) -> int
        C++: int AddLOD(Mapper *m, double time)
        V.add_lod(AbstractVolumeMapper, VolumeProperty, float) -> int
        C++: int AddLOD(AbstractVolumeMapper *m, VolumeProperty *p,
            double time)
        V.add_lod(AbstractVolumeMapper, float) -> int
        C++: int AddLOD(AbstractVolumeMapper *m, double time)
        Add a level of detail with a given mapper, property, backface
        property, texture, and guess of rendering time.  The property and
        texture fields can be set to NULL (the other methods are included
        for script access where null variables are not allowed). The time
        field can be set to 0.0 indicating that no initial guess for
        rendering time is being supplied. The returned integer value is
        an ID that can be used later to delete this LOD, or set it as the
        selected LOD.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLOD, *my_args)
        return ret

    def disable_lod(self, *args):
        """
        V.disable_lod(int)
        C++: void DisableLOD(int id)
        Enable / disable a particular LOD. If it is disabled, it will not
        be used during automatic selection, but can be selected as the
        LOD if automatic LOD selection is off.
        """
        ret = self._wrap_call(self._vtk_obj.DisableLOD, *args)
        return ret

    def enable_lod(self, *args):
        """
        V.enable_lod(int)
        C++: void EnableLOD(int id)
        Enable / disable a particular LOD. If it is disabled, it will not
        be used during automatic selection, but can be selected as the
        LOD if automatic LOD selection is off.
        """
        ret = self._wrap_call(self._vtk_obj.EnableLOD, *args)
        return ret

    def is_lod_enabled(self, *args):
        """
        V.is_lod_enabled(int) -> int
        C++: int IsLODEnabled(int id)
        Enable / disable a particular LOD. If it is disabled, it will not
        be used during automatic selection, but can be selected as the
        LOD if automatic LOD selection is off.
        """
        ret = self._wrap_call(self._vtk_obj.IsLODEnabled, *args)
        return ret

    def remove_lod(self, *args):
        """
        V.remove_lod(int)
        C++: void RemoveLOD(int id)
        Delete a level of detail given an ID. This is the ID returned by
        the add_lod method
        """
        ret = self._wrap_call(self._vtk_obj.RemoveLOD, *args)
        return ret

    def set_lod_backface_property(self, *args):
        """
        V.set_lod_backface_property(int, Property)
        C++: void SetLODBackfaceProperty(int id, Property *t)
        Methods to set / get the backface property of an LOD. This method
        is only valid for LOD ids that are Actors (not Volumes)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLODBackfaceProperty, *my_args)
        return ret

    def set_lod_property(self, *args):
        """
        V.set_lod_property(int, Property)
        C++: void SetLODProperty(int id, Property *p)
        V.set_lod_property(int, VolumeProperty)
        C++: void SetLODProperty(int id, VolumeProperty *p)
        Methods to set / get the property of an LOD. Since the LOD could
        be a volume or an actor, you have to pass in the pointer to the
        property to get it. The returned property will be NULL if the id
        is not valid, or the property is of the wrong type for the
        corresponding prop3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLODProperty, *my_args)
        return ret

    def set_lod_texture(self, *args):
        """
        V.set_lod_texture(int, Texture)
        C++: void SetLODTexture(int id, Texture *t)
        Methods to set / get the texture of an LOD. This method is only
        valid for LOD ids that are Actors (not Volumes)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLODTexture, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'), ('orientation',
    'GetOrientation'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('automatic_pick_lod_selection',
    'GetAutomaticPickLODSelection'), ('selected_pick_lodid',
    'GetSelectedPickLODID'), ('dragable', 'GetDragable'),
    ('automatic_lod_selection', 'GetAutomaticLODSelection'),
    ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('selected_lodid', 'GetSelectedLODID'),
    ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('position',
    'GetPosition'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['automatic_lod_selection', 'automatic_pick_lod_selection', 'debug',
    'dragable', 'global_warning_display', 'pickable', 'use_bounds',
    'visibility', 'allocated_render_time', 'estimated_render_time',
    'orientation', 'origin', 'position', 'render_time_multiplier',
    'scale', 'selected_lodid', 'selected_pick_lodid'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LODProp3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LODProp3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_lod_selection',
            'automatic_pick_lod_selection', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale',
            'selected_lodid', 'selected_pick_lodid']),
            title='Edit LODProp3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LODProp3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

