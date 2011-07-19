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

from tvtk.tvtk_classes.abstract_transform import AbstractTransform


class GeoSphereTransform(AbstractTransform):
    """
    GeoSphereTransform - A transformation between long-lat-alt and
    rect coords
    
    Superclass: AbstractTransform
    
    the cartesian coordinate system is the following (if base_altitude is
    0),
    - the origin is at the center of the earth
    - the x axis goes from the origin to (longtitude=-90,latitude=0),
      intersection of equator and the meridian passing just east of
      Galapagos Islands
    - the y axis goes from the origin to the intersection of Greenwitch
      meridian and equator (longitude=0,latitude=0)
    - the z axis goes from the origin to the Geographic North Pole
      (latitude=90)
    - therefore the frame is right-handed.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoSphereTransform, obj, update, **traits)
    
    to_rectangular = tvtk_base.true_bool_trait(help=\
        """
        If on, this transform converts (long,lat,alt) triples to (x,y,z)
        as an offset from the center of the earth. Alt, x, y, and z are
        all be in meters. If off, the tranform works in the reverse
        direction. Initial value is on.
        """
    )
    def _to_rectangular_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetToRectangular,
                        self.to_rectangular_)

    base_altitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The base altitude to transform coordinates to. This can be useful
        for transforming lines just above the earth's surface. Default is
        0.
        """
    )
    def _base_altitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBaseAltitude,
                        self.base_altitude)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('base_altitude',
    'GetBaseAltitude'), ('to_rectangular', 'GetToRectangular'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'to_rectangular',
    'base_altitude'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoSphereTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoSphereTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['to_rectangular'], [], ['base_altitude']),
            title='Edit GeoSphereTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoSphereTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

