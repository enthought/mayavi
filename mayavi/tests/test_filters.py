import unittest
from unittest.mock import patch

from mayavi import mlab
from .common import get_example_data
from .test_engine_manager import patch_backend


def patch_pyface():
    return patch("mayavi.core.common.pyface", None)


class TestFilters(unittest.TestCase):
    @patch_pyface()
    @patch_backend('test')
    def test_cell_to_point_data(self):
        src = mlab.pipeline.open(get_example_data('pyramid_ug.vtu'))
        cd = mlab.pipeline.cell_derivatives(src)
        cd.filter.vector_mode = 'compute_vorticity'
        c2p = mlab.pipeline.cell_to_point_data(cd)
        st = mlab.pipeline.streamline(c2p)
        st.update_pipeline()
        mlab.clf()
