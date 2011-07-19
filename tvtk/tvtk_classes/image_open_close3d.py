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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageOpenClose3D(ImageAlgorithm):
    """
    ImageOpenClose3D - Will perform opening or closing.
    
    Superclass: ImageAlgorithm
    
    ImageOpenClose3D performs opening or closing by having two
    ImageErodeDilates in series.  The size of operation is determined
    by the method set_kernel_size, and the operator is an ellipse.
    open_value and close_value determine how the filter behaves.  For
    binary images Opening and closing behaves as expected. Close value is
    first dilated, and then eroded. Open value is first eroded, and then
    dilated. Degenerate two dimensional opening/closing can be achieved
    by setting the one axis the 3d kernel_size to 1. Values other than
    open value and close value are not touched. This enables the filter
    to processes segmented images containing more than two tags.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageOpenClose3D, obj, update, **traits)
    
    open_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Determines the value that will opened. Open value is first
        eroded, and then dilated.
        """
    )
    def _open_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpenValue,
                        self.open_value)

    close_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Determines the value that will closed. Close value is first
        dilated, and then eroded
        """
    )
    def _close_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCloseValue,
                        self.close_value)

    def _get_filter0(self):
        return wrap_vtk(self._vtk_obj.GetFilter0())
    filter0 = traits.Property(_get_filter0, help=\
        """
        Needed for Progress functions
        """
    )

    def _get_filter1(self):
        return wrap_vtk(self._vtk_obj.GetFilter1())
    filter1 = traits.Property(_get_filter1, help=\
        """
        Needed for Progress functions
        """
    )

    def set_kernel_size(self, *args):
        """
        V.set_kernel_size(int, int, int)
        C++: void SetKernelSize(int size0, int size1, int size2)
        Selects the size of gaps or objects removed.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernelSize, *args)
        return ret

    _updateable_traits_ = \
    (('open_value', 'GetOpenValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('close_value', 'GetCloseValue'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'close_value', 'open_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageOpenClose3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageOpenClose3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['close_value', 'open_value']),
            title='Edit ImageOpenClose3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageOpenClose3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

