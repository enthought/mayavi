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


class ImageRectilinearWipe(ThreadedImageAlgorithm):
    """
    ImageRectilinearWipe - make a rectilinear combination of two
    images.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageRectilinearWipe makes a rectilinear combination of two
    images. The two input images must correspond in size, scalar type and
    number of components. The resulting image has four possible
    configurations called:
      Quad - alternate input 0 and input 1 horizontally and
        vertically. Select this with set_wipe_mode_to_quad. The Position
        specifies the location of the quad intersection.
      Corner - 3 of one input and 1 of the other. Select the location of
        input 0 with with set_wipe_mode_to_lower_left,
    set_wipe_mode_to_lower_right,
        set_wipe_mode_to_upper_left and set_wipe_mode_to_upper_right. The Position
        selects the location of the corner.
      Horizontal - alternate input 0 and input 1 with a vertical
        split. Select this with set_wipe_mode_to_horizontal. Position[0]
        specifies the location of the vertical transition between input 0
        and input 1.
      Vertical - alternate input 0 and input 1 with a horizontal
        split. Only the y The intersection point of the rectilinear
    points
        is controlled with the Point ivar.
    
    See Also:
    
    ImageCheckerboard
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageRectilinearWipe, obj, update, **traits)
    
    wipe = traits.Trait('quad',
    tvtk_base.TraitRevPrefixMap({'upper_right': 6, 'lower_left': 3, 'vertical': 2, 'upper_left': 5, 'lower_right': 4, 'quad': 0, 'horizontal': 1}), help=\
        """
        Specify the wipe mode. This mode determnis how input 0 and input
        1 are combined to produce the output. Each mode uses one or both
        of the values stored in Position.
          set_wipe_to_quad - alternate input 0 and input 1 horizontally and
            vertically. The Position specifies the location of the quad
            intersection.
          set_wipe_to_lower_left{_lower_right,_upper_left._upper_right} - 3 of one
            input and 1 of the other. Select the location of input 0 to
        the
            lower_left{_lower_right,_upper_left,_upper_right}. Position
            selects the location of the corner.
          set_wipe_to_horizontal - alternate input 0 and input 1 with a
        vertical
            split. Position[0] specifies the location of the vertical
            transition between input 0 and input 1.
          set_wipe_to_vertical - alternate input 0 and input 1 with a
            horizontal split. Position[1] specifies the location of the
            horizonal transition between input 0 and input 1.
        """
    )
    def _wipe_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWipe,
                        self.wipe_)

    position = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    axis = traits.Array(shape=(2,), value=(0, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxis,
                        self.axis)

    def set_input1(self, *args):
        """
        V.set_input1(DataObject)
        C++: virtual void SetInput1(DataObject *in)
        Set the two inputs to this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1, *my_args)
        return ret

    def set_input2(self, *args):
        """
        V.set_input2(DataObject)
        C++: virtual void SetInput2(DataObject *in)
        Set the two inputs to this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('debug',
    'GetDebug'), ('position', 'GetPosition'), ('wipe', 'GetWipe'),
    ('axis', 'GetAxis'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'wipe', 'axis', 'number_of_threads', 'position',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageRectilinearWipe, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['wipe'], ['axis', 'number_of_threads',
            'position']),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

