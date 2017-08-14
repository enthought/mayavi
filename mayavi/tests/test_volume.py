# Standard library imports.
import numpy as np
import unittest
from mock import patch

# Enthought library imports
from mayavi.tests.common import get_example_data
from mayavi import mlab


class TestVolumeWorksWithProbe(unittest.TestCase):
    def setUp(self):
        self._orig_backend = mlab.options.backend
        mlab.options.backend = "test"

    def tearDown(self):
        mlab.options.backend = self._orig_backend

    def test_volume_works_with_probe(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        idp = mlab.pipeline.image_data_probe(src)
        with patch('pyface.api.error') as m:
            vol = mlab.pipeline.volume(idp)
        self.assertEqual(m.call_count, 0)
        self.assertEqual(
            np.allclose(vol.volume.center, (3.0, 3.0, 1.5)),True
        )



if __name__ == '__main__':
    unittest.main()
