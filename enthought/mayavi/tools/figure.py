"""
Functions related to creating the engine or the figures.

"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from types import IntType

# Mayavi imports
from camera import view
from engine_manager import get_engine, options

######################################################################

def figure(name=None, bgcolor=None, fgcolor=None, engine=None,
                size=(400, 350)):
    """ Creates a new scene or retrieves an existing scene. If the mayavi
    engine is not running this also starts it.

    **Keyword arguments**

        :name: The name of the scene.

        :bgcolor: The color of the background (None is default).

        :fgcolor: The color of the foreground (None is default).

        :engine: The mayavi engine that controls the figure.

        :size: The size of the scene created, in pixels. May not apply
               for certain scene viewer.
    """
    if engine is None:
        engine = get_engine()
    if type(name) == IntType:
        name = 'TVTK Scene %d' % name
    if name is not None:
        # Go looking in the engine see if the scene is not already
        # running
        for scene in engine.scenes:
            if scene.name == name:
                engine.current_scene = scene
                return scene
        else:
            engine.new_scene(name=name, size=size)
            engine.current_scene.name = name
    else:
        engine.new_scene(size=size)
    view(40, 50)
    fig = engine.current_scene
    scene = fig.scene
    if scene is not None:
        if bgcolor is None:
            bgcolor = options.background_color
        scene.background = bgcolor
        if fgcolor is None:
            fgcolor = options.foreground_color
        scene.foreground = fgcolor
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


def draw(figure=None):
    """ Forces a redraw of the current figure.
    """
    if figure is None: 
        figure = gcf()
    figure.render()


def savefig(filename, size=None, figure=None, **kwargs):
    """ Save the current scene.
        The output format are deduced by the extension to filename.
        Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
        oogl (geomview), iv (OpenInventor), vrml, obj (wavefront)

        If an additional size (2-tuple) argument is passed the window
        is resized to the specified size in order to produce a
        suitably sized output image.  Please note that when the window
        is resized, the window may be obscured by other widgets and
        the camera zoom is not reset which is likely to produce an
        image that does not reflect what is seen on screen.

        Any extra keyword arguments are passed along to the respective
        image format's save method.
    """
    if figure is None:
        figure = gcf()
    figure.scene.save(filename, size=size, **kwargs)

