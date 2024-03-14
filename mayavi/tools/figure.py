"""
Functions related to creating the engine or the figures.

"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import gc
import warnings
import copy

import numpy as np

# Enthought imports
from pyface.timer.api import do_later

#  imports
from tvtk.api import tvtk
from tvtk.common import vtk_major_version
from mayavi.core.scene import Scene
from mayavi.core.registry import registry
from .camera import view
from .engine_manager import get_engine, options, set_engine

######################################################################

# A list to store the allocated scene numbers
__scene_number_list = set((0,))


def figure(figure=None, bgcolor=None, fgcolor=None, engine=None,
           size=(400, 350)):
    """ Creates a new scene or retrieves an existing scene. If the mayavi
    engine is not running this also starts it.

    **Keyword arguments**

        :figure: The name of the figure, or handle to it.

        :bgcolor: The color of the background (None is default).

        :fgcolor: The color of the foreground, that is the color of all text
                  annotation labels (axes, orientation axes, scalar bar
                  labels). It should be sufficiently far from `bgcolor`
                  to see the annotation texts. (None is default).

        :engine: The mayavi engine that controls the figure.

        :size: The size of the scene created, in pixels. May not apply
               for certain scene viewer.
    """
    if isinstance(figure, Scene):
        if figure.scene is None:
            engine = registry.find_scene_engine(figure)
        else:
            engine = registry.find_scene_engine(figure.scene)
        set_engine(engine)
        engine.current_scene = figure
    else:
        if engine is None:
            engine = get_engine()
        if figure is None:
            name = max(__scene_number_list) + 1
            __scene_number_list.update((name,))
            name = 'Mayavi Scene %d' % name
            engine.new_scene(name=name, size=size)
            engine.current_scene.name = name
        else:
            if type(figure) in (int, np.intp, np.int8,
                                np.int16, np.int32, np.int64):
                name = int(figure)
                __scene_number_list.update((name,))
                name = 'Mayavi Scene %d' % name
            else:
                name = str(figure)
            # Go looking in the engine see if the scene is not already
            # running
            for scene in engine.scenes:
                if scene.name == name:
                    engine.current_scene = scene
                    return scene
            else:
                engine.new_scene(name=name, size=size)
                engine.current_scene.name = name
        figure = engine.current_scene
        scene = figure.scene
        if scene is not None:
            if hasattr(scene, 'isometric_view'):
                scene.isometric_view()
            else:
                # Not every viewer might implement this method
                view(40, 50)
    scene = figure.scene
    if scene is not None:
        if bgcolor is None:
            bgcolor = options.background_color
        scene.background = bgcolor
        if fgcolor is None:
            fgcolor = options.foreground_color
        scene.foreground = fgcolor
    return figure


def gcf(engine=None):
    """Return a handle to the current figure.

    You can supply the engine from which you want to retrieve the
    current figure, if you have several mayavi engines.
    """
    if engine is None:
        engine = get_engine()
    scene = engine.current_scene
    if scene is None:
        return figure(engine=engine)
    return scene


def clf(figure=None):
    """Clear the current figure.

    You can also supply the figure that you want to clear.
    """
    try:
        if figure is None:
            scene = gcf()
        else:
            scene = figure
        if scene.scene is not None:
            disable_render = scene.scene.disable_render
            scene.scene.disable_render = True
        scene.children[:] = []
        scene._mouse_pick_dispatcher.clear_callbacks()
        if scene.scene is not None:
            scene.scene.disable_render = disable_render
    except AttributeError:
        pass
    gc.collect()


def close(scene=None, all=False):
    """ Close a figure window

        close() by itself closes the current figure.

        close(num) closes figure number num.

        close(name) closes figure named name.

        close(figure), where figure is a scene instance, closes that
        figure.

        close(all=True) closes all figures controlled by mlab
    """
    if all is True:
        engine = get_engine()
        # We need the copy, as the list gets pruned as we close scenes
        for scene in copy.copy(engine.scenes):
            engine.close_scene(scene)
        return
    if not isinstance(scene, Scene):
        engine = get_engine()
        if scene is None:
            scene = engine.current_scene
        else:
            if type(scene) in (int, np.intp, np.int8,
                               np.int16, np.int32, np.int64):
                scene = int(scene)
                name = 'Mayavi Scene %d' % scene
            else:
                name = str(scene)
            # Go looking in the engine see if the scene is not already
            # running
            for scene in engine.scenes:
                if scene.name == name:
                    break
            else:
                warnings.warn('Scene %s not managed by mlab' % name)
                return
    else:
        if scene.scene is None:
            engine = registry.find_scene_engine(scene)
        else:
            engine = registry.find_scene_engine(scene.scene)
    engine.close_scene(scene)


def draw(figure=None):
    """ Forces a redraw of the current figure.
    """
    if figure is None:
        figure = gcf()
    figure.render()


def savefig(filename, size=None, figure=None, magnification='auto',
            **kwargs):
    """ Save the current scene.
        The output format are deduced by the extension to filename.
        Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
        oogl (geomview), iv (OpenInventor), wrl, vrml, obj (wavefront),
        x3d, pov (povray).

        **Parameters**

        :size: the size of the image created (unless magnification is
               set, in which case it is the size of the window used
               for rendering).

        :figure: the figure instance to save to a file.

        :magnification: the magnification is the scaling between the
                        pixels on the screen, and the pixels in the
                        file saved. If you do not specify it, it will be
                        calculated so that the file is saved with the
                        specified size. If you specify a magnification,
                        Mayavi will use the given size as a screen size,
                        and the file size will be 'magnification * size'.

        **Notes**

        If the size specified is larger than the window size, and no
        magnification parameter is passed, the magnification of the scene
        is changed so that the image created has the requested size.
        Please note that if you are trying to save images with sizes
        larger than the window size, there will be additional computation
        cost.

        Any extra keyword arguments are passed along to the respective
        image format's save method.
    """
    if figure is None:
        figure = gcf()
    current_mag = figure.scene.magnification
    try:
        if size is not None:
            current_x, current_y = tuple(figure.scene.get_size())
            target_x, target_y = size
            if magnification == 'auto':
                magnification = max(target_x // current_x,
                                    target_y // current_y) + 1
                target_x = int(target_x / magnification)
                target_y = int(target_y / magnification)
                size = target_x, target_y
        elif magnification == 'auto':
            magnification = 1
        figure.scene.magnification = int(magnification)
        figure.scene.save(filename,
                          size=size,
                          **kwargs)
    finally:
        figure.scene.magnification = int(current_mag)


def sync_camera(reference_figure, target_figure):
    """ Synchronise the camera of the target_figure on the camera of the
        reference_figure.
    """
    reference_figure.scene._renderer.sync_trait(
        'active_camera', target_figure.scene._renderer
    )
    target_figure.scene._renderer.active_camera.on_trait_change(
            lambda: do_later(target_figure.scene.render)
    )


def screenshot(figure=None, mode='rgb', antialiased=False):
    """ Return the current figure pixmap as an array.

        **Parameters**

        :figure: a figure instance or None, optional
            If specified, the figure instance to capture the view of.
        :mode: {'rgb', 'rgba'}
            The color mode of the array captured.
        :antialiased: {True, False}
            Use anti-aliasing for rendering the screenshot.
            Uses the number of aa frames set by
            figure.scene.anti_aliasing_frames

        **Notes**

        On most systems, this works similarly to taking a screenshot of
        the rendering window. Thus if it is hidden by another window, you
        will capture the other window. This limitation is due to the
        heavy use of the hardware graphics system.

        **Examples**

        This function can be useful for integrating 3D plotting with
        Mayavi in a 2D plot created by matplotlib.

        >>> from mayavi import mlab
        >>> mlab.test_plot3d()
        >>> arr = mlab.screenshot()
        >>> import pylab as pl
        >>> pl.imshow(arr)
        >>> pl.axis('off')
        >>> pl.show()

    """
    if figure is None:
        figure = gcf()
    # don't use figure.scene.get_size() here because this will be incorrect
    # for HiDPI systems
    x, y = tuple(figure.scene.render_window.size)

    # Try to lift the window
    figure.scene._lift()
    if mode == 'rgb':
        out = tvtk.UnsignedCharArray()
        shape = (y, x, 3)
        pixel_getter = figure.scene.render_window.get_pixel_data
        if vtk_major_version > 7:
            pg_args = (0, 0, x - 1, y - 1, 1, out, 0)
        else:
            pg_args = (0, 0, x - 1, y - 1, 1, out)

    elif mode == 'rgba':
        out = tvtk.FloatArray()
        shape = (y, x, 4)
        pixel_getter = figure.scene.render_window.get_rgba_pixel_data
        if vtk_major_version > 7:
            pg_args = (0, 0, x - 1, y - 1, 1, out, 0)
        else:
            pg_args = (0, 0, x - 1, y - 1, 1, out)

    else:
        raise ValueError('mode type not understood')

    if antialiased:
        # save the current aa value to restore it later
        render_window = figure.scene.render_window
        if hasattr(render_window, 'aa_frames'):
            old_aa = render_window.aa_frames
            render_window.aa_frames = figure.scene.anti_aliasing_frames
        else:
            old_aa = render_window.multi_samples
            render_window.multi_samples = figure.scene.anti_aliasing_frames
        figure.scene.render()
        pixel_getter(*pg_args)
        if hasattr(render_window, 'aa_frames'):
            render_window.aa_frames = old_aa
        else:
            render_window.multi_samples = old_aa
        figure.scene.render()

    else:
        pixel_getter(*pg_args)

    # Return the array in a way that pylab.imshow plots it right:
    out = out.to_array()
    out.shape = shape
    out = np.flipud(out)
    return out
