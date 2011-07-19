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


class ArrayIterator(Object):
    """
    ArrayIterator - Abstract superclass to iterate over elements
    
    Superclass: Object
    
    ArrayIterator is used to iterate over elements in any
    AbstractArray subclass.  The ArrayIteratorTemplateMacro is used
    to centralize the set of types supported by Execute methods.  It also
    avoids duplication of long switch statement case lists.
    
    Note that in this macro VTK_TT is defined to be the type of the
    iterator for the given type of array. One must include the
    ArrayIteratorIncludes.h header file to provide for extending of
    this macro by addition of new iterators.
    
    Example usage:vtk_array_iter* iter = array->_new_iterator();
    switch(array->_get_data_type())
      {
      ArrayIteratorTemplateMacro(myFunc(static_cast<VTK_TT*>(iter),
    arg2));
      }
    iter->Delete();
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayIterator, obj, update, **traits)
    
    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        
        """
    )

    def initialize(self, *args):
        """
        V.initialize(AbstractArray)
        C++: virtual void Initialize(AbstractArray *array)
        Set the array this iterator will iterate over. After Initialize()
        has been called, the iterator is valid so long as the Array has
        not been modified (except using the iterator itself). If the
        array is modified, the iterator must be re-intialized.
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

