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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class TriangularTexture(ImageAlgorithm):
    """
    TriangularTexture - generate 2d triangular texture map
    
    Superclass: ImageAlgorithm
    
    TriangularTexture is a filter that generates a 2d texture map
    based on the paper "Opacity-modulating Triangular Textures for Irregular
    Surfaces," by Penny Rheingans, IEEE Visualization '96, pp. 219-225.
    The textures assume texture coordinates of (0,0), (1.0) and (.5,
    sqrt(3)/2). The sequence of texture values is the same along each
    edge of the triangular texture map. So, the assignment order of
    texture coordinates is arbitrary.
    
    See Also:
    
    TriangularTCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriangularTexture, obj, update, **traits)
    
    y_size = traits.Int(64, enter_set=True, auto_set=False, help=\
        """
        Set the Y texture map dimension. Default is 64.
        """
    )
    def _y_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYSize,
                        self.y_size)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set a Scale Factor.
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    x_size = traits.Int(64, enter_set=True, auto_set=False, help=\
        """
        Set the X texture map dimension. Default is 64.
        """
    )
    def _x_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXSize,
                        self.x_size)

    texture_pattern = traits.Trait(1, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the texture pattern.
           1 = opaque at centroid (default)
           2 = opaque at vertices
           3 = opaque in rings around vertices
        """
    )
    def _texture_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTexturePattern,
                        self.texture_pattern)

    _updateable_traits_ = \
    (('y_size', 'GetYSize'), ('scale_factor', 'GetScaleFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('x_size', 'GetXSize'), ('abort_execute', 'GetAbortExecute'),
    ('texture_pattern', 'GetTexturePattern'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'scale_factor',
    'texture_pattern', 'x_size', 'y_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TriangularTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['scale_factor', 'texture_pattern', 'x_size',
            'y_size']),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

