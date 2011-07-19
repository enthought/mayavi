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


class GeoProjection(Object):
    """
    GeoProjection - Represent a projection from a sphere to a plane
    
    Superclass: Object
    
    This class uses the PROJ.4 library to represent geographic coordinate
    projections.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoProjection, obj, update, **traits)
    
    central_meridian = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the longitude which corresponds to the central meridian
        of the projection. This defaults to 0, the Greenwich Meridian.
        """
    )
    def _central_meridian_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCentralMeridian,
                        self.central_meridian)

    name = traits.String(r"latlong", enter_set=True, auto_set=False, help=\
        """
        Set/get the short name describing the projection you wish to use.
        This defaults to "rpoly" for no reason other than I like it. To
        get a list of valid values, use the get_number_of_projections() and
        get_projection_name(int) static methods.
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def _get_description(self):
        return self._vtk_obj.GetDescription()
    description = traits.Property(_get_description, help=\
        """
        Get the description of a projection. This will return NULL if the
        projection name is invalid.
        """
    )

    def _get_index(self):
        return self._vtk_obj.GetIndex()
    index = traits.Property(_get_index, help=\
        """
        Return the index of the current projection's type in the list of
        all projection types. On error, this will return -1. On success,
        it returns a number in [_0,_get_number_of_projections()[.
        """
    )

    def _get_number_of_projections(self):
        return self._vtk_obj.GetNumberOfProjections()
    number_of_projections = traits.Property(_get_number_of_projections, help=\
        """
        Returns the number of projections that this class offers.
        """
    )

    def get_projection_description(self, *args):
        """
        V.get_projection_description(int) -> string
        C++: static const char *GetProjectionDescription(int projection)
        Returns a description of one of the projections supported by this
        class.
        @param projection the index of a projection, must be in
            [_0,_get_number_of_projections()[.
        """
        ret = self._wrap_call(self._vtk_obj.GetProjectionDescription, *args)
        return ret

    def get_projection_name(self, *args):
        """
        V.get_projection_name(int) -> string
        C++: static const char *GetProjectionName(int projection)
        Returns the name of one of the projections supported by this
        class. You can pass these strings to set_name(char*).
        @param projection the index of a projection, must be in
            [_0,_get_number_of_projections()[.
        """
        ret = self._wrap_call(self._vtk_obj.GetProjectionName, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('central_meridian', 'GetCentralMeridian'), ('name', 'GetName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'central_meridian', 'name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoProjection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['central_meridian', 'name']),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

