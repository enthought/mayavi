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

from tvtk.tvtk_classes.object import Object


class HierarchicalGraphPipeline(Object):
    """
    HierarchicalGraphPipeline - helper class for rendering graphs
    superimposed on a tree.
    
    Superclass: Object
    
    HierarchicalGraphPipeline renders bundled edges that are meant to
    be viewed as an overlay on a tree. This class is not for general use,
    but is used in the internals of RenderedHierarchyRepresentation
    and RenderedTreeAreaRepresentation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHierarchicalGraphPipeline, obj, update, **traits)
    
    color_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        Whether to color the edges by an array.
        """
    )
    def _color_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorEdgesByArray,
                        self.color_edges_by_array_)

    label_visibility = tvtk_base.false_bool_trait(help=\
        """
        The edge label visibility.
        """
    )
    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    visibility = tvtk_base.true_bool_trait(help=\
        """
        The visibility of this graph.
        """
    )
    def _visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVisibility,
                        self.visibility_)

    label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The edge label array name.
        """
    )
    def _label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelArrayName,
                        self.label_array_name)

    hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use while hovering over an edge.
        """
    )
    def _hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHoverArrayName,
                        self.hover_array_name)

    color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The edge color array.
        """
    )
    def _color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorArrayName,
                        self.color_array_name)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        The edge label text property.
        """
    )

    bundling_strength = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        The bundling strength for the bundled edges.
        """
    )
    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    spline_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The spline mode to use in SplineGraphEdges.
        SplineGraphEdges::CUSTOM uses a CardinalSpline.
        SplineGraphEdges::BSPLINE uses a b-spline. The default is
        BSPLINE.
        """
    )
    def _spline_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplineType,
                        self.spline_type)

    def _get_actor(self):
        return wrap_vtk(self._vtk_obj.GetActor())
    actor = traits.Property(_get_actor, help=\
        """
        The actor associated with the hierarchical graph.
        """
    )

    def _get_label_actor(self):
        return wrap_vtk(self._vtk_obj.GetLabelActor())
    label_actor = traits.Property(_get_label_actor, help=\
        """
        The actor associated with the hierarchical graph.
        """
    )

    def apply_view_theme(self, *args):
        """
        V.apply_view_theme(ViewTheme)
        C++: virtual void ApplyViewTheme(ViewTheme *theme)
        Applies the view theme to this graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyViewTheme, *my_args)
        return ret

    def convert_selection(self, *args):
        """
        V.convert_selection(DataRepresentation, Selection)
            -> Selection
        C++: virtual Selection *ConvertSelection(
            DataRepresentation *rep, Selection *sel)
        Returns a new selection relevant to this graph based on an input
        selection and the view that this graph is contained in.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ConvertSelection, *my_args)
        return wrap_vtk(ret)

    def prepare_input_connections(self, *args):
        """
        V.prepare_input_connections(AlgorithmOutput, AlgorithmOutput,
            AlgorithmOutput)
        C++: virtual void PrepareInputConnections(
            AlgorithmOutput *graphConn, AlgorithmOutput *treeConn,
            AlgorithmOutput *annConn)
        Sets the input connections for this graph. graph_conn is the input
        graph connection. tree_conn is the input tree connection. ann_conn
        is the annotation link connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PrepareInputConnections, *my_args)
        return ret

    def register_progress(self, *args):
        """
        V.register_progress(RenderView)
        C++: void RegisterProgress(RenderView *view)
        Register progress with a view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegisterProgress, *my_args)
        return ret

    _updateable_traits_ = \
    (('color_edges_by_array', 'GetColorEdgesByArray'), ('spline_type',
    'GetSplineType'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label_visibility',
    'GetLabelVisibility'), ('hover_array_name', 'GetHoverArrayName'),
    ('debug', 'GetDebug'), ('label_array_name', 'GetLabelArrayName'),
    ('visibility', 'GetVisibility'), ('bundling_strength',
    'GetBundlingStrength'), ('reference_count', 'GetReferenceCount'),
    ('color_array_name', 'GetColorArrayName'))
    
    _full_traitnames_list_ = \
    (['color_edges_by_array', 'debug', 'global_warning_display',
    'label_visibility', 'visibility', 'bundling_strength',
    'color_array_name', 'hover_array_name', 'label_array_name',
    'spline_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HierarchicalGraphPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HierarchicalGraphPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_edges_by_array', 'label_visibility',
            'visibility'], [], ['bundling_strength', 'color_array_name',
            'hover_array_name', 'label_array_name', 'spline_type']),
            title='Edit HierarchicalGraphPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HierarchicalGraphPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

