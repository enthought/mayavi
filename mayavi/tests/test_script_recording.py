"""
A simple test for script recording in Mayavi.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from apptools.scripting.api import Recorder, set_recorder
from mayavi.sources.parametric_surface import \
    ParametricSurface
from mayavi.modules.outline import Outline
from mayavi.modules.surface import Surface

from mayavi.core.null_engine import NullEngine


class TestScriptRecording(unittest.TestCase):
    def setUp(self):
        tape = Recorder()
        # Set the global recorder.
        set_recorder(tape)
        self.tape = tape

    def tearDown(self):
        self.tape.clear()
        set_recorder(None)

    def test_script_recording(self):
        "Does script recording work correctly."
        # Create a mayavi pipeline and record it.
        tape = self.tape
        e = NullEngine()
        e.start()
        # Start recording.
        tape.recording = True
        tape.register(e, known=True, script_id='engine')
        e.new_scene()
        self.assertEqual(tape.lines[-1],
                         "dummy_viewer = engine.new_scene()")

        src = ParametricSurface()
        e.add_source(src)
        expect = 'from mayavi.sources.parametric_surface '\
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
        expect = 'from mayavi.modules.outline import Outline'
        self.assertEqual(tape.lines[-3], expect)
        self.assertEqual(tape.lines[-2], "outline = Outline()")
        self.assertEqual(tape.lines[-1],
                         "engine.add_module(outline)")

        o.actor.property.color = (1,0,0)
        self.assertEqual(tape.lines[-1],
                         "outline.actor.property.color = (1.0, 0.0, 0.0)")

        s = Surface()
        e.add_module(s)
        expect = 'from mayavi.modules.surface import Surface'
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

        # Stop recording and test.
        tape.unregister(e)
        tape.record('#end') # Placeholder
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
