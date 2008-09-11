"""
Unit tests for the script recorder.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

import unittest

from enthought.traits.api import (HasTraits, Float, Instance, 
        Str, List, Bool)
from enthought.tvtk.api import tvtk
from enthought.mayavi.core.recorder import Recorder 


######################################################################
# Test classes.
class Toy(HasTraits):
    color = Str
    type = Str
    ignore = Bool(False, record=False)


class Child(HasTraits):
    name = Str('child')
    age = Float(10.0)
    property = Instance(tvtk.Property, (), record=True)
    toy = Instance(Toy, record=True)
    friends = List(Str)

class Parent(HasTraits):
    children = List(Child, record=True)
    recorder = Instance(Recorder, record=False)


class TestRecorder(unittest.TestCase):
    def setUp(self):
        self.tape = Recorder()
        p = Parent()
        c = Child()
        toy = Toy(color='blue', type='bunny')
        c.toy = toy
        p.children.append(c)
        self.p = p
        return

    def tearDown(self):
        self.tape.clear()
        return

    def test_unique_name(self):
        "Does the get_unique_id method work."
        t = tvtk.XMLUnstructuredGridWriter()
        tape = self.tape
        self.assertEqual(tape._get_unique_name(t),
                         'xml_unstructured_grid_writer')
        self.assertEqual(tape._get_unique_name(t),
                         'xml_unstructured_grid_writer1')
        t = Toy()
        self.assertEqual(tape._get_unique_name(t),
                         'toy')

    def test_record(self):
        "Does recording work correctly."
        tape = self.tape
        p = self.p
        c = p.children[0]
        toy = c.toy
        # start recording.
        tape.recording = True
        tape.register(p)

        # Test if p's recorder attribute is set.
        self.assertEqual(tape, p.recorder)

        # Test script ids and object path.
        self.assertEqual(tape.get_script_id(p), 'parent')
        self.assertEqual(tape.get_object_path(p), '')

        self.assertEqual(tape.get_script_id(c), 'child')
        self.assertEqual(tape.get_object_path(c), 'parent.children[0]')

        self.assertEqual(tape.get_script_id(toy), 'child.toy')
        self.assertEqual(tape.get_object_path(toy),
                         'parent.children[0].toy')

        c.name = 'Ram'
        # The child should first be instantiated.
        self.assertEqual(tape.lines[-2], 
                         "child = parent.children[0]")
        # Then its trait set.
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
        # This trait should be ignored.
        toy.ignore = True  
        self.assertEqual(tape.lines[-1], "child.toy.type = 'teddy'")

        # Turn of recording and test.
        tape.recording = False
        toy.type = 'rat'
        self.assertEqual(tape.lines[-1], "child.toy.type = 'teddy'")

        #print tape.script

        # Stop recording.
        n = len(tape.lines)
        tape.unregister(p)
        c.property.representation = 'points'
        toy.type = 'bunny'
        self.assertEqual(tape.lines[-1], "child.toy.type = 'teddy'")
        self.assertEqual(n, len(tape.lines))

        # Make sure the internal data of the recorder is cleared.
        self.assertEqual(0, len(tape._registry))
        self.assertEqual(0, len(tape._reverse_registry))
        self.assertEqual(0, len(tape._known_ids))

    def test_recorded_trait_replaced(self):
        "Does recording work right when a trait is replaced."
        tape = self.tape
        p = self.p
        c = p.children[0]
        toy = c.toy
        # start recording.
        tape.recording = True
        tape.register(p)

        # Test the original trait.
        toy.color = 'red'
        self.assertEqual(tape.lines[-1], "child.toy.color = 'red'")

        # Now reassign the toy.
        t1 = Toy(name='ball')
        c.toy = t1
        t1.color = 'yellow'
        self.assertEqual(tape.lines[-1], "child.toy.color = 'yellow'")

    def test_clear(self):
        "Test the clear method."
        p = self.p
        tape = self.tape

        tape.register(p)
        tape.clear()
        # Everything should be unregistered.
        self.assertEqual(p.recorder, None)
        # Internal data should be wiped clean.
        self.assertEqual(0, len(tape._registry))
        self.assertEqual(0, len(tape._reverse_registry))
        self.assertEqual(0, len(tape._known_ids))
        self.assertEqual(0, len(tape._name_map))

    def test_create_object(self):
        tape = self.tape
        tape.recording = True
        t = Toy()
        tape.register(t)
        t.type = 'computer'

        # Since the name Toy is unknown, there should be a commented
        # line to create it.
        self.assertEqual(tape.lines[-3][-10:], 
                         "import Toy")
        self.assertEqual(tape.lines[-2], 
                         "#toy = Toy()")
        self.assertEqual(tape.lines[-1], 
                         "toy.type = 'computer'")

        # Since this one is known, there should be no imports or
        # anything.
        t1 = Toy()
        tape.register(t1, known=True)
        t1.type = 'ball'
        self.assertEqual(tape.lines[-2], 
                         "toy.type = 'computer'")
        self.assertEqual(tape.lines[-1], 
                         "toy1.type = 'ball'")

    def test_list_items_changed(self):
        "Test if a list item is changed does the change get recorded."
        p = self.p
        tape = self.tape
        child = p.children[0]
        tape.register(p)
        tape.recording = True

        child.friends = ['Krishna', 'Ajay', 'Ali']
        self.assertEqual(tape.lines[-1], 
                         "child.friends = ['Krishna', 'Ajay', 'Ali']")
        child.friends[1:] = ['Sam', 'Frodo']
        self.assertEqual(tape.lines[-1], 
                         "child.friends[1:3] = ['Sam', 'Frodo']")
        child.friends[1] = 'Hari'
        self.assertEqual(tape.lines[-1], 
                         "child.friends[1] = 'Hari'")


    def test_save(self):
        "Test if saving tape to file works."
        tape = self.tape
        p = self.p
        c = p.children[0]
        toy = c.toy

        # Start recording
        tape.register(p)
        tape.recording = True
        toy.type = 'teddy'
        # Now stop.
        tape.recording = False
        tape.unregister(p)

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
