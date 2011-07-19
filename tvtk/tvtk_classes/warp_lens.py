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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class WarpLens(PointSetAlgorithm):
    """
    WarpLens - deform geometry by applying lens distortion
    
    Superclass: PointSetAlgorithm
    
    WarpLens is a filter that modifies point coordinates by moving in
    accord with a lens distortion model.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWarpLens, obj, update, **traits)
    
    p2 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the decentering distortion parameters for the lens
        """
    )
    def _p2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetP2,
                        self.p2)

    principal_point = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _principal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrincipalPoint,
                        self.principal_point)

    p1 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the decentering distortion parameters for the lens
        """
    )
    def _p1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetP1,
                        self.p1)

    kappa = traits.Float(-1e-06, enter_set=True, auto_set=False, help=\
        """
        Specify second order symmetric radial lens distortion parameter.
        This is obsoleted by newer instance variables.
        """
    )
    def _kappa_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKappa,
                        self.kappa)

    center = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the center of radial distortion in pixels. This is
        obsoleted by newer instance variables.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    format_height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the imager format width / height in mm
        """
    )
    def _format_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFormatHeight,
                        self.format_height)

    format_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the imager format width / height in mm
        """
    )
    def _format_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFormatWidth,
                        self.format_width)

    k2 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the symmetric radial distortion parameters for the lens
        """
    )
    def _k2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetK2,
                        self.k2)

    k1 = traits.Float(-1e-06, enter_set=True, auto_set=False, help=\
        """
        Specify the symmetric radial distortion parameters for the lens
        """
    )
    def _k1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetK1,
                        self.k1)

    image_height = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the image width / height in pixels
        """
    )
    def _image_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageHeight,
                        self.image_height)

    image_width = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the image width / height in pixels
        """
    )
    def _image_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageWidth,
                        self.image_width)

    _updateable_traits_ = \
    (('p2', 'GetP2'), ('format_height', 'GetFormatHeight'), ('p1',
    'GetP1'), ('kappa', 'GetKappa'), ('center', 'GetCenter'),
    ('format_width', 'GetFormatWidth'), ('principal_point',
    'GetPrincipalPoint'), ('progress_text', 'GetProgressText'),
    ('image_width', 'GetImageWidth'), ('debug', 'GetDebug'), ('k2',
    'GetK2'), ('k1', 'GetK1'), ('image_height', 'GetImageHeight'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('abort_execute',
    'GetAbortExecute'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'format_height', 'format_width',
    'image_height', 'image_width', 'k1', 'k2', 'kappa', 'p1', 'p2',
    'principal_point', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WarpLens, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'format_height', 'format_width',
            'image_height', 'image_width', 'k1', 'k2', 'kappa', 'p1', 'p2',
            'principal_point']),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

