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


class MeanValueCoordinatesInterpolator(Object):
    """
    MeanValueCoordinatesInterpolator - compute interpolation computes
    
    Superclass: Object
    
    MeanValueCoordinatesInterpolator computes interpolation weights
    for a closed, manifold polyhedron mesh.  Once computed, the
    interpolation weights can be used to interpolate data anywhere
    interior or exterior to the mesh. This work implements two MVC
    algorithms. The first one is for triangular meshes which is
    documented in the Siggraph 2005 paper by Tao Ju, Scot Schaefer and
    Joe Warren from Rice University "Mean Value Coordinates for Closed
    Triangular Meshes". The second one is for general polyhedron mesh
    which is documented in the Eurographics Symposium on Geometry
    Processing 2006 paper by Torsten Langer, Alexander Belyaev and
    Hans-Peter Seidel from MPI Informatik "Spherical Barycentric
    Coordinates". The filter will automatically choose which algorithm to
    use based on whether the input mesh is triangulated or not.
    
    In VTK this class was initially created to interpolate data across
    polyhedral cells. In addition, the class can be used to interpolate
    data values from a polyhedron mesh, and to smoothly deform a mesh
    from an associated control mesh.
    
    See Also:
    
    PolyhedralCell
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMeanValueCoordinatesInterpolator, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MeanValueCoordinatesInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

