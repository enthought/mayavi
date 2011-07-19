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


class DirectionEncoder(Object):
    """
    DirectionEncoder - encode a direction into a one or two byte value
    
    Superclass: Object
    
    Given a direction, encode it into an integer value. This value should
    be less than 65536, which is the maximum number of encoded directions
    supported by this superclass. A direction encoded is used to encode
    normals in a volume for use during volume rendering, and the amount
    of space that is allocated per normal is 2 bytes. This is an abstract
    superclass - see the subclasses for specific implementation details.
    
    See Also:
    
    RecursiveSphereDirectionEncoder
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDirectionEncoder, obj, update, **traits)
    
    def get_decoded_gradient(self, *args):
        """
        V.get_decoded_gradient(int) -> (float, float, float)
        C++: virtual float *GetDecodedGradient(int value)
        / Given an encoded value, return a pointer to the normal vector
        """
        ret = self._wrap_call(self._vtk_obj.GetDecodedGradient, *args)
        return ret

    def get_encoded_direction(self, *args):
        """
        V.get_encoded_direction([float, float, float]) -> int
        C++: virtual int GetEncodedDirection(float n[3])
        Given a normal vector n, return the encoded direction
        """
        ret = self._wrap_call(self._vtk_obj.GetEncodedDirection, *args)
        return ret

    def _get_number_of_encoded_directions(self):
        return self._vtk_obj.GetNumberOfEncodedDirections()
    number_of_encoded_directions = traits.Property(_get_number_of_encoded_directions, help=\
        """
        Return the number of encoded directions
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DirectionEncoder, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DirectionEncoder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

