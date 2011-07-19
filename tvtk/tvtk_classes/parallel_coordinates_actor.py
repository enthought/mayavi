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

from tvtk.tvtk_classes.actor2d import Actor2D


class ParallelCoordinatesActor(Actor2D):
    """
    ParallelCoordinatesActor - create parallel coordinate display from
    input field
    
    Superclass: Actor2D
    
    ParallelCoordinatesActor generates a parallel coordinates plot
    from an input field (i.e., DataObject). Parallel coordinates
    represent N-dimensional data by using a set of N parallel axes (not
    orthogonal like the usual x-y-z Cartesian axes). Each N-dimensional
    point is plotted as a polyline, were each of the N components of the
    point lie on one of the N axes, and the components are connected by
    straight lines.
    
    To use this class, you must specify an input data object. You'll
    probably also want to specify the position of the plot be setting the
    Position and Position2 instance variables, which define a rectangle
    in which the plot lies. Another important parameter is the
    independent_variables ivar, which tells the instance how to interpret
    the field data (independent variables as the rows or columns of the
    field). There are also many other instance variables that control the
    look of the plot includes its title, attributes, number of ticks on
    the axes, etc.
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated to this actor.
    
    Caveats:
    
    Field data is not necessarily "rectangular" in shape. In these cases,
    some of the data may not be plotted.
    
    Field data can contain non-numeric arrays (i.e. arrays not subclasses
    of DataArray). Such arrays are skipped.
    
    The early implementation lacks many features that could be added in
    the future. This includes the ability to "brush" data (choose regions
    along an axis and highlight any points/lines passing through the
    region); efficiency is really bad; more control over the properties
    of the plot (separate properties for each axes,title,etc.; and using
    the labels found in the field to label each of the axes.
    
    See Also:
    
    AxisActor3D can be used to create axes in world coordinate space.
    Actor2D TextMapper PolyDataMapper2D ScalarBarActor
    Coordinate TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelCoordinatesActor, obj, update, **traits)
    
    independent_variables = traits.Trait('columns',
    tvtk_base.TraitRevPrefixMap({'rows': 1, 'columns': 0}), help=\
        """
        Specify whether to use the rows or columns as independent
        variables. If columns, then each row represents a separate point.
        If rows, then each column represents a separate point.
        """
    )
    def _independent_variables_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndependentVariables,
                        self.independent_variables_)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the axes.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the parallel coordinates plot.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property.
        """
    )

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Remove a dataset from the list of data to append.
        """
    )

    number_of_labels = traits.Trait(2, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show along each axis.
        This values is a suggestion: the number of labels may vary
        depending on the particulars of the data.
        """
    )
    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('layer_number',
    'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('title', 'GetTitle'), ('label_format',
    'GetLabelFormat'), ('number_of_labels', 'GetNumberOfLabels'),
    ('dragable', 'GetDragable'), ('debug', 'GetDebug'), ('height',
    'GetHeight'), ('position2', 'GetPosition2'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('independent_variables', 'GetIndependentVariables'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('width', 'GetWidth'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'independent_variables',
    'allocated_render_time', 'estimated_render_time', 'height',
    'label_format', 'layer_number', 'number_of_labels', 'position',
    'position2', 'render_time_multiplier', 'title', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelCoordinatesActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelCoordinatesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'],
            ['independent_variables'], ['allocated_render_time',
            'estimated_render_time', 'height', 'label_format', 'layer_number',
            'number_of_labels', 'position', 'position2', 'render_time_multiplier',
            'title', 'width']),
            title='Edit ParallelCoordinatesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelCoordinatesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

