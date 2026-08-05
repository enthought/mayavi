"""Every public api module must import and re-export what it advertises."""
# Copyright (c) Enthought, Inc.
# License: BSD Style.

import importlib
import unittest

# these are the documented import points; nothing else in the suite touches
# mayavi.core.api or mayavi.core.ui.api, so a broken re-export went unnoticed
API_MODULES = [
    'mayavi.api',
    'mayavi.core.api',
    'mayavi.core.ui.api',
    'mayavi.filters.api',
    'mayavi.modules.api',
    'mayavi.preferences.api',
    'mayavi.sources.api',
    'tvtk.api',
    'tvtk.pyface.api',
]


class TestApiModules(unittest.TestCase):
    def test_importable(self):
        for name in API_MODULES:
            with self.subTest(name):
                module = importlib.import_module(name)
                exported = [attr for attr in vars(module)
                            if not attr.startswith('_')]
                self.assertNotEqual(exported, [])

    def test_core_api_exports_the_engines(self):
        from mayavi.core.api import Engine, NullEngine, OffScreenEngine
        self.assertTrue(issubclass(NullEngine, Engine))
        self.assertTrue(issubclass(OffScreenEngine, Engine))


if __name__ == "__main__":
    unittest.main()
