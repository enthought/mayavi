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


class UniformGrid(ImageData):
    """
    UniformGrid - image data with blanking
    
    Superclass: ImageData
    
    UniformGrid is a subclass of ImageData. In addition to all the
    image data functionality, it supports blanking.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUniformGrid, obj, update, **traits)
    
    def _get_point_visibility_array(self):
        return wrap_vtk(self._vtk_obj.GetPointVisibilityArray())
    def _set_point_visibility_array(self, arg):
        old_val = self._get_point_visibility_array()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetPointVisibilityArray,
                        my_arg[0])
        self.trait_property_changed('point_visibility_array', old_val, arg)
    point_visibility_array = traits.Property(_get_point_visibility_array, _set_point_visibility_array, help=\
        """
        Get the array that defines the blanking (visibility) of each
        point.
        """
    )

    def _get_cell_visibility_array(self):
        return wrap_vtk(self._vtk_obj.GetCellVisibilityArray())
    def _set_cell_visibility_array(self, arg):
        old_val = self._get_cell_visibility_array()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetCellVisibilityArray,
                        my_arg[0])
        self.trait_property_changed('cell_visibility_array', old_val, arg)
    cell_visibility_array = traits.Property(_get_cell_visibility_array, _set_cell_visibility_array, help=\
        """
        Get the array that defines the blanking (visibility) of each
        cell.
        """
    )

    def _get_cell_blanking(self):
        return self._vtk_obj.GetCellBlanking()
    cell_blanking = traits.Property(_get_cell_blanking, help=\
        """
        Returns 1 if there is any visibility constraint on the cells, 0
        otherwise.
        """
    )

    def _get_point_blanking(self):
        return self._vtk_obj.GetPointBlanking()
    point_blanking = traits.Property(_get_point_blanking, help=\
        """
        Returns 1 if there is any visibility constraint on the points, 0
        otherwise.
        """
    )

    def blank_cell(self, *args):
        """
        V.blank_cell(int)
        C++: virtual void BlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid. These methods should be called
        only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankCell, *args)
        return ret

    def blank_point(self, *args):
        """
        V.blank_point(int)
        C++: virtual void BlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankPoint, *args)
        return ret

    def is_cell_visible(self, *args):
        """
        V.is_cell_visible(int) ->
        C++: virtual unsigned char IsCellVisible(IdType cellId)
        Return non-zero value if specified cell is visible. These methods
        should be called only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsCellVisible, *args)
        return ret

    def is_point_visible(self, *args):
        """
        V.is_point_visible(int) ->
        C++: virtual unsigned char IsPointVisible(IdType ptId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointVisible, *args)
        return ret

    def new_image_data_copy(self):
        """
        V.new_image_data_copy() -> ImageData
        C++: virtual ImageData *NewImageDataCopy()"""
        ret = wrap_vtk(self._vtk_obj.NewImageDataCopy())
        return ret
        

    def un_blank_cell(self, *args):
        """
        V.un_blank_cell(int)
        C++: virtual void UnBlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid. These methods should be called
        only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankCell, *args)
        return ret

    def un_blank_point(self, *args):
        """
        V.un_blank_point(int)
        C++: virtual void UnBlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankPoint, *args)
        return ret

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
            return super(UniformGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
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
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

