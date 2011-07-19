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

from tvtk.tvtk_classes.culler import Culler


class FrustumCoverageCuller(Culler):
    """
    FrustumCoverageCuller - cull props based on frustum coverage
    
    Superclass: Culler
    
    FrustumCoverageCuller will cull props based on the coverage in the
    view frustum. The coverage is computed by enclosing the prop in a
    bounding sphere, projecting that to the viewing coordinate system,
    then taking a slice through the view frustum at the center of the
    sphere. This results in a circle on the plane slice through the view
    frustum. This circle is enclosed in a squared, and the fraction of
    the plane slice that this square covers is the coverage. This is a
    number between 0 and 1. If the number is less than the
    minumum_coverage, the allocated render time for that prop is set to
    zero. If it is greater than the maximum_coverage, the allocated render
    time is set to 1.0. In between, a linear ramp is used to convert
    coverage into allocated render time.
    
    See Also:
    
    Culler
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFrustumCoverageCuller, obj, update, **traits)
    
    sorting_style = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'front_to_back': 1, 'back_to_front': 2}), help=\
        """
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
    )
    def _sorting_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSortingStyle,
                        self.sorting_style_)

    maximum_coverage = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum coverage - props with more coverage than this
        are given an allocated render time of 1.0 (the maximum)
        """
    )
    def _maximum_coverage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumCoverage,
                        self.maximum_coverage)

    minimum_coverage = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum coverage - props with less coverage than this
        are given no time to render (they are culled)
        """
    )
    def _minimum_coverage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumCoverage,
                        self.minimum_coverage)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('sorting_style', 'GetSortingStyle'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_coverage', 'GetMaximumCoverage'), ('reference_count',
    'GetReferenceCount'), ('minimum_coverage', 'GetMinimumCoverage'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'sorting_style',
    'maximum_coverage', 'minimum_coverage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FrustumCoverageCuller, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FrustumCoverageCuller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['sorting_style'], ['maximum_coverage',
            'minimum_coverage']),
            title='Edit FrustumCoverageCuller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FrustumCoverageCuller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

