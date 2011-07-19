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


class GarbageCollector(Object):
    """
    GarbageCollector - Detect and break reference loops
    
    Superclass: Object
    
    GarbageCollector is used by VTK classes that may be involved in
    reference counting loops (such as Algorithm <-> Executive).  It
    detects strongly connected components of the reference graph that
    have been leaked deletes them.  The garbage collector uses the
    report_references method to search the reference graph and construct a
    net reference count for each connected component.  If the net
    reference count is zero the entire set of objects is deleted.
    Deleting each component may leak other components, which are then
    collected recursively.
    
    To enable garbage collection for a class, add these members:
    
    public:
      virtual void register(vtk_object_base* o)
        {
        this->_register_internal(o, 1);
        }
      virtual void un_register(vtk_object_base* o)
        {
        this->_un_register_internal(o, 1);
        }
    
    
     protected:
    
    
      virtual void report_references(vtk_garbage_collector* collector)
        {
        // Report references held by this object that may be in a loop.
        this->_superclass::_report_references(collector);
        GarbageCollectorReport(collector, this->_other_object, "Other
    Object");
        }
    
    The implementations should be in the .cxx file in practice. It is
    important that the reference be reported using the real pointer or
    smart pointer instance that holds the reference.  When collecting the
    garbage collector will actually set this pointer to NULL.  The
    destructor of the class should be written to deal with this.  It is
    also expected that an invariant is maintained for any reference that
    is reported.  The variable holding the reference must always either
    be NULL or refer to a fully constructed valid object.  Therefore code
    like "this->_object->_un_register(this)" must be avoided if
    "this->Object" is a reported reference because it is possible that
    the object is deleted before un_register returns but then
    "this->Object" will be left as a dangling pointer.  Instead use code
    like
    
    ObjectBase* obj = this->Object;
      this->Object = 0;
      obj->_un_register(this);
    
    so that the reported reference maintains the invariant.
    
    If subclassing from a class that already supports garbage collection,
    one need only provide the report_references method.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGarbageCollector, obj, update, **traits)
    
    global_debug_flag = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get global garbage collection debugging flag.  When set to 1,
        all garbage collection checks will produce debugging information.
        """
    )
    def _global_debug_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalDebugFlag,
                        self.global_debug_flag)

    def collect(self, *args):
        """
        V.collect()
        C++: static void Collect()
        V.collect(ObjectBase)
        C++: static void Collect(ObjectBase *root)
        Collect immediately using any objects whose collection was
        previously deferred as a root for the reference graph walk.
        Strongly connected components in the reference graph are
        identified.  Those with a net reference count of zero are
        deleted.  When a component is deleted it may remove references to
        other components that are not part of the same reference loop but
        are held by objects in the original component.  These removed
        references are handled as any other and their corresponding
        checks may be deferred.  This method keeps collecting until no
        deferred collection checks remain.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Collect, *my_args)
        return ret

    def deferred_collection_pop(self):
        """
        V.deferred_collection_pop()
        C++: static void DeferredCollectionPop()
        Push/Pop whether to do deferred collection.  Whenever the total
        number of pushes exceeds the total number of pops collection will
        be deferred.  Code can call the Collect method directly to force
        collection.
        """
        ret = self._vtk_obj.DeferredCollectionPop()
        return ret
        

    def deferred_collection_push(self):
        """
        V.deferred_collection_push()
        C++: static void DeferredCollectionPush()
        Push/Pop whether to do deferred collection.  Whenever the total
        number of pushes exceeds the total number of pops collection will
        be deferred.  Code can call the Collect method directly to force
        collection.
        """
        ret = self._vtk_obj.DeferredCollectionPush()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('global_debug_flag', 'GetGlobalDebugFlag'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'global_debug_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GarbageCollector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GarbageCollector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['global_debug_flag']),
            title='Edit GarbageCollector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GarbageCollector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

