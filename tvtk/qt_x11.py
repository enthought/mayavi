"""Keep Qt off the wayland platform, where VTK render windows cannot embed.

VTK has no Wayland render window: on Unix it draws into a native X11 window
looked up by the id Qt reports.  Qt's wayland backend fabricates ``winId()``
values with no X11 window behind them, so VTK's first X request on one fails
with BadWindow and Xlib aborts the process (see tvtk/WORKAROUNDS.md and
enthought/mayavi#1396).  The fix is to run Qt on XWayland instead, which is
what ``QT_QPA_PLATFORM=xcb`` asks for.

``steer_qt_to_x11`` applies that while the choice is still open -- Qt reads
``QT_QPA_PLATFORM`` when the QApplication is constructed -- so it has to run
before pyface's toolkit initialization, which creates the QApplication as an
import side effect.  ``mayavi/__init__.py`` and ``tvtk/pyface/__init__.py``
call it for that reason.  For the cases it cannot win (the user imported
``traitsui``/``pyface`` before anything mayavi, or pinned
``QT_QPA_PLATFORM=wayland`` themselves), ``embedding_error`` gives the Qt
scene widget a clear error to raise in place of the Xlib abort.

This module must stay importable without Qt, VTK, or a built tvtk: it runs
at ``import mayavi``.
"""
# Author: Enthought, Inc.
# License: BSD Style.

import os


def x11_platform_override(environ):
    """The Qt platform to request so VTK render windows can embed, or None.

    Keyed off the environment rather than ``sys.platform``, so that every OS
    that can run a Wayland session (Linux, the BSDs) is covered without
    naming them: ``WAYLAND_DISPLAY`` is what marks one.

    Pure logic split out for testing; see the module docstring for why.
    """
    if environ.get('ETS_TOOLKIT', 'qt4') not in ('qt4', 'qt', ''):
        return None  # wx or null toolkit: leave Qt alone
    if 'QT_QPA_PLATFORM' in environ:  # an explicit choice wins
        return None
    if 'WAYLAND_DISPLAY' not in environ:  # not a Wayland session
        return None
    if 'DISPLAY' not in environ:  # no X server to steer onto
        return None
    return 'xcb'


def steer_qt_to_x11():
    """Set QT_QPA_PLATFORM=xcb where a wayland default would break VTK."""
    override = x11_platform_override(os.environ)
    if override is not None:
        os.environ['QT_QPA_PLATFORM'] = override


def embedding_error(platform_name):
    """Why a VTK render window cannot embed in a Qt window here, or None.

    ``platform_name`` is ``QGuiApplication.platformName()`` of the running
    application -- the OS is left out of it for the reason
    ``x11_platform_override`` leaves it out -- so this can only be checked,
    and the clear error raised in place of the Xlib abort, once steering is
    already too late.
    """
    if platform_name.startswith('wayland'):
        return (
            "Mayavi cannot embed a VTK render window in Qt on Wayland (Qt is "
            "running on the '%s' platform).  Set the environment variable "
            "QT_QPA_PLATFORM=xcb and try again." % platform_name)
    return None
