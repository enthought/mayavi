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


class DataObject(Object):
    """
    DataObject - general representation of visualization data
    
    Superclass: Object
    
    DataObject is an general representation of visualization data. It
    serves to encapsulate instance variables and methods for
    visualization network execution, as well as representing data
    consisting of a field (i.e., just an unstructured pile of data). This
    is to be compared with a DataSet, which is data with geometric
    and/or topological structure.
    
    DataObjects are used to represent arbitrary repositories of data
    via the FieldData instance variable. These data must be eventually
    mapped into a concrete subclass of DataSet before they can
    actually be displayed.
    
    See Also:
    
    DataSet FieldData DataObjectSource DataObjectFilter
    DataObjectMapper DataObjectToDataSet
    FieldDataToAttributeDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObject, obj, update, **traits)
    
    release_data_flag = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether this object's data is
        released after being used by a filter.
        """
    )
    def _release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReleaseDataFlag,
                        self.release_data_flag_)

    request_exact_extent = tvtk_base.false_bool_trait(help=\
        """
        This request flag indicates whether the requester can handle more
        data than requested.  Right now it is used in ImageData. Image
        filters can return more data than requested.  The the consumer
        cannot handle this (i.e. data_set_to_data_set_fitler) the image will
        crop itself.  This functionality used to be in
        image_to_structured_points.
        """
    )
    def _request_exact_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequestExactExtent,
                        self.request_exact_extent_)

    global_release_data_flag = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether every object releases its
        data after being used by a filter.
        """
    )
    def _global_release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalReleaseDataFlag,
                        self.global_release_data_flag_)

    whole_bounding_box = traits.Array(shape=(6,), value=(0.0, -1.0, 0.0, -1.0, 0.0, -1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the whole bounding box of this data object. The whole
        whole bounding box is meta data for data sets It gets set by the
        source during the update information call.
        """
    )
    def _whole_bounding_box_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeBoundingBox,
                        self.whole_bounding_box)

    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    def _set_information(self, arg):
        old_val = self._get_information()
        self._wrap_call(self._vtk_obj.SetInformation,
                        deref_vtk(arg))
        self.trait_property_changed('information', old_val, arg)
    information = traits.Property(_get_information, _set_information, help=\
        """
        Set/Get the information object associated with this data object.
        """
    )

    def _get_pipeline_information(self):
        return wrap_vtk(self._vtk_obj.GetPipelineInformation())
    def _set_pipeline_information(self, arg):
        old_val = self._get_pipeline_information()
        self._wrap_call(self._vtk_obj.SetPipelineInformation,
                        deref_vtk(arg))
        self.trait_property_changed('pipeline_information', old_val, arg)
    pipeline_information = traits.Property(_get_pipeline_information, _set_pipeline_information, help=\
        """
        Get/Set the pipeline information object that owns this data
        object.
        """
    )

    def _get_field_data(self):
        return wrap_vtk(self._vtk_obj.GetFieldData())
    def _set_field_data(self, arg):
        old_val = self._get_field_data()
        self._wrap_call(self._vtk_obj.SetFieldData,
                        deref_vtk(arg))
        self.trait_property_changed('field_data', old_val, arg)
    field_data = traits.Property(_get_field_data, _set_field_data, help=\
        """
        Assign or retrieve a general field data to this data object.
        """
    )

    maximum_number_of_pieces = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of pieces that can be requested. The
        maximum number of pieces is meta data for unstructured data sets.
        It gets set by the source during the update information call. A
        value of -1 indicates that there is no maximum.
        """
    )
    def _maximum_number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPieces,
                        self.maximum_number_of_pieces)

    update_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the update piece and the update number of pieces.
        Similar to update extent in 3d.
        """
    )
    def _update_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpdatePiece,
                        self.update_piece)

    update_number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set / Get the update piece and the update number of pieces.
        Similar to update extent in 3d.
        """
    )
    def _update_number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpdateNumberOfPieces,
                        self.update_number_of_pieces)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Set/Get the source object creating this data object.
        """
    )

    update_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        A generic way of specifying an update extent.  Subclasses must
        decide what a piece is.  When the number_of_pieces is zero, then no
        data is requested, and the source will not execute.
        """
    )
    def _update_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpdateExtent,
                        self.update_extent)

    update_ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the update ghost level and the update number of ghost
        levels. Similar to update extent in 3d.
        """
    )
    def _update_ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpdateGhostLevel,
                        self.update_ghost_level)

    def _get_extent_translator(self):
        return wrap_vtk(self._vtk_obj.GetExtentTranslator())
    def _set_extent_translator(self, arg):
        old_val = self._get_extent_translator()
        self._wrap_call(self._vtk_obj.SetExtentTranslator,
                        deref_vtk(arg))
        self.trait_property_changed('extent_translator', old_val, arg)
    extent_translator = traits.Property(_get_extent_translator, _set_extent_translator, help=\
        """
        An object that will translate pieces into structured extents.
        """
    )

    whole_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the whole extent of this data object. The whole extent is
        meta data for structured data sets. It gets set by the source
        during the update information call.
        """
    )
    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    def get_active_field_information(self, *args):
        """
        V.get_active_field_information(Information, int, int)
            -> Information
        C++: static Information *GetActiveFieldInformation(
            Information *info, int fieldAssociation, int attributeType)
        Return the information object within the input information
        object's field data corresponding to the specified association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS) and
        attribute (SCALARS, VECTORS, NORMALS, TCOORDS, or TENSORS)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetActiveFieldInformation, *my_args)
        return wrap_vtk(ret)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the actual size of the data in kilobytes. This number is
        valid only after the pipeline has updated. The memory size
        returned is guaranteed to be greater than or equal to the memory
        required to represent the data (e.g., extra space in arrays, etc.
        are not included in the return value).
        """
    )

    def get_association_type_as_string(self, *args):
        """
        V.get_association_type_as_string(int) -> string
        C++: static const char *GetAssociationTypeAsString(
            int associationType)
        Given an integer association type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Points").
        """
        ret = self._wrap_call(self._vtk_obj.GetAssociationTypeAsString, *args)
        return ret

    def get_attribute_type_for_array(self, *args):
        """
        V.get_attribute_type_for_array(AbstractArray) -> int
        C++: virtual int GetAttributeTypeForArray(AbstractArray *arr)
        Retrieves the attribute type that an array came from. This is
        useful for obtaining which attribute type a input array to an
        algorithm came from (retrieved from
        get_input_abstract_array_to_processs).
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.GetAttributeTypeForArray, *my_args)
        return ret

    def get_attributes(self, *args):
        """
        V.get_attributes(int) -> DataSetAttributes
        C++: virtual DataSetAttributes *GetAttributes(int type)
        Returns the attributes of the data object of the specified
        attribute type. The type may be:  POINT  - Defined in DataSet
        subclasses. CELL   - Defined in DataSet subclasses. VERTEX -
        Defined in Graph subclasses. EDGE   - Defined in Graph
        subclasses. ROW    - Defined in Table.  The other attribute
        type, FIELD, will return NULL since field data is stored as a
        FieldData instance, not a DataSetAttributes instance. To
        retrieve field data, use get_attributes_as_field_data.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributes, *args)
        return wrap_vtk(ret)

    def get_attributes_as_field_data(self, *args):
        """
        V.get_attributes_as_field_data(int) -> FieldData
        C++: virtual FieldData *GetAttributesAsFieldData(int type)
        Returns the attributes of the data object as a FieldData. This
        returns non-null values in all the same cases as get_attributes,
        in addition to the case of FIELD, which will return the field
        data for any DataObject subclass.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributesAsFieldData, *args)
        return wrap_vtk(ret)

    def get_data(self, *args):
        """
        V.get_data(Information) -> DataObject
        C++: static DataObject *GetData(Information *info)
        V.get_data(InformationVector, int) -> DataObject
        C++: static DataObject *GetData(InformationVector *v,
            int i=0)
        Retrieve an instance of this class from an information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetData, *my_args)
        return wrap_vtk(ret)

    def _get_data_object_type(self):
        return self._vtk_obj.GetDataObjectType()
    data_object_type = traits.Property(_get_data_object_type, help=\
        """
        Return class name of data type. This is one of
        VTK_STRUCTURED_GRID, VTK_STRUCTURED_POINTS,
        VTK_UNSTRUCTURED_GRID, VTK_POLY_DATA, or VTK_RECTILINEAR_GRID
        (see SetGet.h for definitions). THIS METHOD IS THREAD SAFE
        """
    )

    def _get_data_released(self):
        return self._vtk_obj.GetDataReleased()
    data_released = traits.Property(_get_data_released, help=\
        """
        Get the flag indicating the data has been released.
        """
    )

    def _get_estimated_memory_size(self):
        return self._vtk_obj.GetEstimatedMemorySize()
    estimated_memory_size = traits.Property(_get_estimated_memory_size, help=\
        """
        Get the estimated size of this data object itself. Should be
        called after update_information() and propagate_update_extent() have
        both been called. Should be overridden in a subclass - otherwise
        the default is to assume that this data object requires no
        memory. The size is returned in kilobytes.
        """
    )

    def _get_extent_type(self):
        return self._vtk_obj.GetExtentType()
    extent_type = traits.Property(_get_extent_type, help=\
        """
        The extent_type will be left as VTK_PIECES_EXTENT for data objects
        such as PolyData and UnstructuredGrid. The extent_type will
        be changed to vtk__3d__extent for data objects with 3d structure
        such as ImageData (and its subclass StructuredPoints),
        RectilinearGrid, and StructuredGrid. The default is the
        have an extent in pieces, with only one piece (no streaming
        possible).
        """
    )

    def get_named_field_information(self, *args):
        """
        V.get_named_field_information(Information, int, string)
            -> Information
        C++: static Information *GetNamedFieldInformation(
            Information *info, int fieldAssociation, const char *name)
        Return the information object within the input information
        object's field data corresponding to the specified association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS) and name.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNamedFieldInformation, *my_args)
        return wrap_vtk(ret)

    def get_number_of_elements(self, *args):
        """
        V.get_number_of_elements(int) -> int
        C++: virtual IdType GetNumberOfElements(int type)
        Get the number of elements for a specific attribute type (POINT,
        CELL, etc.).
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfElements, *args)
        return ret

    def _get_pipeline_m_time(self):
        return self._vtk_obj.GetPipelineMTime()
    pipeline_m_time = traits.Property(_get_pipeline_m_time, help=\
        """
        Get the cumulative modified time of everything upstream.  Does
        not include the MTime of this object.
        """
    )

    def _get_producer_port(self):
        return wrap_vtk(self._vtk_obj.GetProducerPort())
    producer_port = traits.Property(_get_producer_port, help=\
        """
        Get the port currently producing this object.
        """
    )

    def _get_update_time(self):
        return self._vtk_obj.GetUpdateTime()
    update_time = traits.Property(_get_update_time, help=\
        """
        Used by Threaded ports to determine if they should initiate an
        asynchronous update (still in development).
        """
    )

    def CELL_DATA_VECTOR(self):
        """
        V.cell__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *CELL_DATA_VECTOR()"""
        ret = wrap_vtk(self._vtk_obj.CELL_DATA_VECTOR())
        return ret
        

    def copy_information(self, *args):
        """
        V.copy_information(DataObject)
        C++: void CopyInformation(DataObject *data)
        Copy the generic information (_whole_extent ...)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformation, *my_args)
        return ret

    def copy_information_from_pipeline(self, *args):
        """
        V.copy_information_from_pipeline(Information)
        C++: virtual void CopyInformationFromPipeline(
            Information *request)
        Copy information about this data object from the
        pipeline_information to its own Information for the given request.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformationFromPipeline, *my_args)
        return ret

    def copy_information_to_pipeline(self, *args):
        """
        V.copy_information_to_pipeline(Information, Information,
            Information, int)
        C++: virtual void CopyInformationToPipeline(
            Information *request, Information *input,
            Information *output, int forceCopy)
        V.copy_information_to_pipeline(Information, Information)
        C++: void CopyInformationToPipeline(Information *request,
            Information *input)
        Copy information about this data object to the output information
        from its own Information for the given request.  If the second
        argument is not NULL then it is the pipeline information object
        for the input to this data object's producer. If force_copy is
        true, information is copied even if it exists in the output.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformationToPipeline, *my_args)
        return ret

    def copy_type_specific_information(self, *args):
        """
        V.copy_type_specific_information(DataObject)
        C++: virtual void CopyTypeSpecificInformation(DataObject *data)
        By default, there is no type specific information
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyTypeSpecificInformation, *my_args)
        return ret

    def crop(self):
        """
        V.crop()
        C++: virtual void Crop()
        This method crops the data object (if necesary) so that the
        extent matches the update extent.
        """
        ret = self._vtk_obj.Crop()
        return ret
        

    def DATA_EXTENT(self):
        """
        V.data__extent() -> InformationIntegerPointerKey
        C++: static InformationIntegerPointerKey *DATA_EXTENT()"""
        ret = wrap_vtk(self._vtk_obj.DATA_EXTENT())
        return ret
        

    def DATA_EXTENT_TYPE(self):
        """
        V.data__extent__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_EXTENT_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.DATA_EXTENT_TYPE())
        return ret
        

    def DATA_GEOMETRY_UNMODIFIED(self):
        """
        V.data__geometry__unmodified() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_GEOMETRY_UNMODIFIED()"""
        ret = wrap_vtk(self._vtk_obj.DATA_GEOMETRY_UNMODIFIED())
        return ret
        

    def DATA_NUMBER_OF_GHOST_LEVELS(self):
        """
        V.data__number__of__ghost__levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_NUMBER_OF_GHOST_LEVELS(
            )"""
        ret = wrap_vtk(self._vtk_obj.DATA_NUMBER_OF_GHOST_LEVELS())
        return ret
        

    def DATA_NUMBER_OF_PIECES(self):
        """
        V.data__number__of__pieces() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_NUMBER_OF_PIECES()"""
        ret = wrap_vtk(self._vtk_obj.DATA_NUMBER_OF_PIECES())
        return ret
        

    def DATA_OBJECT(self):
        """
        V.data__object() -> InformationDataObjectKey
        C++: static InformationDataObjectKey *DATA_OBJECT()"""
        ret = wrap_vtk(self._vtk_obj.DATA_OBJECT())
        return ret
        

    def DATA_PIECE_NUMBER(self):
        """
        V.data__piece__number() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_PIECE_NUMBER()"""
        ret = wrap_vtk(self._vtk_obj.DATA_PIECE_NUMBER())
        return ret
        

    def DATA_RESOLUTION(self):
        """
        V.data__resolution() -> InformationDoubleKey
        C++: static InformationDoubleKey *DATA_RESOLUTION()"""
        ret = wrap_vtk(self._vtk_obj.DATA_RESOLUTION())
        return ret
        

    def DATA_TIME_STEPS(self):
        """
        V.data__time__steps() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *DATA_TIME_STEPS()"""
        ret = wrap_vtk(self._vtk_obj.DATA_TIME_STEPS())
        return ret
        

    def DATA_TYPE_NAME(self):
        """
        V.data__type__name() -> InformationStringKey
        C++: static InformationStringKey *DATA_TYPE_NAME()"""
        ret = wrap_vtk(self._vtk_obj.DATA_TYPE_NAME())
        return ret
        

    def data_has_been_generated(self):
        """
        V.data_has_been_generated()
        C++: void DataHasBeenGenerated()
        This method is called by the source when it executes to generate
        data. It is sort of the opposite of release_data. It sets the
        data_released flag to 0, and sets a new update_time.
        """
        ret = self._vtk_obj.DataHasBeenGenerated()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(DataObject)
        C++: virtual void DeepCopy(DataObject *src)
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def EDGE_DATA_VECTOR(self):
        """
        V.edge__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *EDGE_DATA_VECTOR()"""
        ret = wrap_vtk(self._vtk_obj.EDGE_DATA_VECTOR())
        return ret
        

    def FIELD_ACTIVE_ATTRIBUTE(self):
        """
        V.field__active__attribute() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ACTIVE_ATTRIBUTE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ACTIVE_ATTRIBUTE())
        return ret
        

    def FIELD_ARRAY_TYPE(self):
        """
        V.field__array__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ARRAY_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ARRAY_TYPE())
        return ret
        

    def FIELD_ASSOCIATION(self):
        """
        V.field__association() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ASSOCIATION()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ASSOCIATION())
        return ret
        

    def FIELD_ATTRIBUTE_TYPE(self):
        """
        V.field__attribute__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ATTRIBUTE_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ATTRIBUTE_TYPE())
        return ret
        

    def FIELD_NAME(self):
        """
        V.field__name() -> InformationStringKey
        C++: static InformationStringKey *FIELD_NAME()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NAME())
        return ret
        

    def FIELD_NUMBER_OF_COMPONENTS(self):
        """
        V.field__number__of__components() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_NUMBER_OF_COMPONENTS()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NUMBER_OF_COMPONENTS())
        return ret
        

    def FIELD_NUMBER_OF_TUPLES(self):
        """
        V.field__number__of__tuples() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_NUMBER_OF_TUPLES()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NUMBER_OF_TUPLES())
        return ret
        

    def FIELD_OPERATION(self):
        """
        V.field__operation() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_OPERATION()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_OPERATION())
        return ret
        

    def FIELD_RANGE(self):
        """
        V.field__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *FIELD_RANGE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_RANGE())
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Restore data object to initial state,
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def ORIGIN(self):
        """
        V.origin() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *ORIGIN()"""
        ret = wrap_vtk(self._vtk_obj.ORIGIN())
        return ret
        

    def PIECE_EXTENT(self):
        """
        V.piece__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *PIECE_EXTENT()"""
        ret = wrap_vtk(self._vtk_obj.PIECE_EXTENT())
        return ret
        

    def PIECE_FIELD_RANGE(self):
        """
        V.piece__field__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *PIECE_FIELD_RANGE()"""
        ret = wrap_vtk(self._vtk_obj.PIECE_FIELD_RANGE())
        return ret
        

    def POINT_DATA_VECTOR(self):
        """
        V.point__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *POINT_DATA_VECTOR(
            )"""
        ret = wrap_vtk(self._vtk_obj.POINT_DATA_VECTOR())
        return ret
        

    def prepare_for_new_data(self):
        """
        V.prepare_for_new_data()
        C++: virtual void PrepareForNewData()
        make the output data ready for new data to be inserted. For most
        objects we just call Initialize. But for ImageData we leave
        the old data in case the memory can be reused.
        """
        ret = self._vtk_obj.PrepareForNewData()
        return ret
        

    def propagate_update_extent(self):
        """
        V.propagate_update_extent()
        C++: virtual void PropagateUpdateExtent()
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. The update extent for
        this object is propagated up the pipeline. This propagation may
        early terminate based on the pipeline_m_time.
        """
        ret = self._vtk_obj.PropagateUpdateExtent()
        return ret
        

    def release_data(self):
        """
        V.release_data()
        C++: void ReleaseData()
        Release data back to system to conserve memory resource. Used
        during visualization network execution.  Releasing this data does
        not make down-stream data invalid, so it does not modify the
        MTime of this data object.
        """
        ret = self._vtk_obj.ReleaseData()
        return ret
        

    def remove_named_field_information(self, *args):
        """
        V.remove_named_field_information(Information, int, string)
        C++: static void RemoveNamedFieldInformation(Information *info,
             int fieldAssociation, const char *name)
        Remove the info associated with an array
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNamedFieldInformation, *my_args)
        return ret

    def SIL(self):
        """
        V.sil() -> InformationDataObjectKey
        C++: static InformationDataObjectKey *SIL()"""
        ret = wrap_vtk(self._vtk_obj.SIL())
        return ret
        

    def SPACING(self):
        """
        V.spacing() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SPACING()"""
        ret = wrap_vtk(self._vtk_obj.SPACING())
        return ret
        

    def set_active_attribute(self, *args):
        """
        V.set_active_attribute(Information, int, string, int)
            -> Information
        C++: static Information *SetActiveAttribute(
            Information *info, int fieldAssociation,
            const char *attributeName, int attributeType)
        Set the named array to be the active field for the specified type
        (SCALARS, VECTORS, NORMALS, TCOORDS, or TENSORS) and association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS).  Returns
        the active field information object and creates on entry if one
        not found.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetActiveAttribute, *my_args)
        return wrap_vtk(ret)

    def set_active_attribute_info(self, *args):
        """
        V.set_active_attribute_info(Information, int, int, string, int,
            int, int)
        C++: static void SetActiveAttributeInfo(Information *info,
            int fieldAssociation, int attributeType, const char *name,
            int arrayType, int numComponents, int numTuples)
        Set the name, array type, number of components, and number of
        tuples within the passed information object for the active
        attribute of type attribute_type (in specified association,
        FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS).  If there
        is not an active attribute of the specified type, an entry in the
        information object is created.  If array_type, num_components, or
        num_tuples equal to -1, or name=NULL the value is not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetActiveAttributeInfo, *my_args)
        return ret

    def set_point_data_active_scalar_info(self, *args):
        """
        V.set_point_data_active_scalar_info(Information, int, int)
        C++: static void SetPointDataActiveScalarInfo(
            Information *info, int arrayType, int numComponents)
        Convenience version of previous method for use (primarily) by the
        Imaging filters. If array_type or num_components == -1, the value
        is not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPointDataActiveScalarInfo, *my_args)
        return ret

    def set_update_extent_to_whole_extent(self):
        """
        V.set_update_extent_to_whole_extent()
        C++: void SetUpdateExtentToWholeExtent()
        If the whole input extent is required to generate the requested
        output extent, this method can be called to set the input update
        extent to the whole input extent. This method assumes that the
        whole extent is known (that update_information has been called)
        """
        ret = self._vtk_obj.SetUpdateExtentToWholeExtent()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(DataObject)
        C++: virtual void ShallowCopy(DataObject *src)
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def should_i_release_data(self):
        """
        V.should_i_release_data() -> int
        C++: int ShouldIReleaseData()
        Return flag indicating whether data should be released after use
        by a filter.
        """
        ret = self._vtk_obj.ShouldIReleaseData()
        return ret
        

    def trigger_asynchronous_update(self):
        """
        V.trigger_asynchronous_update()
        C++: virtual void TriggerAsynchronousUpdate()
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. Propagate back up the
        pipeline for ports and trigger the update on the other side of
        the port to allow for asynchronous parallel processing in the
        pipeline. This propagation may early terminate based on the
        pipeline_m_time.
        """
        ret = self._vtk_obj.TriggerAsynchronousUpdate()
        return ret
        

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Provides opportunity for the data object to insure internal
        consistency before access. Also causes owning source/filter (if
        any) to update itself. The Update() method is composed of
        update_information(), propagate_update_extent(),
        trigger_asynchronous_update(), and update_data().
        """
        ret = self._vtk_obj.Update()
        return ret
        

    def update_data(self):
        """
        V.update_data()
        C++: virtual void UpdateData()
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. Propagate the update
        back up the pipeline, and perform the actual work of updating on
        the way down. When the propagate arrives at a port, block and
        wait for the asynchronous update to finish on the other side.
        This propagation may early terminate based on the pipeline_m_time.
        """
        ret = self._vtk_obj.UpdateData()
        return ret
        

    def update_information(self):
        """
        V.update_information()
        C++: virtual void UpdateInformation()
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. Update all the "easy to
        update" information about the object such as the extent which
        will be used to control the update. This propagates all the way
        up then back down the pipeline. As a by-product the pipeline_m_time
        is updated.
        """
        ret = self._vtk_obj.UpdateInformation()
        return ret
        

    def VERTEX_DATA_VECTOR(self):
        """
        V.vertex__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *VERTEX_DATA_VECTOR(
            )"""
        ret = wrap_vtk(self._vtk_obj.VERTEX_DATA_VECTOR())
        return ret
        

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

