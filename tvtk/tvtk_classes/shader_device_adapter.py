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


class ShaderDeviceAdapter(Object):
    """
    ShaderDeviceAdapter - an adapter to pass generic vertex attributes
    
    Superclass: Object
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShaderDeviceAdapter, obj, update, **traits)
    
    def _get_shader_program(self):
        return wrap_vtk(self._vtk_obj.GetShaderProgram())
    def _set_shader_program(self, arg):
        old_val = self._get_shader_program()
        self._wrap_call(self._vtk_obj.SetShaderProgram,
                        deref_vtk(arg))
        self.trait_property_changed('shader_program', old_val, arg)
    shader_program = traits.Property(_get_shader_program, _set_shader_program, help=\
        """
        Set the shader program which is being updated by this device
        adapter. The shader program is not reference counted to avoid
        reference loops.
        """
    )

    def prepare_for_render(self):
        """
        V.prepare_for_render()
        C++: virtual void PrepareForRender()"""
        ret = self._vtk_obj.PrepareForRender()
        return ret
        

    def send_attribute(self, *args):
        """
        V.send_attribute(string, int, int, , int)
        C++: virtual void SendAttribute(const char *attrname,
            int components, int type, const void *attribute,
            unsigned long offset=0)
        Sends a single attribute to the graphics card. The attrname
        parameter identifies the name of attribute. The components
        parameter gives the number of components in the attribute.  In
        general, components must be between 1-4, but a rendering system
        may impose even more constraints.  The type parameter is a VTK
        type enumeration (VTK_FLOAT, VTK_INT, etc.). Again, a rendering
        system may not support all types for all attributes.  The
        attribute parameter is the actual data for the attribute. If
        offset is specified, it is added to attribute pointer after it
        has been casted to the proper type.
        """
        ret = self._wrap_call(self._vtk_obj.SendAttribute, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShaderDeviceAdapter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShaderDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ShaderDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShaderDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

