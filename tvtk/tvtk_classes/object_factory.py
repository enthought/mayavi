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


class ObjectFactory(Object):
    """
    ObjectFactory - abstract base class for ObjectFactories
    
    Superclass: Object
    
    ObjectFactory is used to create vtk objects.   The base class
    ObjectFactory contains a static method create_instance which is
    used to create vtk objects from the list of registered
    ObjectFactory sub-classes.   The first time create_instance is
    called, all dll's or shared libraries in the environment variable
    VTK_AUTOLOAD_PATH are loaded into the current process.   The C
    functions Load, GetFactoryCompilerUsed, and
    GetFactoryVersion are called on each dll.  To implement these
    functions in a shared library or dll, use the macro:
    VTK_FACTORY_INTERFACE_IMPLEMENT. VTK_AUTOLOAD_PATH is an environment
    variable containing a colon separated (semi-colon on win32) list of
    paths.
    
    The ObjectFactory can be use to override the creation of any
    object in VTK with a sub-class of that object.  The factories can be
    registered either at run time with the VTK_AUTOLOAD_PATH, or at
    compile time with the ObjectFactory::RegisterFactory method.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkObjectFactory, obj, update, **traits)
    
    def get_enable_flag(self, *args):
        """
        V.get_enable_flag(int) -> int
        C++: virtual int GetEnableFlag(int index)
        V.get_enable_flag(string, string) -> int
        C++: virtual int GetEnableFlag(const char *className,
            const char *subclassName)
        Return the enable flag for the class at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetEnableFlag, *args)
        return ret

    def set_enable_flag(self, *args):
        """
        V.set_enable_flag(int, string, string)
        C++: virtual void SetEnableFlag(int flag, const char *className,
            const char *subclassName)
        Set and Get the Enable flag for the specific override of
        class_name. if subclass_name is null, then it is ignored.
        """
        ret = self._wrap_call(self._vtk_obj.SetEnableFlag, *args)
        return ret

    def get_class_override_name(self, *args):
        """
        V.get_class_override_name(int) -> string
        C++: virtual const char *GetClassOverrideName(int index)
        Return the name of a class override at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetClassOverrideName, *args)
        return ret

    def get_class_override_with_name(self, *args):
        """
        V.get_class_override_with_name(int) -> string
        C++: virtual const char *GetClassOverrideWithName(int index)
        Return the name of the class that will override the class at the
        given index
        """
        ret = self._wrap_call(self._vtk_obj.GetClassOverrideWithName, *args)
        return ret

    def _get_description(self):
        return self._vtk_obj.GetDescription()
    description = traits.Property(_get_description, help=\
        """
        Return a descriptive string describing the factory.
        """
    )

    def _get_library_path(self):
        return self._vtk_obj.GetLibraryPath()
    library_path = traits.Property(_get_library_path, help=\
        """
        This returns the path to a dynamically loaded factory.
        """
    )

    def _get_number_of_overrides(self):
        return self._vtk_obj.GetNumberOfOverrides()
    number_of_overrides = traits.Property(_get_number_of_overrides, help=\
        """
        Return number of overrides this factory can create.
        """
    )

    def get_override_description(self, *args):
        """
        V.get_override_description(int) -> string
        C++: virtual const char *GetOverrideDescription(int index)
        Return the description for a the class override at the given
        index.
        """
        ret = self._wrap_call(self._vtk_obj.GetOverrideDescription, *args)
        return ret

    def get_override_information(self, *args):
        """
        V.get_override_information(string, OverrideInformationCollection)
        C++: static void GetOverrideInformation(const char *name,
            OverrideInformationCollection *)
        Fill the given collection with all the overrides for the class
        with the given name.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetOverrideInformation, *my_args)
        return ret

    def _get_registered_factories(self):
        return wrap_vtk(self._vtk_obj.GetRegisteredFactories())
    registered_factories = traits.Property(_get_registered_factories, help=\
        """
        Return the list of all registered factories.  This is NOT a copy,
        do not remove items from this list!
        """
    )

    def _get_vtk_source_version(self):
        return self._vtk_obj.GetVTKSourceVersion()
    vtk_source_version = traits.Property(_get_vtk_source_version, help=\
        """
        All sub-classes of ObjectFactory should must return the
        version of VTK they were built with.  This should be implemented
        with the macro VTK_SOURCE_VERSION and NOT a call to
        Version::GetVTKSourceVersion. As the version needs to be
        compiled into the file as a string constant. This is critical to
        determine possible incompatible dynamic factory loads.
        """
    )

    def create_all_instance(self, *args):
        """
        V.create_all_instance(string, Collection)
        C++: static void CreateAllInstance(const char *vtkclassname,
            Collection *retList)
        Create all possible instances of the named vtk object. Each
        registered ObjectFactory will be asked, and the result will be
        stored in the user allocated Collection passed in to the
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateAllInstance, *my_args)
        return ret

    def create_instance(self, *args):
        """
        V.create_instance(string) -> Object
        C++: static Object *CreateInstance(const char *vtkclassname)
        Create and return an instance of the named vtk object. Each
        loaded ObjectFactory will be asked in the order the factory
        was in the VTK_AUTOLOAD_PATH.  After the first factory returns
        the object no other factories are asked.
        """
        ret = self._wrap_call(self._vtk_obj.CreateInstance, *args)
        return wrap_vtk(ret)

    def disable(self, *args):
        """
        V.disable(string)
        C++: virtual void Disable(const char *className)
        Set all enable flags for the given class to 0.  This will mean
        that the factory will stop producing class with the given name.
        """
        ret = self._wrap_call(self._vtk_obj.Disable, *args)
        return ret

    def has_override(self, *args):
        """
        V.has_override(string) -> int
        C++: virtual int HasOverride(const char *className)
        V.has_override(string, string) -> int
        C++: virtual int HasOverride(const char *className,
            const char *subclassName)
        Return 1 if this factory overrides the given class name, 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.HasOverride, *args)
        return ret

    def has_override_any(self, *args):
        """
        V.has_override_any(string) -> int
        C++: static int HasOverrideAny(const char *className)
        return 1 if one of the registered factories overrides the given
        class name
        """
        ret = self._wrap_call(self._vtk_obj.HasOverrideAny, *args)
        return ret

    def re_hash(self):
        """
        V.re_hash()
        C++: static void ReHash()
        Re-check the VTK_AUTOLOAD_PATH for new factory libraries. This
        calls un_register_all before re-loading
        """
        ret = self._vtk_obj.ReHash()
        return ret
        

    def register_factory(self, *args):
        """
        V.register_factory(ObjectFactory)
        C++: static void RegisterFactory(ObjectFactory *)
        Register a factory so it can be used to create vtk objects
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegisterFactory, *my_args)
        return ret

    def set_all_enable_flags(self, *args):
        """
        V.set_all_enable_flags(int, string)
        C++: static void SetAllEnableFlags(int flag,
            const char *className)
        V.set_all_enable_flags(int, string, string)
        C++: static void SetAllEnableFlags(int flag,
            const char *className, const char *subclassName)
        Set the enable flag for a given named class for all registered
        factories.
        """
        ret = self._wrap_call(self._vtk_obj.SetAllEnableFlags, *args)
        return ret

    def un_register_all_factories(self):
        """
        V.un_register_all_factories()
        C++: static void UnRegisterAllFactories()
        Unregister all factories
        """
        ret = self._vtk_obj.UnRegisterAllFactories()
        return ret
        

    def un_register_factory(self, *args):
        """
        V.un_register_factory(ObjectFactory)
        C++: static void UnRegisterFactory(ObjectFactory *)
        Remove a factory from the list of registered factories
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnRegisterFactory, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('enable_flag', 'GetEnableFlag'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'enable_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ObjectFactory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ObjectFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['enable_flag']),
            title='Edit ObjectFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ObjectFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

