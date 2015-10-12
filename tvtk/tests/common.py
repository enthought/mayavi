""" Test utilities
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import contextlib
import gc
import unittest
import weakref

@contextlib.contextmanager
def restore_gc_state():
    """Ensure that gc state is restored on exit of the with statement."""
    originally_enabled = gc.isenabled()
    try:
        yield
    finally:
        if originally_enabled:
            gc.enable()
        else:
            gc.disable()

class TestGarbageCollection(unittest.TestCase):
    """ This is a base class to use when testing garbage collection.
        See: tvtk.tests.test_garbage_collection
             mayavi.tests.test_garbage_collection
    """

    def check_object_garbage_collected(self, obj_create_fn, obj_close_fn=None):
        """ Call this from a test function to test for garbage collection
            passing the following parameters:

            obj_create_fn: function
                A function with no parameters that creates the object

            obj_close_fn: function
                A function of 1 parameter which is the object created by
                obj_create_fn, to handling the object closing, if any.
        """
        # given
        object_collected = []
        object_weakref = None

        def object_collected_callback(weakref):
            object_collected.append(True)

        def do():
            obj = obj_create_fn()
            reference = weakref.ref(obj, object_collected_callback)
            if obj_close_fn:
                obj_close_fn(obj)
            return reference

        # when
        with restore_gc_state():
            gc.disable()
            object_weakref = do()

        # The object should have been collected.
        self.assertTrue(object_collected[0])
        self.assertIsNone(object_weakref())
