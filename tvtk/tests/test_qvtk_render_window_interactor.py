import unittest

try:
    from tvtk.pyface.ui.qt4.QVTKRenderWindowInteractor import (
        QVTKRenderWindowInteractor,
        _repaint_after_render,
    )
except (ImportError, RuntimeError):
    # No binding installed (ImportError) or QT_API set but empty/invalid, as on
    # the headless CI row (RuntimeError) -- both mean "no Qt here".
    QVTKRenderWindowInteractor = _repaint_after_render = None


@unittest.skipIf(_repaint_after_render is None, 'Qt is not available.')
class TestRepaintAfterRender(unittest.TestCase):
    """The macOS Qt >= 6.10 paint storm (see tvtk/WORKAROUNDS.md)."""

    f = staticmethod(_repaint_after_render)

    def test_darwin_qt_610_and_later_repaints_once(self):
        for version in ('6.10.0', '6.11.1', '7.0.0'):
            self.assertFalse(self.f('darwin', version), version)

    def test_darwin_older_qt_unaffected(self):
        for version in ('6.9.2', '5.15.10'):
            self.assertTrue(self.f('darwin', version), version)

    def test_other_platforms_unaffected(self):
        for platform in ('linux', 'win32'):
            self.assertTrue(self.f(platform, '6.11.1'), platform)

    def test_unparseable_version_unaffected(self):
        self.assertTrue(self.f('darwin', 'not.a.version'))


class _FakeAngleDelta:
    def __init__(self, y):
        self._y = y

    def y(self):
        return self._y


class _FakeWheelEvent:
    """Duck-typed QWheelEvent; Qt 5's also carries the deprecated delta()."""

    def __init__(self, y, with_delta=False):
        self._y = y
        if with_delta:
            self.delta = lambda: self._y

    def angleDelta(self):
        return _FakeAngleDelta(self._y)


@unittest.skipIf(QVTKRenderWindowInteractor is None, 'Qt is not available.')
class TestWheelEvent(unittest.TestCase):
    def test_wheel_events_reach_vtk(self):
        """Wheel events must reach VTK on Qt 5 and Qt 6 alike (gh-1276).

        Qt 5 wheel events still carry the deprecated delta() alongside
        angleDelta(), which used to divert them onto a legacy path whose
        coalescing timer was only ever created under Qt 4 -- so wheel
        zooming silently did nothing on PyQt5/PySide2.
        """
        from pyface.qt.QtGui import QApplication
        app = QApplication.instance() or QApplication([])  # noqa: F841
        w = QVTKRenderWindowInteractor()
        try:
            w._Iren.Enable()
            events = []
            w._Iren.AddObserver('MouseWheelForwardEvent',
                                lambda o, e: events.append('+'))
            w._Iren.AddObserver('MouseWheelBackwardEvent',
                                lambda o, e: events.append('-'))
            w.wheelEvent(_FakeWheelEvent(120, with_delta=True))  # Qt 5 notch
            w.wheelEvent(_FakeWheelEvent(-120, with_delta=True))
            w.wheelEvent(_FakeWheelEvent(30))   # Qt 6 trackpad partials...
            w.wheelEvent(_FakeWheelEvent(30))   # ...accumulate to a notch
            w.wheelEvent(_FakeWheelEvent(-20))  # never reaches a notch
            self.assertEqual(events, ['+', '-', '+'])
        finally:
            w.close()
            w.deleteLater()


if __name__ == '__main__':
    unittest.main()
