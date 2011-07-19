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

from tvtk.tvtk_classes.composite_data_set import CompositeDataSet


class HierarchicalBoxDataSet(CompositeDataSet):
    """
    HierarchicalBoxDataSet - hierarchical dataset of UniformGrids
    
    Superclass: CompositeDataSet
    
    HierarchicalBoxDataSet is a concrete implementation of
    CompositeDataSet. The dataset type is restricted to
    UniformGrid. Each dataset has an associated AMRBox that
    represents it's region (similar to extent) in space.
    
    Warning:
    
    To compute the cell_id of a cell within a UniformGrid with
    AMRBox=box, you should not use UniformGrid::ComputeCellId( {x,y,z}
    ) but instead use the following pseudo code: for (int i=0; i<3; i++)
      {
      cell_dims[i] = box._hi_corner[i] - box._lo_corner[i] + 1;
      } IdType cell_id =
      (z-box._lo_corner[_2])*cell_dims[_0]*cell_dims[_1] +
      (y-box._lo_corner[_1])*cell_dims[_0] +
      (x-box._lo_corner[_0]);
    
    NOTE AMRBox is used to compute cell visibility, therefor it should
    be dimensioned according to the visible region.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHierarchicalBoxDataSet, obj, update, **traits)
    
    def get_refinement_ratio(self, *args):
        """
        V.get_refinement_ratio(int) -> int
        C++: int GetRefinementRatio(unsigned int level)
        V.get_refinement_ratio(CompositeDataIterator) -> int
        C++: int GetRefinementRatio(CompositeDataIterator *iter)
        Returns the refinement of a given level.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetRefinementRatio, *my_args)
        return ret

    def set_refinement_ratio(self, *args):
        """
        V.set_refinement_ratio(int, int)
        C++: void SetRefinementRatio(unsigned int level, int refRatio)
        Sets the refinement of a given level. The spacing at level
        level+1 is defined as spacing(level+1) =
        spacing(level)/ref_ratio(level). Note that currently, this is not
        enforced by this class however some algorithms might not function
        properly if the spacing in the blocks (vtk_uniform_grid) does not
        match the one described by the refinement ratio.
        """
        ret = self._wrap_call(self._vtk_obj.SetRefinementRatio, *args)
        return ret

    def get_number_of_data_sets(self, *args):
        """
        V.get_number_of_data_sets(int) -> int
        C++: unsigned int GetNumberOfDataSets(unsigned int level)
        Returns the number of data sets available at any level.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfDataSets, *args)
        return ret

    def set_number_of_data_sets(self, *args):
        """
        V.set_number_of_data_sets(int, int)
        C++: void SetNumberOfDataSets(unsigned int level,
            unsigned int numdatasets)
        Set the number of data set at a given level.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfDataSets, *args)
        return ret

    number_of_levels = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of refinement levels. This call might cause
        allocation if the new number of levels is larger than the current
        one.
        """
    )
    def _number_of_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLevels,
                        self.number_of_levels)

    def get_data_set(self, *args):
        """
        V.get_data_set(CompositeDataIterator) -> DataObject
        C++: virtual DataObject *GetDataSet(
            CompositeDataIterator *iter)
        Unhiding superclass method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *my_args)
        return wrap_vtk(ret)

    def set_data_set(self, *args):
        """
        V.set_data_set(CompositeDataIterator, DataObject)
        C++: virtual void SetDataSet(CompositeDataIterator *iter,
            DataObject *dataObj)
        V.set_data_set(int, int, [int, int, int], [int, int, int],
            UniformGrid)
        C++: void SetDataSet(unsigned int level, unsigned int id,
            int LoCorner[3], int HiCorner[3], UniformGrid *dataSet)
        Sets the data set at the location pointed by the iterator. The
        iterator does not need to be iterating over this dataset itself.
        It can be any composite datasite with similar structure (achieve
        by using copy_structure). Un-hiding superclass overload.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    def get_flat_index(self, *args):
        """
        V.get_flat_index(int, int) -> int
        C++: unsigned int GetFlatIndex(unsigned int level,
            unsigned int index)
        Given the level and dataset index, returns the flat index
        provided level and dataset index are valid.
        """
        ret = self._wrap_call(self._vtk_obj.GetFlatIndex, *args)
        return ret

    def get_level_meta_data(self, *args):
        """
        V.get_level_meta_data(int) -> Information
        C++: Information *GetLevelMetaData(unsigned int level)
        Get meta-data associated with a level. This may allocate a new
        Information object if none is already present. Use
        has_level_meta_data to avoid unnecessary allocations.
        """
        ret = self._wrap_call(self._vtk_obj.GetLevelMetaData, *args)
        return wrap_vtk(ret)

    def BOX(self):
        """
        V.box() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *BOX()"""
        ret = wrap_vtk(self._vtk_obj.BOX())
        return ret
        

    def BOX_DIMENSIONALITY(self):
        """
        V.box__dimensionality() -> InformationIntegerKey
        C++: static InformationIntegerKey *BOX_DIMENSIONALITY()"""
        ret = wrap_vtk(self._vtk_obj.BOX_DIMENSIONALITY())
        return ret
        

    def generate_visibility_arrays(self):
        """
        V.generate_visibility_arrays()
        C++: void GenerateVisibilityArrays()
        Blank lower level cells if they are overlapped by higher level
        ones.
        """
        ret = self._vtk_obj.GenerateVisibilityArrays()
        return ret
        

    def has_level_meta_data(self, *args):
        """
        V.has_level_meta_data(int) -> int
        C++: int HasLevelMetaData(unsigned int level)
        Returns if meta-data exists for a given level.
        """
        ret = self._wrap_call(self._vtk_obj.HasLevelMetaData, *args)
        return ret

    def NUMBER_OF_BLANKED_POINTS(self):
        """
        V.number__of__blanked__points() -> InformationIdTypeKey
        C++: static InformationIdTypeKey *NUMBER_OF_BLANKED_POINTS()"""
        ret = wrap_vtk(self._vtk_obj.NUMBER_OF_BLANKED_POINTS())
        return ret
        

    def REFINEMENT_RATIO(self):
        """
        V.refinement__ratio() -> InformationIntegerKey
        C++: static InformationIntegerKey *REFINEMENT_RATIO()"""
        ret = wrap_vtk(self._vtk_obj.REFINEMENT_RATIO())
        return ret
        

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('number_of_levels',
    'GetNumberOfLevels'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('update_piece', 'GetUpdatePiece'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'number_of_levels', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HierarchicalBoxDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HierarchicalBoxDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'number_of_levels', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit HierarchicalBoxDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HierarchicalBoxDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

