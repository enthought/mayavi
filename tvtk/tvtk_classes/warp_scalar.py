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


class WarpScalar(PointSetAlgorithm):
    """
    WarpScalar - deform geometry with scalar data
    
    Superclass: PointSetAlgorithm
    
    WarpScalar is a filter that modifies point coordinates by moving
    points along point normals by the scalar amount times the scale
    factor. Useful for creating carpet or x-y-z plots.
    
    If normals are not present in data, the Normal instance variable will
    be used as the direction along which to warp the geometry. If normals
    are present but you would like to use the Normal instance variable,
    set the use_normal boolean to true.
    
    If XYPlane boolean is set true, then the z-value is considered to be
    a scalar value (still scaled by scale factor), and the displacement
    is along the z-axis. If scalars are also present, these are copied
    through and can be used to color the surface.
    
    Note that the filter passes both its point data and cell data to its
    output, except for normals, since these are distorted by the warping.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWarpScalar, obj, update, **traits)
    
    use_normal = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off use of user specified normal. If on, data normals
        will be ignored and instance variable Normal will be used
        instead.
        """
    )
    def _use_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseNormal,
                        self.use_normal_)

    xy_plane = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag specifying that input data is x-y plane. If x-y
        plane, then the z value is used to warp the surface in the z-axis
        direction (times the scale factor) and scalars are used to color
        the surface.
        """
    )
    def _xy_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXYPlane,
                        self.xy_plane_)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify value to scale displacement.
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    _updateable_traits_ = \
    (('scale_factor', 'GetScaleFactor'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('normal', 'GetNormal'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('use_normal', 'GetUseNormal'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('xy_plane',
    'GetXYPlane'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_normal', 'xy_plane', 'normal',
    'progress_text', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WarpScalar, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WarpScalar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_normal', 'xy_plane'], [], ['normal',
            'scale_factor']),
            title='Edit WarpScalar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WarpScalar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

