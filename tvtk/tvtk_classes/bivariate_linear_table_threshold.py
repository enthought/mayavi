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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class BivariateLinearTableThreshold(TableAlgorithm):
    """
    BivariateLinearTableThreshold - performs line-based thresholding
    
    Superclass: TableAlgorithm
    
    Class for filtering the rows of a two numeric columns of a Table. 
    The columns are treated as the two variables of a line.  This filter
    will then iterate through the rows of the table determining if X,Y
    values pairs are above/below/between/near one or more lines.
    
    The "between" mode checks to see if a row is contained within the
    convex hull of all of the specified lines.  The "near" mode checks if
    a row is within a distance threshold two one of the specified lines. 
    This class is used in conjunction with various plotting classes, so
    it is useful to rescale the X,Y axes to a particular range of values.
     Distance comparisons can be performed in the scaled space by setting
    the custom_ranges ivar and enabling use_normalized_distance.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBivariateLinearTableThreshold, obj, update, **traits)
    
    use_normalized_distance = tvtk_base.false_bool_trait(help=\
        """
        Renormalize the space of the data such that the X and Y axes are
        "square" over the specified column_ranges.  This essentially
        scales the data space so that column_ranges[_1]-_column_ranges[_0] =
        1.0 and column_ranges[_3]-_column_ranges[_2] = 1.0.  Used for scatter
        plot distance calculations.  Be sure to set distance_threshold
        accordingly, when used.
        """
    )
    def _use_normalized_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseNormalizedDistance,
                        self.use_normalized_distance_)

    linear_threshold_type = traits.Trait('near',
    tvtk_base.TraitRevPrefixMap({'near': 2, 'below': 1, 'above': 0, 'between': 3}), help=\
        """
        Set the threshold type.  Above: find all rows that are above the
        specified lines.  Below: find all rows that are below the
        specified lines.  Near: find all rows that are near the specified
        lines.  Between: find all rows that are between the specified
        lines.
        """
    )
    def _linear_threshold_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinearThresholdType,
                        self.linear_threshold_type_)

    column_ranges = traits.Array(shape=(2,), value=(1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _column_ranges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColumnRanges,
                        self.column_ranges)

    distance_threshold = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The Cartesian distance within which a point will pass the near
        threshold.
        """
    )
    def _distance_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceThreshold,
                        self.distance_threshold)

    inclusive = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Include the line in the threshold.  Essentially whether the
        threshold operation uses > versus >=.
        """
    )
    def _inclusive_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInclusive,
                        self.inclusive)

    def get_column_to_threshold(self, *args):
        """
        V.get_column_to_threshold(int, int, int)
        C++: void GetColumnToThreshold(IdType idx, IdType &column,
            IdType &component)
        Return the column number from the input table for the idx'th
        added column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnToThreshold, *args)
        return ret

    def _get_number_of_columns_to_threshold(self):
        return self._vtk_obj.GetNumberOfColumnsToThreshold()
    number_of_columns_to_threshold = traits.Property(_get_number_of_columns_to_threshold, help=\
        """
        Return how many columns have been added.  Hopefully 2.
        """
    )

    def get_selected_row_ids(self, *args):
        """
        V.get_selected_row_ids(int) -> IdTypeArray
        C++: IdTypeArray *GetSelectedRowIds(int selection=0)
        Get the output as a table of row ids.
        """
        ret = self._wrap_call(self._vtk_obj.GetSelectedRowIds, *args)
        return wrap_vtk(ret)

    def add_column_to_threshold(self, *args):
        """
        V.add_column_to_threshold(int, int)
        C++: void AddColumnToThreshold(IdType column,
            IdType component)
        Add a numeric column to the pair of columns to be thresholded. 
        Call twice.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumnToThreshold, *args)
        return ret

    def add_line_equation(self, *args):
        """
        V.add_line_equation(float, float, float)
        C++: void AddLineEquation(double a, double b, double c)
        Add a line for thresholding in implicit form (ax + by + c = 0)
        """
        ret = self._wrap_call(self._vtk_obj.AddLineEquation, *args)
        return ret

    def clear_columns_to_threshold(self):
        """
        V.clear_columns_to_threshold()
        C++: void ClearColumnsToThreshold()
        Reset the columns to be thresholded.
        """
        ret = self._vtk_obj.ClearColumnsToThreshold()
        return ret
        

    def clear_line_equations(self):
        """
        V.clear_line_equations()
        C++: void ClearLineEquations()
        Reset the list of line equations.
        """
        ret = self._vtk_obj.ClearLineEquations()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Reset the columns to threshold, column ranges, etc.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('inclusive',
    'GetInclusive'), ('column_ranges', 'GetColumnRanges'),
    ('linear_threshold_type', 'GetLinearThresholdType'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('distance_threshold', 'GetDistanceThreshold'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('use_normalized_distance', 'GetUseNormalizedDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_normalized_distance',
    'linear_threshold_type', 'column_ranges', 'distance_threshold',
    'inclusive', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BivariateLinearTableThreshold, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BivariateLinearTableThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_normalized_distance'], ['linear_threshold_type'],
            ['column_ranges', 'distance_threshold', 'inclusive']),
            title='Edit BivariateLinearTableThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BivariateLinearTableThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

