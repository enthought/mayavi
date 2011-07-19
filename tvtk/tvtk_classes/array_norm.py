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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class ArrayNorm(ArrayDataAlgorithm):
    """
    ArrayNorm - Computes L-norms along one dimension of an array.
    
    Superclass: ArrayDataAlgorithm
    
    Given an input matrix (vtk_typed_array), computes the L-norm for each
    vector along either dimension, storing the results in a dense output
    vector (_1d DenseArray).  The caller may optionally request the
    inverse norm as output (useful for subsequent normalization), and may
    limit the computation to a "window" of vector elements, to avoid data
    copying.
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayNorm, obj, update, **traits)
    
    invert = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Controls whether to invert output values.  Default: false
        """
    )
    def _invert_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInvert,
                        self.invert)

    dimension = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Controls the dimension along which norms will be computed.  For
        input matrices, For input matrices, use "0" (rows) or "1"
        (columns). Default: 0
        """
    )
    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    l = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Controls the L-value.  Default: 2
        """
    )
    def _l_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetL,
                        self.l)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('invert',
    'GetInvert'), ('progress_text', 'GetProgressText'), ('dimension',
    'GetDimension'), ('l', 'GetL'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimension', 'invert', 'l', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayNorm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimension', 'invert', 'l']),
            title='Edit ArrayNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

