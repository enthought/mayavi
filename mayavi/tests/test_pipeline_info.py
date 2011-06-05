"""
Tests for the pipeline_info.py module
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

import unittest

from tvtk.api import tvtk
from mayavi.core import pipeline_info


class TestPipelineInfoTest(unittest.TestCase):

    def test_tvtk_dataset_name(self):
        "Can tvtk datasets can be converted to names correctly."
        datasets = [tvtk.ImageData(),
                    tvtk.StructuredPoints(),
                    tvtk.RectilinearGrid(),
                    tvtk.StructuredGrid(),
                    tvtk.PolyData(),
                    tvtk.UnstructuredGrid(),
                    tvtk.Property(), # Not a dataset!
                    'foo', # Not a TVTK object.
                    ]
        expect = ['image_data',
                  'image_data',
                  'rectilinear_grid',
                  'structured_grid',
                  'poly_data',
                  'unstructured_grid',
                  'none',
                  'none'
                  ]
        result = [pipeline_info.get_tvtk_dataset_name(d) for d in datasets]
        self.assertEqual(result, expect)

    def test_default_pipeline_info(self):
        "Is the default PipelineInfo class built right."
        p = pipeline_info.PipelineInfo()
        self.assertEqual(len(p.datasets), 0)
        self.assertEqual(len(p.attribute_types), 0)
        self.assertEqual(len(p.attributes), 0)



if __name__ == '__main__':
    unittest.main()
