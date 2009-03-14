"""
Test mlab with the null engine.

This also tests some numerics with VTK.
"""

import unittest

import numpy as np

from enthought.etsconfig.api import ETSConfig
from enthought.mayavi import mlab
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.tools.engine_manager import engine_manager
from enthought.mayavi.core.registry import registry
from enthought.tvtk.api import tvtk

class TestMlabNullEngine(unittest.TestCase):

    def setUp(self):
        e = Engine()
        e.start()
        self._non_null_engine = e
        mlab.set_engine(e)

    def test_contour_filter(self):
        a = np.zeros((3, 3, 3))
        a[1, 1, 1] = 1

        src = mlab.pipeline.scalar_field(a, figure=False)
        filter = mlab.pipeline.contour(src)

        x, y, z = filter.outputs[0].points.to_array().T

        # Check that the contour filter indeed did its work:
        np.testing.assert_almost_equal(x, [ 2. ,  2. ,  1.5,  2.5,  2. ,  2. ])
        np.testing.assert_almost_equal(y, [ 2. ,  1.5,  2. ,  2. ,  2.5,  2. ])
        np.testing.assert_almost_equal(z, [ 1.5,  2. ,  2. ,  2. ,  2. ,  2.5])

        # Check that the filter was not added to a live scene:
        if filter.scene is not None:
            raise AssertionError, "The NullEngine seems not to work"

    def test_user_defined_filter(self):
        x, y, z = np.random.random((3, 100))
        src = mlab.pipeline.scalar_scatter(x, y, z, figure=False)
        density = mlab.pipeline.user_defined(src, filter='GaussianSplatter')

        self.assertEqual(len(density.outputs), 1)
        self.assert_(isinstance(density.outputs[0], tvtk.ImageData))

    def test_mlab_source(self):
        """ Check that the different objects created by mlab have an 
            'mlab_source' attribute.
        """
        # Test for functions taking 3D scalar data
        pipelines = (
            (mlab.pipeline.scalar_scatter, ),
            (mlab.pipeline.scalar_field, ),
            (mlab.pipeline.scalar_field, mlab.pipeline.image_plane_widget),
            (mlab.contour3d, ),
            (mlab.points3d, ), )
        data = np.random.random((3, 3, 3))
        for pipeline in pipelines:
            obj = pipeline[0](data, figure=False)
            for factory in pipeline[1:]:
                obj = factory(obj)
            self.assertTrue(hasattr(obj, 'mlab_source'))
        # Test for functions taking x, y, z 2d arrays.
        x, y, z = np.random.random((3, 3, 3))
        pipelines = (
            (mlab.mesh, ),
            (mlab.surf, ),
            (mlab.quiver3d, ),
            (mlab.pipeline.vector_scatter, ),
            (mlab.pipeline.vector_scatter,
                            mlab.pipeline.extract_vector_components),
            (mlab.pipeline.vector_scatter,
                            mlab.pipeline.extract_vector_norm),
            (mlab.pipeline.array2d_source, ), )
        for pipeline in pipelines:
            obj = pipeline[0](x, y, z, figure=False)
            for factory in pipeline[1:]:
                obj = factory(obj)
            self.assertTrue(hasattr(obj, 'mlab_source'))


    def tearDown(self):
        # Check that the NullEngine was not set as the default mlab engine.
        if not mlab.get_engine() is self._non_null_engine:
            raise AssertionError, \
                    "The NullEngine has overridden the default one"
        engine_manager.current_engine = None
        # Unregistering all unused engines.
        registry.unregister_engine(self._non_null_engine)
        for engine in registry.engines.keys():
            registry.unregister_engine(engine)
 

class TestRealMlabNullEngine(unittest.TestCase):
    """Tests if the mlab settings via the options.backend and offscreen
    options work correctly."""

    def setUp(self):
        self.backend = mlab.options.backend

    def tearDown(self):
        mlab.options.backend = self.backend
        for engine in registry.engines.keys():
            registry.unregister_engine(engine)

    def test_test_backend(self):
        """Test if setting the backend to 'test' works."""
        mlab.options.backend = 'test'
        mlab.test_contour3d()
        mlab.clf()

if __name__ == '__main__':
    unittest.main()

