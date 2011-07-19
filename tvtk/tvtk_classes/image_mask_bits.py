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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageMaskBits(ThreadedImageAlgorithm):
    """
    ImageMaskBits - applies a bit-mask pattern to each component.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMaskBits applies a bit-mask pattern to each component.  The
    bit-mask can be applied using a variety of boolean bitwise operators.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMaskBits, obj, update, **traits)
    
    operation = traits.Trait('and_',
    tvtk_base.TraitRevPrefixMap({'or_': 1, 'and_': 0, 'xor': 2, 'nand': 3, 'nor': 4}), help=\
        """
        Set/Get the boolean operator. Default is AND.
        """
    )
    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    masks = traits.Array(shape=(4,), value=(4294967295L, 4294967295L, 4294967295L, 4294967295L), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _masks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMasks,
                        self.masks)

    def set_mask(self, *args):
        """
        V.set_mask(int)
        C++: void SetMask(unsigned int mask)
        Set/Get the bit-masks. Default is 0xffffffff.
        """
        ret = self._wrap_call(self._vtk_obj.SetMask, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('masks', 'GetMasks'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('operation', 'GetOperation'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'operation', 'masks', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMaskBits, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['operation'], ['masks', 'number_of_threads']),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

