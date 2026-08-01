"""Keep Qt off the wayland platform, where VTK render windows cannot embed.

VTK has no Wayland render window: on Linux it draws into a native X11 window
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
import sys


def x11_platform_override(platform, environ):
    """The Qt platform to request so VTK render windows can embed, or None.

    Pure logic split out for testing; see the module docstring for why.
    """
    if platform != 'linux':
        return None
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
    override = x11_platform_override(sys.platform, os.environ)
    if override is not None:
        os.environ['QT_QPA_PLATFORM'] = override


def embedding_error(platform, platform_name):
    """Why a VTK render window cannot embed in a Qt window here, or None.

    ``platform_name`` is ``QGuiApplication.platformName()`` of the running
    application, so this can only be checked -- and the clear error raised in
    place of the Xlib abort -- once steering is already too late.
    """
    if platform == 'linux' and platform_name.startswith('wayland'):
        return (
            "A VTK render window cannot be embedded in a Qt window on the "
            "'%s' platform: VTK draws to a native X11 window, and the window "
            "ids Qt fabricates on Wayland have no X11 window behind them, so "
            "VTK's first X request on one fails with BadWindow.  Set the "
            "environment variable QT_QPA_PLATFORM=xcb (XWayland) before the "
            "QApplication is created." % platform_name)
    return None
