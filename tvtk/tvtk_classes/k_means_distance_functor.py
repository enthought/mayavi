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


class KMeansDistanceFunctor(Object):
    """
    KMeansDistanceFunctor - measure distance from k-means cluster
    centers
    
    Superclass: Object
    
    This is an abstract class (with a default concrete subclass) that
    implements algorithms used by the KMeansStatistics filter that
    rely on a distance metric. If you wish to use a non-Euclidean
    distance metric (this could include working with strings that do not
    have a Euclidean distance metric, implementing k-mediods, or trying
    distance metrics in norms other than L2), you should subclass
    KMeansDistanceFunctor.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKMeansDistanceFunctor, obj, update, **traits)
    
    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        Return the data type used to store cluster center coordinates.
        """
    )

    def get_empty_tuple(self, *args):
        """
        V.get_empty_tuple(int) -> VariantArray
        C++: virtual VariantArray *GetEmptyTuple(IdType dimension)
        Return an empty tuple. These values are used as cluster center
        coordinates when no initial cluster centers are specified.
        """
        ret = self._wrap_call(self._vtk_obj.GetEmptyTuple, *args)
        return wrap_vtk(ret)

    def allocate_element_array(self, *args):
        """
        V.allocate_element_array(int) ->
        C++: virtual void *AllocateElementArray(IdType size)
        Allocate an array large enough to hold size coordinates and
        return a void pointer to this array. This is used by
        PKMeansStatistics to send (receive) cluster center coordinates
        to (from) other processes.
        """
        ret = self._wrap_call(self._vtk_obj.AllocateElementArray, *args)
        return ret

    def create_coordinate_array(self):
        """
        V.create_coordinate_array() -> AbstractArray
        C++: virtual AbstractArray *CreateCoordinateArray()
        Return a AbstractArray capable of holding cluster center
        coordinates. This is used by PKMeansStatistics to hold cluster
        center coordinates sent to (received from) other processes.
        """
        ret = wrap_vtk(self._vtk_obj.CreateCoordinateArray())
        return ret
        

    def deallocate_element_array(self):
        """
        V.deallocate_element_array()
        C++: virtual void DeallocateElementArray(void *)
        Free an array allocated with allocate_element_array.
        """
        ret = self._vtk_obj.DeallocateElementArray()
        return ret
        

    def pack_elements(self, *args):
        """
        V.pack_elements(Table, )
        C++: virtual void PackElements(Table *curTable,
            void *vElements)
        Pack the cluster center coordinates in v_elements into columns of
        cur_table. This code may assume that the columns in cur_table are
        all of the type returned by get_new_vtk_array().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PackElements, *my_args)
        return ret

    def pairwise_update(self, *args):
        """
        V.pairwise_update(Table, int, VariantArray, int, int)
        C++: virtual void PairwiseUpdate(Table *clusterCenters,
            IdType row, VariantArray *data,
            IdType dataCardinality, IdType totalCardinality)
        This is called once per observation per run per iteration in
        order to assign the observation to its nearest cluster center
        after the distance functor has been evaluated for all the cluster
        centers.
        
        The distance functor is responsible for incrementally updating
        the cluster centers to account for the assignment.
        """
        my_args = deref_array(args, [('vtkTable', 'int', 'vtkVariantArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.PairwiseUpdate, *my_args)
        return ret

    def perturb_element(self, *args):
        """
        V.perturb_element(Table, Table, int, int, int, float)
        C++: virtual void PerturbElement(Table *, Table *,
            IdType, IdType, IdType, double)
        When a cluster center (1) has no observations that are closer to
        it than other cluster centers or (2) has exactly the same
        coordinates as another cluster center, its coordinates should be
        perturbed. This function should perform that perturbation.
        
        Since perturbation relies on a distance metric, this function is
        the responsibility of the distance functor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PerturbElement, *my_args)
        return ret

    def un_pack_elements(self, *args):
        """
        V.un_pack_elements(Table, Table, , , int)
        C++: virtual void UnPackElements(Table *curTable,
            Table *newTable, void *vLocalElements,
            void *vGlobalElements, int np)
        V.un_pack_elements(Table, , int, int)
        C++: virtual void UnPackElements(Table *curTable,
            void *vLocalElements, IdType numRows, IdType numCols)
        Unpack the cluster center coordinates in v_elements into columns
        of cur_table. This code may assume that the columns in cur_table
        are all of the type returned by get_new_vtk_array().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnPackElements, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KMeansDistanceFunctor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit KMeansDistanceFunctor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit KMeansDistanceFunctor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KMeansDistanceFunctor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

