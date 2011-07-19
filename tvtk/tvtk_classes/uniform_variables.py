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


class UniformVariables(Object):
    """
    UniformVariables - GLSL uniform variables
    
    Superclass: Object
    
    UniformVariables is a list of uniform variables attached to either
    a Shader2 object or to a ShaderProgram2. Uniform variables on a
    ShaderProgram2 override values of uniform variables on a
    Shader2.
    
    See Also:
    
    Shader2 ShaderProgram2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUniformVariables, obj, update, **traits)
    
    def _get_current_name(self):
        return self._vtk_obj.GetCurrentName()
    current_name = traits.Property(_get_current_name, help=\
        """
        Name of the uniform at the current cursor position.
        \pre not_done: !this->_is_at_end()
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(UniformVariables)
        C++: void DeepCopy(UniformVariables *other)
        Copy all the variables from `other'. Any existing variable will
        be deleted first.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def is_at_end(self):
        """
        V.is_at_end() -> bool
        C++: bool IsAtEnd()
        Is the iteration done?
        """
        ret = self._vtk_obj.IsAtEnd()
        return ret
        

    def merge(self, *args):
        """
        V.merge(UniformVariables)
        C++: void Merge(UniformVariables *other)
        Copy all the variables from `other'. Any existing variable will
        be overwritten.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Merge, *my_args)
        return ret

    def next(self):
        """
        V.next()
        C++: void Next()
        Move the cursor to the next uniform.
        \pre not_done: !this->_is_at_end()
        """
        ret = self._vtk_obj.Next()
        return ret
        

    def remove_all_uniforms(self):
        """
        V.remove_all_uniforms()
        C++: void RemoveAllUniforms()
        Remove all uniforms from the list.
        """
        ret = self._vtk_obj.RemoveAllUniforms()
        return ret
        

    def remove_uniform(self, *args):
        """
        V.remove_uniform(string)
        C++: void RemoveUniform(const char *name)
        Remove uniform `name' from the list.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveUniform, *args)
        return ret

    def send(self, *args):
        """
        V.send(string, int)
        C++: void Send(const char *name, int uniformIndex)
        \pre need a valid open_gl context and a shader program in use.
        """
        ret = self._wrap_call(self._vtk_obj.Send, *args)
        return ret

    def send_current_uniform(self, *args):
        """
        V.send_current_uniform(int)
        C++: void SendCurrentUniform(int uniformIndex)
        \pre need a valid open_gl context and a shader program in use.
        \pre not_done: !this->_is_at_end()
        """
        ret = self._wrap_call(self._vtk_obj.SendCurrentUniform, *args)
        return ret

    def start(self):
        """
        V.start()
        C++: void Start()
        Place the internal cursor on the first uniform.
        """
        ret = self._vtk_obj.Start()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UniformVariables, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UniformVariables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit UniformVariables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UniformVariables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

