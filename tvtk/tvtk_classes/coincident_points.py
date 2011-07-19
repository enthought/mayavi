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


class CoincidentPoints(Object):
    """
    CoincidentPoints - contains an octree of labels
    
    Superclass: Object
    
    This class provides a collection of points that is organized such
    that each coordinate is stored with a set of point id's of points
    that are all coincident.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCoincidentPoints, obj, update, **traits)
    
    def get_coincident_point_ids(self, *args):
        """
        V.get_coincident_point_ids((float, float, float)) -> IdList
        C++: IdList *GetCoincidentPointIds(const double point[3])
        Retrieve the list of point Ids that are coincident with the given
        point.
        @param[in] point - the coordinate of coincident points we want to
        retrieve.
        """
        ret = self._wrap_call(self._vtk_obj.GetCoincidentPointIds, *args)
        return wrap_vtk(ret)

    def _get_next_coincident_point_ids(self):
        return wrap_vtk(self._vtk_obj.GetNextCoincidentPointIds())
    next_coincident_point_ids = traits.Property(_get_next_coincident_point_ids, help=\
        """
        Used to iterate the sets of coincident points within the map.
        init_traversal must be called first or NULL will always be
        returned.
        """
    )

    def add_point(self, *args):
        """
        V.add_point(int, (float, float, float))
        C++: void AddPoint(IdType Id, const double point[3])
        Accumulates a set of Ids in a map where the point coordinate is
        the key. All Ids in a given map entry are thus coincident.
        @param Id - a unique Id for the given point that will be stored
            in an IdList.
        @param[in] point - the point coordinate that we will store in the
        map to test if any other points are
        coincident with it.
        """
        ret = self._wrap_call(self._vtk_obj.AddPoint, *args)
        return ret

    def clear(self):
        """
        V.clear()
        C++: void Clear()"""
        ret = self._vtk_obj.Clear()
        return ret
        

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()"""
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def remove_non_coincident_points(self):
        """
        V.remove_non_coincident_points()
        C++: void RemoveNonCoincidentPoints()"""
        ret = self._vtk_obj.RemoveNonCoincidentPoints()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CoincidentPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CoincidentPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CoincidentPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CoincidentPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

