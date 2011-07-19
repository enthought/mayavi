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


class PolyDataPainter(Painter):
    """
    PolyDataPainter - Abstract class for drawing poly data.
    
    Superclass: Painter
    
    PolyDataPainter encapsulates a method of drawing poly data.  This
    is a subset of what a mapper does.  The painter does no maintenance
    of the rendering state (camera, lights, etc.).  It is solely
    responsible for issuing rendering commands that build graphics
    primitives.
    
    To simplify coding, an implementation of PolyDataPainter is
    allowed to support only certain types of poly data or certain types
    of primitives.
    
    See Also:
    
    DefaultPainter StandardPainter PainterDeviceAdapter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataPainter, obj, update, **traits)
    
    def _get_input_as_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetInputAsPolyData())
    input_as_poly_data = traits.Property(_get_input_as_poly_data, help=\
        """
        Get/set the poly data to render.
        """
    )

    def _get_output_as_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetOutputAsPolyData())
    output_as_poly_data = traits.Property(_get_output_as_poly_data, help=\
        """
        Get the output polydata from this Painter. The default
        implementation forwards the input polydata as the output.
        """
    )

    def BUILD_NORMALS(self):
        """
        V.build__normals() -> InformationIntegerKey
        C++: static InformationIntegerKey *BUILD_NORMALS()
        Keys used to specify control the behaviour of the painter. When
        on, the painter creates normals when none are available in the
        polydata. On by default.
        """
        ret = wrap_vtk(self._vtk_obj.BUILD_NORMALS())
        return ret
        

    def DATA_ARRAY_TO_VERTEX_ATTRIBUTE(self):
        """
        V.data__array__to__vertex__attribute() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *DATA_ARRAY_TO_VERTEX_ATTRIBUTE(
            )"""
        ret = wrap_vtk(self._vtk_obj.DATA_ARRAY_TO_VERTEX_ATTRIBUTE())
        return ret
        

    def DISABLE_SCALAR_COLOR(self):
        """
        V.disable__scalar__color() -> InformationIntegerKey
        C++: static InformationIntegerKey *DISABLE_SCALAR_COLOR()
        Key added to disable any scalar coloring for the current pass.
        """
        ret = wrap_vtk(self._vtk_obj.DISABLE_SCALAR_COLOR())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

