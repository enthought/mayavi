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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ArcPlotter(PolyDataAlgorithm):
    """
    ArcPlotter - plot data along an arbitrary polyline
    
    Superclass: PolyDataAlgorithm
    
    ArcPlotter performs plotting of attribute data along polylines
    defined with an input PolyData data object. Any type of attribute
    data can be plotted including scalars, vectors, tensors, normals,
    texture coordinates, and field data. Either one or multiple data
    components can be plotted.
    
    To use this class you must specify an input data set that contains
    one or more polylines, and some attribute data including which
    component of the attribute data. (By default, this class processes
    the first component of scalar data.) You will also need to set an
    offset radius (the distance of the polyline to the median line of the
    plot), a width for the plot (the distance that the minimum and
    maximum plot values are mapped into), an possibly an offset (used to
    offset attribute data with multiple components).
    
    Normally the filter automatically computes normals for generating the
    offset arc plot. However, you can specify a default normal and use
    that instead.
    
    See Also:
    
    XYPlotActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArcPlotter, obj, update, **traits)
    
    use_default_normal = tvtk_base.false_bool_trait(help=\
        """
        Set a boolean to control whether to use default normals. By
        default, normals are automatically computed from the generating
        polyline and camera.
        """
    )
    def _use_default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDefaultNormal,
                        self.use_default_normal_)

    plot_mode = traits.Trait('plot_scalars',
    tvtk_base.TraitRevPrefixMap({'plot_tensors': 5, 'plot_t_coords': 4, 'plot_normals': 3, 'plot_field_data': 6, 'plot_vectors': 2, 'plot_scalars': 1}), help=\
        """
        Specify which data to plot: scalars, vectors, normals, texture
        coords, tensors, or field data. If the data has more than one
        component, use the method set_plot_component to control which
        component to plot.
        """
    )
    def _plot_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotMode,
                        self.plot_mode_)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Specify a camera used to orient the plot along the arc. If no
        camera is specified, then the orientation of the plot is
        arbitrary.
        """
    )

    default_normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormal,
                        self.default_normal)

    height = traits.Trait(0.5, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set the height of the plot. (The radius combined with the height
        define the location of the plot relative to the generating
        polyline.)
        """
    )
    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    plot_component = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the component number to plot if the data has more than
        one component. If the value of the plot component is == (-1),
        then all the components will be plotted.
        """
    )
    def _plot_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotComponent,
                        self.plot_component)

    radius = traits.Trait(0.5, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set the radius of the "median" value of the first plotted
        component.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    offset = traits.Trait(0.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Specify an offset that translates each subsequent plot (if there
        is more than one component plotted) from the defining arc (i.e.,
        polyline).
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    field_data_array = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the field data array to plot. This instance variable is
        only applicable if field data is plotted.
        """
    )
    def _field_data_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataArray,
                        self.field_data_array)

    _updateable_traits_ = \
    (('field_data_array', 'GetFieldDataArray'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('plot_mode', 'GetPlotMode'),
    ('default_normal', 'GetDefaultNormal'), ('progress_text',
    'GetProgressText'), ('height', 'GetHeight'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('radius', 'GetRadius'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('offset', 'GetOffset'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('plot_component', 'GetPlotComponent'), ('use_default_normal',
    'GetUseDefaultNormal'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_default_normal', 'plot_mode',
    'default_normal', 'field_data_array', 'height', 'offset',
    'plot_component', 'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArcPlotter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArcPlotter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_default_normal'], ['plot_mode'],
            ['default_normal', 'field_data_array', 'height', 'offset',
            'plot_component', 'radius']),
            title='Edit ArcPlotter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArcPlotter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

