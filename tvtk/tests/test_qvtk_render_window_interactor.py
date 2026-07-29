import unittest

try:
    from tvtk.pyface.ui.qt4.QVTKRenderWindowInteractor import (
        _repaint_after_render,
    )
except ImportError:
    _repaint_after_render = None


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


if __name__ == '__main__':
    unittest.main()
