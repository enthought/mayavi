"""A TVTK interactor scene widget.  This class only uses TVTK and
Traits.  It does not even use any Pyface widgets.  This is nice when
you want to create a raw TVTK window but with some nice funcationality
that is similar to the widgets.  It is also the base class for the
toolkit specific classes since it implements the core
functionality. See the class docs for more details.

"""
# Author: Prabhu Ramachandran <prabhu@enthought.com>
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

import os
import os.path

from apptools.persistence import state_pickler
from tvtk.api import tvtk
from tvtk import messenger
from tvtk.tvtk_base import vtk_color_trait
from tvtk.common import configure_input

from traits.api import HasPrivateTraits, HasTraits, Any, Int, \
     Property, Instance, Event, Range, Bool, Trait, Str

from tvtk.pyface import light_manager


def set_magnification(w2if, magnification):
    if hasattr(w2if, 'magnification'):
        w2if.magnification = magnification
    else:
        w2if.scale = magnification, magnification


######################################################################
# `TVTKScene` class.
######################################################################
class TVTKScene(HasPrivateTraits):
    """A TVTK interactor scene widget.

    This widget uses a RenderWindowInteractor and therefore supports
    interaction with VTK widgets.  The widget uses TVTK.  The widget
    also supports the following:

    - Save the scene to a bunch of common (and not so common) image
      formats.

    - save the rendered scene to the clipboard.

    - adding/removing lists/tuples of actors

    - setting the view to useful predefined views (just like in
      MayaVi).

    - If one passes `stereo=1` to the constructor, stereo rendering is
      enabled.  By default this is disabled.  Changing the stereo trait
      has no effect during runtime.

    - One can disable rendering by setting `disable_render` to True.

    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    ###########################################################################
    # Traits.
    ###########################################################################

    # Turn on/off stereo rendering.  This is set on initialization and
    # has no effect once the widget is realized.
    stereo = Bool(False)

    # Perform line smoothing for all renderered lines.  This produces
    # much nicer looking lines but renders slower.  This setting works
    # only when called before the first render.
    line_smoothing = Bool(False)

    # Perform point smoothing for all renderered points.  This
    # produces much nicer looking points but renders slower.  This
    # setting works only when called before the first render.
    point_smoothing = Bool(False)

    # Perform polygon smoothing (anti-aliasing) for all rendered
    # polygons.  This produces much nicer looking points but renders
    # slower.  This setting works only when called before the first
    # render.
    polygon_smoothing = Bool(False)

    # Enable parallel projection.  This trait is synchronized with
    # that of the camera.
    parallel_projection = Bool(False, desc='if the camera uses parallel projection')

    # Disable rendering.
    disable_render = Bool(False, desc='if rendering is to be disabled')

    # Enable off-screen rendering.  This allows a user to render the
    # scene to an image without the need to have the window active.
    # For example, the application can be minimized and the saved
    # scene should be generated correctly.  This is handy for batch
    # scripts and the like.  This works under Win32.  Under Mac OS X
    # and Linux it requires a recent VTK version (later than Oct 2005
    # and ideally later than March 2006) to work correctly.
    off_screen_rendering = Bool(False, desc='if off-screen rendering is enabled')

    # The background color of the window.  This is really a shadow
    # trait of the renderer's background.  Delegation does not seem to
    # work nicely for this.
    background = Trait(vtk_color_trait((0.5, 0.5, 0.5)),
                       desc='the background color of the window')

    # The default foreground color of any actors.  This basically
    # saves the preference and actors will listen to changes --
    # the scene itself does not use this.
    foreground = Trait(vtk_color_trait((1.0, 1.0, 1.0)),
                       desc='the default foreground color of actors')

    # The magnification to use when generating images from the render
    # window.
    magnification = Range(1, 2048, 1,
                          desc='the magnification used when the screen is saved to an image')

    # Specifies the number of frames to use for anti-aliasing when
    # saving a scene.  This basically increases
    # `self.render_window.aa_frames` in order to produce anti-aliased
    # figures when a scene is saved to an image.  It then restores the
    # `aa_frames` in order to get interactive rendering rates.
    anti_aliasing_frames = Range(
        0, 20, 8,
        desc='number of frames to use for anti-aliasing when saving a scene'
    )

    # Default JPEG quality.
    jpeg_quality = Range(10, 100, 95, desc='the quality of the JPEG image to produce')

    # Default JPEG progressive setting.
    jpeg_progressive = Bool(True, desc='if the generated JPEG should be progressive')

    # The light manager.
    light_manager = Instance(light_manager.LightManager, record=True)

    # The movie maker instance.
    movie_maker = Instance('tvtk.pyface.movie_maker.MovieMaker', record=True)

    # Is the scene busy or not.
    busy = Property(Bool, record=False)

    ########################################
    # Events

    # Lifecycle events: there are no opening/opened events since the
    # control is actually created in __init__.

    # The control is going to be closed.
    closing = Event(record=False)

    # The control has been closed.
    closed = Event(record=False)

    # Event fired when an actor is added to the scene.
    actor_added = Event(record=False)
    # Event fired when any actor is removed from the scene.
    actor_removed = Event(record=False)

    ########################################
    # Properties.

    # The interactor used by the scene.
    interactor = Property(Instance(tvtk.GenericRenderWindowInteractor))

    # The render_window.
    render_window = Property(Instance(tvtk.RenderWindow))

    # The renderer.
    renderer = Property(Instance(tvtk.Renderer))

    # The camera.
    camera = Property(Instance(tvtk.Camera))

    # The control to mimic the Widget behavior.
    control = Any

    ########################################
    # Private traits.

    # A recorder for script recording.
    recorder = Instance(HasTraits, record=False, transient=True)
    # Cached last camera state.
    _last_camera_state = Any(transient=True)
    _camera_observer_id = Int(transient=True)
    _script_id = Str(transient=True)

    # Saved light_manager settings while loading a scene.  The light manager
    # may not be created at the time a scene is loaded from disk, so if it
    # is saved here, when it is created the state is set.
    _saved_light_manager_state = Any(transient=True)

    # The renderer instance.
    _renderer = Instance(tvtk.Renderer)
    _renwin = Instance(tvtk.RenderWindow)
    _interactor = Instance(tvtk.RenderWindowInteractor)
    _camera = Instance(tvtk.Camera)
    _busy_count = Int(0)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, parent=None, **traits):
        """ Initializes the object. """

        # Base class constructor.
        super(TVTKScene, self).__init__(**traits)

        # Used to set the view of the scene.
        self._def_pos = 1
        self.control = self._create_control(parent)
        self._renwin.update_traits()

    def __get_pure_state__(self):
        """Allows us to pickle the scene."""
        # The control attribute is not picklable since it is a VTK
        # object so we remove it.
        d = self.__dict__.copy()
        for x in ['control', '_renwin', '_interactor', '_camera',
                  '_busy_count', '__sync_trait__', 'recorder',
                  '_last_camera_state', '_camera_observer_id',
                  '_saved_light_manager_state',
                  '_script_id', '__traits_listener__']:
            d.pop(x, None)
        # Additionally pickle these.
        d['camera'] = self.camera
        return d

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        # This method is unnecessary since this object will almost
        # never be pickled by itself and only via an object that
        # contains it, therefore __init__ will be called when the
        # scene is constructed.  However, setstate is defined just for
        # completeness.
        state_pickler.set_state(self, state_pickler.loads_state(str_state))

    ###########################################################################
    # 'event' interface.
    ###########################################################################
    def _closed_fired(self):
        self.light_manager = None
        self._interactor = None
        self.movie_maker = None

    ###########################################################################
    # 'Scene' interface.
    ###########################################################################
    def render(self):
        """ Force the scene to be rendered. Nothing is done if the
        `disable_render` trait is set to True."""
        if not self.disable_render:
            self._renwin.render()

    def add_actors(self, actors):
        """ Adds a single actor or a tuple or list of actors to the
        renderer."""
        # Reset the zoom if this is the first actor.
        reset_zoom = (len(self._renderer.actors) == 0 and len(self._renderer.volumes)==0)
        if hasattr(actors, '__iter__'):
            for actor in actors:
                self._renderer.add_actor(actor)
        else:
            self._renderer.add_actor(actors)
        self.actor_added = actors

        if reset_zoom:
            self.reset_zoom()
        else:
            self.render()

    def remove_actors(self, actors):
        """ Removes a single actor or a tuple or list of actors from
        the renderer."""
        if hasattr(actors, '__iter__'):
            for actor in actors:
                self._renderer.remove_actor(actor)
        else:
            self._renderer.remove_actor(actors)
        self.actor_removed = actors
        self.render()

    # Conevenience methods.
    add_actor = add_actors
    remove_actor = remove_actors

    def add_widgets(self, widgets, enabled=True):
        """Adds a single 3D widget or a sequence of widgets to the renderer.
        If `enabled` is True the widget is also enabled once it is added."""
        if not hasattr(widgets, '__iter__'):
            widgets = [widgets]
        iren = self._interactor
        for widget in widgets:
            widget.interactor = iren
            widget.enabled = enabled
        self.render()

    def remove_widgets(self, widgets):
        """Removes a single 3D widget or a sequence of widgets from the
        renderer."""
        if not hasattr(widgets, '__iter__'):
            widgets = [widgets]
        iren = self._interactor
        for widget in widgets:
            if widget.interactor is not None:
                widget.enabled = False
                widget.interactor = None
        self.render()

    def close(self):
        """Close the scene cleanly.  This ensures that the scene is
        shutdown cleanly.  This should be called if you are getting
        async errors when closing a scene from a UI.  This is based on
        the observations of Charl Botha here:

          http://public.kitware.com/pipermail/vtkusers/2008-May/095291.html

        """
        # Return if we are already closed.
        if self._renwin is None:
            return

        # Fire the "closing" event.
        self.closing = True
        # Disable any renders through traits listner callbacks.
        self.disable_render = True
        # Remove sync trait listeners.
        self.sync_trait('background', self._renderer, remove=True)
        self.sync_trait('parallel_projection', self.camera, remove=True)
        self.sync_trait('off_screen_rendering', self._renwin, remove=True)

        # Remove all the renderer's props.
        self._renderer.remove_all_view_props()
        # Set the renderwindow to release all resources and the OpenGL
        # context.
        self._renwin.finalize()
        # Disconnect the interactor from the renderwindow.
        self._interactor.render_window = None
        # Remove the reference to the render window.
        del self._renwin
        # Fire the "closed" event.
        self.closed = True

    def x_plus_view(self):
        """View scene down the +X axis. """
        self._update_view(self._def_pos, 0, 0, 0, 0, 1)
        self._record_methods('x_plus_view()')

    def x_minus_view(self):
        """View scene down the -X axis. """
        self._update_view(-self._def_pos, 0, 0, 0, 0, 1)
        self._record_methods('x_minus_view()')

    def z_plus_view(self):
        """View scene down the +Z axis. """
        self._update_view(0, 0, self._def_pos, 0, 1, 0)
        self._record_methods('z_plus_view()')

    def z_minus_view(self):
        """View scene down the -Z axis. """
        self._update_view(0, 0, -self._def_pos, 0, 1, 0)
        self._record_methods('z_minus_view()')

    def y_plus_view(self):
        """View scene down the +Y axis. """
        self._update_view(0, self._def_pos, 0, 1, 0, 0)
        self._record_methods('y_plus_view()')

    def y_minus_view(self):
        """View scene down the -Y axis. """
        self._update_view(0, -self._def_pos, 0, 1, 0, 0)
        self._record_methods('y_minus_view()')

    def isometric_view(self):
        """Set the view to an iso-metric view. """
        self._update_view(self._def_pos, self._def_pos, self._def_pos,
                          0, 0, 1)
        self._record_methods('isometric_view()')

    def reset_zoom(self):
        """Reset the camera so everything in the scene fits."""
        self._renderer.reset_camera()
        self.render()
        self._record_methods('reset_zoom()')

    def save(self, file_name, size=None, **kw_args):
        """Saves rendered scene to one of several image formats
        depending on the specified extension of the filename.

        If an additional size (2-tuple) argument is passed the window
        is resized to the specified size in order to produce a
        suitably sized output image.  Please note that when the window
        is resized, the window may be obscured by other widgets and
        the camera zoom is not reset which is likely to produce an
        image that does not reflect what is seen on screen.

        Any extra keyword arguments are passed along to the respective
        image format's save method.
        """
        ext = os.path.splitext(file_name)[1]
        meth_map = {'.ps': 'ps', '.bmp': 'bmp', '.tiff': 'tiff',
                    '.png': 'png', '.jpg': 'jpg', '.jpeg': 'jpg',
                    '.iv': 'iv', '.wrl': 'vrml', '.vrml':'vrml',
                    '.oogl': 'oogl', '.rib': 'rib', '.obj': 'wavefront',
                    '.eps': 'gl2ps', '.pdf':'gl2ps', '.tex': 'gl2ps',
                    '.x3d': 'x3d', '.pov': 'povray'}
        if ext.lower() not in meth_map:
            raise ValueError(
                'Unable to find suitable image type for given file extension.'
            )
        meth = getattr(self, 'save_' + meth_map[ext.lower()])
        if size is not None:
            orig_size = self.get_size()
            self.set_size(size)
            meth(file_name, **kw_args)
            self.set_size(orig_size)
            self._record_methods('save(%r, %r)'%(file_name, size))
        else:
            meth(file_name, **kw_args)
            self._record_methods('save(%r)'%(file_name))

    def save_ps(self, file_name):
        """Saves the rendered scene to a rasterized PostScript image.
        For vector graphics use the save_gl2ps method."""
        if len(file_name) != 0:
            w2if = self._get_window_to_image()
            ex = tvtk.PostScriptWriter()
            ex.file_name = file_name
            configure_input(ex, w2if)
            self._exporter_write(ex)

    def save_bmp(self, file_name):
        """Save to a BMP image file."""
        if len(file_name) != 0:
            w2if = self._get_window_to_image()
            ex = tvtk.BMPWriter()
            ex.file_name = file_name
            configure_input(ex, w2if)
            self._exporter_write(ex)

    def save_tiff(self, file_name):
        """Save to a TIFF image file."""
        if len(file_name) != 0:
            w2if = self._get_window_to_image()
            ex = tvtk.TIFFWriter()
            ex.file_name = file_name
            configure_input(ex, w2if)
            self._exporter_write(ex)

    def save_png(self, file_name):
        """Save to a PNG image file."""
        if len(file_name) != 0:
            w2if = self._get_window_to_image()
            ex = tvtk.PNGWriter()
            ex.file_name = file_name
            configure_input(ex, w2if)
            self._exporter_write(ex)

    def save_jpg(self, file_name, quality=None, progressive=None):
        """Arguments: file_name if passed will be used, quality is the
        quality of the JPEG(10-100) are valid, the progressive
        arguments toggles progressive jpegs."""
        if len(file_name) != 0:
            if not quality and not progressive:
                quality, progressive = self.jpeg_quality, self.jpeg_progressive
            w2if = self._get_window_to_image()
            ex = tvtk.JPEGWriter()
            ex.quality = quality
            ex.progressive = progressive
            ex.file_name = file_name
            configure_input(ex, w2if)
            self._exporter_write(ex)

    def save_iv(self, file_name):
        """Save to an OpenInventor file."""
        if len(file_name) != 0:
            ex = tvtk.IVExporter()
            self._lift()
            ex.input = self._renwin
            ex.file_name = file_name
            self._exporter_write(ex)

    def save_vrml(self, file_name):
        """Save to a VRML file."""
        if len(file_name) != 0:
            ex = tvtk.VRMLExporter()
            self._lift()
            ex.input = self._renwin
            ex.file_name = file_name
            self._exporter_write(ex)

    def save_oogl(self, file_name):
        """Saves the scene to a Geomview OOGL file. Requires VTK 4 to
        work."""
        if len(file_name) != 0:
            ex = tvtk.OOGLExporter()
            self._lift()
            ex.input = self._renwin
            ex.file_name = file_name
            self._exporter_write(ex)

    def save_rib(self, file_name, bg=0, resolution=None, resfactor=1.0):
        """Save scene to a RenderMan RIB file.

        Keyword Arguments:

        file_name -- File name to save to.

        bg -- Optional background option.  If 0 then no background is
        saved.  If non-None then a background is saved.  If left alone
        (defaults to None) it will result in a pop-up window asking
        for yes/no.

        resolution -- Specify the resolution of the generated image in
        the form of a tuple (nx, ny).

        resfactor -- The resolution factor which scales the resolution.
        """
        if resolution is None:
            # get present window size
            Nx, Ny = self.render_window.size
        else:
            try:
                Nx, Ny = resolution
            except TypeError:
                raise TypeError(
                    "Resolution (%s) should be a sequence with two elements"%resolution
                )

        if len(file_name) == 0:
            return

        f_pref = os.path.splitext(file_name)[0]
        ex = tvtk.RIBExporter()
        ex.size = int(resfactor*Nx), int(resfactor*Ny)
        ex.file_prefix = f_pref
        ex.texture_prefix = f_pref + "_tex"
        self._lift()
        ex.render_window = self._renwin
        ex.background = bg

        self._exporter_write(ex)

    def save_wavefront(self, file_name):
        """Save scene to a Wavefront OBJ file.  Two files are
        generated.  One with a .obj extension and another with a .mtl
        extension which contains the material properties.

        Keyword Arguments:

        file_name -- File name to save to
        """
        if len(file_name) != 0:
            ex = tvtk.OBJExporter()
            self._lift()
            ex.input = self._renwin
            f_pref = os.path.splitext(file_name)[0]
            ex.file_prefix = f_pref
            self._exporter_write(ex)

    def save_gl2ps(self, file_name, exp=None):
        """Save scene to a vector PostScript/EPS/PDF/TeX file using
        GL2PS.  If you choose to use a TeX file then note that only
        the text output is saved to the file.  You will need to save
        the graphics separately.

        Keyword Arguments:

        file_name -- File name to save to.

        exp -- Optionally configured vtkGL2PSExporter object.
        Defaults to None and this will use the default settings with
        the output file type chosen based on the extention of the file
        name.
        """

        # Make sure the exporter is available.
        if not hasattr(tvtk, 'GL2PSExporter'):
            msg = "Saving as a vector PS/EPS/PDF/TeX file using GL2PS is "\
                  "either not supported by your version of VTK or "\
                  "you have not configured VTK to work with GL2PS -- read "\
                  "the documentation for the vtkGL2PSExporter class."
            print(msg)
            return

        if len(file_name) != 0:
            f_prefix, f_ext = os.path.splitext(file_name)
            ex = None
            if exp:
                ex = exp
                if not isinstance(exp, tvtk.GL2PSExporter):
                    msg = "Need a vtkGL2PSExporter you passed a "\
                          "%s"%exp.__class__.__name__
                    raise TypeError(msg)
                ex.file_prefix = f_prefix
            else:
                ex = tvtk.GL2PSExporter()
                # defaults
                ex.file_prefix = f_prefix
                if f_ext == ".ps":
                    ex.file_format = 'ps'
                elif f_ext == ".tex":
                    ex.file_format = 'tex'
                elif f_ext == ".pdf":
                    ex.file_format = 'pdf'
                else:
                    ex.file_format = 'eps'
                ex.sort = 'bsp'
                ex.compress = 1
                ex.edit_traits(kind='livemodal')

            self._lift()
            ex.render_window = self._renwin
            if ex.write3d_props_as_raster_image:
                self._exporter_write(ex)
            else:
                ex.write()
            # Work around for a bug in VTK where it saves the file as a
            # .pdf.gz when the file is really a PDF file.
            if f_ext == '.pdf' and os.path.exists(f_prefix + '.pdf.gz'):
                os.rename(f_prefix + '.pdf.gz', file_name)

    def save_x3d(self, file_name):
        """Save scene to an X3D file (http://www.web3d.org/x3d/).

        Keyword Arguments:

        file_name -- File name to save to.
        """
        # Make sure the exporter is available.
        if not hasattr(tvtk, 'X3DExporter'):
            msg = "Saving as a X3D file does not appear to be  "\
                  "supported by your version of VTK."
            print(msg)
            return

        if len(file_name) != 0:
            ex = tvtk.X3DExporter()
            ex.input = self._renwin
            ex.file_name = file_name
            ex.update()
            ex.write()

    def save_povray(self, file_name):
        """Save scene to a POVRAY (Persistence of Vision Raytracer),
        file (http://www.povray.org).

        Keyword Arguments:

        file_name -- File name to save to.
        """
        # Make sure the exporter is available.
        if not hasattr(tvtk, 'POVExporter'):
            msg = "Saving as a POVRAY file does not appear to be  "\
                  "supported by your version of VTK."
            print(msg)
            return

        if len(file_name) != 0:
            ex = tvtk.POVExporter()
            ex.input = self._renwin
            if hasattr(ex, 'file_name'):
                ex.file_name = file_name
            else:
                ex.file_prefix = os.path.splitext(file_name)[0]
            ex.update()
            ex.write()

    def get_size(self):
        """Return size of the render window."""
        return self._interactor.size

    def set_size(self, size):
        """Set the size of the window."""
        self._interactor.size = size
        self._renwin.size = size


    ###########################################################################
    # Properties.
    ###########################################################################
    def _get_interactor(self):
        """Returns the vtkRenderWindowInteractor of the parent class"""
        return self._interactor

    def _set_interactor(self, iren):
        if self._interactor is not None:
            self._interactor.render_window = None
        self._interactor = iren
        iren.render_window = self._renwin

    def _get_render_window(self):
        """Returns the scene's render window."""
        return self._renwin

    def _get_renderer(self):
        """Returns the scene's renderer."""
        return self._renderer

    def _get_camera(self):
        """ Returns the active camera. """
        return self._renderer.active_camera

    def _get_busy(self):
        return self._busy_count > 0

    def _set_busy(self, value):
        """The `busy` trait is either `True` or `False`.  However,
        this could be problematic since we could have two methods
        `foo` and `bar that both set `scene.busy = True`.  As soon as
        `bar` is done it sets `busy` back to `False`.  This is wrong
        since the UI is still busy as `foo` is not done yet.  We
        therefore store the number of busy calls and either increment
        it or decrement it and change the state back to `False` only
        when the count is zero.
        """
        bc = self._busy_count
        if value:
            bc += 1
        else:
            bc -= 1
            bc = max(0, bc)

        self._busy_count = bc
        if bc == 1:
            self.trait_property_changed('busy', False, True)
        if bc == 0:
            self.trait_property_changed('busy', True, False)

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the widget. """

        if self.off_screen_rendering:
            if hasattr(tvtk, 'EGLRenderWindow'):
                renwin = tvtk.EGLRenderWindow()
            elif hasattr(tvtk, 'OSOpenGLRenderWindow'):
                renwin = tvtk.OSOpenGLRenderWindow()
            else:
                renwin = tvtk.RenderWindow()
                # If we are doing offscreen rendering we set the window size to
                # (1,1) so the window does not appear at all
                renwin.size = (1, 1)

            self._renwin = renwin
            self._interactor = tvtk.GenericRenderWindowInteractor(
                render_window=renwin
            )
        else:
            renwin = self._renwin = tvtk.RenderWindow()
            self._interactor = tvtk.RenderWindowInteractor(
                render_window=renwin
            )

        renwin.trait_set(point_smoothing=self.point_smoothing,
                         line_smoothing=self.line_smoothing,
                         polygon_smoothing=self.polygon_smoothing)
        # Create a renderer and add it to the renderwindow
        self._renderer = tvtk.Renderer()
        renwin.add_renderer(self._renderer)
        # Save a reference to our camera so it is not GC'd -- needed for
        # the sync_traits to work.
        self._camera = self.camera

        # Sync various traits.
        self._renderer.background = self.background
        self.sync_trait('background', self._renderer)
        self._renderer.on_trait_change(self.render, 'background')
        self._camera.parallel_projection = self.parallel_projection
        self.sync_trait('parallel_projection', self._camera)
        renwin.off_screen_rendering = self.off_screen_rendering
        self.sync_trait('off_screen_rendering', self._renwin)
        self.render_window.on_trait_change(self.render, 'off_screen_rendering')
        self.render_window.on_trait_change(self.render, 'stereo_render')
        self.render_window.on_trait_change(self.render, 'stereo_type')
        self.camera.on_trait_change(self.render, 'parallel_projection')

        self._interactor.initialize()
        self._interactor.render()
        self.light_manager = light_manager.LightManager(self)
        if self.off_screen_rendering:
            # We want the default size to be the normal (300, 300).
            # Setting the size now should not resize the window if
            # offscreen is working properly in VTK.
            renwin.size = (300, 300)

        return self._interactor

    def _get_window_to_image(self):
        w2if = tvtk.WindowToImageFilter(
            read_front_buffer=not self.off_screen_rendering
        )
        set_magnification(w2if, self.magnification)
        self._lift()
        w2if.input = self._renwin
        return w2if

    def _lift(self):
        """Lift the window to the top. Useful when saving screen to an
        image."""
        return

    def _exporter_write(self, ex):
        """Abstracts the exporter's write method."""
        # Bumps up the anti-aliasing frames when the image is saved so
        # that the saved picture looks nicer.
        rw = self.render_window
        if hasattr(rw, 'aa_frames'):
            aa_frames = rw.aa_frames
            rw.aa_frames = self.anti_aliasing_frames
        else:
            aa_frames = rw.multi_samples
            rw.multi_samples = self.anti_aliasing_frames
        rw.render()
        ex.update()
        ex.write()
        # Set the frames back to original setting.
        if hasattr(rw, 'aa_frames'):
            rw.aa_frames = aa_frames
        else:
            rw.multi_samples = aa_frames
        rw.render()

    def _update_view(self, x, y, z, vx, vy, vz):
        """Used internally to set the view."""
        camera = self.camera
        camera.focal_point = 0.0, 0.0, 0.0
        camera.position = x, y, z
        camera.view_up = vx, vy, vz
        self._renderer.reset_camera()
        self.render()

    def _disable_render_changed(self, val):
        if not val and self._renwin is not None:
            self.render()

    def _record_methods(self, calls):
        """A method to record a simple method called on self.  We need a
        more powerful and less intrusive way like decorators to do this.
        Note that calls can be a string with new lines in which case we
        interpret this as multiple calls.
        """
        r = self.recorder
        if r is not None:
            sid = self._script_id
            for call in calls.split('\n'):
                r.record('%s.%s'%(sid, call))

    def _record_camera_position(self, vtk_obj=None, event=None):
        """Callback to record the camera position."""
        r = self.recorder
        if r is not None:
            state = self._get_camera_state()
            lcs = self._last_camera_state
            if state != lcs:
                self._last_camera_state = state
                sid = self._script_id
                for key, value in state:
                    r.record('%s.camera.%s = %r'%(sid, key, value))
                r.record('%s.camera.compute_view_plane_normal()'%sid)
                r.record('%s.render()'%sid)

    def _get_camera_state(self):
        c = self.camera
        state = []
        state.append(('position', list(c.position)))
        state.append(('focal_point', list(c.focal_point)))
        state.append(('view_angle', c.view_angle))
        state.append(('view_up', list(c.view_up)))
        state.append(('clipping_range', list(c.clipping_range)))
        return state

    def _recorder_changed(self, r):
        """When the recorder is set we add an event handler so we can
        record the change to the camera position after the interaction.
        """
        iren = self._interactor
        if r is not None:
            self._script_id = r.get_script_id(self)
            id = iren.add_observer('EndInteractionEvent',
                                   messenger.send)
            self._camera_observer_id = id
            i_vtk = tvtk.to_vtk(iren)
            messenger.connect(i_vtk, 'EndInteractionEvent',
                              self._record_camera_position)
        else:
            self._script_id = ''
            iren.remove_observer(self._camera_observer_id)
            i_vtk = tvtk.to_vtk(iren)
            messenger.disconnect(i_vtk, 'EndInteractionEvent',
                                 self._record_camera_position)

    def _light_manager_changed(self, lm):
        if lm is not None:
            if self._saved_light_manager_state is not None:
                lm.__set_pure_state__(self._saved_light_manager_state)
                self._saved_light_manager_state = None

    def _movie_maker_default(self):
        from tvtk.pyface.movie_maker import MovieMaker
        return MovieMaker(scene=self)


######################################################################
# `TVTKScene` class.
######################################################################
class TVTKWindow(HasTraits):
    """A basic TVTK window class that can be used in the MayaVi engine
    for visualization without envisage/pyface etc.  Technically we
    could just have used the `TVTKScene` class but we want to support
    the closing and activated events since they are used to notify the
    MayaVi engine if the window is closed or activated.  In this case
    we do nothing but honour the interface.
    """

    closing = Event
    activated = Event
    def __init__(self, **traits):
        """All the keyword arguments are passed on to the `TVTKScene`
        instance created."""
        self.scene = TVTKScene(**traits)
