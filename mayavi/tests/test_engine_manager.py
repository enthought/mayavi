"""
Tests for mayavi.tools.engine_manager
"""
import unittest
from unittest.mock import patch

from mayavi.core.null_engine import NullEngine
from mayavi.plugins.envisage_engine import EnvisageEngine
from mayavi.api import OffScreenEngine, Engine

from mayavi.tools.engine_manager import get_engine


def patch_registry_engines(engines):
    return patch("mayavi.tools.engine_manager.registry.engines", engines)


def patch_backend(backend):
    return patch("mayavi.tools.engine_manager.options.backend", backend)


def patch_offscreen(switch_on):
    return patch("mayavi.tools.engine_manager.options.offscreen", switch_on)


class TestEngineManager(unittest.TestCase):

    @patch_backend("test")
    def test_get_engine_backend_test(self):
        self.assertIsInstance(get_engine(), NullEngine)

    @patch_backend("envisage")
    @patch_registry_engines({"EnvisageEngine1": EnvisageEngine()})
    def test_get_engine_backend_envisage(self):
        self.assertIs(type(get_engine()), EnvisageEngine)

    @patch_backend("simple")
    @patch_registry_engines({"Engine1": NullEngine()})
    def test_get_engine_backend_simple_with_existing_engine(self):
        self.assertIs(type(get_engine()), Engine)

    @patch_backend("auto")
    @patch_registry_engines({"Engine1": EnvisageEngine()})
    def test_get_engine_backend_auto_with_existing_engine(self):
        self.assertIs(type(get_engine()), EnvisageEngine)

    @patch_backend("envisage")
    @patch_registry_engines({"EnvisageEngine1": EnvisageEngine()})
    @patch_offscreen(True)
    def test_get_engine_offscreen_backend_envisage(self):
        self.assertIs(type(get_engine()), EnvisageEngine)

    @patch_backend("test")
    @patch_offscreen(True)
    def test_get_engine_offscreen_backend_test(self):
        self.assertIs(type(get_engine()), NullEngine)

    @patch_backend("auto")
    @patch_offscreen(True)
    @patch_registry_engines({"Engine1": Engine()})
    def test_get_engine_offscreen_backend_auto_with_existing_engine(self):
        self.assertIs(type(get_engine()), OffScreenEngine)

    @patch_backend("auto")
    @patch_offscreen(True)
    @patch_registry_engines({"Engine1": Engine()})
    def test_get_engine_offscreen_backend_auto_switched_twice(self):
        self.assertIs(type(get_engine()), OffScreenEngine)
        # Now OffScreenEngine is the last used engine
        # if offscreen is switched back to False
        # get_engine should not return an OffScreenEngine
        from mayavi.tools.engine_manager import options
        options.offscreen = False
        self.assertIs(type(get_engine()), Engine)

    @patch_backend("simple")
    @patch_offscreen(True)
    @patch_registry_engines({"Engine1": Engine()})
    def test_get_engine_offscreen_backend_simple_with_started_engine(self):
        self.assertIs(type(get_engine()), OffScreenEngine)
