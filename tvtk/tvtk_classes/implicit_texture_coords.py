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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class ImplicitTextureCoords(DataSetAlgorithm):
    """
    ImplicitTextureCoords - generate 1d, 2d, or 3d texture coordinates
    based on implicit function(s)
    
    Superclass: DataSetAlgorithm
    
    ImplicitTextureCoords is a filter to generate 1d, 2d, or 3d
    texture coordinates from one, two, or three implicit functions,
    respectively. In combinations with a BooleanTexture map (or
    another texture map of your own creation), the texture coordinates
    can be used to highlight (via color or intensity) or cut (via
    transparency) dataset geometry without any complex geometric
    processing. (Note: the texture coordinates are referred to as r-s-t
    coordinates.)
    
    The texture coordinates are automatically normalized to lie between
    (0,1). Thus, no matter what the implicit functions evaluate to, the
    resulting texture coordinates lie between (0,1), with the zero
    implicit function value mapped to the 0.5 texture coordinates value.
    Depending upon the maximum negative/positive implicit function
    values, the full (0,1) range may not be occupied (i.e., the
    positive/negative ranges are mapped using the same scale factor).
    
    A boolean variable invert_texture is available to flip the texture
    coordinates around 0.5 (value 1.0 becomes 0.0, 0.25->0.75). This is
    equivalent to flipping the texture map (but a whole lot easier).
    
    Caveats:
    
    You can use the transformation capabilities of ImplicitFunction to
    orient, translate, and scale the implicit functions. Also, the
    dimension of the texture coordinates is implicitly defined by the
    number of implicit functions defined.
    
    See Also:
    
    ImplicitFunction Texture BooleanTexture TransformTexture
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitTextureCoords, obj, update, **traits)
    
    flip_texture = tvtk_base.false_bool_trait(help=\
        """
        If enabled, this will flip the sense of inside and outside the
        implicit function (i.e., a rotation around the r-s-t=0.5 axis).
        """
    )
    def _flip_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipTexture,
                        self.flip_texture_)

    def _get_t_function(self):
        return wrap_vtk(self._vtk_obj.GetTFunction())
    def _set_t_function(self, arg):
        old_val = self._get_t_function()
        self._wrap_call(self._vtk_obj.SetTFunction,
                        deref_vtk(arg))
        self.trait_property_changed('t_function', old_val, arg)
    t_function = traits.Property(_get_t_function, _set_t_function, help=\
        """
        Specify an implicit function to compute the t texture coordinate.
        """
    )

    def _get_s_function(self):
        return wrap_vtk(self._vtk_obj.GetSFunction())
    def _set_s_function(self, arg):
        old_val = self._get_s_function()
        self._wrap_call(self._vtk_obj.SetSFunction,
                        deref_vtk(arg))
        self.trait_property_changed('s_function', old_val, arg)
    s_function = traits.Property(_get_s_function, _set_s_function, help=\
        """
        Specify an implicit function to compute the s texture coordinate.
        """
    )

    def _get_r_function(self):
        return wrap_vtk(self._vtk_obj.GetRFunction())
    def _set_r_function(self, arg):
        old_val = self._get_r_function()
        self._wrap_call(self._vtk_obj.SetRFunction,
                        deref_vtk(arg))
        self.trait_property_changed('r_function', old_val, arg)
    r_function = traits.Property(_get_r_function, _set_r_function, help=\
        """
        Specify an implicit function to compute the r texture coordinate.
        """
    )

    _updateable_traits_ = \
    (('flip_texture', 'GetFlipTexture'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'flip_texture', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitTextureCoords, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['flip_texture'], [], []),
            title='Edit ImplicitTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

