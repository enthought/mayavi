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


class StructuredVisibilityConstraint(Object):
    """
    StructuredVisibilityConstraint - helper object to manage the
    
    Superclass: Object
    
    StructuredVisibilityConstraint is a general class to manage a list
    of points/cell marked as invalid or invisible. Currently, it does
    this by maintaining an unsigned char array associated with
    points/cells. To conserve memory, this array is allocated only when
    it is needed (when Blank() is called the first time). Make sure to
    call Initialize() with the right dimensions before calling any
    methods that set/get visibility.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredVisibilityConstraint, obj, update, **traits)
    
    def _get_visibility_by_id(self):
        return wrap_vtk(self._vtk_obj.GetVisibilityById())
    def _set_visibility_by_id(self, arg):
        old_val = self._get_visibility_by_id()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetVisibilityById,
                        my_arg[0])
        self.trait_property_changed('visibility_by_id', old_val, arg)
    visibility_by_id = traits.Property(_get_visibility_by_id, _set_visibility_by_id, help=\
        """
        Set/Get the array used to store the visibility flags.
        """
    )

    def _get_dimensions(self):
        return self._vtk_obj.GetDimensions()
    dimensions = traits.Property(_get_dimensions, help=\
        """
        Get the dimensions used to initialize the object.
        """
    )

    def blank(self, *args):
        """
        V.blank(int)
        C++: void Blank(IdType id)
        Sets the visibility flag of the given point/cell off. The first
        time blank is called, a new visibility array is created if it
        doesn't exist.
        """
        ret = self._wrap_call(self._vtk_obj.Blank, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(StructuredVisibilityConstraint)
        C++: void DeepCopy(StructuredVisibilityConstraint *src)
        Copies the dimensions, the visibility array and the initialized
        flag.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize([int, int, int])
        C++: void Initialize(int dims[3])
        Set the dimensions and set the Initialized flag to 1. Once an
        object is initialized, it's dimensions can not be changed
        anymore.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def is_constrained(self):
        """
        V.is_constrained() ->
        C++: unsigned char IsConstrained()
        Returns 0 if there is no visibility array (all cells/points are
        visible), 0 otherwise.
        """
        ret = self._vtk_obj.IsConstrained()
        return ret
        

    def is_visible(self, *args):
        """
        V.is_visible(int) ->
        C++: unsigned char IsVisible(IdType id)
        Returns 1 is the point/cell is visible, 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.IsVisible, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(StructuredVisibilityConstraint)
        C++: void ShallowCopy(StructuredVisibilityConstraint *src)
        Copies the dimensions, the visibility array pointer and the
        initialized flag.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def un_blank(self, *args):
        """
        V.un_blank(int)
        C++: void UnBlank(IdType id)
        Sets the visibility flag of the given point/cell on.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlank, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredVisibilityConstraint, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredVisibilityConstraint properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit StructuredVisibilityConstraint properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredVisibilityConstraint properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

