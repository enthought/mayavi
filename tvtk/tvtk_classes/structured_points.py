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

from tvtk.tvtk_classes.image_data import ImageData


class StructuredPoints(ImageData):
    """
    StructuredPoints - A subclass of image_data.
    
    Superclass: ImageData
    
    structured_points is a subclass of image_data that requires the data
    extent to exactly match the update extent. Normall image data allows
    that the data extent may be larger than the update extent.
    structured_points also defines the origin differently that
    ImageData. For structured points the origin is the location of
    first point. Whereas images define the origin as the location of
    point 0, 0, 0. Image Origin is stored in ivar, and structured points
    have special methods for setting/getting the origin/extents.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredPoints, obj, update, **traits)
    
    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('dimensions', 'GetDimensions'),
    ('whole_extent', 'GetWholeExtent'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('spacing', 'GetSpacing'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('update_piece', 'GetUpdatePiece'), ('extent',
    'GetExtent'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('scalar_type',
    'GetScalarType'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('request_exact_extent',
    'GetRequestExactExtent'), ('whole_bounding_box',
    'GetWholeBoundingBox'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'scalar_type',
    'dimensions', 'extent', 'maximum_number_of_pieces',
    'number_of_scalar_components', 'origin', 'spacing', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            ['scalar_type'], ['dimensions', 'extent', 'maximum_number_of_pieces',
            'number_of_scalar_components', 'origin', 'spacing', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit StructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

