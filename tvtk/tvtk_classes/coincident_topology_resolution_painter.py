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

from tvtk.tvtk_classes.poly_data_painter import PolyDataPainter


class CoincidentTopologyResolutionPainter(PolyDataPainter):
    """
    CoincidentTopologyResolutionPainter - painter that resolves 
    
    Superclass: PolyDataPainter
    
    Provides the ability to shift the z-buffer to resolve coincident
    topology. For example, if you'd like to draw a mesh with some edges a
    different color, and the edges lie on the mesh, this feature can be
    useful to get nice looking lines.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCoincidentTopologyResolutionPainter, obj, update, **traits)
    
    def POLYGON_OFFSET_FACES(self):
        """
        V.polygon__offset__faces() -> InformationIntegerKey
        C++: static InformationIntegerKey *POLYGON_OFFSET_FACES()
        When set and when RESOLVE_COINCIDENT_TOPOLOGY is set to use
        polygon offset, solid polygonal faces will be offsetted,
        otherwise lines/vertices will be offsetted.
        """
        ret = wrap_vtk(self._vtk_obj.POLYGON_OFFSET_FACES())
        return ret
        

    def POLYGON_OFFSET_PARAMETERS(self):
        """
        V.polygon__offset__parameters() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *POLYGON_OFFSET_PARAMETERS(
            )
        Used to set the polygon offset scale factor and units. Used when
        resolve_coincident_topology is set to polygon_offset.
        """
        ret = wrap_vtk(self._vtk_obj.POLYGON_OFFSET_PARAMETERS())
        return ret
        

    def RESOLVE_COINCIDENT_TOPOLOGY(self):
        """
        V.resolve__coincident__topology() -> InformationIntegerKey
        C++: static InformationIntegerKey *RESOLVE_COINCIDENT_TOPOLOGY(
            )
        Set/Get a global flag that controls whether coincident topology
        (e.g., a line on top of a polygon) is shifted to avoid z-buffer
        resolution (and hence rendering problems). If not off, there are
        two methods to choose from. polygon_offset uses graphics systems
        calls to shift polygons, but does not distinguish vertices and
        lines from one another. shift_z_buffer remaps the z-buffer to
        distinguish vertices, lines, and polygons, but does not always
        produce acceptable results. If you use the shift_z_buffer approach,
        you may also want to set the resolve_coincident_topology_z_shift
        value. (Note: not all mappers/graphics systems implement this
        functionality.)
        """
        ret = wrap_vtk(self._vtk_obj.RESOLVE_COINCIDENT_TOPOLOGY())
        return ret
        

    def Z_SHIFT(self):
        """
        V.z__shift() -> InformationDoubleKey
        C++: static InformationDoubleKey *Z_SHIFT()
        Used to set the z-shift if resolve_coincident_topology is set to
        shift_z_buffer.
        """
        ret = wrap_vtk(self._vtk_obj.Z_SHIFT())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CoincidentTopologyResolutionPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CoincidentTopologyResolutionPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CoincidentTopologyResolutionPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CoincidentTopologyResolutionPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

