"""The ivtk viewer windows."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import unittest

try:
    from pyface.api import GUI
    from pyface.qt import QtGui, qt_api
except (ImportError, RuntimeError):
    # no binding installed, or QT_API set but empty, as on the headless CI row
    GUI = QtGui = qt_api = None


# Neither of these is ours to fix, and the second is not even catchable -- see
# tvtk/WORKAROUNDS.md.  pyface's `_MenuItem` calls `QMenu.addAction(text, slot,
# shortcut)`, an overload PyQt6 does not have, so every one of these windows
# fails building its menu bar; and traitsui's `_GroupSplitter._resize_items`
# hands `QSplitter.setSizes` the floats it seeded from `Item.width` whenever the
# splitter is still zero-sized, which PyQt6 rejects from inside a `showEvent`,
# where the TypeError is unraisable and Qt aborts the process.  PySide6 coerces
# and carries on, so the rest of the matrix covers what these are here for.
# Both reproduce on pyface and traitsui `main` as of 2026-08-19.
@unittest.skipIf(QtGui is None, 'Qt is not available.')
@unittest.skipIf(qt_api == 'pyqt6',
                 'pyface and traitsui break the ivtk windows on PyQt6')
class TestIVTKWindows(unittest.TestCase):
    """Each of the four windows builds, all the way down to its control.

    pyface 8 stopped creating a widget's control from its constructor, which
    left the ones built here handing a None to QSplitter.addWidget -- a
    segfault, not an exception, and so invisible to anything short of running
    the window.  See examples/tvtk/ivtk_example.py.
    """

    def setUp(self):
        from tvtk.tools import ivtk
        self.ivtk = ivtk
        GUI()   # the windows need a QApplication to build against

    def _check(self, name):
        from tvtk.pyface import actors

        window = getattr(self.ivtk, name)(size=(300, 200))
        try:
            window.open()
            self.assertIsNotNone(window.control, name)
            self.assertIsNotNone(window.scene, name)
            window.scene.add_actors(actors.cone_actor())
            window.scene.reset_zoom()
        finally:
            window.close()

    def test_ivtk(self):
        self._check('IVTK')

    def test_ivtk_with_crust(self):
        self._check('IVTKWithCrust')

    def test_ivtk_with_browser(self):
        self._check('IVTKWithBrowser')

    def test_ivtk_with_crust_and_browser(self):
        self._check('IVTKWithCrustAndBrowser')
