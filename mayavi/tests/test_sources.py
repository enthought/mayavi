# Author: Stefano Borini <stefano borini at enthought dot com>
# Copyright (c) 2009-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest
import numpy as np

# Local imports.
from mayavi.tools.sources import convert_to_arrays


class TestSources(unittest.TestCase):
    def test_convert_to_arrays(self):
        """Test if the convert_to_arrays routine works properly"""

        values = convert_to_arrays(
            (1, 2, 3, np.float32(4), np.float64(5), np.array([6])))

        all_dims = set(x.shape for x in values)

        self.assertEqual(len(all_dims), 1)
        self.assertIn((1,), all_dims)


if __name__ == '__main__':
    unittest.main()
