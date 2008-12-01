"""
Test mlab with the null engine.

This also tests some numerics with VTK.
"""

import unittest

import numpy as np

from enthought.mayavi import mlab
from enthought.mayavi.core.engine import Engine


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

    def tearDown(self):
        # Check that the NullEngine was not set as the default mlab engine.
        if not mlab.get_engine() is self._non_null_engine:
            raise AssertionError, \
                    "The NullEngine has overridden the default one"
 

if __name__ == '__main__':
    unittest.main()

