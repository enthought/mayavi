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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class PlatonicSolidSource(PolyDataAlgorithm):
    """
    PlatonicSolidSource - produce polygonal Platonic solids
    
    Superclass: PolyDataAlgorithm
    
    PlatonicSolidSource can generate each of the five Platonic solids:
    tetrahedron, cube, octahedron, icosahedron, and dodecahedron. Each of
    the solids is placed inside a sphere centered at the origin with
    radius 1.0. To use this class, simply specify the solid to create.
    Note that this source object creates cell scalars that are (integral
    value) face numbers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlatonicSolidSource, obj, update, **traits)
    
    solid_type = traits.Trait('tetrahedron',
    tvtk_base.TraitRevPrefixMap({'icosahedron': 3, 'octahedron': 2, 'cube': 1, 'tetrahedron': 0, 'dodecahedron': 4}), help=\
        """
        Specify the type of platonic_solid solid to create.
        """
    )
    def _solid_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSolidType,
                        self.solid_type_)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('solid_type',
    'GetSolidType'), ('progress_text', 'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'solid_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlatonicSolidSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlatonicSolidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['solid_type'], []),
            title='Edit PlatonicSolidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlatonicSolidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

