"""
Tests for the CSV file sniffer
"""
# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Ilan Schnell, Enthought, Inc.
# License: BSD Style.
import os.path
import unittest

from numpy import array, ndarray, float64

from enthought.mayavi.tools.wizards.csv_sniff import \
     Sniff, loadtxt, loadtxt_unknown, array2dict


CSV_PATH = os.path.join(os.path.dirname(__file__), 'csv_files')


class Util(object):

    def assertClose(self, x, y):
        self.assertEqual(len(x), len(y))
        for i in xrange(len(x)):
            if isinstance(x[i], (int, float)):
                if repr(x[i]) == 'nan':
                    self.assert_(repr(y[i]) == 'nan')
                else:
                    self.assert_(abs(x[i] - y[i]) < 1e-12 * max(1, abs(x[i])),
                                 '%r %r  %r != %r  %r' %
                                 (type(x[i]),
                                  type(y[i]),
                                  x[i], y[i], abs(x[i] - y[i])))
                    
            elif isinstance(x[i], str):
                self.assertEqual(x[i], y[i])


class Test_Files(unittest.TestCase, Util):

    def test_1(self):
        filename = os.path.join(CSV_PATH, '1.csv')
        
        s = Sniff(filename)
        self.assertEqual(s.delimiter(), ',')
        self.assertEqual(s.skiprows(), 1)
        self.assertEqual(s.dtype()['names'], ('A', 'B', 'C'))
        
        delimiter = s.delimiter()
        if delimiter == ' ':
            delimiter = None
            
        x = loadtxt(filename,
                    delimiter=delimiter,
                    skiprows=s.skiprows(),
                    dtype=s.dtype())

        self.assert_(isinstance(x, ndarray))

        y = array([(1.0, 2.0, 3.20),
                   (7.0, 4.0, 1.87)], 
                  dtype=[('A', float64), ('B', float64), ('C', float64)])
        
        self.assertEqual(x.shape, y.shape)
        self.assertClose(x['A'], y['A'])
        self.assertClose(x['B'], y['B'])
        self.assertClose(x['C'], y['C'])

        d = array2dict(loadtxt_unknown(filename))
        self.assertEqual(type(d), type({}))
        self.assertClose(x['A'], [1, 7])
        self.assertClose(x['B'], [2, 4])
        self.assertClose(x['C'], [3.2, 1.87])


    def test_comment1(self):
        filename = os.path.join(CSV_PATH, 'comment1.csv')
        s = Sniff(filename)
        self.assertEqual(s.comments(), '%')
        
        x = loadtxt_unknown(filename)
        self.assertEqual(x.dtype.names, ('A', 'B', 'C'))
        self.assertClose([x['A']], [1])
        self.assertClose([x['B']], [2])
        self.assertClose([x['C']], [3.2])


class Test_csv_py_files(unittest.TestCase, Util):
    
    def check_csv_py(self, name):
        """ Check if the output array from csv_files/<name>.csv
            (which is of unkown format)
            is the same as the array in csv_files/<name>.py
        """
        x = loadtxt_unknown(os.path.join(CSV_PATH, '%s.csv' % name))
        #print repr(x)
        nan = float('nan')
        y = eval(open(os.path.join(CSV_PATH, '%s.py' % name)).read())
        for name in y.dtype.names:
            self.assertClose(x[name], y[name])
    
    def test_file_example1(self):
        self.check_csv_py('example1')
        
    def test_file_colors(self):
        self.check_csv_py('colors')
        
    def test_file_OObeta3(self):
        self.check_csv_py('OObeta3')
        
    #def test_file_hp11c(self):
    #    self.check_csv_py('hp11c')
        
    #def test_file_1col(self):
    #    self.check_csv_py('1col')
        
    #def test_file_tarray(self):
    #    self.check_csv_py('tarray')


if __name__ == '__main__':
    unittest.main()
