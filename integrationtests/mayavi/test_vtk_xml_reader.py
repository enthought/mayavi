"""Simple test to check the VTK XML reader -- this is basically a copy
of test_contour.py with just the reader changed.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020,  Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import abspath
import copy

# Local imports.
from common import TestCase, get_example_data
from test_vtk_data_source import TestVTKDataSource

class TestVTKXMLReader(TestVTKDataSource):
    def make_data(self):
        script = self.script
        from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

        ############################################################
        # Create a new scene and set up the visualization.
        s = self.new_scene()

        # Read a VTK XML data file.
        r = VTKXMLFileReader()
        r.initialize(get_example_data('heart.vti'))
        script.add_source(r)

    def test(self):
        self.main()

if __name__ == "__main__":
    t = TestVTKXMLReader()
    t.test()
