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


class DebugLeaks(Object):
    """
    DebugLeaks - identify memory leaks at program termination
    
    Superclass: Object
    
    DebugLeaks is used to report memory leaks at the exit of the
    program. It uses the ObjectFactory to intercept the construction
    of all VTK objects. It uses the un_register method of Object to
    intercept the destruction of all objects. A table of object name to
    number of instances is kept. At the exit of the program if there are
    still VTK objects around it will print them out.  To enable this
    class add the flag
    -DVTK_DEBUG_LEAKS to the compile line, and rebuild Object and
        ObjectFactory.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDebugLeaks, obj, update, **traits)
    
    exit_error = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set flag for exiting with an error when leaks are present.
        Default is on when testing and off otherwise.
        """
    )
    def _exit_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExitError,
                        self.exit_error)

    def construct_class(self, *args):
        """
        V.construct_class(string)
        C++: static void ConstructClass(const char *classname)
        Call this when creating a class of a given name.
        """
        ret = self._wrap_call(self._vtk_obj.ConstructClass, *args)
        return ret

    def destruct_class(self, *args):
        """
        V.destruct_class(string)
        C++: static void DestructClass(const char *classname)
        Call this when deleting a class of a given name.
        """
        ret = self._wrap_call(self._vtk_obj.DestructClass, *args)
        return ret

    def print_current_leaks(self):
        """
        V.print_current_leaks() -> int
        C++: static int PrintCurrentLeaks()
        Print all the values in the table.  Returns non-zero if there
        were leaks.
        """
        ret = self._vtk_obj.PrintCurrentLeaks()
        return ret
        

    def prompt_user_off(self):
        """
        V.prompt_user_off()
        C++: static void PromptUserOff()
        @deprecated Turn prompt at exit on/off (this setting is
        deprecated and will be ignored).
        """
        ret = self._vtk_obj.PromptUserOff()
        return ret
        

    def prompt_user_on(self):
        """
        V.prompt_user_on()
        C++: static void PromptUserOn()
        @deprecated Turn prompt at exit on/off (this setting is
        deprecated and will be ignored).
        """
        ret = self._vtk_obj.PromptUserOn()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('exit_error',
    'GetExitError'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'exit_error'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DebugLeaks, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['exit_error']),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

