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


class LinkEdgels(PolyDataAlgorithm):
    """
    LinkEdgels - links edgels together to form digital curves.
    
    Superclass: PolyDataAlgorithm
    
    LinkEdgels links edgels into digital curves which are then stored
    as polylines. The algorithm works one pixel at a time only looking at
    its immediate neighbors. There is a gradient_threshold that can be set
    that eliminates any pixels with a smaller gradient value. This can be
    used as the lower threshold of a two value edgel thresholding.
    
    For the remaining edgels, links are first tried for the four
    connected neighbors.  A successful neighbor will satisfy three tests.
    First both edgels must be above the gradient threshold. Second, the
    difference between the orientation between the two edgels (Alpha) and
    each edgels orientation (Phi) must be less than link_threshold. Third,
    the difference between the two edgels Phi values must be less than
    phi_threshold. The most successful link is selected. The measure is
    simply the sum of the three angle differences (actually stored as the
    sum of the cosines). If none of the four connect neighbors succeeds,
    then the eight connect neighbors are examined using the same method.
    
    This filter requires gradient information so you will need to use a
    ImageGradient at some point prior to this filter.  Typically a
    NonMaximumSuppression filter is also used. ThresholdEdgels can
    be used to complete the two value edgel thresholding as used in a
    Canny edge detector. The SubpixelPositionEdgels filter can also be
    used after this filter to adjust the edgel locations.
    
    See Also:
    
    ImageData ImageGradient ImageNonMaximumSuppression
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLinkEdgels, obj, update, **traits)
    
    gradient_threshold = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the threshold for image gradient thresholding.
        """
    )
    def _gradient_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientThreshold,
                        self.gradient_threshold)

    link_threshold = traits.Float(90.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the threshold for Phi vs. Alpha link thresholding.
        """
    )
    def _link_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinkThreshold,
                        self.link_threshold)

    phi_threshold = traits.Float(90.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the threshold for Phi vs. Phi link thresholding.
        """
    )
    def _phi_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiThreshold,
                        self.phi_threshold)

    _updateable_traits_ = \
    (('phi_threshold', 'GetPhiThreshold'), ('debug', 'GetDebug'),
    ('gradient_threshold', 'GetGradientThreshold'), ('abort_execute',
    'GetAbortExecute'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('link_threshold', 'GetLinkThreshold'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'gradient_threshold', 'link_threshold',
    'phi_threshold', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LinkEdgels, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LinkEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['gradient_threshold', 'link_threshold',
            'phi_threshold']),
            title='Edit LinkEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LinkEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

