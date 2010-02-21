# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2010,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import unittest

import numpy as np

# Local imports.
from enthought.mayavi.core.null_engine import NullEngine

# Enthought library imports
from enthought.mayavi.filters.threshold import Threshold
from enthought.mayavi.sources.array_source import ArraySource


class TestThresholdFilter(unittest.TestCase):
    
    def make_src(self, nan=False):
        data      = np.empty((3, 3, 3))
        if nan:
            data[0]   = np.nan
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
        self.assertEqual(np.nanmin(src.scalar_data),
                         np.nanmin(
                            threshold.outputs[0].point_data.scalars.to_array()
                         ))
        self.assertEqual(np.nanmax(src.scalar_data),
                         np.nanmax(
                            threshold.outputs[0].point_data.scalars.to_array()
                         ))


    def test_threshold_filter_threhsold(self):
        src = self.make_src()
        self.e.add_source(src)
        threshold = Threshold()
        self.e.add_filter(threshold) 
        threshold.upper_threshold = 20.
        self.assertTrue(20 >=
                         np.nanmax(
                            threshold.outputs[0].point_data.scalars.to_array()
                         ))
        return
    

    
if __name__ == '__main__':
    unittest.main()
