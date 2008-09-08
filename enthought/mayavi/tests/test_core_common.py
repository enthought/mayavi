"""
Tests for the enthought.mayavi.core.common module.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from enthought.traits.api import HasTraits, Any, Event
from enthought.mayavi.core.common import get_object_path, get_engine
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.core.scene import Scene
from enthought.mayavi.sources.parametric_surface import \
    ParametricSurface
from enthought.mayavi.modules.outline import Outline


class DummyViewer(HasTraits):
    scene = Any
    closing = Event
    activated = Event


class TestCoreCommon(unittest.TestCase):
    def setUp(self):
        e = Engine()
        e.start()
        e.new_scene(DummyViewer())
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


if __name__ == '__main__':
    unittest.main()
