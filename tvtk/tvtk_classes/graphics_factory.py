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


class GraphicsFactory(Object):
    """
    GraphicsFactory - 
    
    Superclass: Object
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphicsFactory, obj, update, **traits)
    
    off_screen_only_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This option enables the off-screen only mode. In this mode no X
        calls will be made even when interactor is used.
        """
    )
    def _off_screen_only_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffScreenOnlyMode,
                        self.off_screen_only_mode)

    use_mesa_classes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This option enables the creation of Mesa classes instead of the
        open_gl classes when using mangled Mesa.
        """
    )
    def _use_mesa_classes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseMesaClasses,
                        self.use_mesa_classes)

    def _get_render_library(self):
        return self._vtk_obj.GetRenderLibrary()
    render_library = traits.Property(_get_render_library, help=\
        """
        What rendering library has the user requested
        """
    )

    def create_instance(self, *args):
        """
        V.create_instance(string) -> Object
        C++: static Object *CreateInstance(const char *vtkclassname)
        Create and return an instance of the named vtk object. This
        method first checks the ObjectFactory to support dynamic
        loading.
        """
        ret = self._wrap_call(self._vtk_obj.CreateInstance, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('use_mesa_classes', 'GetUseMesaClasses'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('off_screen_only_mode',
    'GetOffScreenOnlyMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'off_screen_only_mode',
    'use_mesa_classes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphicsFactory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphicsFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['off_screen_only_mode', 'use_mesa_classes']),
            title='Edit GraphicsFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphicsFactory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

