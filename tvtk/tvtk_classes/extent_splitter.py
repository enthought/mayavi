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


class ExtentSplitter(Object):
    """
    ExtentSplitter - Split an extent across other extents.
    
    Superclass: Object
    
    ExtentSplitter splits each input extent into non-overlapping
    sub-extents that are completely contained within other "source
    extents".  A source extent corresponds to some resource providing an
    extent.  Each source extent has an integer identifier, integer
    priority, and an extent.  The input extents are split into
    sub-extents according to priority, availability, and amount of
    overlap of the source extents.  This can be used by parallel data
    readers to read as few piece files as possible.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtentSplitter, obj, update, **traits)
    
    point_mode = tvtk_base.false_bool_trait(help=\
        """
        Get/Set whether "point mode" is on.  In point mode, sub-extents
        are generated to ensure every point in the update request is
        read, but not necessarily every cell.  This can be used when
        point data are stored in a planar slice per piece with no cell
        data.  The default is OFF.
        """
    )
    def _point_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointMode,
                        self.point_mode_)

    def _get_number_of_sub_extents(self):
        return self._vtk_obj.GetNumberOfSubExtents()
    number_of_sub_extents = traits.Property(_get_number_of_sub_extents, help=\
        """
        Get the number of sub-extents into which the original set of
        extents have been split across the available sources.  Valid
        after a call to compute_sub_extents.
        """
    )

    def get_sub_extent(self, *args):
        """
        V.get_sub_extent(int) -> (int, int, int, int, int, int)
        C++: int *GetSubExtent(int index)
        Get the sub-extent associated with the given index.  Use
        get_sub_extent_source to get the id of the source from which this
        sub-extent should be read.  Valid after a call to
        compute_sub_extents.
        """
        ret = self._wrap_call(self._vtk_obj.GetSubExtent, *args)
        return ret

    def get_sub_extent_source(self, *args):
        """
        V.get_sub_extent_source(int) -> int
        C++: int GetSubExtentSource(int index)
        Get the id of the source from which the sub-extent associated
        with the given index should be read.  Returns -1 if no source
        provides the sub-extent.
        """
        ret = self._wrap_call(self._vtk_obj.GetSubExtentSource, *args)
        return ret

    def add_extent(self, *args):
        """
        V.add_extent(int, int, int, int, int, int)
        C++: void AddExtent(int x0, int x1, int y0, int y1, int z0,
            int z1)
        Add an extent to the queue of extents to be split among the
        available sources.
        """
        ret = self._wrap_call(self._vtk_obj.AddExtent, *args)
        return ret

    def add_extent_source(self, *args):
        """
        V.add_extent_source(int, int, int, int, int, int, int, int)
        C++: void AddExtentSource(int id, int priority, int x0, int x1,
            int y0, int y1, int z0, int z1)
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ret = self._wrap_call(self._vtk_obj.AddExtentSource, *args)
        return ret

    def compute_sub_extents(self):
        """
        V.compute_sub_extents() -> int
        C++: int ComputeSubExtents()
        Split the extents currently in the queue among the available
        sources.  The queue is empty when this returns.  Returns 1 if all
        extents could be read.  Returns 0 if any portion of any extent
        was not available through any source.
        """
        ret = self._vtk_obj.ComputeSubExtents()
        return ret
        

    def remove_all_extent_sources(self):
        """
        V.remove_all_extent_sources()
        C++: void RemoveAllExtentSources()
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ret = self._vtk_obj.RemoveAllExtentSources()
        return ret
        

    def remove_extent_source(self, *args):
        """
        V.remove_extent_source(int)
        C++: void RemoveExtentSource(int id)
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveExtentSource, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('point_mode',
    'GetPointMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'point_mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtentSplitter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtentSplitter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['point_mode'], [], []),
            title='Edit ExtentSplitter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtentSplitter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

