"""
Functions related to creating the engine or the figures.

"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from types import IntType
import gc

import numpy as np

# Enthought imports
from enthought.pyface.timer.api import do_later

#  imports
from .camera import view
from .engine_manager import get_engine, options

######################################################################

# A list to store the allocated scene numbers
__scene_number_list = set((0,))


def figure(name=None, bgcolor=None, fgcolor=None, engine=None,
                size=(400, 350)):
    """ Creates a new scene or retrieves an existing scene. If the mayavi
    engine is not running this also starts it.

    **Keyword arguments**

        :name: The name of the scene.

        :bgcolor: The color of the background (None is default).

        :fgcolor: The color of the foreground, that is the color of all text
                  annotation labels (axes, orientation axes, scalar bar 
                  labels). It should be sufficiently far from `bgcolor` 
                  to see the annotation texts. (None is default).

        :engine: The mayavi engine that controls the figure.

        :size: The size of the scene created, in pixels. May not apply
               for certain scene viewer.
    """
    if engine is None:
        engine = get_engine()
    if name is None:
        name = max(__scene_number_list) + 1
        __scene_number_list.update((name,))
        name = 'Mayavi Scene %d' % name
        engine.new_scene(name=name, size=size)
        engine.current_scene.name = name
    else:
        if type(name) in (IntType, np.int, np.int0, np.int8,
                        np.int16, np.int32, np.int64):
            name = int(name)
            __scene_number_list.update((name,))
            name = 'Mayavi Scene %d' % name
        # Go looking in the engine see if the scene is not already
        # running
        for scene in engine.scenes:
            name = str(name)
            if scene.name == name:
                engine.current_scene = scene
                return scene
        else:
            engine.new_scene(name=name, size=size)
            engine.current_scene.name = name
    fig = engine.current_scene
    scene = fig.scene
    if scene is not None:
        if bgcolor is None:
            bgcolor = options.background_color
        scene.background = bgcolor
        if fgcolor is None:
            fgcolor = options.foreground_color
        scene.foreground = fgcolor
        if hasattr(scene, 'isometric_view'):
            scene.isometric_view()
        else:
            # Not every viewer might implement this method
            view(40, 50)
    return fig


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
        scene.scene.disable_render = True
        scene.children[:] = []
        scene.scene.disable_render = False
    except AttributeError:
        pass
    gc.collect()


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
        oogl (geomview), iv (OpenInventor), vrml, obj (wavefront)

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
    current_x, current_y = tuple(figure.scene.get_size())
    target_x, target_y = size
    current_mag = figure.scene.magnification
    if magnification is 'auto':
        magnification = max(target_x//current_x,
                                     target_y//current_y) + 1
        target_x = int(target_x/magnification)
        target_y = int(target_y/magnification)
    figure.scene.magnification = magnification
    figure.scene.save(filename, 
                        size=(target_x, target_y),
                        **kwargs)
    figure.scene.magnification = current_mag 


def sync_camera(reference_figure, target_figure):
    """ Synchronise the camera of the target_figure on the camera of the
        reference_figure.
    """
    reference_figure.scene._renderer.sync_trait('active_camera', 
                        target_figure.scene._renderer)
    target_figure.scene._renderer.active_camera.on_trait_change(
            lambda: do_later(target_figure.scene.render))



