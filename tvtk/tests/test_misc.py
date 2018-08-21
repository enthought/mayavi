"""
Tests for enthought/tvtk/misc.py
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2018, Enthought, Inc.
# License: BSD Style.

import unittest
import tempfile
import os.path
import os

from tvtk.api import tvtk, write_data
from tvtk.common import suppress_vtk_warnings


class TestMisc(unittest.TestCase):
    def setUp(self):

        datasets = [tvtk.ImageData(),
                    tvtk.StructuredPoints(),
                    tvtk.RectilinearGrid(),
                    tvtk.StructuredGrid(),
                    tvtk.PolyData(),
                    tvtk.UnstructuredGrid(),
                    ]
        exts = ['.vti', '.vti', '.vtr', '.vts', '.vtp', '.vtu']
        self.datasets = datasets
        self.exts = exts

    def test_write_data_xml_noext(self):
        "XML file writing without extensions"
        # Check if write_data writes out XML files with the correct
        # extension when none is specified.

        datasets = self.datasets
        exts = self.exts

        for d, ext in zip(datasets, exts):
            fh, fname = tempfile.mkstemp(ext)
            fbase = os.path.splitext(fname)[0]
            os.close(fh)
            os.remove(fname)
            write_data(d, fbase)
            self.assertEqual(os.path.exists(fname), True)
            os.remove(fname)

    def test_write_data_xml(self):
        "XML file writing with specified extension"
        datasets = self.datasets

        for d in datasets:
            fh, fname = tempfile.mkstemp('.xml')
            os.close(fh)
            os.remove(fname)
            self.assertEqual(os.path.exists(fname), False)
            write_data(d, fname)
            self.assertEqual(os.path.exists(fname), True)
            os.remove(fname)

    def test_write_data_xml_kwargs(self):
        "XML file writing with extra keyword arguments"
        datasets = self.datasets
        exts = self.exts

        for d, ext in zip(datasets, exts):
            fh, fname = tempfile.mkstemp(ext)
            fbase = os.path.splitext(fname)[0]
            os.close(fh)
            os.remove(fname)
            # Test if passing extra keyword args is supported.
            write_data(d, fbase, compressor=None, data_mode='ascii')
            self.assertEqual(os.path.exists(fname), True)
            os.remove(fname)

    def test_write_data_vtk(self):
        "Old-style VTK file writing with specified extension"
        datasets = self.datasets

        for d in datasets:
            fh, fname = tempfile.mkstemp('.vtk')
            os.close(fh)
            os.remove(fname)
            self.assertEqual(os.path.exists(fname), False)
            write_data(d, fname)
            self.assertEqual(os.path.exists(fname), True)
            r = tvtk.DataSetReader(file_name=fname)
            r.update()
            self.assertEqual(isinstance(r.output, d.__class__), True)
            os.remove(fname)

    def test_suppress_vtk_warnings(self):
        obj = tvtk.to_vtk(tvtk.Object())
        self.assertEqual(obj.GetGlobalWarningDisplay(), 1)
        with suppress_vtk_warnings():
            self.assertEqual(obj.GetGlobalWarningDisplay(), 0)
        self.assertEqual(obj.GetGlobalWarningDisplay(), 1)


if __name__ == '__main__':
    unittest.main()
