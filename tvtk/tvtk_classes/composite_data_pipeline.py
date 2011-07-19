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

from tvtk.tvtk_classes.streaming_demand_driven_pipeline import StreamingDemandDrivenPipeline


class CompositeDataPipeline(StreamingDemandDrivenPipeline):
    """
    CompositeDataPipeline - Executive supporting composite datasets.
    
    Superclass: StreamingDemandDrivenPipeline
    
    CompositeDataPipeline is an executive that supports the processing
    of composite dataset. It supports algorithms that are aware of
    composite dataset as well as those that are not. Type checking is
    performed at run time. Algorithms that are not composite
    dataset-aware have to support all dataset types contained in the
    composite dataset. The pipeline execution can be summarized as
    follows:
    
    * REQUEST_INFORMATION: The producers have to provide information
      about the contents of the composite dataset in this pass. Sources
      that can produce more than one piece (note that a piece is
      different than a block; each piece consistes of 0 or more blocks)
      should set MAXIMUM_NUMBER_OF_PIECES to -1.
    
    * REQUEST_UPDATE_EXTENT: This pass is identical to the one
      implemented in StreamingDemandDrivenPipeline
    
    * REQUEST_DATA: This is where the algorithms execute. If the
      CompositeDataPipeline is assigned to a simple filter, it will
      invoke the  StreamingDemandDrivenPipeline passes in a loop,
      passing a different block each time and will collect the results in
    a composite dataset.
    
    See also:
    
    
     CompositeDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataPipeline, obj, update, **traits)
    
    def get_composite_output_data(self, *args):
        """
        V.get_composite_output_data(int) -> DataObject
        C++: DataObject *GetCompositeOutputData(int port)
        Returns the data object stored with the DATA_OBJECT() in the
        output port
        """
        ret = self._wrap_call(self._vtk_obj.GetCompositeOutputData, *args)
        return wrap_vtk(ret)

    def COMPOSITE_DATA_META_DATA(self):
        """
        V.composite__data__meta__data() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *COMPOSITE_DATA_META_DATA(
            )
        COMPOSITE_DATA_META_DATA is a key placed in the output-port
        information by readers/sources producing composite datasets. This
        meta-data provides information about the structure of the
        composite dataset and things like data-bounds etc.
        *** THIS IS AN EXPERIMENTAL FEATURE. IT MAY CHANGE WITHOUT NOTICE
        ***
        """
        ret = wrap_vtk(self._vtk_obj.COMPOSITE_DATA_META_DATA())
        return ret
        

    def COMPOSITE_INDICES(self):
        """
        V.composite__indices() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *COMPOSITE_INDICES()
        COMPOSITE_INDICES() is put in the output information by the
        executive if the request has UPDATE_COMPOSITE_INDICES() using the
        generated composite dataset's structure. Note that
        COMPOSITE_INDICES has to be sorted vector with increasing
        indices.
        *** THIS IS AN EXPERIMENTAL FEATURE. IT MAY CHANGE WITHOUT NOTICE
        ***
        """
        ret = wrap_vtk(self._vtk_obj.COMPOSITE_INDICES())
        return ret
        

    def REQUIRES_TIME_DOWNSTREAM(self):
        """
        V.requires__time__downstream() -> InformationIntegerKey
        C++: static InformationIntegerKey *REQUIRES_TIME_DOWNSTREAM()
        CompositeDataPipeline specific keys
        """
        ret = wrap_vtk(self._vtk_obj.REQUIRES_TIME_DOWNSTREAM())
        return ret
        

    def UPDATE_COMPOSITE_INDICES(self):
        """
        V.update__composite__indices() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *UPDATE_COMPOSITE_INDICES(
            )
        UPDATE_COMPOSITE_INDICES is a key placed in the request to
        request a set of composite indices from a reader/source producing
        composite dataset. Typically, the reader publishes its structure
        using COMPOSITE_DATA_META_DATA() and then the sink requests
        blocks of interest using UPDATE_COMPOSITE_INDICES(). Note that
        UPDATE_COMPOSITE_INDICES has to be sorted vector with increasing
        indices.
        *** THIS IS AN EXPERIMENTAL FEATURE. IT MAY CHANGE WITHOUT NOTICE
        ***
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_COMPOSITE_INDICES())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeDataPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CompositeDataPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

