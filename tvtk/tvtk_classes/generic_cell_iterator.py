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


class GenericCellIterator(Object):
    """
    GenericCellIterator - iterator used to traverse cells
    
    Superclass: Object
    
    This class (and subclasses) are used to iterate over cells. Use it
    only in conjunction with GenericDataSet (i.e., the adaptor
    framework).
    
    Typical use is:
    
    GenericDataSet *dataset; GenericCellIterator *it =
    dataset->_new_cell_iterator(_2); for (it->Begin(); !it->_is_at_end();
    it->Next());
      {
      spec=it->_get_cell();
      } 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericCellIterator, obj, update, **traits)
    
    def _get_cell(self):
        return wrap_vtk(self._vtk_obj.GetCell())
    cell = traits.Property(_get_cell, help=\
        """
        Get the cell at current position. The cell should be instantiated
        with the new_cell() method.
        \pre not_at_end: !_is_at_end()
        \pre c_exists: c!=0
        THREAD SAFE
        """
    )

    def begin(self):
        """
        V.begin()
        C++: virtual void Begin()
        Move iterator to first position if any (loop initialization).
        """
        ret = self._vtk_obj.Begin()
        return ret
        

    def is_at_end(self):
        """
        V.is_at_end() -> int
        C++: virtual int IsAtEnd()
        Is the iterator at the end of traversal?
        """
        ret = self._vtk_obj.IsAtEnd()
        return ret
        

    def new_cell(self):
        """
        V.new_cell() -> GenericAdaptorCell
        C++: virtual GenericAdaptorCell *NewCell()
        Create an empty cell. The user is responsible for deleting it.
        \post result_exists: result!=0
        """
        ret = wrap_vtk(self._vtk_obj.NewCell())
        return ret
        

    def next(self):
        """
        V.next()
        C++: virtual void Next()
        Move the iterator to the next position in the list.
        \pre not_at_end: !_is_at_end()
        """
        ret = self._vtk_obj.Next()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericCellIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericCellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GenericCellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericCellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

