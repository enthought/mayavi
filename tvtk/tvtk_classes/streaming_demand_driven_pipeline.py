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

from tvtk.tvtk_classes.demand_driven_pipeline import DemandDrivenPipeline


class StreamingDemandDrivenPipeline(DemandDrivenPipeline):
    """
    StreamingDemandDrivenPipeline - Executive supporting partial
    updates.
    
    Superclass: DemandDrivenPipeline
    
    StreamingDemandDrivenPipeline is an executive that supports
    updating only a portion of the data set in the pipeline.  This is the
    style of pipeline update that is provided by the old-style VTK 4.x
    pipeline.  Instead of always updating an entire data set, this
    executive supports asking for pieces or sub-extents.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamingDemandDrivenPipeline, obj, update, **traits)
    
    def get_whole_bounding_box(self, *args):
        """
        V.get_whole_bounding_box(int, [float, float, float, float, float,
            float])
        C++: void GetWholeBoundingBox(int port, double bb[6])
        Set/Get the whole bounding box of an output port data object. The
        whole whole bounding box is meta data for data sets.  It gets set
        by the algorithm during the update information pass.
        """
        ret = self._wrap_call(self._vtk_obj.GetWholeBoundingBox, *args)
        return ret

    def set_whole_bounding_box(self, *args):
        """
        V.set_whole_bounding_box(int, [float, float, float, float, float,
            float]) -> int
        C++: int SetWholeBoundingBox(int port, double bb[6])
        Set/Get the whole bounding box of an output port data object. The
        whole whole bounding box is meta data for data sets.  It gets set
        by the algorithm during the update information pass.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeBoundingBox, *args)
        return ret

    def get_maximum_number_of_pieces(self, *args):
        """
        V.get_maximum_number_of_pieces(int) -> int
        C++: int GetMaximumNumberOfPieces(int port)
        V.get_maximum_number_of_pieces(Information) -> int
        C++: int GetMaximumNumberOfPieces(Information *)
        Set/Get the maximum number of pieces that can be requested from
        the given port.  The maximum number of pieces is meta data for
        unstructured data sets.  It gets set by the source during the
        update information call.  A value of -1 indicates that there is
        no maximum.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMaximumNumberOfPieces, *my_args)
        return ret

    def set_maximum_number_of_pieces(self, *args):
        """
        V.set_maximum_number_of_pieces(int, int) -> int
        C++: int SetMaximumNumberOfPieces(int port, int n)
        V.set_maximum_number_of_pieces(Information, int) -> int
        C++: int SetMaximumNumberOfPieces(Information *, int n)
        Set/Get the maximum number of pieces that can be requested from
        the given port.  The maximum number of pieces is meta data for
        unstructured data sets.  It gets set by the source during the
        update information call.  A value of -1 indicates that there is
        no maximum.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMaximumNumberOfPieces, *my_args)
        return ret

    def get_update_resolution(self, *args):
        """
        V.get_update_resolution(Information) -> float
        C++: double GetUpdateResolution(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateResolution, *my_args)
        return ret

    def set_update_resolution(self, *args):
        """
        V.set_update_resolution(int, float) -> int
        C++: int SetUpdateResolution(int port, double r)
        V.set_update_resolution(Information, float) -> int
        C++: int SetUpdateResolution(Information *, double r)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateResolution, *my_args)
        return ret

    def get_update_piece(self, *args):
        """
        V.get_update_piece(Information) -> int
        C++: int GetUpdatePiece(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdatePiece, *my_args)
        return ret

    def set_update_piece(self, *args):
        """
        V.set_update_piece(Information, int) -> int
        C++: int SetUpdatePiece(Information *, int piece)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdatePiece, *my_args)
        return ret

    def get_request_exact_extent(self, *args):
        """
        V.get_request_exact_extent(int) -> int
        C++: int GetRequestExactExtent(int port)
        This request flag indicates whether the requester can handle more
        data than requested for the given port.  Right now it is used in
        ImageData.  Image filters can return more data than requested.
        The the consumer cannot handle this (i.e. data_set_to_data_set_fitler)
        the image will crop itself.  This functionality used to be in
        image_to_structured_points.
        """
        ret = self._wrap_call(self._vtk_obj.GetRequestExactExtent, *args)
        return ret

    def set_request_exact_extent(self, *args):
        """
        V.set_request_exact_extent(int, int) -> int
        C++: int SetRequestExactExtent(int port, int flag)
        This request flag indicates whether the requester can handle more
        data than requested for the given port.  Right now it is used in
        ImageData.  Image filters can return more data than requested.
        The the consumer cannot handle this (i.e. data_set_to_data_set_fitler)
        the image will crop itself.  This functionality used to be in
        image_to_structured_points.
        """
        ret = self._wrap_call(self._vtk_obj.SetRequestExactExtent, *args)
        return ret

    def get_piece_bounding_box(self, *args):
        """
        V.get_piece_bounding_box(int, [float, float, float, float, float,
            float])
        C++: void GetPieceBoundingBox(int port, double bb[6])
        Set/Get the piece bounding box of an output port data object. The
        piece bounding box is meta data for data sets.  It gets set by
        the algorithm during the update extent information pass.
        """
        ret = self._wrap_call(self._vtk_obj.GetPieceBoundingBox, *args)
        return ret

    def set_piece_bounding_box(self, *args):
        """
        V.set_piece_bounding_box(int, [float, float, float, float, float,
            float]) -> int
        C++: int SetPieceBoundingBox(int port, double bb[6])
        Set/Get the piece bounding box of an output port data object. The
        piece bounding box is meta data for data sets.  It gets set by
        the algorithm during the update extent information pass.
        """
        ret = self._wrap_call(self._vtk_obj.SetPieceBoundingBox, *args)
        return ret

    def get_update_extent(self, *args):
        """
        V.get_update_extent(Information, [int, int, int, int, int, int])
        C++: void GetUpdateExtent(Information *, int extent[6])
        Get/Set the update extent for output ports that use 3d extents.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateExtent, *my_args)
        return ret

    def set_update_extent(self, *args):
        """
        V.set_update_extent(int, [int, int, int, int, int, int]) -> int
        C++: int SetUpdateExtent(int port, int extent[6])
        V.set_update_extent(Information, [int, int, int, int, int, int])
            -> int
        C++: int SetUpdateExtent(Information *, int extent[6])
        V.set_update_extent(int, int, int, int) -> int
        C++: int SetUpdateExtent(int port, int piece, int numPieces,
            int ghostLevel)
        V.set_update_extent(Information, int, int, int) -> int
        C++: int SetUpdateExtent(Information *, int piece,
            int numPieces, int ghostLevel)
        Get/Set the update extent for output ports that use 3d extents.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtent, *my_args)
        return ret

    def get_update_ghost_level(self, *args):
        """
        V.get_update_ghost_level(Information) -> int
        C++: int GetUpdateGhostLevel(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateGhostLevel, *my_args)
        return ret

    def set_update_ghost_level(self, *args):
        """
        V.set_update_ghost_level(Information, int) -> int
        C++: int SetUpdateGhostLevel(Information *, int n)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateGhostLevel, *my_args)
        return ret

    def get_whole_extent(self, *args):
        """
        V.get_whole_extent(Information, [int, int, int, int, int, int])
        C++: void GetWholeExtent(Information *, int extent[6])
        Set/Get the whole extent of an output port.  The whole extent is
        meta data for structured data sets.  It gets set by the algorithm
        during the update information pass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetWholeExtent, *my_args)
        return ret

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(Information, [int, int, int, int, int, int])
            -> int
        C++: int SetWholeExtent(Information *, int extent[6])
        Set/Get the whole extent of an output port.  The whole extent is
        meta data for structured data sets.  It gets set by the algorithm
        during the update information pass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *my_args)
        return ret

    def get_extent_translator(self, *args):
        """
        V.get_extent_translator(int) -> ExtentTranslator
        C++: ExtentTranslator *GetExtentTranslator(int port)
        V.get_extent_translator(Information) -> ExtentTranslator
        C++: ExtentTranslator *GetExtentTranslator(
            Information *info)
        Get/Set the object that will translate pieces into structured
        extents for an output port.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetExtentTranslator, *my_args)
        return wrap_vtk(ret)

    def set_extent_translator(self, *args):
        """
        V.set_extent_translator(int, ExtentTranslator) -> int
        C++: int SetExtentTranslator(int port,
            ExtentTranslator *translator)
        V.set_extent_translator(Information, ExtentTranslator) -> int
        C++: int SetExtentTranslator(Information *,
            ExtentTranslator *translator)
        Get/Set the object that will translate pieces into structured
        extents for an output port.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetExtentTranslator, *my_args)
        return ret

    def get_update_number_of_pieces(self, *args):
        """
        V.get_update_number_of_pieces(Information) -> int
        C++: int GetUpdateNumberOfPieces(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateNumberOfPieces, *my_args)
        return ret

    def set_update_number_of_pieces(self, *args):
        """
        V.set_update_number_of_pieces(Information, int) -> int
        C++: int SetUpdateNumberOfPieces(Information *, int n)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateNumberOfPieces, *my_args)
        return ret

    def CONTINUE_EXECUTING(self):
        """
        V.continue__executing() -> InformationIntegerKey
        C++: static InformationIntegerKey *CONTINUE_EXECUTING()
        Key for an algorithm to store in a request to tell this executive
        to keep executing it.
        """
        ret = wrap_vtk(self._vtk_obj.CONTINUE_EXECUTING())
        return ret
        

    def compute_priority(self, *args):
        """
        V.compute_priority() -> float
        C++: double ComputePriority()
        V.compute_priority(int) -> float
        C++: virtual double ComputePriority(int port)
        Issues pipeline request to determine and return the priority of
        the piece described by the current update extent. The priority is
        a number between 0.0 and 1.0 with 0 meaning skippable
        (REQUEST_DATA not needed) and 1.0 meaning important.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePriority, *args)
        return ret

    def EXACT_EXTENT(self):
        """
        V.exact__extent() -> InformationIntegerKey
        C++: static InformationIntegerKey *EXACT_EXTENT()
        Key to specify the request for exact extent in pipeline
        information.
        """
        ret = wrap_vtk(self._vtk_obj.EXACT_EXTENT())
        return ret
        

    def EXTENT_TRANSLATOR(self):
        """
        V.extent__translator() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *EXTENT_TRANSLATOR()
        Key to store an extent translator in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.EXTENT_TRANSLATOR())
        return ret
        

    def FAST_PATH_FOR_TEMPORAL_DATA(self):
        """
        V.fast__path__for__temporal__data() -> InformationIntegerKey
        C++: static InformationIntegerKey *FAST_PATH_FOR_TEMPORAL_DATA(
            )"""
        ret = wrap_vtk(self._vtk_obj.FAST_PATH_FOR_TEMPORAL_DATA())
        return ret
        

    def FAST_PATH_ID_TYPE(self):
        """
        V.fast__path__id__type() -> InformationStringKey
        C++: static InformationStringKey *FAST_PATH_ID_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FAST_PATH_ID_TYPE())
        return ret
        

    def FAST_PATH_OBJECT_ID(self):
        """
        V.fast__path__object__id() -> InformationIdTypeKey
        C++: static InformationIdTypeKey *FAST_PATH_OBJECT_ID()"""
        ret = wrap_vtk(self._vtk_obj.FAST_PATH_OBJECT_ID())
        return ret
        

    def FAST_PATH_OBJECT_TYPE(self):
        """
        V.fast__path__object__type() -> InformationStringKey
        C++: static InformationStringKey *FAST_PATH_OBJECT_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FAST_PATH_OBJECT_TYPE())
        return ret
        

    def MAXIMUM_NUMBER_OF_PIECES(self):
        """
        V.maximum__number__of__pieces() -> InformationIntegerKey
        C++: static InformationIntegerKey *MAXIMUM_NUMBER_OF_PIECES()
        Key to store the maximum number of pieces provided in pipeline
        information.
        """
        ret = wrap_vtk(self._vtk_obj.MAXIMUM_NUMBER_OF_PIECES())
        return ret
        

    def PIECE_BOUNDING_BOX(self):
        """
        V.piece__bounding__box() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *PIECE_BOUNDING_BOX()
        Key to store the bounding box of a portion of the data set in
        pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.PIECE_BOUNDING_BOX())
        return ret
        

    def PRIORITY(self):
        """
        V.priority() -> InformationDoubleKey
        C++: static InformationDoubleKey *PRIORITY()
        Key that specifies from 0.0 to 1.0 the pipeline computed priority
        of this update extent. 0.0 means does not contribute and can be
        skipped.
        """
        ret = wrap_vtk(self._vtk_obj.PRIORITY())
        return ret
        

    def propagate_update_extent(self, *args):
        """
        V.propagate_update_extent(int) -> int
        C++: int PropagateUpdateExtent(int outputPort)
        Propagate the update request from the given output port back
        through the pipeline.  Should be called only when information is
        up to date.
        """
        ret = self._wrap_call(self._vtk_obj.PropagateUpdateExtent, *args)
        return ret

    def REMOVE_ATTRIBUTE_INFORMATION(self):
        """
        V.remove__attribute__information() -> InformationIntegerKey
        C++: static InformationIntegerKey *REMOVE_ATTRIBUTE_INFORMATION(
            )
        Used internally to validate meta information as it flows through
        pipeline
        """
        ret = wrap_vtk(self._vtk_obj.REMOVE_ATTRIBUTE_INFORMATION())
        return ret
        

    def REQUEST_RESOLUTION_PROPAGATE(self):
        """
        V.request__resolution__propagate() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_RESOLUTION_PROPAGATE(
            )
        Key defining to propagate resolution changes up the pipeline.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_RESOLUTION_PROPAGATE())
        return ret
        

    def REQUEST_UPDATE_EXTENT(self):
        """
        V.request__update__extent() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_UPDATE_EXTENT()
        Key defining a request to propagate the update extent upstream.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_UPDATE_EXTENT())
        return ret
        

    def REQUEST_UPDATE_EXTENT_INFORMATION(self):
        """
        V.request__update__extent__information() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_UPDATE_EXTENT_INFORMATION(
            )
        Key defining a request to propagate information about the update
        extent downstream.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_UPDATE_EXTENT_INFORMATION())
        return ret
        

    def set_update_extent_to_whole_extent(self, *args):
        """
        V.set_update_extent_to_whole_extent(int) -> int
        C++: int SetUpdateExtentToWholeExtent(int port)
        V.set_update_extent_to_whole_extent(Information) -> int
        C++: int SetUpdateExtentToWholeExtent(Information *)
        If the whole input extent is required to generate the requested
        output extent, this method can be called to set the input update
        extent to the whole input extent. This method assumes that the
        whole extent is known (that update_information has been called)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtentToWholeExtent, *my_args)
        return ret

    def set_update_time_step(self, *args):
        """
        V.set_update_time_step(int, float) -> int
        C++: int SetUpdateTimeStep(int port, double time)
        Get/Set the update extent for output ports that use Temporal
        Extents
        """
        ret = self._wrap_call(self._vtk_obj.SetUpdateTimeStep, *args)
        return ret

    def TIME_RANGE(self):
        """
        V.time__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *TIME_RANGE()
        Key to store available time range for continuous sources.
        """
        ret = wrap_vtk(self._vtk_obj.TIME_RANGE())
        return ret
        

    def TIME_STEPS(self):
        """
        V.time__steps() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *TIME_STEPS()
        Key to store available time steps.
        """
        ret = wrap_vtk(self._vtk_obj.TIME_STEPS())
        return ret
        

    def UNRESTRICTED_UPDATE_EXTENT(self):
        """
        V.unrestricted__update__extent() -> InformationIntegerKey
        C++: static InformationIntegerKey *UNRESTRICTED_UPDATE_EXTENT()
        This is set if the update extent is not restricted to the whole
        extent, for sources that can generate an extent of any requested
        size.
        """
        ret = wrap_vtk(self._vtk_obj.UNRESTRICTED_UPDATE_EXTENT())
        return ret
        

    def UPDATE_EXTENT(self):
        """
        V.update__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *UPDATE_EXTENT()
        Keys to store an update request in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_EXTENT())
        return ret
        

    def UPDATE_EXTENT_INITIALIZED(self):
        """
        V.update__extent__initialized() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_EXTENT_INITIALIZED()
        Keys to store an update request in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_EXTENT_INITIALIZED())
        return ret
        

    def UPDATE_EXTENT_TRANSLATED(self):
        """
        V.update__extent__translated() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_EXTENT_TRANSLATED()
        This is set if the extent was set through extent translation.
        generate_ghost_level_array() is called only when this is set.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_EXTENT_TRANSLATED())
        return ret
        

    def UPDATE_NUMBER_OF_GHOST_LEVELS(self):
        """
        V.update__number__of__ghost__levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_NUMBER_OF_GHOST_LEVELS(
            )
        Keys to store an update request in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_NUMBER_OF_GHOST_LEVELS())
        return ret
        

    def UPDATE_NUMBER_OF_PIECES(self):
        """
        V.update__number__of__pieces() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_NUMBER_OF_PIECES()
        Keys to store an update request in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_NUMBER_OF_PIECES())
        return ret
        

    def UPDATE_PIECE_NUMBER(self):
        """
        V.update__piece__number() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_PIECE_NUMBER()
        Keys to store an update request in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_PIECE_NUMBER())
        return ret
        

    def UPDATE_RESOLUTION(self):
        """
        V.update__resolution() -> InformationDoubleKey
        C++: static InformationDoubleKey *UPDATE_RESOLUTION()
        Key that specifies a requested resolution level for this update
        extent. 0.0 is very low and 1.0 is full resolution.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_RESOLUTION())
        return ret
        

    def UPDATE_TIME_STEPS(self):
        """
        V.update__time__steps() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *UPDATE_TIME_STEPS()
        Update time steps requested by the pipeline.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_TIME_STEPS())
        return ret
        

    def update_whole_extent(self):
        """
        V.update_whole_extent() -> int
        C++: virtual int UpdateWholeExtent()
        Bring the outputs up-to-date.
        """
        ret = self._vtk_obj.UpdateWholeExtent()
        return ret
        

    def WHOLE_BOUNDING_BOX(self):
        """
        V.whole__bounding__box() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *WHOLE_BOUNDING_BOX()
        Key to store the bounding box of the entire data set in pipeline
        information.
        """
        ret = wrap_vtk(self._vtk_obj.WHOLE_BOUNDING_BOX())
        return ret
        

    def WHOLE_EXTENT(self):
        """
        V.whole__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *WHOLE_EXTENT()
        Key to store the whole extent provided in pipeline information.
        """
        ret = wrap_vtk(self._vtk_obj.WHOLE_EXTENT())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamingDemandDrivenPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

