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


class FrustumSource(PolyDataAlgorithm):
    """
    FrustumSource - create a polygonal representation of a frustum
    
    Superclass: PolyDataAlgorithm
    
    FrustumSource creates a frustum defines by a set of planes. The
    frustum is represented with four-sided polygons. It is possible to
    specify extra lines to better visualize the field of view.
    
    Usage:
    
    Typical use consists of 3 steps:
    1. get the planes coefficients from a Camera with
       Camera::GetFrustumPlanes()
    2. initialize the planes with Planes::SetFrustumPlanes() with the
       planes coefficients
    3. pass the Planes to a FrustumSource.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFrustumSource, obj, update, **traits)
    
    show_lines = tvtk_base.true_bool_trait(help=\
        """
        Tells if some extra lines will be generated. Initial value is
        true.
        """
    )
    def _show_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLines,
                        self.show_lines_)

    lines_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Length of the extra lines. This a stricly positive value. Initial
        value is 1.0.
        """
    )
    def _lines_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinesLength,
                        self.lines_length)

    def _get_planes(self):
        return wrap_vtk(self._vtk_obj.GetPlanes())
    def _set_planes(self, arg):
        old_val = self._get_planes()
        self._wrap_call(self._vtk_obj.SetPlanes,
                        deref_vtk(arg))
        self.trait_property_changed('planes', old_val, arg)
    planes = traits.Property(_get_planes, _set_planes, help=\
        """
        Return the 6 planes defining the frustum. Initial value is NULL.
        The 6 planes are defined in this order:
        left,right,bottom,top,far,near. If Planes==NULL or if
        planes->_get_number_of_planes()!=_6 when request_data() is called, an
        error message will be emitted and request_data() will return right
        away.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('lines_length',
    'GetLinesLength'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('show_lines', 'GetShowLines'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'show_lines', 'lines_length', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FrustumSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['show_lines'], [], ['lines_length']),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

