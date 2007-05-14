"""Unit tests for the array related extension code.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004, Enthought, Inc.
# License: BSD Style.

import unittest
import sys
try:
    import Numeric
except ImportError:
    print "This test only works when Numeric is installed."
    sys.exit(0)
    
import vtk
import weakref
import gc

from enthought.tvtk import array_ext

class TestArrayExt(unittest.TestCase):
    def test_empty_array(self):
        shapes = [(1,2), (2,2), (3,3), (4,5)]
        typecodes = ['l', 'i', 'd', 'f']
        for shape, typecode in zip(shapes, typecodes):
            a = array_ext.empty_array(shape, typecode)
            self.assertEqual(a.shape, shape)
            self.assertEqual(a.typecode(), typecode)
            # Check garbage collection.
            r = weakref.ref(a)
            del a
            gc.collect()
            self.assertEqual(r(), None)

    def test_set_id_type_array(self):
        N = 5
        a = Numeric.zeros((N,4), 'l')
        a[:,1] = 1
        a[:,2] = 2
        a[:,3] = 3
        
        def diff_arr(x, y):
            return Numeric.sum(Numeric.ravel(x) - Numeric.ravel(y[:,1:]))                

        # Test contiguous arrays.
        b = Numeric.zeros((N,5), 'l')
        array_ext.set_id_type_array(a, b)
        self.assertEqual(diff_arr(a, b), 0)

        # Test non-contiguous arrays.
        b = Numeric.zeros((N,3), 'l')
        array_ext.set_id_type_array(a[:,::2], b)
        self.assertEqual(diff_arr(a[:,::2], b), 0)

        # Test 1D array.
        b = Numeric.zeros(N*5, 'l')
        array_ext.set_id_type_array(a, b)
        self.assertEqual(diff_arr(a, Numeric.reshape(b, (N,5))), 0)

        # Test assertions.
        d = a.astype('d')
        b = Numeric.zeros((N, 5), 'l')
        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          d, b)
        
        b = Numeric.zeros((N, 5), 'd')
        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          a, b)

        # B should b contiguous.
        b = Numeric.zeros((N, 10), 'l')
        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          a, b[:,::2])

        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          a[0], b)

        # Test size check assertion.
        b = Numeric.zeros((N, 4), 'l')
        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          a, b)
        
        b = Numeric.zeros(N*6, 'l')
        self.assertRaises(AssertionError, array_ext.set_id_type_array,
                          a, b)

        # This should work!
        array_ext.set_id_type_array(a, b[:N*5])
        self.assertEqual(diff_arr(a, Numeric.reshape(b[:N*5], (N,5))), 0)
        
        

def test_suite():
    """Collects all the tests to be run."""
    suites = []
    suites.append(unittest.makeSuite(TestArrayExt, 'test_'))
    total_suite = unittest.TestSuite(suites)
    return total_suite

def test(verbose=2):
    """Useful when you need to run the tests interactively."""
    all_tests = test_suite()
    runner = unittest.TextTestRunner(verbosity=verbose)
    result = runner.run(all_tests)
    return result, runner

if __name__ == "__main__":
    unittest.main()
