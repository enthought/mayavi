"""The ivtk viewer windows."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import unittest

try:
    from pyface.api import GUI
    from pyface.qt import QtGui
except (ImportError, RuntimeError):
    # no binding installed, or QT_API set but empty, as on the headless CI row
    GUI = QtGui = None


@unittest.skipIf(QtGui is None, 'Qt is not available.')
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
