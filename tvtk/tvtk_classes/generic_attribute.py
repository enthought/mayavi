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


class GenericAttribute(Object):
    """
    GenericAttribute - abstract class defined API for attribute data
    
    Superclass: Object
    
    GenericAttribute is an abstract class that defines an API for
    attribute data. Attribute data is data associated with the topology
    or geometry of a dataset (i.e., points, cells, etc.).
    GenericAttribute is part of the adaptor framework (see
    generic_filtering/_readme.html).
    
    GenericAttribute provides a more general interface to attribute
    data than its counterpart DataArray (which assumes a linear,
    contiguous array). It adopts an iterator interface, and allows
    attributes to be associated with points, edges, faces, or edges.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericAttribute, obj, update, **traits)
    
    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Size in kilobytes taken by the attribute.
        """
    )

    def _get_centering(self):
        return self._vtk_obj.GetCentering()
    centering = traits.Property(_get_centering, help=\
        """
        Is the attribute centered either on points, cells or boundaries?
        \post valid_result:
            (result==vtk_point_centered)||(result==vtk_cell_centered)
        """
    )

    def get_component(self, *args):
        """
        V.get_component(int, GenericPointIterator) -> float
        C++: virtual double GetComponent(int i,
            GenericPointIterator *p)
        Value of the component `i' of the attribute at position `p'.
        \pre valid_component: (i>=0) && (i<_get_number_of_components())
        \pre p_exists: p!=0
        \pre p_valid: !p->_is_at_end()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetComponent, *my_args)
        return ret

    def _get_component_type(self):
        return self._vtk_obj.GetComponentType()
    component_type = traits.Property(_get_component_type, help=\
        """
        Type of the components of the attribute: int, float, double
        \post valid_result: (result==VTK_BIT)          
            ||(result==VTK_CHAR)
                          ||(result==VTK_UNSIGNED_CHAR)
        ||(result==VTK_SHORT)
                         
        ||(result==VTK_UNSIGNED_SHORT)||(result==VTK_INT)
                          ||(result==VTK_UNSIGNED_INT) 
        ||(result==VTK_LONG)
                          ||(result==VTK_UNSIGNED_LONG)
        ||(result==VTK_FLOAT)
                          ||(result==VTK_DOUBLE)       
        ||(result==VTK_ID_TYPE)
        """
    )

    def _get_max_norm(self):
        return self._vtk_obj.GetMaxNorm()
    max_norm = traits.Property(_get_max_norm, help=\
        """
        Return the maximum euclidean norm for the tuples.
        \post positive_result: result>=0
        """
    )

    def _get_name(self):
        return self._vtk_obj.GetName()
    name = traits.Property(_get_name, help=\
        """
        Name of the attribute. (e.g. "velocity")
        \post result_may_not_exist: result!=0 || result==0
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Dimension of the attribute. (1 for scalar, 3 for velocity)
        \post positive_result: result>=0
        \post get_type()==_vtk__scalars implies result==1
        \post
            (_get_type()==_vtk__vectors||(_get_type()==_vtk__normals)||(_get_type()=
            =VTK_TCOORDS) implies result==3
        \post get_type()==_vtk__tensors implies result==6
        """
    )

    def get_range(self, *args):
        """
        V.get_range(int, [float, float])
        C++: virtual void GetRange(int component, double range[2])
        Range of the attribute component `component'. If `component'==-1,
        it returns the range of the magnitude (euclidean norm). THREAD
        SAFE
        \pre valid_component:
            (component>=-_1)&&(component<_get_number_of_components())
        """
        ret = self._wrap_call(self._vtk_obj.GetRange, *args)
        return ret

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Number of tuples.
        \post valid_result: result>=0
        """
    )

    def _get_type(self):
        return self._vtk_obj.GetType()
    type = traits.Property(_get_type, help=\
        """
        Type of the attribute: scalar, vector, normal, texture
        coordinate, tensor
        \post valid_result: (result==vtk_data_set_attributes::_scalars)
                          ||(result==vtk_data_set_attributes::_vectors)
                          ||(result==vtk_data_set_attributes::_normals)
                          ||(result==vtk_data_set_attributes::_tcoords)
                          ||(result==vtk_data_set_attributes::_tensors)
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(GenericAttribute)
        C++: virtual void DeepCopy(GenericAttribute *other)
        Recursive duplication of `other' in `this'.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(GenericAttribute)
        C++: virtual void ShallowCopy(GenericAttribute *other)
        Update `this' using fields of `other'.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericAttribute, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GenericAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericAttribute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

