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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class ImplicitBoolean(ImplicitFunction):
    """
    ImplicitBoolean - implicit function consisting of boolean
    combinations of implicit functions
    
    Superclass: ImplicitFunction
    
    ImplicitBoolean is an implicit function consisting of boolean
    combinations of implicit functions. The class has a list of functions
    (_function_list) that are combined according to a specified operator
    (VTK_UNION or VTK_INTERSECTION or VTK_DIFFERENCE). You can use nested
    combinations of ImplicitFunction's (and/or ImplicitBoolean) to
    create elaborate implicit functions.  ImplicitBoolean is a
    concrete implementation of ImplicitFunction.
    
    The operators work as follows. The VTK_UNION operator takes the
    minimum value of all implicit functions. The VTK_INTERSECTION
    operator takes the maximum value of all implicit functions. The
    VTK_DIFFERENCE operator subtracts the 2nd through last implicit
    functions from the first. The VTK_UNION_OF_MAGNITUDES takes the
    minimum absolute value of the implicit functions.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitBoolean, obj, update, **traits)
    
    operation_type = traits.Trait('union',
    tvtk_base.TraitRevPrefixMap({'union': 0, 'intersection': 1, 'difference': 2, 'union_of_magnitudes': 3}), help=\
        """
        Specify the type of boolean operation.
        """
    )
    def _operation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperationType,
                        self.operation_type_)

    def _get_function(self):
        return wrap_vtk(self._vtk_obj.GetFunction())
    function = traits.Property(_get_function, help=\
        """
        Return the collection of implicit functions.
        """
    )

    def add_function(self, *args):
        """
        V.add_function(ImplicitFunction)
        C++: void AddFunction(ImplicitFunction *in)
        Add another implicit function to the list of functions.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddFunction, *my_args)
        return ret

    def remove_function(self, *args):
        """
        V.remove_function(ImplicitFunction)
        C++: void RemoveFunction(ImplicitFunction *in)
        Remove a function from the list of implicit functions to boolean.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveFunction, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('operation_type', 'GetOperationType'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'operation_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitBoolean, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitBoolean properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['operation_type'], []),
            title='Edit ImplicitBoolean properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitBoolean properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

