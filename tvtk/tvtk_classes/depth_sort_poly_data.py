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


class DepthSortPolyData(PolyDataAlgorithm):
    """
    DepthSortPolyData - sort poly data along camera view direction
    
    Superclass: PolyDataAlgorithm
    
    DepthSortPolyData rearranges the order of cells so that certain
    rendering operations (e.g., transparency or Painter's algorithms)
    generate correct results. To use this filter you must specify the
    direction vector along which to sort the cells. You can do this by
    specifying a camera and/or prop to define a view direction; or
    explicitly set a view direction.
    
    Caveats:
    
    The sort operation will not work well for long, thin primitives, or
    cells that intersect, overlap, or interpenetrate each other.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDepthSortPolyData, obj, update, **traits)
    
    sort_scalars = tvtk_base.false_bool_trait(help=\
        """
        Set/Get a flag that controls the generation of scalar values
        corresponding to the sort order. If enabled, the output of this
        filter will include scalar values that range from 0 to
        (ncells-1), where 0 is closest to the sort direction.
        """
    )
    def _sort_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSortScalars,
                        self.sort_scalars_)

    direction = traits.Trait('back_to_front',
    tvtk_base.TraitRevPrefixMap({'specified_vector': 2, 'front_to_back': 1, 'back_to_front': 0}), help=\
        """
        Specify the sort method for the polygonal primitives. By default,
        the poly data is sorted from back to front.
        """
    )
    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction_)

    depth_sort_mode = traits.Trait('first_point',
    tvtk_base.TraitRevPrefixMap({'bounds_center': 1, 'first_point': 0, 'parametric_center': 2}), help=\
        """
        Specify the point to use when sorting. The fastest is to just
        take the first cell point. Other options are to take the bounding
        box center or the parametric center of the cell. By default, the
        first cell point is used.
        """
    )
    def _depth_sort_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthSortMode,
                        self.depth_sort_mode_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Specify a camera that is used to define a view direction along
        which the cells are sorted. This ivar only has effect if the
        direction is set to front-to-back or back-to-front, and a camera
        is specified.
        """
    )

    def _get_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetProp3D())
    def _set_prop3d(self, arg):
        old_val = self._get_prop3d()
        self._wrap_call(self._vtk_obj.SetProp3D,
                        deref_vtk(arg))
        self.trait_property_changed('prop3d', old_val, arg)
    prop3d = traits.Property(_get_prop3d, _set_prop3d, help=\
        """
        Specify a transformation matrix (via the Prop3D::GetMatrix()
        method) that is used to include the effects of transformation.
        This ivar only has effect if the direction is set to
        front-to-back or back-to-front, and a camera is specified.
        Specifying the Prop3D is optional.
        """
    )

    vector = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVector,
                        self.vector)

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('direction', 'GetDirection'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('sort_scalars', 'GetSortScalars'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('vector', 'GetVector'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('depth_sort_mode',
    'GetDepthSortMode'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'sort_scalars', 'depth_sort_mode', 'direction',
    'origin', 'progress_text', 'vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DepthSortPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DepthSortPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['sort_scalars'], ['depth_sort_mode', 'direction'],
            ['origin', 'vector']),
            title='Edit DepthSortPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DepthSortPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

