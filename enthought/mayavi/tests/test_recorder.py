"""
Unit tests for the script recorder.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from enthought.traits.api import (HasTraits, Int, Float, Instance, 
        Str, List, Bool, implements)
from enthought.tvtk.api import tvtk
from enthought.mayavi.core.recorder import (Recorder, Listner,
        IRecordable, setup_recording, do_record)


class Recordable(HasTraits):

    implements(IRecordable)

    recorder = Instance(Recorder, transient=True)

    _script_id = Str(transient=True)

    _listners = List(transient=True)

    def record(self, obj, name, old, new):
        do_record(self, obj, name, old, new)


class Toy(HasTraits):
    color = Str
    type = Str
    ignore = Bool(False, record=False)


class Child(Recordable):
    name = Str('child')
    age = Float(10.0)
    property = Instance(tvtk.Property, (), listen=True)
    _script_id = ''
    toy = Instance(Toy, listen=True)

    def _recorder_changed(self, old, new):
        setup_recording(self, new)


class Parent(HasTraits):
    children = List(Child)

    recorder = Instance(Recorder)

    # We assume that the active child is settable always.
    active_child = Int

    def _recorder_changed(self, old, new):
        for child in self.children:
            child.recorder = new
        if new is not None:
            self._active_child_changed(self.active_child)

    def _active_child_changed(self, new):
        if self.recorder is not None:
            child_name = self.children[new]._script_id
            self.recorder.record('%s = parent.children[%d]'%(child_name,
                new))


class TestListner(unittest.TestCase):
    def test_listner(self):
        "Test the Listner class."
        class A(HasTraits):
            toy = Instance(Toy)
            test = List
            def record(self, obj, name, old, new):
                self.test = [obj, name, old, new]

        toy = Toy(color='blue', type='bunny')
        a = A(toy=toy)
        l = Listner(a, 'toy')
        toy.color = 'black'
        self.assertEqual(a.test, [toy, 'toy.color', 'blue', 'black'])
        # Should not listen to traits marked with record=False.
        toy.ignore = True
        self.assertEqual(a.test, [toy, 'toy.color', 'blue', 'black'])
        self.assertEqual(a.test, [toy, 'toy.color', 'blue', 'black'])
        l.stop()
        toy.color = 'red'
        self.assertEqual(a.test, [toy, 'toy.color', 'blue', 'black'])


class TestRecorder(unittest.TestCase):
    def setUp(self):
        self.tape = Recorder()
        return
    def tearDown(self):
        self.tape.clear()
        return

    def test_unique_id(self):
        "Does the get_unique_id method work."
        t = tvtk.XMLUnstructuredGridWriter()
        tape = self.tape
        self.assertEqual(tape.get_unique_id(t),
                         'xml_unstructured_grid_writer')
        self.assertEqual(tape.get_unique_id(t),
                         'xml_unstructured_grid_writer1')
        t = Toy()
        self.assertEqual(tape.get_unique_id(t),
                         'toy')

    def test_record(self):
        "Does recording work correctly."
        tape = self.tape

        p = Parent()
        c = Child()
        toy = Toy(color='blue', type='bunny')
        c.toy = toy
        p.children.append(c)
        # start recording.
        p.recorder = tape
        # Check that the script ids are set.
        self.assertEqual(c._script_id, 'child')
        p.active_child = 0
        self.assertEqual(tape.lines[-1], 
                         "child = parent.children[0]")
        c.name = 'Ram'
        self.assertEqual(tape.lines[-1], "child.name = 'Ram'")
        c.age = 10.5
        self.assertEqual(tape.lines[-1], "child.age = 10.5")
        c.property.representation = 'w'
        self.assertEqual(tape.lines[-1], 
                         "child.property.representation = 'wireframe'")
        c.property.color = (1, 0, 0)
        self.assertEqual(tape.lines[-1], 
                         "child.property.color = (1.0, 0.0, 0.0)")
        toy.color = 'red'
        self.assertEqual(tape.lines[-1], "child.toy.color = 'red'")
        toy.type = 'teddy'
        self.assertEqual(tape.lines[-1], "child.toy.type = 'teddy'")

        # Stop recording.
        n = len(tape.lines)
        p.recorder = None
        c.property.representation = 'points'
        toy.type = 'bunny'
        self.assertEqual(tape.lines[-1], "child.toy.type = 'teddy'")
        self.assertEqual(n, len(tape.lines))
        # The script ids should be reset to ''
        self.assertEqual(c._script_id, '')


    def test_save(self):
        "Test if saving tape to file works."
        tape = self.tape
        p = Parent()
        c = Child()
        toy = Toy(color='blue', type='bunny')
        c.toy = toy
        p.children.append(c)
        # Start recording
        p.recorder = tape
        p.active_child = 0
        toy.type = 'teddy'
        p.recorder = None
        import StringIO
        f = StringIO.StringIO()
        tape.save(f)
        # Test if the file is OK.
        expect = ["child = parent.children[0]\n",
                  "child.toy.type = 'teddy'\n"
                  ]
        f.seek(0)
        lines = f.readlines()
        self.assertEqual(expect, lines)
        f.close()

if __name__ == '__main__':
    unittest.main()
