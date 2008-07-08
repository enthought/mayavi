"""
Tests for the CSV file sniffer
"""
# Author: Ilan Schnell <ischnell@enthought.com>
# Copyright (c) 2008, Ilan Schnell, Enthought, Inc.
# License: BSD Style.

import unittest
import numpy as N

from enthought.mayavi.tools.wizards.csv_sniff import \
     Sniff, loadtxt, loadtxt_unknown, array2dict


class Test_Files(unittest.TestCase):

    def test_1(self):
        s = Sniff('csv_files/1.csv')
        self.assertEqual(s.delimiter(), ',')
        self.assertEqual(s.skiprows(), 1)
        self.assertEqual(s.dtype()['names'], ('A', 'B', 'C'))
        self.assertEqual(s.dtype()['formats'], (float, float, float))
        
        delimiter = s.delimiter()
        if delimiter == ' ':
            delimiter = None
            
        x = loadtxt('csv_files/1.csv',
                    delimiter=delimiter,
                    skiprows=s.skiprows(),
                    dtype=s.dtype())

        self.assertEqual(type(x), N.ndarray)

        y = N.array([(1.0, 2.0, 3.20),
                     (7.0, 4.0, 1.87)], 
                    dtype=[('A', 'f'), ('B', 'f'), ('C', 'f')])

        self.assertEqual(x.shape, y.shape)
        self.assert_(N.allclose(x['A'], y['A']))
        self.assert_(N.allclose(x['B'], y['B']))
        self.assert_(N.allclose(x['C'], y['C']))

        d = array2dict(loadtxt_unknown('csv_files/1.csv'))
        self.assertEqual(type(d), type({}))
        self.assert_(N.allclose(x['A'], [1, 7]))
        self.assert_(N.allclose(x['B'], [2, 4]))
        self.assert_(N.allclose(x['C'], [3.2, 1.87]))


    def test_comment1(self):
        s = Sniff('csv_files/comment1.csv')
        self.assertEqual(s.comments(), '%')
        
        x = loadtxt_unknown('csv_files/comment1.csv')
        self.assertEqual(x.dtype.names, ('A', 'B', 'C'))
        

    def test_colors(self):
        x = loadtxt_unknown('csv_files/colors.dat')
        self.assertEqual(x.dtype.names, ('Name', 'r', 'g', 'b'))
        self.assertEqual(list(x['Name']),
                         ['Red', 'Green', 'Blue', 'Orange', 'Yellow'])

if __name__ == '__main__':
    unittest.main()
