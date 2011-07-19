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


class VideoSource(ImageAlgorithm):
    """
    VideoSource - Superclass of video input devices for VTK
    
    Superclass: ImageAlgorithm
    
    VideoSource is a superclass for video input interfaces for VTK.
    The goal is to provide an interface which is very similar to the
    interface of a VCR, where the 'tape' is an internal frame buffer
    capable of holding a preset number of video frames.  Specialized
    versions of this class record input from various video input sources.
    This base class records input from a noise source.
    
    Caveats:
    
    You must call the release_system_resources() method before the
    application exits.  Otherwise the application might hang while trying
    to exit.
    
    See Also:
    
    Win32VideoSource MILVideoSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVideoSource, obj, update, **traits)
    
    auto_advance = tvtk_base.true_bool_trait(help=\
        """
        Set whether to automatically advance the buffer before each grab.
        Default: on
        """
    )
    def _auto_advance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdvance,
                        self.auto_advance_)

    output_format = traits.Trait('luminance',
    tvtk_base.TraitRevPrefixMap({'rgb': 3, 'luminance': 1, 'rgba': 4}), help=\
        """
        Set the output format.  This must be appropriate for device,
        usually only VTK_LUMINANCE, VTK_RGB, and VTK_RGBA are supported.
        """
    )
    def _output_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputFormat,
                        self.output_format_)

    opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        For RGBA output only (4 scalar components), set the opacity. 
        This will not modify the existing contents of the framebuffer,
        only subsequently grabbed frames.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    frame_size = traits.Array(shape=(3,), value=(320, 240, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the full-frame size.  This must be an allowed size for the
        device, the device may either refuse a request for an illegal
        frame size or automatically choose a new frame size. The default
        is usually 320x240x1, but can be device specific. The 'depth'
        should always be 1 (unless you have a device that can handle 3d
        acquisition).
        """
    )
    def _frame_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameSize,
                        self.frame_size)

    frame_buffer_size = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set size of the frame buffer, i.e. the number of frames that the
        'tape' can store.
        """
    )
    def _frame_buffer_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameBufferSize,
                        self.frame_buffer_size)

    start_time_stamp = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        And internal variable which marks the beginning of a Record
        session. These methods are for internal use only.
        """
    )
    def _start_time_stamp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartTimeStamp,
                        self.start_time_stamp)

    frame_rate = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Request a particular frame rate (default 30 frames per second).
        """
    )
    def _frame_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameRate,
                        self.frame_rate)

    output_whole_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _output_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputWholeExtent,
                        self.output_whole_extent)

    data_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    data_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    clip_region = traits.Array(shape=(6,), value=(0, 2147483647, 0, 2147483647, 0, 2147483647), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the clip rectangle for the frames.  The video will be clipped
        before it is copied into the framebuffer.  Changing the
        clip_region will destroy the current contents of the framebuffer.
        The default clip_region is
        (0,VTK_INT_MAX,0,VTK_INT_MAX,0,VTK_INT_MAX).
        """
    )
    def _clip_region_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipRegion,
                        self.clip_region)

    number_of_output_frames = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of frames to copy to the output on each execute.
        The frames will be concatenated along the Z dimension, with the
        most recent frame first. Default: 1
        """
    )
    def _number_of_output_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfOutputFrames,
                        self.number_of_output_frames)

    frame_count = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This value is incremented each time a frame is grabbed. reset it
        to zero (or any other value) at any time.
        """
    )
    def _frame_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameCount,
                        self.frame_count)

    def _get_frame_index(self):
        return self._vtk_obj.GetFrameIndex()
    frame_index = traits.Property(_get_frame_index, help=\
        """
        Get the frame index relative to the 'beginning of the tape'. 
        This value wraps back to zero if it increases past the
        frame_buffer_size.
        """
    )

    def _get_frame_time_stamp(self):
        return self._vtk_obj.GetFrameTimeStamp()
    frame_time_stamp = traits.Property(_get_frame_time_stamp, help=\
        """
        Get a time stamp in seconds (resolution of milliseconds) for a
        video frame.   Time began on Jan 1, 1970.  You can specify a
        number (negative or positive) to specify the position of the
        video frame relative to the current frame.
        """
    )

    def _get_initialized(self):
        return self._vtk_obj.GetInitialized()
    initialized = traits.Property(_get_initialized, help=\
        """
        Initialize the hardware.  This is called automatically on the
        first Update or Grab.
        """
    )

    def _get_playing(self):
        return self._vtk_obj.GetPlaying()
    playing = traits.Property(_get_playing, help=\
        """
        Are we in play mode? (record mode and play mode are mutually
        exclusive).
        """
    )

    def _get_recording(self):
        return self._vtk_obj.GetRecording()
    recording = traits.Property(_get_recording, help=\
        """
        Are we in record mode? (record mode and play mode are mutually
        exclusive).
        """
    )

    def fast_forward(self):
        """
        V.fast_forward()
        C++: virtual void FastForward()
        fast_forward to the last frame that was recorded (i.e. to the
        frame that has the most recent timestamp).
        """
        ret = self._vtk_obj.FastForward()
        return ret
        

    def grab(self):
        """
        V.grab()
        C++: virtual void Grab()
        Grab a single video frame.
        """
        ret = self._vtk_obj.Grab()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Initialize the hardware.  This is called automatically on the
        first Update or Grab.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def internal_grab(self):
        """
        V.internal_grab()
        C++: virtual void InternalGrab()
        The internal function which actually does the grab.  You will
        definitely want to override this if you develop a VideoSource
        subclass.
        """
        ret = self._vtk_obj.InternalGrab()
        return ret
        

    def play(self):
        """
        V.play()
        C++: virtual void Play()
        Play through the 'tape' sequentially at the specified frame rate.
        If you have just finished Recoding, you should call Rewind()
        first.
        """
        ret = self._vtk_obj.Play()
        return ret
        

    def record(self):
        """
        V.record()
        C++: virtual void Record()
        Record incoming video at the specified frame_rate.  The recording
        continues indefinitely until Stop() is called.
        """
        ret = self._vtk_obj.Record()
        return ret
        

    def release_system_resources(self):
        """
        V.release_system_resources()
        C++: virtual void ReleaseSystemResources()
        Release the video driver.  This method must be called before
        application exit, or else the application might hang during exit.
        """
        ret = self._vtk_obj.ReleaseSystemResources()
        return ret
        

    def rewind(self):
        """
        V.rewind()
        C++: virtual void Rewind()
        Rewind to the frame with the earliest timestamp.  Record
        operations will start on the following frame, therefore if you
        want to re-record over this frame you must call Seek(-1) before
        calling Grab() or Record().
        """
        ret = self._vtk_obj.Rewind()
        return ret
        

    def seek(self, *args):
        """
        V.seek(int)
        C++: virtual void Seek(int n)
        Seek forwards or backwards by the specified number of frames
        (positive is forward, negative is backward).
        """
        ret = self._wrap_call(self._vtk_obj.Seek, *args)
        return ret

    def stop(self):
        """
        V.stop()
        C++: virtual void Stop()
        Stop recording or playing.
        """
        ret = self._vtk_obj.Stop()
        return ret
        

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('output_whole_extent',
    'GetOutputWholeExtent'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('frame_rate', 'GetFrameRate'), ('clip_region', 'GetClipRegion'),
    ('progress_text', 'GetProgressText'), ('number_of_output_frames',
    'GetNumberOfOutputFrames'), ('debug', 'GetDebug'), ('auto_advance',
    'GetAutoAdvance'), ('abort_execute', 'GetAbortExecute'),
    ('start_time_stamp', 'GetStartTimeStamp'), ('data_spacing',
    'GetDataSpacing'), ('frame_size', 'GetFrameSize'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('output_format',
    'GetOutputFormat'), ('frame_count', 'GetFrameCount'),
    ('frame_buffer_size', 'GetFrameBufferSize'), ('data_origin',
    'GetDataOrigin'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_advance', 'debug', 'global_warning_display',
    'release_data_flag', 'output_format', 'clip_region', 'data_origin',
    'data_spacing', 'frame_buffer_size', 'frame_count', 'frame_rate',
    'frame_size', 'number_of_output_frames', 'opacity',
    'output_whole_extent', 'progress_text', 'start_time_stamp'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VideoSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_advance'], ['output_format'], ['clip_region',
            'data_origin', 'data_spacing', 'frame_buffer_size', 'frame_count',
            'frame_rate', 'frame_size', 'number_of_output_frames', 'opacity',
            'output_whole_extent', 'start_time_stamp']),
            title='Edit VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

