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

from tvtk.tvtk_classes.painter import Painter


class DefaultPainter(Painter):
    """
    DefaultPainter - sets up a default chain of painters.
    
    Superclass: Painter
    
    This painter does not do any actual rendering. Sets up a default
    pipeline of painters to mimick the behaiour of old PolyDataMapper.
    The chain is as follows: input--> ScalarsToColorsPainter -->
    ClipPlanesPainter --> DisplayListPainter -->
    CompositePainter --> CoincidentTopologyResolutionPainter -->
    LightingPainter --> RepresentationPainter --><Delegate of
    DefaultPainter>. Typically, the delegate of the default painter be
    one that is capable of r rendering graphics primitives or a
    ChooserPainter which can select appropriate painters to do the
    rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDefaultPainter, obj, update, **traits)
    
    def _get_clip_planes_painter(self):
        return wrap_vtk(self._vtk_obj.GetClipPlanesPainter())
    def _set_clip_planes_painter(self, arg):
        old_val = self._get_clip_planes_painter()
        self._wrap_call(self._vtk_obj.SetClipPlanesPainter,
                        deref_vtk(arg))
        self.trait_property_changed('clip_planes_painter', old_val, arg)
    clip_planes_painter = traits.Property(_get_clip_planes_painter, _set_clip_planes_painter, help=\
        """
        Get/Set the painter that handles clipping.
        """
    )

    def _get_delegate_painter(self):
        return wrap_vtk(self._vtk_obj.GetDelegatePainter())
    def _set_delegate_painter(self, arg):
        old_val = self._get_delegate_painter()
        self._wrap_call(self._vtk_obj.SetDelegatePainter,
                        deref_vtk(arg))
        self.trait_property_changed('delegate_painter', old_val, arg)
    delegate_painter = traits.Property(_get_delegate_painter, _set_delegate_painter, help=\
        """
        Set/Get the painter to which this painter should propagare its
        draw calls. These methods are overridden so that the delegate is
        set to the end of the Painter Chain.
        """
    )

    def _get_coincident_topology_resolution_painter(self):
        return wrap_vtk(self._vtk_obj.GetCoincidentTopologyResolutionPainter())
    def _set_coincident_topology_resolution_painter(self, arg):
        old_val = self._get_coincident_topology_resolution_painter()
        self._wrap_call(self._vtk_obj.SetCoincidentTopologyResolutionPainter,
                        deref_vtk(arg))
        self.trait_property_changed('coincident_topology_resolution_painter', old_val, arg)
    coincident_topology_resolution_painter = traits.Property(_get_coincident_topology_resolution_painter, _set_coincident_topology_resolution_painter, help=\
        """
        Painter used to resolve coincident topology.
        """
    )

    def _get_composite_painter(self):
        return wrap_vtk(self._vtk_obj.GetCompositePainter())
    def _set_composite_painter(self, arg):
        old_val = self._get_composite_painter()
        self._wrap_call(self._vtk_obj.SetCompositePainter,
                        deref_vtk(arg))
        self.trait_property_changed('composite_painter', old_val, arg)
    composite_painter = traits.Property(_get_composite_painter, _set_composite_painter, help=\
        """
        Get/Set the painter used to handle composite datasets.
        """
    )

    def _get_display_list_painter(self):
        return wrap_vtk(self._vtk_obj.GetDisplayListPainter())
    def _set_display_list_painter(self, arg):
        old_val = self._get_display_list_painter()
        self._wrap_call(self._vtk_obj.SetDisplayListPainter,
                        deref_vtk(arg))
        self.trait_property_changed('display_list_painter', old_val, arg)
    display_list_painter = traits.Property(_get_display_list_painter, _set_display_list_painter, help=\
        """
        Get/Set the painter that builds display lists.
        """
    )

    def _get_lighting_painter(self):
        return wrap_vtk(self._vtk_obj.GetLightingPainter())
    def _set_lighting_painter(self, arg):
        old_val = self._get_lighting_painter()
        self._wrap_call(self._vtk_obj.SetLightingPainter,
                        deref_vtk(arg))
        self.trait_property_changed('lighting_painter', old_val, arg)
    lighting_painter = traits.Property(_get_lighting_painter, _set_lighting_painter, help=\
        """
        Get/Set the painter that controls lighting.
        """
    )

    def _get_scalars_to_colors_painter(self):
        return wrap_vtk(self._vtk_obj.GetScalarsToColorsPainter())
    def _set_scalars_to_colors_painter(self, arg):
        old_val = self._get_scalars_to_colors_painter()
        self._wrap_call(self._vtk_obj.SetScalarsToColorsPainter,
                        deref_vtk(arg))
        self.trait_property_changed('scalars_to_colors_painter', old_val, arg)
    scalars_to_colors_painter = traits.Property(_get_scalars_to_colors_painter, _set_scalars_to_colors_painter, help=\
        """
        Get/Set the painter that maps scalars to colors.
        """
    )

    def _get_representation_painter(self):
        return wrap_vtk(self._vtk_obj.GetRepresentationPainter())
    def _set_representation_painter(self, arg):
        old_val = self._get_representation_painter()
        self._wrap_call(self._vtk_obj.SetRepresentationPainter,
                        deref_vtk(arg))
        self.trait_property_changed('representation_painter', old_val, arg)
    representation_painter = traits.Property(_get_representation_painter, _set_representation_painter, help=\
        """
        Painter used to convert polydata to Wireframe/Points
        representation.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DefaultPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DefaultPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

