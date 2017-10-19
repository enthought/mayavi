"""
Tests for traits defined in mayavi.core.traits
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

import unittest
import numpy
from traits.api import (HasTraits, Either, Array, Any,
                TraitError, Float, Int)
from mayavi.core.trait_defs import (ArrayNumberOrNone, ArrayOrNone,
    ShadowProperty)


class DataNotSmart(HasTraits):
    x = ShadowProperty(ArrayOrNone, smart_notify=False)
    # Test attribute.
    _test = Any
    def _x_changed(self, value):
        self._test = value.copy()

class DataSmart(HasTraits):
    x = ShadowProperty(ArrayOrNone, smart_notify=True)
    # Test attribute.
    _test = Any
    def _x_changed(self, value):
        self._test = value.copy()

class Simple(HasTraits):
    x = ShadowProperty(Float)
    # Test attribute.
    _test = Int(0)
    def _x_changed(self, value):
        self._test += 1

class HasArrays(HasTraits):
    x = ArrayOrNone
    y = ArrayNumberOrNone

    # Test attribute.
    _test_x = Int(0)
    _test_y = Int(0)

    def _x_changed(self, value):
        self._test_x += 1

    def _y_changed(self, value):
        self._test_y += 1


class TestShadowProperty(unittest.TestCase):
    def test_simple_case(self):
        "Test a simple trait wrapped as a shadow property."
        s = Simple(x=10.0)
        self.assertEqual(s._test, 1)
        self.assertEqual(s.x, 10.0)
        s.x = 10.0
        self.assertEqual(s._test, 1)
        self.assertEqual(s.x, 10.0)
        s.x = 20.0
        self.assertEqual(s._test, 2)
        self.assertEqual(s.x, 20.0)
        self.assertRaises(TraitError, s.__setattr__, 'x', 'hey')

    def test_shadow_property_smart(self):
        "Test if the shadow property trait type works correctly."
        x = numpy.linspace(0, 1)
        d = DataSmart(x=x)
        self.assertEqual(numpy.all(d.x == x), True)
        self.assertEqual(numpy.all(d._x == x), True)
        self.assertEqual(numpy.all(d._test == x), True)
        old = x.copy()
        x *= 2
        d.x = x
        self.assertEqual(numpy.all(d.x == x), True)
        self.assertEqual(numpy.all(d._x == x), True)
        # Notifier shouldn't be called.
        self.assertEqual(numpy.all(d._test == old), True)

    def test_shadow_property_not_smart(self):
        "Test if the shadow property trait type works correctly."
        x = numpy.linspace(0, 1)
        d = DataNotSmart(x=x)
        self.assertEqual(numpy.all(d.x == x), True)
        self.assertEqual(numpy.all(d._x == x), True)
        self.assertEqual(numpy.all(d._test == x), True)
        x *= 2
        d.x = x
        self.assertEqual(numpy.all(d.x == x), True)
        self.assertEqual(numpy.all(d._x == x), True)
        self.assertEqual(numpy.all(d._test == x), True)

    def test_type_checking(self):
        "Test if the validation works correctly."
        x = numpy.linspace(0, 1)
        d = DataNotSmart(x=x)
        self.assertRaises(TraitError, d.__setattr__, 'x', 'hey')

    def test_set_trait_change_notify(self):
        "If trait_change_notify is honored."
        s = Simple()
        trait_names = s.trait_names()
        s.x = 10.0
        self.assertEqual(s._test, 1)
        self.assertEqual(s.x, 10.0)
        s.trait_set(x=20.0, trait_change_notify=False)
        self.assertEqual(s._test, 1)
        self.assertEqual(s.x, 20.0)
        # Assert that no new traits were added and no new notifiers were
        # added.
        self.assertEqual(s.trait_names(), trait_names)
        self.assertEqual(s._notifiers(False), None)


class TestArrayOrNone(unittest.TestCase):

    def test_default(self):
        a = HasArrays()
        self.assertIsNone(a.x)
        self.assertIsNone(a.y)

    def test_no_compare(self):
        a = HasArrays()
        a.x = numpy.arange(10)
        self.assertEqual(a._test_x, 1)
        a.x = numpy.arange(10)
        self.assertEqual(a._test_x, 2)
        a.x = a.x
        self.assertEqual(a._test_x, 3)
        a.x = None
        self.assertEqual(a._test_x, 4)

        a.y = numpy.arange(10)
        self.assertEqual(a._test_y, 1)
        a.y = 1.0
        self.assertEqual(a.y.shape, (1,))
        self.assertEqual(a._test_y, 2)
        a.y = a.y
        self.assertEqual(a._test_y, 3)
        a.y = None
        self.assertEqual(a._test_y, 4)


if __name__ == '__main__':
    unittest.main()

