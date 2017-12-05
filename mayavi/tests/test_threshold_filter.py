# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2010,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

import numpy as np

# Local imports.
from mayavi.core.null_engine import NullEngine

# Enthought library imports
from mayavi.filters.threshold import Threshold
from mayavi.filters.cut_plane import CutPlane
from mayavi.sources.array_source import ArraySource


class TestThresholdFilter(unittest.TestCase):

    def make_src(self, nan=False):
        data = np.empty((3, 3, 3))
        if nan:
            data[0] = np.nan
        data.flat[:] = np.arange(data.size)
        return ArraySource(scalar_data=data)

    def setUp(self):
        """Initial setting up of test fixture, automatically called by
        TestCase before any other test method is invoked"""
        e = NullEngine()
        # Uncomment to see visualization for debugging etc.
        #e = Engine()
        e.start()
        s = e.new_scene()
        self.e = e
        self.s = s


        self.scene = e.current_scene
        return

    def tearDown(self):
        """For necessary clean up, automatically called by TestCase
        after the test methods have been invoked"""
        self.e.stop()
        return

    def test_threshold_filter_nan(self):
        src = self.make_src(nan=True)
        self.e.add_source(src)
        threshold = Threshold()
        self.e.add_filter(threshold)
        self.assertEqual(
            np.nanmin(src.scalar_data),
            np.nanmin(
                threshold.get_output_dataset().point_data.scalars.to_array()
            )
        )
        self.assertEqual(
            np.nanmax(src.scalar_data),
            np.nanmax(
                threshold.get_output_dataset().point_data.scalars.to_array()
            )
        )

    def test_threshold_filter_threhsold(self):
        src = self.make_src()
        self.e.add_source(src)
        threshold = Threshold()
        self.e.add_filter(threshold)
        threshold.upper_threshold = 20.
        self.assertTrue(
            20 >= np.nanmax(
                threshold.get_output_dataset().point_data.scalars.to_array()
            )
        )
        return

    def test_threshold_filter_data_range_changes(self):
        # Regression test for GitHub issue #136.
        src = self.make_src()
        self.e.add_source(src)
        threshold = Threshold()
        self.e.add_filter(threshold)

        # Move from one data range to another non-overlapping range,
        # first downwards, then back up.
        src.scalar_data = np.linspace(3.0, 5.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, 3.0)
        self.assertAlmostEqual(threshold.upper_threshold, 5.0)
        src.scalar_data = np.linspace(-5.0, -3.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, -5.0)
        self.assertAlmostEqual(threshold.upper_threshold, -3.0)
        src.scalar_data = np.linspace(3.0, 5.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, 3.0)
        self.assertAlmostEqual(threshold.upper_threshold, 5.0)

        # Narrow and widen.
        src.scalar_data = np.linspace(4.2, 4.6, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, 4.2)
        self.assertAlmostEqual(threshold.upper_threshold, 4.6)
        src.scalar_data = np.linspace(-20.0, 20.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, -20.0)
        self.assertAlmostEqual(threshold.upper_threshold, 20.0)

        # Shift to a range overlapping the previous one.
        src.scalar_data = np.linspace(-10.0, -30.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, -30.0)
        self.assertAlmostEqual(threshold.upper_threshold, -10.0)
        src.scalar_data = np.linspace(-20.0, 20.0, 27).reshape((3, 3, 3))
        self.assertAlmostEqual(threshold.lower_threshold, -20.0)
        self.assertAlmostEqual(threshold.upper_threshold, 20.0)

    def test_threshold_with_other_filter_as_input(self):
        # Given
        x, y, z = np.mgrid[-1:1:10j, -1:1:10j, -1:1:10j]
        s = x*x + y*y + z*z

        src = ArraySource(scalar_data=s)
        self.e.add_source(src)
        scp = CutPlane()
        self.e.add_filter(scp)

        # When
        threshold = Threshold()
        self.e.add_filter(threshold)
        threshold.trait_set(
            lower_threshold=0.25, upper_threshold=0.75,
            auto_reset_lower=False, auto_reset_upper=False
        )

        # Then
        output = threshold.get_output_dataset()
        self.assertTrue(output is not None)
        self.assertTrue(output.is_a('vtkUnstructuredGrid'))
        output_range = output.point_data.scalars.range
        self.assertTrue(output_range[0] >= 0.25)
        self.assertTrue(output_range[1] <= 0.75)


if __name__ == '__main__':
    unittest.main()
