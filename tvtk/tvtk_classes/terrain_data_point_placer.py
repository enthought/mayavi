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

from tvtk.tvtk_classes.point_placer import PointPlacer


class TerrainDataPointPlacer(PointPlacer):
    """
    TerrainDataPointPlacer - Place points on terrain data
    
    Superclass: PointPlacer
    
    TerrainDataPointPlacer dictates the placement of points on height
    field data. The class takes as input the list of props that represent
    the terrain in a rendered scene. A height offset can be specified to
    dicatate the placement of points at a certain height above the
    surface.
    
    Usage:
    
    A typical usage of this class is as
    follows:point_placer->_add_prop(dem_actor);    // the actor(s) containing
    the terrain.
    rep->_set_point_placer(point_placer);
    point_placer->_set_height_offset( 100 );
    
    See Also:
    
    PointPlacer TerrainContourLineInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTerrainDataPointPlacer, obj, update, **traits)
    
    height_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        This is the height above (or below) the terrain that the dictated
        point should be placed. Positive values indicate distances above
        the terrain; negative values indicate distances below the
        terrain. The default is 0.0.
        """
    )
    def _height_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeightOffset,
                        self.height_offset)

    def _get_prop_picker(self):
        return wrap_vtk(self._vtk_obj.GetPropPicker())
    prop_picker = traits.Property(_get_prop_picker, help=\
        """
        Get the Prop picker.
        """
    )

    def add_prop(self, *args):
        """
        V.add_prop(Prop)
        C++: virtual void AddProp(Prop *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddProp, *my_args)
        return ret

    def remove_all_props(self):
        """
        V.remove_all_props()
        C++: virtual void RemoveAllProps()"""
        ret = self._vtk_obj.RemoveAllProps()
        return ret
        

    _updateable_traits_ = \
    (('height_offset', 'GetHeightOffset'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pixel_tolerance', 'GetPixelTolerance'), ('reference_count',
    'GetReferenceCount'), ('world_tolerance', 'GetWorldTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'height_offset',
    'pixel_tolerance', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TerrainDataPointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TerrainDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['height_offset', 'pixel_tolerance',
            'world_tolerance']),
            title='Edit TerrainDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TerrainDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

