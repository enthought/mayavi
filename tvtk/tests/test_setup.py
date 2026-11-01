"""Tests for the build-time helpers in tvtk/_setup.py."""

import os
import tempfile
import unittest
import zipfile

from tvtk._setup import _zip_stamp


class TestZipStamp(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.zip = os.path.join(self.tmp.name, 'tvtk_classes.zip')

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, code):
        with zipfile.ZipFile(self.zip, 'w') as z:
            z.writestr('tvtk_classes/vtk_version.py', code)

    def test_reads_the_stamp(self):
        self._write("vtk_build_version = '9.7'\n"
                    "generation_stamp = 'vtk 9.7.0, python 3.14, generator x'\n")
        self.assertEqual(_zip_stamp(self.zip),
                         'vtk 9.7.0, python 3.14, generator x')

    def test_unstamped_zip_is_not_current(self):
        # what every ZIP generated before stamps were introduced looks like
        self._write("vtk_build_version = '9.7'\n")
        self.assertIsNone(_zip_stamp(self.zip))

    def test_missing_zip_is_not_current(self):
        self.assertIsNone(_zip_stamp(self.zip))


if __name__ == '__main__':
    unittest.main()
