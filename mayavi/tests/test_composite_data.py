import unittest
from numpy import testing as npt
import numpy as np
from tvtk.api import tvtk

from mayavi import mlab

from mayavi.tests.common import get_example_data
from .test_mlab_integration import TestMlabNullEngine


def make_mb_dataset():
    fpath = get_example_data('pyramid_ug.vtu')
    r = tvtk.XMLUnstructuredGridReader(file_name=fpath)
    r.update()
    ug0 = r.output
    ug1 = tvtk.UnstructuredGrid()
    ug1.deep_copy(ug0)
    pts = ug1.points.to_array()
    pts[:, 0] += 10.0
    ug1.points = pts
    mb = tvtk.MultiBlockDataSet()
    mb.set_block(0, ug0)
    mb.set_block(1, ug1)
    return mb


class TestCompositeData(TestMlabNullEngine):
    def test_mb_contour(self):
        # Given
        mb = make_mb_dataset()

        # When
        src = mlab.pipeline.add_dataset(mb)
        iso = mlab.pipeline.iso_surface(src)

        # Then
        bounds = iso.actor.actor.bounds
        self.assertTrue((bounds[1] > 6) and (bounds[1] < 17))
        self.assertEqual(bounds[0], 0)
        self.assertEqual(bounds[2], 0)
        self.assertEqual(bounds[4], 0)
        self.assertTrue(bounds[5] < 3.1)

    def test_mb_surface(self):
        # Given
        mb = make_mb_dataset()

        # When
        src = mlab.pipeline.add_dataset(mb)
        surf = mlab.pipeline.surface(src)

        # Then
        bounds = surf.actor.actor.bounds
        expect = (0.0, 16.0, 0.0, 6.0, 0.0, 3.0)
        npt.assert_almost_equal(bounds, expect)

    def test_mb_scalar_cut_plane(self):
        # Given
        mb = make_mb_dataset()

        # When
        src = mlab.pipeline.add_dataset(mb)
        scp = mlab.pipeline.scalar_cut_plane(src)
        scp.implicit_plane.widget.normal_to_y_axis = True

        # Then
        bounds = scp.actor.actor.bounds
        expect = (0.0, 16.0, 3.0, 3.0, 0.0, 3.0)
        npt.assert_allclose(bounds, expect)

    def test_mb_vector_cut_plane(self):
        # Given
        mb = make_mb_dataset()

        # When
        src = mlab.pipeline.add_dataset(mb)
        vcp = mlab.pipeline.vector_cut_plane(src)
        vcp.implicit_plane.widget.normal_to_y_axis = True

        # Then
        bounds = vcp.actor.actor.bounds
        expect = np.array((0.0, 16.0, 3.0, 3.0, 0.0, 3.0))
        # print(expect - 1.0, expect + 1.0, bounds)
        self.assertTrue(
            np.all(bounds > (expect - 1.0)) and np.all(bounds < (expect + 1.0))
        )


if __name__ == '__main__':
    unittest.main()
