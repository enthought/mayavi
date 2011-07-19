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


class Exporter(Object):
    """
    Exporter - abstract class to write a scene to a file
    
    Superclass: Object
    
    Exporter is an abstract class that exports a scene to a file. It
    is very similar to Writer except that a writer only writes out the
    geometric and topological data for an object, where an exporter can
    write out material properties, lighting, camera parameters etc. The
    concrete subclasses of this class may not write out all of this
    information. For example OBJExporter writes out Wavefront obj
    files which do not include support for camera parameters.
    
    Exporter provides the convenience methods start_write() and
    end_write(). These methods are executed before and after execution of
    the Write() method. You can also specify arguments to these methods.
    This class defines set_input and get_input methods which take or return
    a RenderWindow.
    
    Caveats:
    
    Every subclass of Exporter must implement a write_data() method.
    
    See Also:
    
    OBJExporter RenderWindow Writer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExporter, obj, update, **traits)
    
    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Set/Get the rendering window that contains the scene to be
        written.
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
        These methods are provided for backward compatibility. Will
        disappear soon.
        """
    )

    def set_end_write(self, *args):
        """
        V.set_end_write(function)
        C++: void SetEndWrite(void (*f)(void *) , void *arg)
        Specify a function to be called after data is written. Function
        will be called with argument provided.
        """
        ret = self._wrap_call(self._vtk_obj.SetEndWrite, *args)
        return ret

    def set_start_write(self, *args):
        """
        V.set_start_write(function)
        C++: void SetStartWrite(void (*f)(void *) , void *arg)
        Specify a function to be called before data is written.  Function
        will be called with argument provided.
        """
        ret = self._wrap_call(self._vtk_obj.SetStartWrite, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: void Update()
        Convenient alias for Write() method.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    def write(self):
        """
        V.write()
        C++: virtual void Write()
        Write data to output. Method executes subclasses write_data()
        method, as well as start_write() and end_write() methods.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Exporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Exporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Exporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Exporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

