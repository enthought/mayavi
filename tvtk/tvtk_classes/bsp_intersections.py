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

from tvtk.tvtk_classes.object import Object


class BSPIntersections(Object):
    """
    BSPIntersections - Perform calculations (mostly intersection
    
    Superclass: Object
    
    Given an axis aligned binary spatial partitioning described by a
       BSPCuts object, perform intersection queries on various
       geometric entities with regions of the spatial partitioning.
    
    See Also:
    
    
       BSPCuts  KdTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBSPIntersections, obj, update, **traits)
    
    compute_intersections_using_data_bounds = tvtk_base.false_bool_trait(help=\
        """
        When computing the intersection of k-d tree regions with other
          objects, we use the spatial bounds of the region.  To use the
          tighter bound of the bounding box of the data within the
        region,
          set this variable ON.  (Specifying data bounds in the
        BSPCuts
          object is optional.  If data bounds were not specified, this
          option has no meaning.)
        """
    )
    def _compute_intersections_using_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeIntersectionsUsingDataBounds,
                        self.compute_intersections_using_data_bounds_)

    def _get_cuts(self):
        return wrap_vtk(self._vtk_obj.GetCuts())
    def _set_cuts(self, arg):
        old_val = self._get_cuts()
        self._wrap_call(self._vtk_obj.SetCuts,
                        deref_vtk(arg))
        self.trait_property_changed('cuts', old_val, arg)
    cuts = traits.Property(_get_cuts, _set_cuts, help=\
        """
        Define the binary spatial partitioning.
        """
    )

    def _get_number_of_regions(self):
        return self._vtk_obj.GetNumberOfRegions()
    number_of_regions = traits.Property(_get_number_of_regions, help=\
        """
        The number of regions in the binary spatial partitioning
        """
    )

    def get_region_bounds(self, *args):
        """
        V.get_region_bounds(int, [float, float, float, float, float, float])
             -> int
        C++: int GetRegionBounds(int regionID, double bounds[6])
        Get the spatial bounds of a particular region
          Return 0 if OK, 1 on error.
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionBounds, *args)
        return ret

    def get_region_data_bounds(self, *args):
        """
        V.get_region_data_bounds(int, [float, float, float, float, float,
            float]) -> int
        C++: int GetRegionDataBounds(int regionID, double bounds[6])
        Get the bounds of the data within the k-d tree region, possibly
           smaller than the bounds of the region.
          Return 0 if OK, 1 on error.
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionDataBounds, *args)
        return ret

    def intersects_box(self, *args):
        """
        V.intersects_box(int, float, float, float, float, float, float)
            -> int
        C++: int IntersectsBox(int regionId, double xmin, double xmax,
            double ymin, double ymax, double zmin, double zmax)
        Determine whether a region of the spatial decomposition
           intersects an axis aligned box.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectsBox, *args)
        return ret

    def intersects_cell(self, *args):
        """
        V.intersects_cell(int, Cell, int) -> int
        C++: int IntersectsCell(int regionId, Cell *cell,
            int cellRegion=-1)
        Determine whether a region of the spatial decomposition
           intersects the given cell.  If you already
           know the region that the cell centroid lies in, provide
           that as the last argument to make the computation quicker.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IntersectsCell, *my_args)
        return ret

    def intersects_sphere2(self, *args):
        """
        V.intersects_sphere2(int, float, float, float, float) -> int
        C++: int IntersectsSphere2(int regionId, double x, double y,
            double z, double rSquared)
        Determine whether a region of the spatial decomposition
           intersects a sphere, given the center of the sphere
           and the square of it's radius.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectsSphere2, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('compute_intersections_using_data_bounds',
    'GetComputeIntersectionsUsingDataBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['compute_intersections_using_data_bounds', 'debug',
    'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BSPIntersections, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BSPIntersections properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_intersections_using_data_bounds'], [], []),
            title='Edit BSPIntersections properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BSPIntersections properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

