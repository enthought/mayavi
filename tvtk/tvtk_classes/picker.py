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

from tvtk.tvtk_classes.abstract_prop_picker import AbstractPropPicker


class Picker(AbstractPropPicker):
    """
    Picker - superclass for 3d geometric pickers (uses ray cast)
    
    Superclass: AbstractPropPicker
    
    Picker is used to select instances of Prop3D by shooting a ray
    into a graphics window and intersecting with the actor's bounding
    box. The ray is defined from a point defined in window (or pixel)
    coordinates, and a point located from the camera's position.
    
    Picker may return more than one Prop3D, since more than one
    bounding box may be intersected. Picker returns an unsorted list
    of props that were hit, and a list of the corresponding world points
    of the hits. For the Prop3D that is closest to the camera,
    Picker returns the pick coordinates in world and untransformed
    mapper space, the prop itself, the data set, and the mapper.  For
    Picker the closest prop is the one whose center point (i.e.,
    center of bounding box) projected on the view ray is closest to the
    camera.  Subclasses of Picker use other methods for computing the
    pick point.
    
    See Also:
    
    Picker is used for quick geometric picking. If you desire more
    precise picking of points or cells based on the geometry of any
    Prop3D, use the subclasses PointPicker or CellPicker.  For
    hardware-accelerated picking of any type of Prop, use
    PropPicker or WorldPointPicker.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPicker, obj, update, **traits)
    
    tolerance = traits.Float(0.025, enter_set=True, auto_set=False, help=\
        """
        Specify tolerance for performing pick operation. Tolerance is
        specified as fraction of rendering window size. (Rendering window
        size is measured across diagonal.)
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_actors(self):
        return wrap_vtk(self._vtk_obj.GetActors())
    actors = traits.Property(_get_actors, help=\
        """
        Return a collection of all the actors that were intersected. This
        collection is not sorted. (This is a convenience method to
        maintain backward compatibility.)
        """
    )

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    data_set = traits.Property(_get_data_set, help=\
        """
        Get a pointer to the dataset that was picked (if any). If nothing
        was picked then NULL is returned.
        """
    )

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    mapper = traits.Property(_get_mapper, help=\
        """
        Return mapper that was picked (if any).
        """
    )

    def _get_mapper_position(self):
        return self._vtk_obj.GetMapperPosition()
    mapper_position = traits.Property(_get_mapper_position, help=\
        """
        Return position in mapper (i.e., non-transformed) coordinates of
        pick point.
        """
    )

    def _get_picked_positions(self):
        return wrap_vtk(self._vtk_obj.GetPickedPositions())
    picked_positions = traits.Property(_get_picked_positions, help=\
        """
        Return a list of the points the the actors returned by get_prop3ds
        were intersected at. The order of this list will match the order
        of get_prop3ds.
        """
    )

    def _get_prop3ds(self):
        return wrap_vtk(self._vtk_obj.GetProp3Ds())
    prop3ds = traits.Property(_get_prop3ds, help=\
        """
        Return a collection of all the prop 3d's that were intersected by
        the pick ray. This collection is not sorted.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('tolerance', 'GetTolerance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Picker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Picker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], ['tolerance']),
            title='Edit Picker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Picker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

