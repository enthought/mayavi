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


class QuadricLODActor(Actor):
    """
    QuadricLODActor - a specific level-of-detail strategy using the 
    
    Superclass: Actor
    
    QuadricLODActor implements a specific strategy for level-of-detail
    using the QuadricClustering decimation algorithm. It supports only
    two levels of detail: full resolution and a decimated version. The
    decimated LOD is generated using a tuned strategy to produce output
    consistent with the requested interactive frame rate (i.e., the
    RenderWindowInteractor's desired_update_rate). It also makes use of
    display lists for performance, and adjusts the QuadricClustering
    algorithm to take into account the dimensionality of the data (e.g.,
    2d, x-y surfaces may be binned into n x n x 1 to reduce extra
    polygons in the z-direction). Finally, the filter may optionally be
    set in "Static" mode (this works with the Mapper::SetStatic()
    method). `Enabling Static results in a one time execution of the
    Mapper's pipeline. After that, the pipeline no longer updated (unless
    manually forced to do so).
    
    Caveats:
    
    By default the algorithm is set up to pre-compute the LODs. That is,
    on the first render (whether a full resolution render or interactive
    render) the LOD is computed. This behavior can be changed so that the
    LOD construction is deferred until the first interactive render.
    Either way, when the LOD is constructed, the user may notice a short
    pause.
    
    This class can be used as a direct replacement for Actor. It may
    also be used as a replacement for Follower's (the ability to track
    a camera is provided).
    
    See Also:
    
    LODActor QuadricClustering
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadricLODActor, obj, update, **traits)
    
    defer_lod_construction = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to build the LOD immediately (i.e., on the first
        render) or to wait until the LOD is requested in a subsequent
        render. By default, LOD construction is not deferred
        (_defer_lod_construction is false).
        """
    )
    def _defer_lod_construction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeferLODConstruction,
                        self.defer_lod_construction_)

    static = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off a flag to control whether the underlying pipeline is
        static. If static, this means that the data pipeline executes
        once and then not again until the user manually modifies this
        class. By default, Static is off because trying to debug this is
        tricky, and you should only use it when you know what you are
        doing.
        """
    )
    def _static_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStatic,
                        self.static_)

    prop_type = traits.Trait('actor',
    tvtk_base.TraitRevPrefixMap({'follower': 0, 'actor': 1}), help=\
        """
        Indicate that this actor is actually a follower. By default, the
        prop type is a Actor.
        """
    )
    def _prop_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPropType,
                        self.prop_type_)

    data_configuration = traits.Trait('unknown',
    tvtk_base.TraitRevPrefixMap({'xyz_volume': 7, 'unknown': 0, 'x_line': 1, 'y_line': 2, 'z_line': 3, 'xz_plane': 5, 'xy_plane': 4, 'yz_plane': 6}), help=\
        """
        Force the binning of the quadric clustering according to
        application knowledge relative to the dimension of the data. For
        example, if you know your data lies in a 2d x-y plane, the
        performance of the quadric clustering algorithm can be greatly
        improved by indicating this (i.e., the number of resulting
        triangles, and the quality of the decimation version is better).
        Setting this parameter forces the binning to be configured
        consistent with the dimnesionality of the data, and the collapse
        dimension ratio is ignored. Specifying the value of
        data_configuration to UNKNOWN (the default value) means that the
        class will attempt to figure the dimension of the class
        automatically using the collapse_dimension_ratio ivar.
        """
    )
    def _data_configuration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataConfiguration,
                        self.data_configuration_)

    maximum_display_list_size = traits.Trait(25000, traits.Range(1000, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum display list size. This variable is used to
        determine whether to use display lists
        (_immediate_mode_rendering_off) or not. Controlling display list size
        is important to prevent program crashes (i.e., overly large
        display lists on some graphics hardware will cause faults). The
        display list size is the length of the CellArray representing
        the topology of the input PolyData.
        """
    )
    def _maximum_display_list_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDisplayListSize,
                        self.maximum_display_list_size)

    def _get_lod_filter(self):
        return wrap_vtk(self._vtk_obj.GetLODFilter())
    def _set_lod_filter(self, arg):
        old_val = self._get_lod_filter()
        self._wrap_call(self._vtk_obj.SetLODFilter,
                        deref_vtk(arg))
        self.trait_property_changed('lod_filter', old_val, arg)
    lod_filter = traits.Property(_get_lod_filter, _set_lod_filter, help=\
        """
        This class will create a QuadricClustering algorithm
        automatically. However, if you would like to specify the filter
        to use, or to access it and configure it, these method provide
        access to the filter.
        """
    )

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera to follow. This method is only applicable when
        the prop type is set to a Follower.
        """
    )

    collapse_dimension_ratio = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        If the data configuration is set to UNKNOWN, this class attempts
        to figure out the dimensionality of the data using
        collapse_dimension_ratio. This ivar is the ratio of short edge of
        the input bounding box to its long edge, which is then used to
        collapse the data dimension (and set the quadric bin size in that
        direction to one). By default, this value is 0.05.
        """
    )
    def _collapse_dimension_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCollapseDimensionRatio,
                        self.collapse_dimension_ratio)

    _updateable_traits_ = \
    (('collapse_dimension_ratio', 'GetCollapseDimensionRatio'),
    ('maximum_display_list_size', 'GetMaximumDisplayListSize'), ('scale',
    'GetScale'), ('orientation', 'GetOrientation'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('data_configuration', 'GetDataConfiguration'), ('debug', 'GetDebug'),
    ('dragable', 'GetDragable'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('allocated_render_time', 'GetAllocatedRenderTime'), ('static',
    'GetStatic'), ('defer_lod_construction', 'GetDeferLODConstruction'),
    ('prop_type', 'GetPropType'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('origin',
    'GetOrigin'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'defer_lod_construction', 'dragable',
    'global_warning_display', 'pickable', 'static', 'use_bounds',
    'visibility', 'data_configuration', 'prop_type',
    'allocated_render_time', 'collapse_dimension_ratio',
    'estimated_render_time', 'maximum_display_list_size', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuadricLODActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadricLODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['defer_lod_construction', 'static', 'use_bounds',
            'visibility'], ['data_configuration', 'prop_type'],
            ['allocated_render_time', 'collapse_dimension_ratio',
            'estimated_render_time', 'maximum_display_list_size', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale']),
            title='Edit QuadricLODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadricLODActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

