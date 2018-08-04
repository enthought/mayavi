import unittest
import numpy as np

from tvtk.api import tvtk
from mayavi.core.utils import DataSetHelper


class TestDataSetHelper(unittest.TestCase):
    def _make_data(self, factor=1.0):
        id = tvtk.ImageData(dimensions=(2, 2, 1), origin=(0, 0, 0),
                            spacing=(1, 1, 1))
        id.point_data.scalars = np.arange(4, dtype=float)*factor
        id.point_data.scalars.name = 'ps'
        id.point_data.vectors = np.ones((4, 3), dtype=float)*factor
        id.point_data.vectors.name = 'pv'
        id.cell_data.scalars = np.arange(4, dtype=float)*0.5*factor
        id.cell_data.scalars.name = 'cs'
        id.cell_data.vectors = np.ones((4, 3), dtype=float)*0.5*factor
        id.cell_data.vectors.name = 'cv'
        return id

    def test_get_range_works_for_simple_datasets(self):
        # Given
        id = self._make_data()

        # When
        dsh = DataSetHelper(id)

        # Then
        name, rng = dsh.get_range('scalars', 'point')
        self.assertEqual(name, 'ps')
        self.assertEqual(rng, [0.0, 3.0])

        name, rng = dsh.get_range('scalars', 'cell')
        self.assertEqual(name, 'cs')
        self.assertEqual(rng, [0.0, 1.5])

        name, rng = dsh.get_range('vectors', 'point')
        self.assertEqual(name, 'pv')
        self.assertEqual(rng, [0.0, np.sqrt(3.0)])

        name, rng = dsh.get_range('vectors', 'cell')
        self.assertEqual(name, 'cv')
        self.assertEqual(rng, [0.0, np.sqrt(3.0)*0.5])

    def test_get_range_works_for_multiblock_datasets(self):
        # Given
        id1 = self._make_data()
        id2 = self._make_data(factor=2.0)

        mb = tvtk.MultiBlockDataSet()
        mb.set_block(0, id1)
        mb.set_block(1, id2)

        # When
        dsh = DataSetHelper(mb)

        # Then
        name, rng = dsh.get_range('scalars', 'point')
        self.assertEqual(name, 'ps')
        self.assertEqual(rng, [0.0, 6.0])

        name, rng = dsh.get_range('scalars', 'cell')
        self.assertEqual(name, 'cs')
        self.assertEqual(rng, [0.0, 3.0])

        name, rng = dsh.get_range('vectors', 'point')
        self.assertEqual(name, 'pv')
        self.assertEqual(rng, [0.0, np.sqrt(3.0)*2.0])

        name, rng = dsh.get_range('vectors', 'cell')
        self.assertEqual(name, 'cv')
        self.assertEqual(rng, [0.0, np.sqrt(3.0)])


if __name__ == '__main__':
    unittest.main()
