"""
Tests for the mayavi.core.common module.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import os
from subprocess import check_output
import sys
import unittest

from traitsui.api import View

from mayavi.core.common import get_object_path, get_engine
from mayavi.core.file_data_source import NoUITimer
from mayavi.sources.parametric_surface import \
    ParametricSurface
from mayavi.modules.outline import Outline
from mayavi.modules.surface import Surface

from mayavi.core.null_engine import NullEngine


def test_core_common_pyface_import_honors_env_var():
    # Given
    cmd = [sys.executable, "-c",
           "import mayavi.core.common as C; print(C.pyface)"]

    def _make_env(ets=None, ci=None):
        env = dict(os.environ)
        if 'ETS_TOOLKIT' in env:
            del env['ETS_TOOLKIT']
        if 'CI' in env:
            del env['CI']
        if ets is not None:
            env['ETS_TOOLKIT'] = ets
        if ci is not None:
            env['CI'] = ci
        return env

    # When
    out = check_output(cmd, env=_make_env())
    result = out.strip().decode('utf-8')

    # Then
    assert result != 'None'

    # When
    out = check_output(cmd, env=_make_env(ets='qt'))
    result = out.strip().decode('utf-8')

    # Then
    assert result != 'None'

    # When
    out = check_output(cmd, env=_make_env(ets='null'))
    result = out.strip().decode('utf-8')

    # Then
    assert result == 'None'

    # When
    out = check_output(cmd, env=_make_env(ets='qt', ci='1'))
    result = out.strip().decode('utf-8')

    # Then
    assert result == 'None'


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
        self.assertEqual(value, 'engine.scenes[0]')
        value = get_object_path(s, e)
        self.assertEqual(value, 'engine.scenes[0].children[0]')
        value = get_object_path(o.module_manager, e)
        self.assertEqual(value,
                        'engine.scenes[0].children[0].children[0]')
        value = get_object_path(o, e)
        self.assertEqual(value,
                        'engine.scenes[0].children[0].children[0].children[0]')
        value = get_object_path(o1, e)
        self.assertEqual(value,
                        'engine.scenes[0].children[0].children[0].children[1]')
        # With respect to the scene.
        value = get_object_path(o, scene, 'scene')
        self.assertEqual(value,
                         'scene.children[0].children[0].children[0]')
        # With respect to the source.
        value = get_object_path(o, s, 's')
        self.assertEqual(value, 's.children[0].children[0]')
        value = get_object_path(o1, s, 's')
        self.assertEqual(value, 's.children[0].children[1]')

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


class TestHandCraftedView(unittest.TestCase):
    def test_that_custom_views_are_loaded(self):
        # Given/When
        s = Surface()

        # Then
        self.assertTrue(os.path.exists(s._view_filename))
        self.assertTrue(s._module_view is not None)
        self.assertTrue(isinstance(s._module_view,  View))

        # When there is no view, it should work safely.
        # Given/When
        o = Outline()

        # Then
        self.assertFalse(os.path.exists(o._view_filename))
        self.assertEqual(o._module_view, None)


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
                raise(RuntimeError('Oops'))

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
                    raise(StopIteration('Stop'))

        a = A()
        a.timer.Start()
        self.assertEqual(a.count, 11)
        self.assertFalse(a.timer.IsRunning())


if __name__ == '__main__':
    unittest.main()
