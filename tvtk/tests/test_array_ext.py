"""Unit tests for the array related extension code.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

import unittest

import numpy

from tvtk.array_handler import ID_TYPE_CODE, set_id_type_array_py
from tvtk.array_ext import set_id_type_array


class TestArrayExt(unittest.TestCase):
    def check(self, set_id_type_array):
        N = 5
        a = numpy.zeros((N, 4), ID_TYPE_CODE)
        a[:, 1] = 1
        a[:, 2] = 2
        a[:, 3] = 3

        def diff_arr(x, y):
            return numpy.sum(numpy.ravel(x) - numpy.ravel(y[:, 1:]))

        # Test contiguous arrays.
        b = numpy.zeros((N, 5), ID_TYPE_CODE)
        set_id_type_array(a, b)
        self.assertEqual(diff_arr(a, b), 0)

        # Test non-contiguous arrays.
        b = numpy.zeros((N, 3), ID_TYPE_CODE)
        set_id_type_array(a[:, ::2], b)
        self.assertEqual(diff_arr(a[:, ::2], b), 0)

        # Test 1D array.
        b = numpy.zeros(N*5, ID_TYPE_CODE)
        set_id_type_array(a, b)
        self.assertEqual(diff_arr(a, numpy.reshape(b, (N, 5))), 0)

        # Test assertions.
        d = a.astype('d')
        b = numpy.zeros((N, 5), ID_TYPE_CODE)
        self.assertRaises(AssertionError, set_id_type_array,
                          d, b)

        # B should b contiguous.
        b = numpy.zeros((N, 10), ID_TYPE_CODE)
        self.assertRaises(AssertionError, set_id_type_array,
                          a, b[:, ::2])

        self.assertRaises(AssertionError, set_id_type_array,
                          a[0], b)

        # Test size check assertion.
        b = numpy.zeros((N, 4), ID_TYPE_CODE)
        self.assertRaises(AssertionError, set_id_type_array,
                          a, b)

        b = numpy.zeros(N*6, ID_TYPE_CODE)
        self.assertRaises(AssertionError, set_id_type_array,
                          a, b)

        # This should work!
        set_id_type_array(a, b[:N*5])
        self.assertEqual(diff_arr(a, numpy.reshape(b[:N*5], (N, 5))), 0)

    def test_set_id_type_array(self):
        self.check(set_id_type_array)

    def test_set_id_type_array_py(self):
        self.check(set_id_type_array_py)


if __name__ == "__main__":
    unittest.main()
