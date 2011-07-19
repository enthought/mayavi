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


class Axes(PolyDataAlgorithm):
    """
    Axes - create an x-y-z axes
    
    Superclass: PolyDataAlgorithm
    
    Axes creates three lines that form an x-y-z axes. The origin of
    the axes is user specified (0,0,0 is default), and the size is
    specified with a scale factor. Three scalar values are generated for
    the three lines and can be used (via color map) to indicate a
    particular coordinate axis.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxes, obj, update, **traits)
    
    symmetric = tvtk_base.false_bool_trait(help=\
        """
        If Symetric is on, the the axis continue to negative values.
        """
    )
    def _symmetric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSymmetric,
                        self.symmetric_)

    compute_normals = tvtk_base.true_bool_trait(help=\
        """
        Option for computing normals.  By default they are computed.
        """
    )
    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the scale factor of the axes. Used to control size.
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('scale_factor', 'GetScaleFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('compute_normals',
    'GetComputeNormals'), ('symmetric', 'GetSymmetric'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_normals', 'debug',
    'global_warning_display', 'release_data_flag', 'symmetric', 'origin',
    'progress_text', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Axes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Axes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_normals', 'symmetric'], [], ['origin',
            'scale_factor']),
            title='Edit Axes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Axes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

