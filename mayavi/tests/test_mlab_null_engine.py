"""
Test the mlab null engine.
"""

import unittest

from mayavi import mlab
from mayavi.core.engine import Engine
from mayavi.tools.engine_manager import engine_manager
from mayavi.core.registry import registry
from mayavi.tests.common import get_example_data

################################################################################
# class `TestMlabNullEngineBase`
################################################################################
class TestMlabNullEngineBase(unittest.TestCase):
    """ Base class to test mlab with the null engine
    """
    def setUp(self):
        e = Engine()
        e.start()
        self._non_null_engine = e
        mlab.set_engine(e)

    def tearDown(self):
        # Check that the NullEngine was not set as the default mlab engine.
        if not mlab.get_engine() is self._non_null_engine:
            raise AssertionError("The NullEngine has overridden the default one")
        engine_manager.current_engine = None
        # Unregistering all unused engines.
        registry.unregister_engine(self._non_null_engine)
        for engine in list(registry.engines):
            registry.unregister_engine(engine)


################################################################################
# class `TestRealMlabNullEngine`
################################################################################
class TestRealMlabNullEngine(unittest.TestCase):
    """Tests if the mlab settings via the options.backend and offscreen
    options work correctly."""

    def setUp(self):
        self.backend = mlab.options.backend

    def tearDown(self):
        mlab.options.backend = self.backend
        for engine in list(registry.engines):
            registry.unregister_engine(engine)

    def test_test_backend(self):
        """Test if setting the backend to 'test' works."""
        mlab.options.backend = 'test'
        mlab.test_contour3d()
        mlab.clf()
        mlab.pipeline.open(get_example_data('cube.vti'))
        mlab.clf()

if __name__ == '__main__':
    unittest.main()
