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

from tvtk.tvtk_classes.label_hierarchy_algorithm import LabelHierarchyAlgorithm


class PointSetToLabelHierarchy(LabelHierarchyAlgorithm):
    """
    PointSetToLabelHierarchy - build a label hierarchy for a graph or
    point set.
    
    Superclass: LabelHierarchyAlgorithm
    
    Every point in the input Points object is taken to be an anchor
    point for a label. Statistics on the input points are used to
    subdivide an octree referencing the points until the points each
    octree node contains have a variance close to the node size and a
    limited population (< 100).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointSetToLabelHierarchy, obj, update, **traits)
    
    use_unicode_strings = tvtk_base.false_bool_trait(help=\
        """
        Whether to use unicode strings.
        """
    )
    def _use_unicode_strings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseUnicodeStrings,
                        self.use_unicode_strings_)

    label_array_name = traits.String(r"LabelText", enter_set=True, auto_set=False, help=\
        """
        Set/get the label array name.
        """
    )
    def _label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelArrayName,
                        self.label_array_name)

    orientation_array_name = traits.String(r"Orientation", enter_set=True, auto_set=False, help=\
        """
        Set/get the text orientation array name.
        """
    )
    def _orientation_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationArrayName,
                        self.orientation_array_name)

    size_array_name = traits.String(r"LabelSize", enter_set=True, auto_set=False, help=\
        """
        Set/get the priority array name.
        """
    )
    def _size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeArrayName,
                        self.size_array_name)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/get the text property assigned to the hierarchy.
        """
    )

    maximum_depth = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set/get the maximum tree depth in the output hierarchy.
        """
    )
    def _maximum_depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDepth,
                        self.maximum_depth)

    priority_array_name = traits.String(r"Priority", enter_set=True, auto_set=False, help=\
        """
        Set/get the priority array name.
        """
    )
    def _priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPriorityArrayName,
                        self.priority_array_name)

    bounded_size_array_name = traits.String(r"BoundedSize", enter_set=True, auto_set=False, help=\
        """
        Set/get the maximum text width (in world coordinates) array name.
        """
    )
    def _bounded_size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundedSizeArrayName,
                        self.bounded_size_array_name)

    icon_index_array_name = traits.String(r"IconIndex", enter_set=True, auto_set=False, help=\
        """
        Set/get the icon index array name.
        """
    )
    def _icon_index_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconIndexArrayName,
                        self.icon_index_array_name)

    target_label_count = traits.Int(32, enter_set=True, auto_set=False, help=\
        """
        Set/get the "ideal" number of labels to associate with each node
        in the output hierarchy.
        """
    )
    def _target_label_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetLabelCount,
                        self.target_label_count)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('icon_index_array_name', 'GetIconIndexArrayName'), ('progress_text',
    'GetProgressText'), ('label_array_name', 'GetLabelArrayName'),
    ('target_label_count', 'GetTargetLabelCount'),
    ('orientation_array_name', 'GetOrientationArrayName'), ('debug',
    'GetDebug'), ('size_array_name', 'GetSizeArrayName'),
    ('priority_array_name', 'GetPriorityArrayName'), ('release_data_flag',
    'GetReleaseDataFlag'), ('maximum_depth', 'GetMaximumDepth'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('bounded_size_array_name', 'GetBoundedSizeArrayName'),
    ('abort_execute', 'GetAbortExecute'), ('use_unicode_strings',
    'GetUseUnicodeStrings'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_unicode_strings', 'bounded_size_array_name',
    'icon_index_array_name', 'label_array_name', 'maximum_depth',
    'orientation_array_name', 'priority_array_name', 'progress_text',
    'size_array_name', 'target_label_count'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointSetToLabelHierarchy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointSetToLabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_unicode_strings'], [],
            ['bounded_size_array_name', 'icon_index_array_name',
            'label_array_name', 'maximum_depth', 'orientation_array_name',
            'priority_array_name', 'size_array_name', 'target_label_count']),
            title='Edit PointSetToLabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointSetToLabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

