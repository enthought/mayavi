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


class StructuredExtent(Object):
    """
    StructuredExtent - helper class to aid working with structured
    
    Superclass: Object
    
    StructuredExtent is an helper class that helps in arithmetic with
     structured extents. It defines a bunch of static methods (most of
    which are
     inlined) to aid in dealing with extents.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredExtent, obj, update, **traits)
    
    def get_dimensions(self, *args):
        """
        V.get_dimensions((int, int, int, int, int, int), [int, int, int])
        C++: static void GetDimensions(const int ext[6], int dims[3])
        Given the extents, computes the dimensions.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensions, *args)
        return ret

    def clamp(self, *args):
        """
        V.clamp([int, int, int, int, int, int], [int, int, int, int, int,
            int])
        C++: static void Clamp(int ext[6], int wholeExt[6])
        Clamps ext to fit in whole_ext.
        """
        ret = self._wrap_call(self._vtk_obj.Clamp, *args)
        return ret

    def grow(self, *args):
        """
        V.grow([int, int, int, int, int, int], int)
        C++: static void Grow(int ext[6], int count)
        Grows the ext on each side by the given count.
        """
        ret = self._wrap_call(self._vtk_obj.Grow, *args)
        return ret

    def smaller(self, *args):
        """
        V.smaller((int, int, int, int, int, int), (int, int, int, int,
            int, int)) -> bool
        C++: static bool Smaller(const int ext[6], const int wholeExt[6])
        Returns if ext fits within whole_ext. Unline strictly_smaller, this
        method returns true even if ext == whole_ext.
        """
        ret = self._wrap_call(self._vtk_obj.Smaller, *args)
        return ret

    def strictly_smaller(self, *args):
        """
        V.strictly_smaller((int, int, int, int, int, int), (int, int, int,
            int, int, int)) -> bool
        C++: static bool StrictlySmaller(const int ext[6],
            const int wholeExt[6])
        Returns true if ext is fits within whole_ext with atleast 1
        dimension smaller than the whole_ext.
        """
        ret = self._wrap_call(self._vtk_obj.StrictlySmaller, *args)
        return ret

    def transform(self, *args):
        """
        V.transform([int, int, int, int, int, int], [int, int, int, int,
            int, int])
        C++: static void Transform(int ext[6], int wholeExt[6])
        Makes ext relative to whole_ext.
        """
        ret = self._wrap_call(self._vtk_obj.Transform, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredExtent, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit StructuredExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

