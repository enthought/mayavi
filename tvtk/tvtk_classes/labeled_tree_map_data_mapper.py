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

from tvtk.tvtk_classes.labeled_data_mapper import LabeledDataMapper


class LabeledTreeMapDataMapper(LabeledDataMapper):
    """
    LabeledTreeMapDataMapper - draw text labels on a tree map
    
    Superclass: LabeledDataMapper
    
    LabeledTreeMapDataMapper is a mapper that renders text on a tree
    map. A tree map is a Tree with an associated 4-tuple array used
    for storing the boundary rectangle for each vertex in the tree. The
    user must specify the array name used for storing the rectangles.
    
    The mapper iterates through the tree and attempts and renders a label
    inside the vertex's rectangle as long as the following conditions
    hold:
    1. The vertex level is within the range of levels specified for
       labeling.
    2. The label can fully fit inside its box.
    3. The label does not overlap an ancestor's label.
    
    See Also:
    
    LabeledDataMapper
    
    Thanks:
    
    Thanks to Patricia Crossno, Ken Moreland, Andrew Wilson and Brian
    Wylie from Sandia National Laboratories for their help in developing
    this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabeledTreeMapDataMapper, obj, update, **traits)
    
    clip_text_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Indicates if the label can be displayed clipped by the Window
        mode = 0 - ok to clip labels 1 - auto center labels w/r to the
        area of the vertex's clipped region
        """
    )
    def _clip_text_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipTextMode,
                        self.clip_text_mode)

    dynamic_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Indicates at which level labeling should be dynamic
        """
    )
    def _dynamic_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDynamicLevel,
                        self.dynamic_level)

    def get_level_range(self, *args):
        """
        V.get_level_range([int, int])
        C++: void GetLevelRange(int range[2])
        The range of levels to attempt to label. The level of a vertex is
        the length of the path to the root (the root has level 0).
        """
        ret = self._wrap_call(self._vtk_obj.GetLevelRange, *args)
        return ret

    def set_level_range(self, *args):
        """
        V.set_level_range(int, int)
        C++: void SetLevelRange(int startLevel, int endLevel)
        The range of levels to attempt to label. The level of a vertex is
        the length of the path to the root (the root has level 0).
        """
        ret = self._wrap_call(self._vtk_obj.SetLevelRange, *args)
        return ret

    def get_font_size_range(self, *args):
        """
        V.get_font_size_range([int, int, int])
        C++: void GetFontSizeRange(int range[3])
        The range of font sizes to use when rendering the labels.
        """
        ret = self._wrap_call(self._vtk_obj.GetFontSizeRange, *args)
        return ret

    def set_font_size_range(self, *args):
        """
        V.set_font_size_range(int, int, int)
        C++: void SetFontSizeRange(int maxSize, int minSize, int delta=4)
        The range of font sizes to use when rendering the labels.
        """
        ret = self._wrap_call(self._vtk_obj.SetFontSizeRange, *args)
        return ret

    child_motion = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Indicates if the label can be moved by its ancestors
        """
    )
    def _child_motion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChildMotion,
                        self.child_motion)

    def _get_input_tree(self):
        return wrap_vtk(self._vtk_obj.GetInputTree())
    input_tree = traits.Property(_get_input_tree, help=\
        """
        The input to this filter.
        """
    )

    def set_rectangles_array_name(self, *args):
        """
        V.set_rectangles_array_name(string)
        C++: virtual void SetRectanglesArrayName(const char *name)
        The name of the 4-tuple array used for
        """
        ret = self._wrap_call(self._vtk_obj.SetRectanglesArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('field_data_array', 'GetFieldDataArray'), ('dynamic_level',
    'GetDynamicLevel'), ('coordinate_system', 'GetCoordinateSystem'),
    ('label_format', 'GetLabelFormat'), ('clip_text_mode',
    'GetClipTextMode'), ('progress_text', 'GetProgressText'),
    ('label_mode', 'GetLabelMode'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('labeled_component',
    'GetLabeledComponent'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('field_data_name', 'GetFieldDataName'), ('child_motion',
    'GetChildMotion'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'label_mode', 'child_motion', 'clip_text_mode',
    'coordinate_system', 'dynamic_level', 'field_data_array',
    'field_data_name', 'label_format', 'labeled_component',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabeledTreeMapDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabeledTreeMapDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['label_mode'], ['child_motion', 'clip_text_mode',
            'coordinate_system', 'dynamic_level', 'field_data_array',
            'field_data_name', 'label_format', 'labeled_component']),
            title='Edit LabeledTreeMapDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabeledTreeMapDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

