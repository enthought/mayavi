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

from tvtk.tvtk_classes.painter import Painter


class ScalarsToColorsPainter(Painter):
    """
    ScalarsToColorsPainter - painter that converts scalars to 
    
    Superclass: Painter
    
    This is a painter that converts scalars to colors. It enable/disables
    coloring state depending on the scalar_mode. This painter is composite
    dataset enabled.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarsToColorsPainter, obj, update, **traits)
    
    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify a lookup table for the mapper to use.
        """
    )

    def get_premultiply_colors_with_alpha(self, *args):
        """
        V.get_premultiply_colors_with_alpha(Actor) -> int
        C++: virtual int GetPremultiplyColorsWithAlpha(Actor *actor)
        For alpha blending, we sometime premultiply the colors with alpha
        and change the alpha blending function. This call returns whether
        we are premultiplying or using the default blending function.
        Currently this checks if the actor has a texture, if not it
        returns true. TODO: It is possible to make this decision
        dependent on key passed down from a painter upstream that makes a
        more informed decision for alpha blending depending on extensions
        available, for example.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPremultiplyColorsWithAlpha, *my_args)
        return ret

    def _get_texture_size_limit(self):
        return self._vtk_obj.GetTextureSizeLimit()
    texture_size_limit = traits.Property(_get_texture_size_limit, help=\
        """
        Return the texture size limit. Subclasses need to override this
        to return the actual correct texture size limit.  Here it is
        hardcoded to 1024.
        """
    )

    def ARRAY_ACCESS_MODE(self):
        """
        V.array__access__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_ACCESS_MODE()
        Controls what data array is used to generate colors.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_ACCESS_MODE())
        return ret
        

    def ARRAY_COMPONENT(self):
        """
        V.array__component() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_COMPONENT()
        Controls what data array is used to generate colors.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_COMPONENT())
        return ret
        

    def ARRAY_ID(self):
        """
        V.array__id() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_ID()
        Controls what data array is used to generate colors.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_ID())
        return ret
        

    def ARRAY_NAME(self):
        """
        V.array__name() -> InformationStringKey
        C++: static InformationStringKey *ARRAY_NAME()
        Controls what data array is used to generate colors.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_NAME())
        return ret
        

    def COLOR_MODE(self):
        """
        V.color__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *COLOR_MODE()
        Control how the scalar data is mapped to colors. By default
        (_color_mode_to_default), unsigned char scalars are treated as
        colors, and NOT mapped through the lookup table, while everything
        else is. Setting color_mode_to_map_scalars means that all scalar data
        will be mapped through the lookup table.
        """
        ret = wrap_vtk(self._vtk_obj.COLOR_MODE())
        return ret
        

    def create_default_lookup_table(self):
        """
        V.create_default_lookup_table()
        C++: virtual void CreateDefaultLookupTable()
        Create default lookup table. Generally used to create one when
        none is available with the scalar data.
        """
        ret = self._vtk_obj.CreateDefaultLookupTable()
        return ret
        

    def INTERPOLATE_SCALARS_BEFORE_MAPPING(self):
        """
        V.interpolate__scalars__before__mapping() -> InformationIntegerKey
        C++: static InformationIntegerKey *INTERPOLATE_SCALARS_BEFORE_MAPPING(
            )
        By default, vertex color is used to map colors to a surface.
        Colors are interpolated after being mapped. This option avoids
        color interpolation by using a one dimensional texture map for
        the colors.
        """
        ret = wrap_vtk(self._vtk_obj.INTERPOLATE_SCALARS_BEFORE_MAPPING())
        return ret
        

    def LOOKUP_TABLE(self):
        """
        V.lookup__table() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *LOOKUP_TABLE()
        Specify a lookup table for the mapper to use.
        """
        ret = wrap_vtk(self._vtk_obj.LOOKUP_TABLE())
        return ret
        

    def SCALAR_MATERIAL_MODE(self):
        """
        V.scalar__material__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *SCALAR_MATERIAL_MODE()
        Set the light-model color mode.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_MATERIAL_MODE())
        return ret
        

    def SCALAR_MODE(self):
        """
        V.scalar__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *SCALAR_MODE()
        Control how the painter works with scalar point data and cell
        attribute data. See Mapper::ScalarMode for more details.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_MODE())
        return ret
        

    def SCALAR_RANGE(self):
        """
        V.scalar__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SCALAR_RANGE()
        Specify range in terms of scalar minimum and maximum (smin,smax).
        These values are used to map scalars into lookup table. Has no
        effect when use_lookup_table_scalar_range is true.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_RANGE())
        return ret
        

    def SCALAR_VISIBILITY(self):
        """
        V.scalar__visibility() -> InformationIntegerKey
        C++: static InformationIntegerKey *SCALAR_VISIBILITY()
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_VISIBILITY())
        return ret
        

    def USE_LOOKUP_TABLE_SCALAR_RANGE(self):
        """
        V.use__lookup__table__scalar__range() -> InformationIntegerKey
        C++: static InformationIntegerKey *USE_LOOKUP_TABLE_SCALAR_RANGE(
            )
        Control whether the mapper sets the lookuptable range based on
        its own scalar_range, or whether it will use the lookup_table
        scalar_range regardless of it's own setting. By default the Mapper
        is allowed to set the lookup_table range, but users who are
        sharing lookup_tables between mappers/actors will probably wish to
        force the mapper to use the lookup_table unchanged.
        """
        ret = wrap_vtk(self._vtk_obj.USE_LOOKUP_TABLE_SCALAR_RANGE())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarsToColorsPainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarsToColorsPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ScalarsToColorsPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarsToColorsPainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

