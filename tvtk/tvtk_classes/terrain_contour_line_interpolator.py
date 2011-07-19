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

from tvtk.tvtk_classes.contour_line_interpolator import ContourLineInterpolator


class TerrainContourLineInterpolator(ContourLineInterpolator):
    """
    TerrainContourLineInterpolator - Contour interpolator for DEM data.
    
    Superclass: ContourLineInterpolator
    
    TerrainContourLineInterpolator interpolates nodes on height field
    data. The class is meant to be used in conjunciton with a
    ContourWidget, enabling you to draw paths on terrain data. The
    class internally uses a ProjectedTerrainPath. Users can set kind
    of interpolation desired between two node points by setting the modes
    of the this filter. For instance:
    
    contour_representation->_set_line_interpolator(interpolator);
    interpolator->_set_image_data( dem_data_file );
    interpolator->_get_projector()->_set_projection_mode_to_hug();
    interpolator->_set_height_offset(_25._0);
    
    You are required to set the image_data to this class as the
    height-field image.
    
    See Also:
    
    TerrainDataPointPlacer ProjectedTerrainPath
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTerrainContourLineInterpolator, obj, update, **traits)
    
    def _get_image_data(self):
        return wrap_vtk(self._vtk_obj.GetImageData())
    def _set_image_data(self, arg):
        old_val = self._get_image_data()
        self._wrap_call(self._vtk_obj.SetImageData,
                        deref_vtk(arg))
        self.trait_property_changed('image_data', old_val, arg)
    image_data = traits.Property(_get_image_data, _set_image_data, help=\
        """
        Set the height field data. The height field data is a 2d image.
        The scalars in the image represent the height field. This must be
        set.
        """
    )

    def _get_projector(self):
        return wrap_vtk(self._vtk_obj.GetProjector())
    projector = traits.Property(_get_projector, help=\
        """
        Get the ProjectedTerrainPath operator used to project the
        terrain onto the data. This operator has several modes, See the
        documentation of ProjectedTerrainPath. The default mode is to
        hug the terrain data at 0 height offset.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TerrainContourLineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TerrainContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TerrainContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TerrainContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

