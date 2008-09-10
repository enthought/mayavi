"""
A simple test for script recording in Mayavi.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from enthought.traits.api import HasTraits, Any, Event

from enthought.mayavi.core.recorder import Recorder
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.sources.parametric_surface import \
    ParametricSurface
from enthought.mayavi.modules.outline import Outline
from enthought.mayavi.modules.surface import Surface


class DummyViewer(HasTraits):
    scene = Any
    closing = Event
    activated = Event


class TestScriptRecording(unittest.TestCase):
    def test_script_recording(self):
        "Does script recording work correctly."
        # Create a mayavi pipeline and record it.
        tape = Recorder()
        e = Engine()
        e.start()
        # Start recording.
        tape.recording = True
        tape.register(e, known=True)
        v = DummyViewer()
        e.new_scene(v)
        self.assertEqual(tape.lines[-1], 
                         "scene = engine.new_scene()")

        src = ParametricSurface()
        e.add_source(src)
        expect = 'from enthought.mayavi.sources.parametric_surface '\
                 'import ParametricSurface'
        self.assertEqual(tape.lines[-3], expect)
        self.assertEqual(tape.lines[-2], 
                         "parametric_surface = ParametricSurface()")
        self.assertEqual(tape.lines[-1], 
                         "engine.add_source(parametric_surface)")

        src.function = 'dini'
        self.assertEqual(tape.lines[-1], 
                         "parametric_surface.function = 'dini'")

        o = Outline()
        e.add_module(o)
        expect = 'from enthought.mayavi.modules.outline import Outline'
        self.assertEqual(tape.lines[-3], expect)
        self.assertEqual(tape.lines[-2], "outline = Outline()")
        self.assertEqual(tape.lines[-1], 
                         "engine.add_module(outline)")

        o.actor.property.color = (1,0,0)
        self.assertEqual(tape.lines[-1], 
                         "outline.actor.property.color = (1.0, 0.0, 0.0)")

        s = Surface()
        e.add_module(s)
        expect = 'from enthought.mayavi.modules.surface import Surface'
        self.assertEqual(tape.lines[-3], expect)
        self.assertEqual(tape.lines[-2], "surface = Surface()")
        self.assertEqual(tape.lines[-1], 
                         "engine.add_module(surface)")

        s.actor.property.representation = 'wireframe'
        self.assertEqual(tape.lines[-1], 
                         "surface.actor.property.representation = 'wireframe'")

        o.actor.property.representation = 'wireframe'
        self.assertEqual(tape.lines[-1], 
                         "outline.actor.property.representation = 'wireframe'")
        
        s.actor.property.opacity = 0.5
        self.assertEqual(tape.lines[-1], 
                         "surface.actor.property.opacity = 0.5")

        s.actor.mapper.scalar_visibility = False
        self.assertEqual(tape.lines[-1], 
                         "surface.actor.mapper.scalar_visibility = False")

        print tape.script

        # Stop recording and test.
        tape.record('#end') # Placeholder
        tape.unregister(e)
        o.actor.property.opacity = 0.5
        self.assertEqual(tape.lines[-1], '#end')
        s.actor.property.color = (1,0,0)
        self.assertEqual(tape.lines[-1], '#end')
        s.enable_contours = True
        self.assertEqual(tape.lines[-1], '#end')
        src.function = 'klein'
        self.assertEqual(tape.lines[-1], '#end')


if __name__ == '__main__':
    unittest.main()
