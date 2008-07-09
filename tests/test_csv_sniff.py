"""
Tests for the CSV file sniffer
"""
# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Ilan Schnell, Enthought, Inc.
# License: BSD Style.

import unittest

from numpy import array, ndarray, float64

from enthought.mayavi.tools.wizards.csv_sniff import \
     Sniff, loadtxt, loadtxt_unknown, array2dict


class Test_Files(unittest.TestCase):

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
            

    def test_1(self):
        s = Sniff('csv_files/1.csv')
        self.assertEqual(s.delimiter(), ',')
        self.assertEqual(s.skiprows(), 1)
        self.assertEqual(s.dtype()['names'], ('A', 'B', 'C'))
        
        delimiter = s.delimiter()
        if delimiter == ' ':
            delimiter = None
            
        x = loadtxt('csv_files/1.csv',
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

        d = array2dict(loadtxt_unknown('csv_files/1.csv'))
        self.assertEqual(type(d), type({}))
        self.assertClose(x['A'], [1, 7])
        self.assertClose(x['B'], [2, 4])
        self.assertClose(x['C'], [3.2, 1.87])


    def test_comment1(self):
        s = Sniff('csv_files/comment1.csv')
        self.assertEqual(s.comments(), '%')
        
        x = loadtxt_unknown('csv_files/comment1.csv')
        self.assertEqual(x.dtype.names, ('A', 'B', 'C'))
        self.assertClose([x['A']], [1])
        self.assertClose([x['B']], [2])
        self.assertClose([x['C']], [3.2])

    def test_colors(self):
        x = loadtxt_unknown('csv_files/colors.csv')
        self.assertEqual(x.dtype.names, ('Name', 'r', 'g', 'b'))
        self.assertEqual(list(x['Name']),
                         ['Red', 'Green', 'Blue', 'Orange', 'Yellow'])

    def test_files(self):
        # Test various files in `csv_files` subfolder for each .csv
        # there must be a .py which contains the corresponding array.
        for name in '''example1 colors
                    '''.split():
            x = loadtxt_unknown('csv_files/%s.csv' % name)
            #print repr(x)
            nan = float('nan')
            y = eval(open('csv_files/%s.py' % name).read())
            for name in y.dtype.names:
                self.assertClose(x[name], y[name])


if __name__ == '__main__':
    unittest.main()
