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

from tvtk.tvtk_classes.executive import Executive


class DemandDrivenPipeline(Executive):
    """
    DemandDrivenPipeline - Executive supporting on-demand execution.
    
    Superclass: Executive
    
    DemandDrivenPipeline is an executive that will execute an
    algorithm only when its outputs are out-of-date with respect to its
    inputs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDemandDrivenPipeline, obj, update, **traits)
    
    def get_release_data_flag(self, *args):
        """
        V.get_release_data_flag(int) -> int
        C++: virtual int GetReleaseDataFlag(int port)
        Get whether the given output port releases data when it is
        consumed.
        """
        ret = self._wrap_call(self._vtk_obj.GetReleaseDataFlag, *args)
        return ret

    def set_release_data_flag(self, *args):
        """
        V.set_release_data_flag(int, int) -> int
        C++: virtual int SetReleaseDataFlag(int port, int n)
        Set whether the given output port releases data when it is
        consumed.  Returns 1 if the the value changes and 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.SetReleaseDataFlag, *args)
        return ret

    def _get_pipeline_m_time(self):
        return self._vtk_obj.GetPipelineMTime()
    pipeline_m_time = traits.Property(_get_pipeline_m_time, help=\
        """
        Get the pipeline_m_time for this exective.
        """
    )

    def DATA_NOT_GENERATED(self):
        """
        V.data__not__generated() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_NOT_GENERATED()
        Key to store a mark for an output that will not be generated.
        Algorithms use this to tell the executive that they will not
        generate certain outputs for a REQUEST_DATA.
        """
        ret = wrap_vtk(self._vtk_obj.DATA_NOT_GENERATED())
        return ret
        

    def new_data_object(self, *args):
        """
        V.new_data_object(string) -> DataObject
        C++: static DataObject *NewDataObject(const char *type)
        Create (New) and return a data object of the given type. This is
        here for backwards compatibility. Use
        DataObjectTypes::NewDataObject() instead.
        """
        ret = self._wrap_call(self._vtk_obj.NewDataObject, *args)
        return wrap_vtk(ret)

    def RELEASE_DATA(self):
        """
        V.release__data() -> InformationIntegerKey
        C++: static InformationIntegerKey *RELEASE_DATA()
        Key to specify in pipeline information the request that data be
        released after it is used.
        """
        ret = wrap_vtk(self._vtk_obj.RELEASE_DATA())
        return ret
        

    def REQUEST_DATA(self):
        """
        V.request__data() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_DATA()
        Key defining a request to make sure the output data are up to
        date.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_DATA())
        return ret
        

    def REQUEST_DATA_NOT_GENERATED(self):
        """
        V.request__data__not__generated() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_DATA_NOT_GENERATED()
        Key defining a request to mark outputs that will NOT be generated
        during a REQUEST_DATA.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_DATA_NOT_GENERATED())
        return ret
        

    def REQUEST_DATA_OBJECT(self):
        """
        V.request__data__object() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_DATA_OBJECT()
        Key defining a request to make sure the output data objects
        exist.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_DATA_OBJECT())
        return ret
        

    def REQUEST_INFORMATION(self):
        """
        V.request__information() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_INFORMATION()
        Key defining a request to make sure the output information is up
        to date.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_INFORMATION())
        return ret
        

    def REQUEST_REGENERATE_INFORMATION(self):
        """
        V.request__regenerate__information() -> InformationIntegerKey
        C++: static InformationIntegerKey *REQUEST_REGENERATE_INFORMATION(
            )
        Key to be used for REQUEST_INFORMATION and REQUEST_DATA_OBJECT
        passes when you modification time should not be taken into
        account.
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_REGENERATE_INFORMATION())
        return ret
        

    def update_data(self, *args):
        """
        V.update_data(int) -> int
        C++: virtual int UpdateData(int outputPort)
        Bring the output data up to date.  This should be called only
        when information is up to date.  Use the Update method if it is
        not known that the information is up to date.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateData, *args)
        return ret

    def update_data_object(self):
        """
        V.update_data_object() -> int
        C++: virtual int UpdateDataObject()
        Bring the output data object's existence up to date.  This does
        not actually produce data, but does create the data object that
        will store data produced during the update_data step.
        """
        ret = self._vtk_obj.UpdateDataObject()
        return ret
        

    def update_information(self):
        """
        V.update_information() -> int
        C++: virtual int UpdateInformation()
        Bring the output information up to date.
        """
        ret = self._vtk_obj.UpdateInformation()
        return ret
        

    def update_pipeline_m_time(self):
        """
        V.update_pipeline_m_time() -> int
        C++: virtual int UpdatePipelineMTime()
        Bring the pipeline_m_time up to date.
        """
        ret = self._vtk_obj.UpdatePipelineMTime()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DemandDrivenPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

