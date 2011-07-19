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

from tvtk.tvtk_classes.mapper2d import Mapper2D


class LabeledDataMapper(Mapper2D):
    """
    LabeledDataMapper - draw text labels at dataset points
    
    Superclass: Mapper2D
    
    LabeledDataMapper is a mapper that renders text at dataset points.
    Various items can be labeled including point ids, scalars, vectors,
    normals, texture coordinates, tensors, and field data components.
    
    The format with which the label is drawn is specified using a printf
    style format string. The font attributes of the text can be set
    through the TextProperty associated to this mapper.
    
    By default, all the components of multi-component data such as
    vectors, normals, texture coordinates, tensors, and multi-component
    scalars are labeled. However, you can specify a single component if
    you prefer. (Note: the label format specifies the format to use for a
    single component. The label is creating by looping over all
    components and using the label format to render each component.)
    
    Caveats:
    
    Use this filter in combination with SelectVisiblePoints if you
    want to label only points that are visible. If you want to label
    cells rather than points, use the filter CellCenters to generate
    points at the center of the cells. Also, you can use the class
    IdFilter to generate ids as scalars or field data, which can then
    be labeled.
    
    See Also:
    
    Mapper2D Actor2D TextMapper TextProperty
    SelectVisiblePoints IdFilter CellCenters
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabeledDataMapper, obj, update, **traits)
    
    label_mode = traits.Trait('label_ids',
    tvtk_base.TraitRevPrefixMap({'label_scalars': 1, 'label_tensors': 5, 'label_normals': 3, 'label_vectors': 2, 'label_field_data': 6, 'label_ids': 0, 'label_t_coords': 4}), help=\
        """
        Specify which data to plot: IDs, scalars, vectors, normals,
        texture coords, tensors, or field data. If the data has more than
        one component, use the method set_labeled_component to control
        which components to plot. The default is VTK_LABEL_IDS.
        """
    )
    def _label_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelMode,
                        self.label_mode_)

    label_format = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the format with which to print the labels.  This should
        be a printf-style format string.
        
        By default, the mapper will try to print each component of the
        tuple using a sane format: %d for integers, %f for floats, %g for
        doubles, %ld for longs, et cetera.  If you need a different
        format, set it here.  You can do things like limit the number of
        significant digits, add prefixes/suffixes, basically anything
        that printf can do.  If you only want to print one component of a
        vector, see the ivar labeled_component.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    coordinate_system = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
    )
    def _coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordinateSystem,
                        self.coordinate_system)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        The transform to apply to the labels before mapping to 2d.
        """
    )

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the text property. If an integer argument is provided,
        you may provide different text properties for different label
        types. The type is determined by an optional type input array.
        """
    )

    field_data_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the field data array to label.  This instance
        variable is only applicable if field data is labeled.  This will
        override field_data_array when set.
        """
    )
    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Use get_input_data_object() to get the input data object for
        composite datasets.
        """
    )

    field_data_array = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the field data array to label. This instance variable is
        only applicable if field data is labeled.  This will clear
        field_data_name when set.
        """
    )
    def _field_data_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataArray,
                        self.field_data_array)

    labeled_component = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the component number to label if the data to print has
        more than one component. For example, all the components of
        scalars, vectors, normals, etc. are labeled by default
        (_labeled_component=(-_1)). However, if this ivar is nonnegative,
        then only the one component specified is labeled.
        """
    )
    def _labeled_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabeledComponent,
                        self.labeled_component)

    def coordinate_system_display(self):
        """
        V.coordinate_system_display()
        C++: void CoordinateSystemDisplay()
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
        ret = self._vtk_obj.CoordinateSystemDisplay()
        return ret
        

    def coordinate_system_world(self):
        """
        V.coordinate_system_world()
        C++: void CoordinateSystemWorld()
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
        ret = self._vtk_obj.CoordinateSystemWorld()
        return ret
        

    _updateable_traits_ = \
    (('field_data_array', 'GetFieldDataArray'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('coordinate_system',
    'GetCoordinateSystem'), ('label_format', 'GetLabelFormat'),
    ('progress_text', 'GetProgressText'), ('label_mode', 'GetLabelMode'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('labeled_component', 'GetLabeledComponent'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('field_data_name', 'GetFieldDataName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'label_mode', 'coordinate_system',
    'field_data_array', 'field_data_name', 'label_format',
    'labeled_component', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabeledDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabeledDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['label_mode'], ['coordinate_system',
            'field_data_array', 'field_data_name', 'label_format',
            'labeled_component']),
            title='Edit LabeledDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabeledDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

