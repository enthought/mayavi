"""
TODO:

 * We need a cleaner way to manipulate the camera  and other things as a model.
   The current approach will be far from perfect but should work.

Caveats:

 * You can't have multiple views of the model.  This will not be supported.

"""
# Author: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Dict, Event, \
                                 Instance, List, Property
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.pyface.tvtk_scene import TVTKScene


#####################################################################
# `SceneModelError` class
#####################################################################
class SceneModelError(Exception):
    pass


#####################################################################
# `SceneModel` class
#####################################################################
class SceneModel(TVTKScene):

    ########################################
    # TVTKScene traits.

    picker = Property

    ########################################
    # SceneModel traits.

    # A convenient dictionary based interface to add/remove actors and widgets.
    # This is similar to the interface provided for the ActorEditor.
    actor_map = Dict()

    # This is used primarily to implement the add_actor/remove_actor methods.
    actor_list = List()

    # The actual scene being edited.
    scene_editor = Instance(TVTKScene)

    do_render = Event()

    # Fired when this is activated.
    activated = Event()

    # The control is going to be closed.
    closing = Event()

    # This exists just to mirror the TVTKWindow api.
    scene = Property

    ###################################
    # View related traits.

    # Render_window's view.
    _stereo_view = Group(Item(name='stereo_render'),
                         Item(name='stereo_type'),
                         show_border=True,
                         label='Stereo rendering',
                         )

    # The default view of this object.
    default_view = View(Group(
                            Group(Item(name='background'),
                                  Item(name='foreground'),
                                  Item(name='parallel_projection'),
                                  Item(name='disable_render'),
                                  Item(name='off_screen_rendering'),
                                  Item(name='jpeg_quality'),
                                  Item(name='jpeg_progressive'),
                                  Item(name='magnification'),
                                  Item(name='anti_aliasing_frames'),
                                  ),
                            Group(Item(name='render_window',
                                       style='custom',
                                       visible_when='object.stereo',
                                       editor=InstanceEditor(view=View(_stereo_view)),                                       show_label=False),
                                  ),
                            label='Scene'),
                        Group(Item(name='light_manager',
                                   style='custom',
                                   editor=InstanceEditor(),
                                   show_label=False),
                                   label='Lights')
                        )

    ###################################
    # Private traits.

    # Used by the editor to determine if the widget was enabled or not.
    enabled_info = Dict()

    def __init__(self, parent=None, **traits):
        """ Initializes the object. """
        # Base class constructor.  We call TVTKScene's super here on purpose.
        # Calling TVTKScene's init will create a new window which we do not
        # want.
        super(TVTKScene, self).__init__(**traits)
        self.control = None

    ######################################################################
    # TVTKScene API.
    ######################################################################
    def render(self):
        """ Force the scene to be rendered. Nothing is done if the
        `disable_render` trait is set to True."""

        self.do_render = True

    def add_actors(self, actors):
        """ Adds a single actor or a tuple or list of actors to the
        renderer."""
        if hasattr(actors, '__iter__'):
            self.actor_list.extend(actors)
        else:
            self.actor_list.append(actors)

    def remove_actors(self, actors):
        """ Removes a single actor or a tuple or list of actors from
        the renderer."""
        my_actors = self.actor_list
        if hasattr(actors, '__iter__'):
            for actor in actors:
                my_actors.remove(actor)
        else:
            my_actors.remove(actors)

    # Conevenience methods.
    add_actor = add_actors
    remove_actor = remove_actors

    def add_widgets(self, widgets, enabled=True):
        """Adds widgets to the renderer.
        """
        if not hasattr(widgets, '__iter__'):
            widgets = [widgets]
        for widget in widgets:
            self.enabled_info[widget] = enabled
        self.add_actors(widgets)

    def remove_widgets(self, widgets):
        """Removes widgets from the renderer."""
        if not hasattr(widgets, '__iter__'):
            widgets = [widgets]
        self.remove_actors(widgets)
        for widget in widgets:
            del self.enabled_info[widget]

    def reset_zoom(self):
        """Reset the camera so everything in the scene fits."""
        if self.scene_editor is not None:
            self.scene_editor.reset_zoom()

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
        self._check_scene_editor()
        self.scene_editor.save(file_name, size, **kw_args)

    def save_ps(self, file_name):
        """Saves the rendered scene to a rasterized PostScript image.
        For vector graphics use the save_gl2ps method."""
        self._check_scene_editor()
        self.scene_editor.save_ps(file_name)

    def save_bmp(self, file_name):
        """Save to a BMP image file."""
        self._check_scene_editor()
        self.scene_editor.save_bmp(file_name)

    def save_tiff(self, file_name):
        """Save to a TIFF image file."""
        self._check_scene_editor()
        self.scene_editor.save_tiff(file_name)

    def save_png(self, file_name):
        """Save to a PNG image file."""
        self._check_scene_editor()
        self.scene_editor.save_png(file_name)

    def save_jpg(self, file_name, quality=None, progressive=None):
        """Arguments: file_name if passed will be used, quality is the
        quality of the JPEG(10-100) are valid, the progressive
        arguments toggles progressive jpegs."""
        self._check_scene_editor()
        self.scene_editor.save_jpg(file_name, quality, progressive)

    def save_iv(self, file_name):
        """Save to an OpenInventor file."""
        self._check_scene_editor()
        self.scene_editor.save_iv(file_name)

    def save_vrml(self, file_name):
        """Save to a VRML file."""
        self._check_scene_editor()
        self.scene_editor.save_vrml(file_name)

    def save_oogl(self, file_name):
        """Saves the scene to a Geomview OOGL file. Requires VTK 4 to
        work."""
        self._check_scene_editor()
        self.scene_editor.save_oogl(file_name)

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
        self._check_scene_editor()
        self.scene_editor.save_rib(file_name, bg, resolution, resfactor)

    def save_wavefront(self, file_name):
        """Save scene to a Wavefront OBJ file.  Two files are
        generated.  One with a .obj extension and another with a .mtl
        extension which contains the material proerties.

        Keyword Arguments:

        file_name -- File name to save to
        """
        self._check_scene_editor()
        self.scene_editor.save_wavefront(file_name)

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
        self._check_scene_editor()
        self.scene_editor.save_gl2ps(file_name, exp)

    def save_povray(self, file_name):
        self._check_scene_editor()
        self.scene_editor.save_povray(file_name)

    def save_x3d(self, filename):
        self._check_scene_editor()
        self.scene_editor.save_x3d(file_name)

    def get_size(self):
        """Return size of the render window."""
        self._check_scene_editor()
        return self.scene_editor.get_size()

    def set_size(self, size):
        """Set the size of the window."""
        self._check_scene_editor()
        self.scene_editor.set_size(size)

    def _update_view(self, x, y, z, vx, vy, vz):
        """Used internally to set the view."""
        if self.scene_editor is not None:
            self.scene_editor._update_view(x, y, z, vx, vy, vz)

    def _check_scene_editor(self):
        if self.scene_editor is None:
            msg = """
            This method requires that there be an active scene editor.
            To do this, you will typically need to invoke::
              object.edit_traits()
            where object is the object that contains the SceneModel.
            """
            raise SceneModelError(msg)

    def _scene_editor_changed(self, old, new):
        if new is None:
            self._renderer = None
            self._renwin = None
            self._interactor = None
        else:
            self._renderer = new._renderer
            self._renwin = new._renwin
            self._interactor = new._interactor

    def _get_picker(self):
        """Getter for the picker."""
        se = self.scene_editor
        if se is not None and hasattr(se, 'picker'):
            return se.picker
        return None

    def _get_light_manager(self):
        """Getter for the light manager."""
        se = self.scene_editor
        if se is not None:
            return se.light_manager
        return None

    ######################################################################
    # SceneModel API.
    ######################################################################
    def _get_scene(self):
        """Getter for the scene property."""
        return self

