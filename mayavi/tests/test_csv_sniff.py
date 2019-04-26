"""
Tests for the CSV file sniffer
"""
# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.
import glob
import os
import os.path
import sys
import unittest
import tempfile
from unittest import SkipTest

from numpy import array, ndarray

from mayavi.tools.data_wizards.csv_sniff import \
     Sniff, loadtxt, loadtxt_unknown, array2dict


class Util(unittest.TestCase):

    def assertNamedClose(self, x, y):
        self.assertEqual(x.shape, y.shape)
        self.assertEqual(x.dtype.names, y.dtype.names)
        for name in x.dtype.names:
            self.assertAllClose(x[name], y[name])

    def assertAllClose(self, x, y):
        self.assertEqual(len(x), len(y))
        for a, b in zip(x, y):
            self.assertClose(a, b)

    def assertClose(self, a, b):
        if isinstance(a, (int, float)):
            if repr(a) == 'nan':
                self.assertTrue(repr(b) == 'nan')
            else:
                self.assertTrue(abs(a - b) < 1e-6 * max(1, abs(a)),
                             '%r != %r  %r' % (a, b, abs(a - b)))

        elif isinstance(a, (str, bytes)):
            self.assertEqual(a, b)

        else:
            self.assertFalse("Hmm, did not expect: %s" % a)

class Test(Util):

    def test_API(self):
        fo = tempfile.mktemp()
        with open(fo, 'w') as f:
            f.write(''' "A", "B", "C"
                         1, 2, 3.2
                         7, 4, 1.87''')

        s = Sniff(fo)
        self.assertEqual(s.comments(), '#')
        self.assertEqual(s.delimiter(), ',')
        self.assertEqual(s.skiprows(), 1)
        self.assertEqual(s.dtype(), {'names': ('A', 'B', 'C'),
                                     'formats': (float, float, float)})
        x = s.loadtxt()
        y = array([(1.0, 2.0, 3.20),
                   (7.0, 4.0, 1.87)],
                  dtype=[('A', float), ('B', float), ('C', float)])
        self.assertNamedClose(x, y)

        y = loadtxt(fo, **s.kwds())
        self.assertNamedClose(x, y)

        y = loadtxt_unknown(fo)
        self.assertNamedClose(x, y)

        d = array2dict(y)
        self.assertEqual(type(d), type({}))
        self.assertAllClose(x['A'], [1, 7])
        self.assertAllClose(x['B'], [2, 4])
        self.assertAllClose(x['C'], [3.2, 1.87])


    def test_comment(self):
        fo = tempfile.mktemp()
        with open(fo, 'w') as f:
            f.write('''
            % "A"  "B"  "C"
               1    2   4.2   % comment''')

        s = Sniff(fo)
        self.assertEqual(s.kwds(),
          {'dtype': {'names': ('A', 'B', 'C'),
                     'formats': (float, float, float)},
           'delimiter': None,
           'skiprows': 0,   # FIXME
           'comments': '%'})


    def test_tabs(self):
        fo = tempfile.mktemp()
        with open(fo, 'w') as f:
            f.write('''54\t87\n21\t32''')

        s = Sniff(fo)
        self.assertEqual(s.delimiter(), None)
        self.assertEqual(s.skiprows(), 0)


    def test_nohead(self):
        fo = tempfile.mktemp()
        with open(fo, 'w') as f:
            f.write('''Hello;54;87\nWorld;42;86.5''')

        s = Sniff(fo)
        self.assertEqual(s.kwds(),
          {'comments': '#',
           'delimiter': ';',
           'skiprows': 0,
           'dtype': {'names': ('Column 1', 'Column 2', 'Column 3'),
                     'formats': ('S5', float, float)}})


    def test_empty_file(self):
        fo = tempfile.mktemp()
        with open(fo, 'w') as f:
            f.write('')
        self.assertRaises(IndexError, Sniff, fo)

class Test_csv_py_files(Util):
    """
        These tests require files in csv_files/
    """
    def check(self, name, skip_if_win=False):
        """
            Check if the output array from csv_files/<name>.csv
            (which is of unkown format)
            is the same as the array in csv_files/<name>.py
        """
        if skip_if_win and sys.platform.startswith('win'):
            raise SkipTest

        # Note: The files needed for the test are currently accessed directly.
        #       This assumes that the files are present, and not in a zipped
        #       egg.  traits.util.resource as supposed to always work, but
        #       when it ran the striped the tests in the EPD installer tests,
        #       it was broken.  Since we define zip_safe = False in setup.py
        #       it is safe to assume the files are always present.

        s = Sniff(os.path.join(os.path.dirname(__file__),
                               'csv_files', name + '.csv'))

        f_py = os.path.join(os.path.dirname(__file__),
                            'csv_files', name + '.py')

        if not sys.platform.startswith('win'):
            nan = float('nan') # must be in namespace for some .py files

        d = eval(open(f_py).read())

        self.assertEqual(d['kwds'], s.kwds())
        self.assertNamedClose(d['array'], s.loadtxt())

    def test_11(self):
        self.check('11')

    def test_1col(self):
        self.check('1col')

    def test_54(self):
        self.check('54')

    def test_79(self):
        self.check('79')

    def test_82(self):
        self.check('82')

    def test_89(self):
        self.check('89')

    def test_99(self):
        self.check('99')

    def test_colors(self):
        self.check('colors')

    def test_example1(self):
        # this test need to be skipped on Windows because the data file
        # has some floats nan, and float('nan') fails on on Windows.
        self.check('example1', skip_if_win=True)

    def test_hp11c(self):
        self.check('hp11c')

    def test_loc(self):
        self.check('loc')

    def test_multi_col(self):
        self.check('multi-col')

    def test_mydata(self):
        self.check('mydata')

    def test_OObeta3(self):
        self.check('OObeta3')

    def test_post(self):
        self.check('post')

    def test_webaccess(self):
        self.check('webaccess')


if __name__ == '__main__':
    unittest.main()
