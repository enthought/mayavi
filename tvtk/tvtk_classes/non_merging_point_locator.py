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

from tvtk.tvtk_classes.point_locator import PointLocator


class NonMergingPointLocator(PointLocator):
    """
    NonMergingPointLocator - direct / check-free point insertion.
    
    Superclass: PointLocator
    
    As a special sub-class of PointLocator, NonMergingPointLocator
    is
     intended for direct / check-free insertion of points into a
    Points
     object. In other words, any given point is always directly inserted.
     The name emphasizes the difference between this class and its
    sibling
     class MergePoints in that the latter class performs check-based
    zero
     tolerance point insertion (or to 'merge' exactly duplicate /
    coincident
     points) by exploiting the uniform bin mechanism employed by the
    parent
     class PointLocator. PointLocator allows for generic (zero and
    non-
     zero) tolerance point insertion as well as point location.
    
    See Also:
    
    
     IncrementalPointLocator PointLocator MergePoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNonMergingPointLocator, obj, update, **traits)
    
    _updateable_traits_ = \
    (('divisions', 'GetDivisions'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_level', 'GetMaxLevel'),
    ('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('reference_count', 'GetReferenceCount'), ('tolerance',
    'GetTolerance'), ('number_of_points_per_bucket',
    'GetNumberOfPointsPerBucket'))
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'divisions',
    'max_level', 'number_of_points_per_bucket', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NonMergingPointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit NonMergingPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic'], [], ['divisions', 'max_level',
            'number_of_points_per_bucket', 'tolerance']),
            title='Edit NonMergingPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NonMergingPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

