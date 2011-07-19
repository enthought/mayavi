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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class DataRepresentation(PassInputTypeAlgorithm):
    """
    DataRepresentation - The superclass for all representations
    
    Superclass: PassInputTypeAlgorithm
    
    DataRepresentation the superclass for representations of data
    objects. This class itself may be instantiated and used as a
    representation that simply holds a connection to a pipeline.
    
    If there are multiple representations present in a view, you should
    use a subclass of DataRepresentation.  The representation is
    responsible for taking the input pipeline connection and converting
    it to an object usable by a view.  In the most common case, the
    representation will contain the pipeline necessary to convert a data
    object into an actor or set of actors.
    
    The representation has a concept of a selection.  If the user
    performs a selection operation on the view, the view forwards this on
    to its representations.  The representation is responsible for
    displaying that selection in an appropriate way.
    
    Representation selections may also be linked.  The representation
    shares the selection by converting it into a view-independent format,
    then setting the selection on its AnnotationLink.  Other
    representations sharing the same selection link instance will get the
    same selection from the selection link when the view is updated.  The
    application is responsible for linking representations as appropriate
    by setting the same AnnotationLink on each linked representation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataRepresentation, obj, update, **traits)
    
    selectable = tvtk_base.true_bool_trait(help=\
        """
        Whether this representation is able to handle a selection.
        Default is true.
        """
    )
    def _selectable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectable,
                        self.selectable_)

    def _get_selection_array_names(self):
        return wrap_vtk(self._vtk_obj.GetSelectionArrayNames())
    def _set_selection_array_names(self, arg):
        old_val = self._get_selection_array_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetSelectionArrayNames,
                        my_arg[0])
        self.trait_property_changed('selection_array_names', old_val, arg)
    selection_array_names = traits.Property(_get_selection_array_names, _set_selection_array_names, help=\
        """
        If a VALUES selection, the arrays used to produce a selection.
        """
    )

    def _get_annotation_link(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLink())
    def _set_annotation_link(self, arg):
        old_val = self._get_annotation_link()
        self._wrap_call(self._vtk_obj.SetAnnotationLink,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_link', old_val, arg)
    annotation_link = traits.Property(_get_annotation_link, _set_annotation_link, help=\
        """
        The annotation link for this representation. To link annotations,
        set the same AnnotationLink object in multiple
        representations.
        """
    )

    selection_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        If a VALUES selection, the array used to produce a selection.
        """
    )
    def _selection_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionArrayName,
                        self.selection_array_name)

    selection_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set the selection type produced by this view. This should be one
        of the content type constants defined in SelectionNode.h.
        Common values are SelectionNode::INDICES
        SelectionNode::PEDIGREEIDS SelectionNode::VALUES
        """
    )
    def _selection_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionType,
                        self.selection_type)

    def _get_internal_annotation_output_port(self):
        return wrap_vtk(self._vtk_obj.GetInternalAnnotationOutputPort())
    internal_annotation_output_port = traits.Property(_get_internal_annotation_output_port, help=\
        """
        The output port that contains the annotations whose selections
        are localized for a particular input data object. This should be
        used when connecting the internal pipelines.
        """
    )

    def _get_internal_output_port(self):
        return wrap_vtk(self._vtk_obj.GetInternalOutputPort())
    internal_output_port = traits.Property(_get_internal_output_port, help=\
        """
        Retrieves an output port for the input data object at the
        specified port and connection index. This may be connected to the
        representation's internal pipeline.
        """
    )

    def _get_internal_selection_output_port(self):
        return wrap_vtk(self._vtk_obj.GetInternalSelectionOutputPort())
    internal_selection_output_port = traits.Property(_get_internal_selection_output_port, help=\
        """
        The output port that contains the selection associated with the
        current annotation (normally the interactive selection). This
        should be used when connecting the internal pipelines.
        """
    )

    def annotate(self, *args):
        """
        V.annotate(View, AnnotationLayers)
        C++: void Annotate(View *view,
            AnnotationLayers *annotations)
        V.annotate(View, AnnotationLayers, bool)
        C++: void Annotate(View *view,
            AnnotationLayers *annotations, bool extend)
        Analagous to Select(). The view calls this method when it needs
        to change the underlying annotations (some views might perform
        the creation of annotations). The representation takes the
        annotations and converts them into a selection on its data by
        calling convert_annotations, then calls update_annotations with the
        converted selection. Subclasses should not overrride this method,
        but should instead override convert_selection. The optional third
        argument specifies whether the selection should be added to the
        previous selection on this representation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Annotate, *my_args)
        return ret

    def apply_view_theme(self, *args):
        """
        V.apply_view_theme(ViewTheme)
        C++: virtual void ApplyViewTheme(ViewTheme *theme)
        Apply a theme to this representation. Subclasses should override
        this method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyViewTheme, *my_args)
        return ret

    def convert_selection(self, *args):
        """
        V.convert_selection(View, Selection) -> Selection
        C++: virtual Selection *ConvertSelection(View *view,
            Selection *selection)
        Convert the selection to a type appropriate for sharing with
        other representations through AnnotationLink, possibly using
        the view. For the superclass, we just return the same selection.
        Subclasses may do something more fancy, like convert the
        selection from a frustrum to a list of pedigree ids.  If the
        selection cannot be applied to this representation, return NULL.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ConvertSelection, *my_args)
        return wrap_vtk(ret)

    def select(self, *args):
        """
        V.select(View, Selection)
        C++: void Select(View *view, Selection *selection)
        V.select(View, Selection, bool)
        C++: void Select(View *view, Selection *selection,
            bool extend)
        The view calls this method when a selection occurs. The
        representation takes this selection and converts it into a
        selection on its data by calling convert_selection, then calls
        update_selection with the converted selection. Subclasses should
        not overrride this method, but should instead override
        convert_selection. The optional third argument specifies whether
        the selection should be added to the previous selection on this
        representation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Select, *my_args)
        return ret

    def update_annotations(self, *args):
        """
        V.update_annotations(AnnotationLayers)
        C++: void UpdateAnnotations(AnnotationLayers *annotations)
        V.update_annotations(AnnotationLayers, bool)
        C++: void UpdateAnnotations(AnnotationLayers *annotations,
            bool extend)
        Updates the selection in the selection link and fires a selection
        change event. Subclasses should not overrride this method, but
        should instead override convert_selection. The optional second
        argument specifies whether the selection should be added to the
        previous selection on this representation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateAnnotations, *my_args)
        return ret

    def update_selection(self, *args):
        """
        V.update_selection(Selection)
        C++: void UpdateSelection(Selection *selection)
        V.update_selection(Selection, bool)
        C++: void UpdateSelection(Selection *selection, bool extend)
        Updates the selection in the selection link and fires a selection
        change event. Subclasses should not overrride this method, but
        should instead override convert_selection. The optional second
        argument specifies whether the selection should be added to the
        previous selection on this representation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateSelection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('selection_type', 'GetSelectionType'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('selection_array_name', 'GetSelectionArrayName'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('selectable',
    'GetSelectable'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'progress_text',
    'selection_array_name', 'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['selectable'], [], ['selection_array_name',
            'selection_type']),
            title='Edit DataRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

