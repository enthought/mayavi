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

from tvtk.tvtk_classes.actor import Actor


class LODActor(Actor):
    """
    LODActor - an actor that supports multiple levels of detail
    
    Superclass: Actor
    
    LODActor is an actor that stores multiple levels of detail (LOD)
    and can automatically switch between them. It selects which level of
    detail to use based on how much time it has been allocated to render.
     Currently a very simple method of total_time/_number_of_actors is used. 
    (In the future this should be modified to dynamically allocate the
    rendering time between different actors based on their needs.)
    
    There are three levels of detail by default. The top level is just
    the normal data.  The lowest level of detail is a simple bounding box
    outline of the actor. The middle level of detail is a point cloud of
    a fixed number of points that have been randomly sampled from the
    mapper's input data.  Point attributes are copied over to the point
    cloud.  These two lower levels of detail are accomplished by creating
    instances of a OutlineFilter (low-res) and MaskPoints
    (medium-res). Additional levels of detail can be add using the
    add_lod_mapper() method.
    
    To control the frame rate, you typically set the
    RenderWindowInteractor desired_update_rate and still_update_rate. This
    then will cause LODActor to adjust its LOD to fulfill the
    requested update rate.
    
    For greater control on levels of detail, see also LODProp3D. That
    class allows arbitrary definition of each LOD.
    
    Caveats:
    
    If you provide your own mappers, you are responsible for setting its
    ivars correctly, such as scalar_range, lookup_table, and so on.
    
    On some systems the point cloud rendering (the default, medium level
    of detail) can result in points so small that they can hardly be
    seen. In this case, use the get_property()->_set_point_size() method to
    increase the rendered size of the points.
    
    See Also:
    
    Actor Renderer LODProp3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLODActor, obj, update, **traits)
    
    number_of_cloud_points = traits.Int(150, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of random points for the point cloud.
        """
    )
    def _number_of_cloud_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCloudPoints,
                        self.number_of_cloud_points)

    def _get_medium_res_filter(self):
        return wrap_vtk(self._vtk_obj.GetMediumResFilter())
    def _set_medium_res_filter(self, arg):
        old_val = self._get_medium_res_filter()
        self._wrap_call(self._vtk_obj.SetMediumResFilter,
                        deref_vtk(arg))
        self.trait_property_changed('medium_res_filter', old_val, arg)
    medium_res_filter = traits.Property(_get_medium_res_filter, _set_medium_res_filter, help=\
        """
        You may plug in your own filters to decimate/subsample the input.
        The default is to use a OutlineFilter (low-res) and
        MaskPoints (medium-res).
        """
    )

    def _get_low_res_filter(self):
        return wrap_vtk(self._vtk_obj.GetLowResFilter())
    def _set_low_res_filter(self, arg):
        old_val = self._get_low_res_filter()
        self._wrap_call(self._vtk_obj.SetLowResFilter,
                        deref_vtk(arg))
        self.trait_property_changed('low_res_filter', old_val, arg)
    low_res_filter = traits.Property(_get_low_res_filter, _set_low_res_filter, help=\
        """
        You may plug in your own filters to decimate/subsample the input.
        The default is to use a OutlineFilter (low-res) and
        MaskPoints (medium-res).
        """
    )

    def _get_lod_mappers(self):
        return wrap_vtk(self._vtk_obj.GetLODMappers())
    lod_mappers = traits.Property(_get_lod_mappers, help=\
        """
        All the mappers for different LODs are stored here. The order is
        not important.
        """
    )

    def add_lod_mapper(self, *args):
        """
        V.add_lod_mapper(Mapper)
        C++: void AddLODMapper(Mapper *mapper)
        Add another level of detail.  They do not have to be in any order
        of complexity.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLODMapper, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale', 'GetScale'),
    ('number_of_cloud_points', 'GetNumberOfCloudPoints'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('reference_count', 'GetReferenceCount'),
    ('position', 'GetPosition'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('orientation', 'GetOrientation'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'number_of_cloud_points', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LODActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time',
            'number_of_cloud_points', 'orientation', 'origin', 'position',
            'render_time_multiplier', 'scale']),
            title='Edit LODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

