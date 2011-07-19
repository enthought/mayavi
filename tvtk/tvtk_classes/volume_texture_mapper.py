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

from tvtk.tvtk_classes.volume_mapper import VolumeMapper


class VolumeTextureMapper(VolumeMapper):
    """
    VolumeTextureMapper - Abstract class for a volume mapper
    
    Superclass: VolumeMapper
    
    VolumeTextureMapper is the abstract definition of a volume mapper
    that uses a texture mapping approach.
    
    See Also:
    
    VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeTextureMapper, obj, update, **traits)
    
    def _get_gradient_estimator(self):
        return wrap_vtk(self._vtk_obj.GetGradientEstimator())
    def _set_gradient_estimator(self, arg):
        old_val = self._get_gradient_estimator()
        self._wrap_call(self._vtk_obj.SetGradientEstimator,
                        deref_vtk(arg))
        self.trait_property_changed('gradient_estimator', old_val, arg)
    gradient_estimator = traits.Property(_get_gradient_estimator, _set_gradient_estimator, help=\
        """
        Set / Get the gradient estimator used to estimate normals
        """
    )

    def _get_data_origin(self):
        return self._vtk_obj.GetDataOrigin()
    data_origin = traits.Property(_get_data_origin, help=\
        """
        Allow access to the arrays / variables from the templated
        functions in the subclasses.
        """
    )

    def _get_data_spacing(self):
        return self._vtk_obj.GetDataSpacing()
    data_spacing = traits.Property(_get_data_spacing, help=\
        """
        Allow access to the arrays / variables from the templated
        functions in the subclasses.
        """
    )

    def _get_gradient_shader(self):
        return wrap_vtk(self._vtk_obj.GetGradientShader())
    gradient_shader = traits.Property(_get_gradient_shader, help=\
        """
        Get the gradient shader.
        """
    )

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    render_window = traits.Property(_get_render_window, help=\
        """
        Allow access to the arrays / variables from the templated
        functions in the subclasses.
        """
    )

    def _get_shade(self):
        return self._vtk_obj.GetShade()
    shade = traits.Property(_get_shade, help=\
        """
        Allow access to the arrays / variables from the templated
        functions in the subclasses.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'), ('scalar_mode',
    'GetScalarMode'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('cropping',
    'GetCropping'), ('abort_execute', 'GetAbortExecute'), ('blend_mode',
    'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'cropping_region_planes', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeTextureMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeTextureMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['cropping_region_planes']),
            title='Edit VolumeTextureMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeTextureMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

