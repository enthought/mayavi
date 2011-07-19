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


class WeightedTransformFilter(PointSetAlgorithm):
    """
    WeightedTransformFilter - transform based on per-point or per-cell
    weighting functions.
    
    Superclass: PointSetAlgorithm
    
    Caveats:
    
    Weighted combination of normals and vectors are probably not
    appropriate in many cases.  Surface normals are treated somewhat
    specially, but in many cases you may need to regenerate the surface
    normals.
    
    Cell data can only be transformed if all transforms are linear.
    
    See Also:
    
    AbstractTransform LinearTransform TransformPolyDataFilter
    Actor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWeightedTransformFilter, obj, update, **traits)
    
    add_input_values = tvtk_base.false_bool_trait(help=\
        """
        If add_input_values is true, the output values of this filter will
        be offset from the input values.  The effect is exactly
        equivalent to having an identity transform of weight 1 added into
        each output point.
        """
    )
    def _add_input_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAddInputValues,
                        self.add_input_values_)

    cell_data_transform_index_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _cell_data_transform_index_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellDataTransformIndexArray,
                        self.cell_data_transform_index_array)

    def get_transform(self, *args):
        """
        V.get_transform(int) -> AbstractTransform
        C++: virtual AbstractTransform *GetTransform(int num)
        Set or Get one of the filter's transforms. The transform number
        must be less than the number of transforms allocated for the
        object.  Setting a transform slot to NULL is equivalent to
        assigning an overriding weight of zero to that filter slot.
        """
        ret = self._wrap_call(self._vtk_obj.GetTransform, *args)
        return wrap_vtk(ret)

    def set_transform(self, *args):
        """
        V.set_transform(AbstractTransform, int)
        C++: virtual void SetTransform(AbstractTransform *transform,
            int num)
        Set or Get one of the filter's transforms. The transform number
        must be less than the number of transforms allocated for the
        object.  Setting a transform slot to NULL is equivalent to
        assigning an overriding weight of zero to that filter slot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTransform, *my_args)
        return ret

    cell_data_weight_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The cell_data_weight_array is analogous to the weight_array, except
        for cell_data.  The array is searched for first in the cell_data
        field_data, then in the input's field_data.  The data array must
        have a tuple for each cell.  This array is used to transform only
        normals and vectors.
        """
    )
    def _cell_data_weight_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellDataWeightArray,
                        self.cell_data_weight_array)

    number_of_transforms = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of transforms for the filter.  References to
        non-existent filter numbers in the data array is equivalent to a
        weight of zero (i.e., no contribution of that filter or weight). 
        The maximum number of transforms is limited to 65536 if transform
        index arrays are used.
        """
    )
    def _number_of_transforms_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTransforms,
                        self.number_of_transforms)

    transform_index_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        transform_index_array is the string name of the data_array in the
        input's field_data that holds the indices for the transforms for
        each point. These indices are used to select which transforms
        each weight of the data_array refers.  If the transform_index_array
        is not specified, the weights of each point are assumed to map
        directly to a transform. This data_array must be of type
        unsigned_short, which effectively limits the number of transforms
        to 65536 if a transform index array is used.
        
        The filter will first look for the array in the input's point_data
        field_data.  If the array isn't there, the filter looks in the
        input's field_data.  The transform_index_array can have tuples of
        any length, but must have a tuple for every point in the input
        data set. This array transforms points, normals, and vectors.
        """
    )
    def _transform_index_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransformIndexArray,
                        self.transform_index_array)

    weight_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        weight_array is the string name of the data_array in the input's
        field_data that holds the weighting coefficients for each point.
        The filter will first look for the array in the input's point_data
        field_data.  If the array isn't there, the filter looks in the
        input's field_data.  The weight_array can have tuples of any
        length, but must have a tuple for every point in the input data
        set. This array transforms points, normals, and vectors.
        """
    )
    def _weight_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWeightArray,
                        self.weight_array)

    _updateable_traits_ = \
    (('cell_data_weight_array', 'GetCellDataWeightArray'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('number_of_transforms', 'GetNumberOfTransforms'),
    ('debug', 'GetDebug'), ('cell_data_transform_index_array',
    'GetCellDataTransformIndexArray'), ('abort_execute',
    'GetAbortExecute'), ('weight_array', 'GetWeightArray'),
    ('add_input_values', 'GetAddInputValues'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('transform_index_array', 'GetTransformIndexArray'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'add_input_values', 'debug',
    'global_warning_display', 'release_data_flag',
    'cell_data_transform_index_array', 'cell_data_weight_array',
    'number_of_transforms', 'progress_text', 'transform_index_array',
    'weight_array'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WeightedTransformFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WeightedTransformFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['add_input_values'], [],
            ['cell_data_transform_index_array', 'cell_data_weight_array',
            'number_of_transforms', 'transform_index_array', 'weight_array']),
            title='Edit WeightedTransformFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WeightedTransformFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

