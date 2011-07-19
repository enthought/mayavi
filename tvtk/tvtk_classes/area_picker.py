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


class AreaPicker(AbstractPropPicker):
    """
    AreaPicker - Picks props behind a selection rectangle on a
    viewport.
    
    Superclass: AbstractPropPicker
    
    The AreaPicker picks all Prop3Ds that lie behind the screen
    space rectangle from x0,y0 and x1,y1. The selection is based upon the
    bounding box of the prop and is thus not exact.
    
    Like Picker, a pick results in a list of prop3ds because many
    props may lie within the pick frustum. You can also get an
    assembly_path, which in this case is defined to be the path to the one
    particular prop in the prop3d list that lies nearest to the near
    plane.
    
    This picker also returns the selection frustum, defined as either a
    Planes, or a set of eight corner vertices in world space. The
    Planes version is an implicit_function, which is suitable for use
    with the ExtractGeometry. The six frustum planes are in order:
    left, right, bottom, top, near, far
    
    Because this picker picks everything within a volume, the world pick
    point result is ill-defined. Therefore if you ask this class for the
    world pick position, you will get the centroid of the pick frustum.
    This may be outside of all props in the prop list.
    
    See Also:
    
    InteractorStyleRubberBandPick, ExtractSelectedFrustum.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAreaPicker, obj, update, **traits)
    
    def _get_clip_points(self):
        return wrap_vtk(self._vtk_obj.GetClipPoints())
    clip_points = traits.Property(_get_clip_points, help=\
        """
        Return eight points that define the selection frustum.
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

    def _get_frustum(self):
        return wrap_vtk(self._vtk_obj.GetFrustum())
    frustum = traits.Property(_get_frustum, help=\
        """
        Return the six planes that define the selection frustum. The
        implicit function defined by the planes evaluates to negative
        inside and positive outside.
        """
    )

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    mapper = traits.Property(_get_mapper, help=\
        """
        Return mapper that was picked (if any).
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

    def area_pick(self, *args):
        """
        V.area_pick(float, float, float, float, Renderer) -> int
        C++: virtual int AreaPick(double x0, double y0, double x1,
            double y1, Renderer *renderer=NULL)
        Perform pick operation in volume behind the given screen
        coordinates. Props intersecting the selection frustum will be
        accessible via get_prop3d. get_planes returns a ImplicitFunciton
        suitable for ExtractGeometry.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AreaPick, *my_args)
        return ret

    def set_pick_coords(self, *args):
        """
        V.set_pick_coords(float, float, float, float)
        C++: void SetPickCoords(double x0, double y0, double x1,
            double y1)
        Set the default screen rectangle to pick in.
        """
        ret = self._wrap_call(self._vtk_obj.SetPickCoords, *args)
        return ret

    def set_renderer(self, *args):
        """
        V.set_renderer(Renderer)
        C++: void SetRenderer(Renderer *)
        Set the default renderer to pick on.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRenderer, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pick_from_list', 'GetPickFromList'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AreaPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AreaPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pick_from_list'], [], []),
            title='Edit AreaPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AreaPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

