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


class Points2D(Object):
    """
    Points2D - represent and manipulate 2d points
    
    Superclass: Object
    
    Points2D represents 2d points. The data model for Points2D is
    an array of vx-vy doublets accessible by (point or cell) id.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPoints2D, obj, update, **traits)
    
    data_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'short': 4, 'int': 6, 'double': 11, 'float': 10, 'unsigned_long': 9, 'long': 8, 'char': 2, 'unsigned_int': 7, 'unsigned_char': 3, 'unsigned_short': 5, 'bit': 1}), help=\
        """
        Specify the underlying data type of the object.
        """
    )
    def _data_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataType,
                        self.data_type_)

    def get_point(self, *args):
        """
        V.get_point(int, [float, float])
        C++: void GetPoint(IdType id, double x[2])
        Copy point components into user provided array v[2] for specified
        id.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def set_point(self, *args):
        """
        V.set_point(int, (float, float))
        C++: void SetPoint(IdType id, const double x[2])
        V.set_point(int, float, float)
        C++: void SetPoint(IdType id, double x, double y)
        Insert point into object. No range checking performed (fast!).
        Make sure you use set_number_of_points() to allocate memory prior to
        using set_point().
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint, *args)
        return ret

    def _get_data(self):
        return wrap_vtk(self._vtk_obj.GetData())
    def _set_data(self, arg):
        old_val = self._get_data()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetData,
                        my_arg[0])
        self.trait_property_changed('data', old_val, arg)
    data = traits.Property(_get_data, _set_data, help=\
        """
        Set/Get the underlying data array. This function must be
        implemented in a concrete subclass to check for consistency. (The
        tuple size must match the type of data. For example, 3-tuple data
        array can be assigned to a vector, normal, or points object, but
        not a tensor object, which has a tuple dimension of 9. Scalars,
        on the other hand, can have tuple dimension
         from 1-4, depending on the type of scalar.)
        """
    )

    number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of points for this object to hold. Does an
        allocation as well as setting the max_id ivar. Used in conjunction
        with set_point() method for fast insertion.
        """
    )
    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this attribute data.
        Used to support streaming and reading/writing data. The value
        returned is guaranteed to be greater than or equal to the memory
        required to actually represent the data represented by this
        object. The information returned is valid only after the pipeline
        has been updated.
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: void GetBounds(double bounds[4])
        Return the bounds of the points.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def get_points(self, *args):
        """
        V.get_points(IdList, Points2D)
        C++: void GetPoints(IdList *ptId, Points2D *fp)
        Given a list of pt ids, return an array of points.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkPoints2D')])
        ret = self._wrap_call(self._vtk_obj.GetPoints, *my_args)
        return ret

    def get_void_pointer(self, *args):
        """
        V.get_void_pointer(int) ->
        C++: void *GetVoidPointer(const int id)
        Return a void pointer. For image pipeline interface and other
        special pointer manipulation.
        """
        ret = self._wrap_call(self._vtk_obj.GetVoidPointer, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: virtual int Allocate(const IdType sz,
            const IdType ext=1000)
        Allocate initial memory size.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: virtual void ComputeBounds()
        Determine (xmin,xmax, ymin,ymax) bounds of points.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(Points2D)
        C++: virtual void DeepCopy(Points2D *ad)
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Return object to instantiated state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_next_point(self, *args):
        """
        V.insert_next_point((float, float)) -> int
        C++: IdType InsertNextPoint(const double x[2])
        V.insert_next_point(float, float) -> int
        C++: IdType InsertNextPoint(double x, double y)
        Insert point into next available slot. Returns id of slot.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextPoint, *args)
        return ret

    def insert_point(self, *args):
        """
        V.insert_point(int, (float, float))
        C++: void InsertPoint(IdType id, const double x[2])
        V.insert_point(int, float, float)
        C++: void InsertPoint(IdType id, double x, double y)
        Insert point into object. Range checking performed and memory
        allocated as necessary.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: virtual void Reset()
        Make object look empty but do not delete memory.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Points2D)
        C++: virtual void ShallowCopy(Points2D *ad)
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()
        Reclaim any extra memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('number_of_points',
    'GetNumberOfPoints'), ('data_type', 'GetDataType'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'data_type', 'number_of_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Points2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Points2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['data_type'], ['number_of_points']),
            title='Edit Points2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Points2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

