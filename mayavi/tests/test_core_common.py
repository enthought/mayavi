"""
Tests for the mayavi.core.common module.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from mayavi.core.common import get_object_path, get_engine
from mayavi.core.file_data_source import NoUITimer
from mayavi.sources.parametric_surface import ParametricSurface
from mayavi.modules.outline import Outline

from mayavi.core.null_engine import NullEngine


class TestCoreCommon(unittest.TestCase):
    def setUp(self):
        e = NullEngine()
        e.start()
        e.new_scene()
        scene = e.scenes[-1]
        s = ParametricSurface()
        e.add_source(s)
        o = Outline()
        s.add_child(o)
        o1 = Outline()
        s.add_child(o1)
        self.scene = scene
        self.e = e
        self.s = s
        self.o = o
        self.o1 = o1
        return

    def test_get_object_path(self):
        "Check if the get_object_path method works correctly."
        e, scene, s, o, o1 = self.e, self.scene, self.s, self.o, self.o1

        value = get_object_path(scene, e)
        self.assertEqual(value, "engine.scenes[0]")
        value = get_object_path(s, e)
        self.assertEqual(value, "engine.scenes[0].children[0]")
        value = get_object_path(o.module_manager, e)
        self.assertEqual(value, "engine.scenes[0].children[0].children[0]")
        value = get_object_path(o, e)
        self.assertEqual(value, "engine.scenes[0].children[0].children[0].children[0]")
        value = get_object_path(o1, e)
        self.assertEqual(value, "engine.scenes[0].children[0].children[0].children[1]")
        # With respect to the scene.
        value = get_object_path(o, scene, "scene")
        self.assertEqual(value, "scene.children[0].children[0].children[0]")
        # With respect to the source.
        value = get_object_path(o, s, "s")
        self.assertEqual(value, "s.children[0].children[0]")
        value = get_object_path(o1, s, "s")
        self.assertEqual(value, "s.children[0].children[1]")

    def test_get_engine(self):
        e, scene, s, o, o1 = self.e, self.scene, self.s, self.o, self.o1
        self.assertEqual(e, get_engine(scene))
        self.assertEqual(e, get_engine(s))
        self.assertEqual(e, get_engine(o))
        self.assertEqual(e, get_engine(o1))
        self.assertEqual(e, get_engine(o.module_manager))
        self.assertEqual(e, get_engine(o1.module_manager))

    def test_remove(self):
        "Does obj.remove() work correctly"
        # Fails only when the current object is the one that is removed.
        self.e.current_object = self.o1
        mm = self.o1.module_manager
        # Remove the object.
        self.o1.remove()
        # Now add another object.
        o1 = Outline()
        self.e.add_module(o1)
        # Is it really added?
        self.assertEqual(o1.module_manager, mm)
        self.assertEqual(o1.parent, mm)


class TestNoUITimer(unittest.TestCase):
    def test_simple_timer(self):
        class A(object):
            def __init__(self):
                self.count = 0
                self.timer = NoUITimer(10, self.step)

            def step(self):
                self.count += 1
                if self.count > 10:
                    self.timer.Stop()

        a = A()
        a.timer.Start()
        self.assertEqual(a.count, 11)
        self.assertFalse(a.timer.IsRunning())

    def test_timer_stops_on_error_and_raises(self):
        class A(object):
            def __init__(self):
                self.count = 0
                self.timer = NoUITimer(10, self.step)

            def step(self):
                self.count += 1
                raise (RuntimeError("Oops"))

        a = A()
        self.assertRaises(RuntimeError, a.timer.Start)
        self.assertEqual(a.count, 1)
        self.assertFalse(a.timer.IsRunning())

    def test_timer_stops_on_stop_iteration(self):
        class A(object):
            def __init__(self):
                self.count = 0
                self.timer = NoUITimer(10, self.step)

            def step(self):
                self.count += 1
                if self.count > 10:
                    raise (StopIteration("Stop"))

        a = A()
        a.timer.Start()
        self.assertEqual(a.count, 11)
        self.assertFalse(a.timer.IsRunning())


if __name__ == "__main__":
    unittest.main()
