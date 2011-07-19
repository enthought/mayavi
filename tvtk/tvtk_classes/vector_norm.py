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


class VectorNorm(DataSetAlgorithm):
    """
    VectorNorm - generate scalars from Euclidean norm of vectors
    
    Superclass: DataSetAlgorithm
    
    VectorNorm is a filter that generates scalar values by computing
    Euclidean norm of vector triplets. Scalars can be normalized 0<=s<=1
    if desired.
    
    Note that this filter operates on point or cell attribute data, or
    both.  By default, the filter operates on both point and cell data if
    vector point and cell data, respectively, are available from the
    input. Alternatively, you can choose to generate scalar norm values
    for just cell or point data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVectorNorm, obj, update, **traits)
    
    normalize = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to normalize scalar values.
        """
    )
    def _normalize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalize,
                        self.normalize_)

    attribute_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_cell_data': 2, 'use_point_data': 1}), help=\
        """
        Control how the filter works to generate scalar data from the
        input vector data. By default, (_attribute_mode_to_default) the
        filter will generate the scalar norm for point and cell data (if
        vector data present in the input). Alternatively, you can
        explicitly set the filter to generate point data
        (_attribute_mode_to_use_point_data) or cell data
        (_attribute_mode_to_use_cell_data).
        """
    )
    def _attribute_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeMode,
                        self.attribute_mode_)

    _updateable_traits_ = \
    (('normalize', 'GetNormalize'), ('attribute_mode',
    'GetAttributeMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'normalize',
    'release_data_flag', 'attribute_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VectorNorm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VectorNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['normalize'], ['attribute_mode'], []),
            title='Edit VectorNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VectorNorm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

