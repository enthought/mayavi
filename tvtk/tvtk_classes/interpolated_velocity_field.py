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

from tvtk.tvtk_classes.abstract_interpolated_velocity_field import AbstractInterpolatedVelocityField


class InterpolatedVelocityField(AbstractInterpolatedVelocityField):
    """
    InterpolatedVelocityField - A concrete class for obtaining
    
    Superclass: AbstractInterpolatedVelocityField
    
    InterpolatedVelocityField acts as a continuous velocity field via
     cell interpolation on a DataSet, number_of_independent_variables = 4
     (x,y,z,t) and number_of_functions = 3 (u,v,w). As a concrete sub-class
     of AbstractInterpolatedVelocityField, this class adopts two
    levels
     of cell caching for faster though less robust cell location than its
     sibling class CellLocatorInterpolatedVelocityField. Level #0
    begins
     with intra-cell caching. Specifically, if the previous cell is valid
     and the nex point is still within it, ( Cell::EvaluatePosition()
     returns 1, coupled with the new parametric coordinates and weights
    ),
     the function values are interpolated and Cell::EvaluatePosition()
     is invoked only. If it fails, level #1 follows by inter-cell
    location
     of the target cell (that contains the next point). By inter-cell,
    the
     previous cell gives an important clue / guess or serves as an
    immediate
     neighbor to aid in the location of the target cell (as is typically
    the
     case with integrating a streamline across cells) by means of
    DataSet::
     find_cell(). If this still fails, a global cell search is invoked via
     DataSet::FindCell().
    
    
     Regardless of inter-cell or global search, PointLocator is
    employed
     as a crucial tool underlying the cell locator. The use of
    PointLocator
     casues InterpolatedVelocityField to return false target cells for
     datasets defined on complex grids.
    
    Caveats:
    
    
     InterpolatedVelocityField is not thread safe. A new instance
    should be
     created by each thread.
    
    See Also:
    
    
     AbstractInterpolatedVelocityField
    CellLocatorInterpolatedVelocityField
     GenericInterpolatedVelocityField
    CachingInterpolatedVelocityField
     TemporalInterpolatedVelocityField FunctionSet Streamer
    StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInterpolatedVelocityField, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('last_cell_id',
    'GetLastCellId'), ('caching', 'GetCaching'), ('normalize_vector',
    'GetNormalizeVector'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'caching', 'last_cell_id',
    'normalize_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['caching', 'last_cell_id',
            'normalize_vector']),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

