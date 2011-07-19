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

from tvtk.tvtk_classes.render_pass import RenderPass


class SequencePass(RenderPass):
    """
    SequencePass - Execute render passes sequentially.
    
    Superclass: RenderPass
    
    SequencePass executes a list of render passes sequentially. This
    class allows to define a sequence of render passes at run time. The
    other solution to write a sequence of render passes is to write an
    effective subclass of RenderPass.
    
    As SequencePass is a RenderPass itself, it is possible to have
    a hierarchy of render passes built at runtime.
    
    See Also:
    
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSequencePass, obj, update, **traits)
    
    def _get_passes(self):
        return wrap_vtk(self._vtk_obj.GetPasses())
    def _set_passes(self, arg):
        old_val = self._get_passes()
        self._wrap_call(self._vtk_obj.SetPasses,
                        deref_vtk(arg))
        self.trait_property_changed('passes', old_val, arg)
    passes = traits.Property(_get_passes, _set_passes, help=\
        """
        The ordered list of render passes to execute sequentially. If the
        pointer is NULL or the list is empty, it is silently ignored.
        There is no warning. Initial value is a NULL pointer.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SequencePass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SequencePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SequencePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SequencePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

