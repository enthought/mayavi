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


class ImageBlend(ThreadedImageAlgorithm):
    """
    ImageBlend - blend images together using alpha or opacity
    
    Superclass: ThreadedImageAlgorithm
    
    ImageBlend takes L, LA, RGB, or RGBA images as input and blends
    them according to the alpha values and/or the opacity setting for
    each input.
    
    The spacing, origin, extent, and number of components of the output
    are the same as those for the first input.  If the input has an alpha
    component, then this component is copied unchanged into the output.
    In addition, if the first input has either one component or two
    components i.e. if it is either L (greyscale) or LA (greyscale +
    alpha) then all other inputs must also be L or LA.
    
    Different blending modes are available:
    
    Normal (default) : This is the standard blending mode used by open_gl
    and other graphics packages.  The output always has the same number
    of components and the same extent as the first input.  The alpha
    value of the first input is not used in the blending computation,
    instead it is copied directly to the output.
    
    output <- input[0]
    foreach input i {
      foreach pixel px {
        r <- input[i](px)(alpha) * opacity[i]
        f <- (255 - r)
        output(px) <- output(px) * f + input(px) * r
      }
    }
    
    Compound : Images are compounded together and each component is
    scaled by the sum of the alpha/opacity values. Use the
    compound_threshold method to set specify a threshold in compound mode.
    Pixels with opacity*alpha less or equal than this threshold are
    ignored. The alpha value of the first input, if present, is NOT
    copied to the alpha value of the output.  The output always has the
    same number of components and the same extent as the first input.
    
    output <- 0
    foreach pixel px {
      sum <- 0
      foreach input i {
        r <- input[i](px)(alpha) * opacity(i)
        sum <- sum + r
        if r > threshold {
          output(px) <- output(px) + input(px) * r
        }
      }
      output(px) <- output(px) / sum
    }
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageBlend, obj, update, **traits)
    
    blend_mode = traits.Trait('normal',
    tvtk_base.TraitRevPrefixMap({'compound': 1, 'normal': 0}), help=\
        """
        Set the blend mode
        """
    )
    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode_)

    def get_opacity(self, *args):
        """
        V.get_opacity(int) -> float
        C++: double GetOpacity(int idx)
        Set the opacity of an input image: the alpha values of the image
        are multiplied by the opacity.  The opacity of image idx=0 is
        ignored.
        """
        ret = self._wrap_call(self._vtk_obj.GetOpacity, *args)
        return ret

    def set_opacity(self, *args):
        """
        V.set_opacity(int, float)
        C++: void SetOpacity(int idx, double opacity)
        Set the opacity of an input image: the alpha values of the image
        are multiplied by the opacity.  The opacity of image idx=0 is
        ignored.
        """
        ret = self._wrap_call(self._vtk_obj.SetOpacity, *args)
        return ret

    compound_threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify a threshold in compound mode. Pixels with opacity*alpha
        less or equal the threshold are ignored.
        """
    )
    def _compound_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompoundThreshold,
                        self.compound_threshold)

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    def _set_stencil(self, arg):
        old_val = self._get_stencil()
        self._wrap_call(self._vtk_obj.SetStencil,
                        deref_vtk(arg))
        self.trait_property_changed('stencil', old_val, arg)
    stencil = traits.Property(_get_stencil, _set_stencil, help=\
        """
        Set a stencil to apply when blending the data.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int num)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get one input to this filter. This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use Algorithm::GetInputConnection(0, num).
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(int, DataObject)
        C++: void SetInput(int num, DataObject *input)
        V.set_input(DataObject)
        C++: void SetInput(DataObject *input)
        Set an Input of this filter.  This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use set_input_connection(), add_input_connection(), and
        replace_nth_input_connection() instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def _get_number_of_inputs(self):
        return self._vtk_obj.GetNumberOfInputs()
    number_of_inputs = traits.Property(_get_number_of_inputs, help=\
        """
        Get the number of inputs to this filter. This method is only for
        support of old-style pipeline connections.  When writing new code
        you should use Algorithm::GetNumberOfInputConnections(0).
        """
    )

    def replace_nth_input_connection(self, *args):
        """
        V.replace_nth_input_connection(int, AlgorithmOutput)
        C++: virtual void ReplaceNthInputConnection(int idx,
            AlgorithmOutput *input)
        Replace one of the input connections with a new input.  You can
        only replace input connections that you previously created with
        add_input_connection() or, in the case of the first input, with
        set_input_connection().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReplaceNthInputConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('number_of_threads', 'GetNumberOfThreads'),
    ('compound_threshold', 'GetCompoundThreshold'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('blend_mode',
    'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'compound_threshold',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageBlend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageBlend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['blend_mode'], ['compound_threshold',
            'number_of_threads']),
            title='Edit ImageBlend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageBlend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

