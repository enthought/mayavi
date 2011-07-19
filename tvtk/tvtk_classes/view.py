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


class View(Object):
    """
    View - The superclass for all views.
    
    Superclass: Object
    
    View is the superclass for views.  A view is generally an area of
    an application's canvas devoted to displaying one or more VTK data
    objects. Associated representations (subclasses of
    DataRepresentation) are responsible for converting the data into a
    displayable format.  These representations are then added to the
    view.
    
    For views which display only one data object at a time you may set a
    data object or pipeline connection directly on the view itself (e.g.
    GraphLayoutView, LandscapeView, TreeMapView). The view will
    internally create a DataRepresentation for the data.
    
    A view has the concept of linked selection.  If the same data is
    displayed in multiple views, their selections may be linked by
    setting the same AnnotationLink on their representations (see
    DataRepresentation).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkView, obj, update, **traits)
    
    def get_representation(self, *args):
        """
        V.get_representation(int) -> DataRepresentation
        C++: DataRepresentation *GetRepresentation(int index=0)
        The representation at a specified index.
        """
        ret = self._wrap_call(self._vtk_obj.GetRepresentation, *args)
        return wrap_vtk(ret)

    def set_representation(self, *args):
        """
        V.set_representation(DataRepresentation)
        C++: void SetRepresentation(DataRepresentation *rep)
        Set the representation to the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentation, *my_args)
        return ret

    def _get_number_of_representations(self):
        return self._vtk_obj.GetNumberOfRepresentations()
    number_of_representations = traits.Property(_get_number_of_representations, help=\
        """
        Returns the number of representations from first port(0) in this
        view.
        """
    )

    def _get_observer(self):
        return wrap_vtk(self._vtk_obj.GetObserver())
    observer = traits.Property(_get_observer, help=\
        """
        Returns the observer that the subclasses can use to listen to
        additional events. Additionally these subclasses should override
        process_events() to handle these events.
        """
    )

    def add_representation(self, *args):
        """
        V.add_representation(DataRepresentation)
        C++: void AddRepresentation(DataRepresentation *rep)
        Adds the representation to the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddRepresentation, *my_args)
        return ret

    def add_representation_from_input(self, *args):
        """
        V.add_representation_from_input(DataObject)
            -> DataRepresentation
        C++: DataRepresentation *AddRepresentationFromInput(
            DataObject *input)
        Convenience method which creates a simple representation with the
        specified input and adds it to the view. NOTE: The returned
        representation pointer is not reference-counted, so you MUST call
        Register() on the representation if you want to keep a reference
        to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddRepresentationFromInput, *my_args)
        return wrap_vtk(ret)

    def add_representation_from_input_connection(self, *args):
        """
        V.add_representation_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *AddRepresentationFromInputConnection(
            AlgorithmOutput *conn)
        Convenience method which creates a simple representation with the
        connection and adds it to the view. Returns the representation
        internally created. NOTE: The returned representation pointer is
        not reference-counted, so you MUST call Register() on the
        representation if you want to keep a reference to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddRepresentationFromInputConnection, *my_args)
        return wrap_vtk(ret)

    def apply_view_theme(self, *args):
        """
        V.apply_view_theme(ViewTheme)
        C++: virtual void ApplyViewTheme(ViewTheme *theme)
        Apply a theme to the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyViewTheme, *my_args)
        return ret

    def is_representation_present(self, *args):
        """
        V.is_representation_present(DataRepresentation) -> bool
        C++: bool IsRepresentationPresent(DataRepresentation *rep)
        Check to see if a representation is present in the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsRepresentationPresent, *my_args)
        return ret

    def register_progress(self, *args):
        """
        V.register_progress(Object, string)
        C++: void RegisterProgress(Object *algorithm,
            const char *message=NULL)
        Meant for use by subclasses and Representation subclasses.
        Call this method to register Objects (generally Algorithm
        subclasses) which fire Command::ProgressEvent with the view.
        The view listens to Command::ProgressEvent and fires
        view_progress_event with view_progress_event_call_data containing the
        message and the progress amount. If message is not provided, then
        the class name for the algorithm is used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegisterProgress, *my_args)
        return ret

    def remove_all_representations(self):
        """
        V.remove_all_representations()
        C++: void RemoveAllRepresentations()
        Removes all representations from the view.
        """
        ret = self._vtk_obj.RemoveAllRepresentations()
        return ret
        

    def remove_representation(self, *args):
        """
        V.remove_representation(DataRepresentation)
        C++: void RemoveRepresentation(DataRepresentation *rep)
        V.remove_representation(AlgorithmOutput)
        C++: void RemoveRepresentation(AlgorithmOutput *rep)
        Removes the representation from the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveRepresentation, *my_args)
        return ret

    def set_representation_from_input(self, *args):
        """
        V.set_representation_from_input(DataObject)
            -> DataRepresentation
        C++: DataRepresentation *SetRepresentationFromInput(
            DataObject *input)
        Convenience method which sets the representation to the specified
        input and adds it to the view. NOTE: The returned representation
        pointer is not reference-counted, so you MUST call Register() on
        the representation if you want to keep a reference to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentationFromInput, *my_args)
        return wrap_vtk(ret)

    def set_representation_from_input_connection(self, *args):
        """
        V.set_representation_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *SetRepresentationFromInputConnection(
            AlgorithmOutput *conn)
        Convenience method which sets the representation with the
        connection and adds it to the view. Returns the representation
        internally created. NOTE: The returned representation pointer is
        not reference-counted, so you MUST call Register() on the
        representation if you want to keep a reference to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentationFromInputConnection, *my_args)
        return wrap_vtk(ret)

    def un_register_progress(self, *args):
        """
        V.un_register_progress(Object)
        C++: void UnRegisterProgress(Object *algorithm)
        Unregister objects previously registered with register_progress.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnRegisterProgress, *my_args)
        return ret

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Update the view.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(View, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit View properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit View properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit View properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

