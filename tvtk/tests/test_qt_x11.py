import unittest

from tvtk.qt_x11 import embedding_error, x11_platform_override

WAYLAND_SESSION = {'WAYLAND_DISPLAY': 'wayland-0', 'DISPLAY': ':0'}


class TestX11PlatformOverride(unittest.TestCase):
    """Steering Qt onto XWayland (see tvtk/WORKAROUNDS.md)."""

    f = staticmethod(x11_platform_override)

    def test_wayland_session_steers_to_xcb(self):
        self.assertEqual(self.f('linux', dict(WAYLAND_SESSION)), 'xcb')

    def test_explicit_qt_qpa_platform_wins(self):
        for choice in ('wayland', 'xcb', 'offscreen'):
            environ = dict(WAYLAND_SESSION, QT_QPA_PLATFORM=choice)
            self.assertIsNone(self.f('linux', environ), choice)

    def test_x11_session_untouched(self):
        self.assertIsNone(self.f('linux', {'DISPLAY': ':0'}))

    def test_no_x_server_untouched(self):
        self.assertIsNone(self.f('linux', {'WAYLAND_DISPLAY': 'wayland-0'}))

    def test_other_platforms_untouched(self):
        for platform in ('darwin', 'win32'):
            self.assertIsNone(self.f(platform, dict(WAYLAND_SESSION)),
                              platform)

    def test_qt_toolkits_steered_others_untouched(self):
        for toolkit in ('qt4', 'qt', ''):
            environ = dict(WAYLAND_SESSION, ETS_TOOLKIT=toolkit)
            self.assertEqual(self.f('linux', environ), 'xcb', toolkit)
        for toolkit in ('wx', 'null'):
            environ = dict(WAYLAND_SESSION, ETS_TOOLKIT=toolkit)
            self.assertIsNone(self.f('linux', environ), toolkit)


class TestEmbeddingError(unittest.TestCase):
    """The error raised in place of the Xlib BadWindow abort."""

    f = staticmethod(embedding_error)

    def test_wayland_platforms_error(self):
        for name in ('wayland', 'wayland-egl'):
            error = self.f('linux', name)
            self.assertIn('QT_QPA_PLATFORM=xcb', error)
            self.assertIn(name, error)

    def test_embeddable_platforms_pass(self):
        for name in ('xcb', 'offscreen', 'minimal', ''):
            self.assertIsNone(self.f('linux', name), name)

    def test_other_oses_pass(self):
        self.assertIsNone(self.f('darwin', 'cocoa'))
        self.assertIsNone(self.f('win32', 'windows'))


if __name__ == '__main__':
    unittest.main()
