"""
Unit tests for the script recorder -- the script recorder has been
refactored to move to AppTools however we repeat the tests here with a
TVTK object to ensure that the test works with TVTK objects.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2015, Enthought, Inc.
# License: BSD Style.

import sys
import unittest

from traits.api import (HasTraits, Float, Instance,
        Str, List, Bool)
from tvtk.api import tvtk
from apptools.scripting.api import (Recorder, recordable,
    set_recorder)


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

    @recordable
    def grow(self, x):
        """Increase age by x years."""
        self.age += x
        self.f(1)

    @recordable
    def f(self, args):
        """Function f."""
        return args

    def not_recordable(self):
        pass


class Parent(HasTraits):
    children = List(Child, record=True)
    recorder = Instance(Recorder, record=False)


class _Test(HasTraits):
    # This should be set.
    recorder = Instance(HasTraits)

    # These should be ignored.
    _ignore = Bool(False)
    ignore_ = Bool(False)


class TestRecorder(unittest.TestCase):
    def setUp(self):
        self.tape = Recorder()
        set_recorder(self.tape)
        p = Parent()
        c = Child()
        toy = Toy(color='blue', type='bunny')
        c.toy = toy
        p.children.append(c)
        self.p = p
        return

    def tearDown(self):
        self.tape.clear()
        set_recorder(None)
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
        t = (1, 2)
        self.assertEqual(tape._get_unique_name(t),
                         'tuple0')
        l = [1, 2]
        self.assertEqual(tape._get_unique_name(l),
                         'list0')
        d = {'a': 1}
        self.assertEqual(tape._get_unique_name(d),
                         'dict0')

        self.assertEqual(tape._get_unique_name(1),
                         'int0')

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
        "Is the object imported and created if unknown?"
        tape = self.tape
        tape.recording = True
        t = Toy()
        tape.register(t)
        t.type = 'computer'

        # Since the name toy is unknown, there should be a
        # line to create it.
        self.assertEqual(tape.lines[-3][-10:],
                         "import Toy")
        self.assertEqual(tape.lines[-2],
                         "toy = Toy()")
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
        tape.register(p, known=True)
        tape.recording = True

        child.friends = ['Krishna', 'Ajay', 'Ali']
        self.assertEqual(tape.lines[-1],
                         "child.friends = ['Krishna', 'Ajay', 'Ali']")
        child.friends[1:] = ['Sam', 'Frodo']
        self.assertEqual(tape.lines[-1],
                         "child.friends[1:3] = ['Sam', 'Frodo']")
        child.friends[1] = 'Hari'
        self.assertEqual(tape.lines[-1],
                    "child.friends[1:2] = ['Hari']")

        # What if we change a list where record=True.
        child1 = Child()
        tape.register(child1)
        p.children.append(child1)
        self.assertEqual(tape.lines[-1],
                         "parent.children[1:1] = [child1]")
        del p.children[1]
        self.assertEqual(tape.lines[-1],
                         "parent.children[1:2] = []")
        p.children[0] = child1
        self.assertEqual(tape.lines[-1],
                         "parent.children[0:1] = [child1]")

    def test_path_change_on_list(self):
        "Does the object path update when a list has changed?"
        # Test the case where we have a hierarchy and we change the
        # list.
        tape = self.tape
        p = self.p
        child1 = Child()
        p.children.append(child1)
        tape.register(p)
        tape.recording = True
        self.assertEqual(tape.get_object_path(child1),
                         'parent.children[1]')
        self.assertEqual(tape.get_script_id(child1),
                         'child1')
        del p.children[0]
        self.assertEqual(tape.get_object_path(child1),
                         'parent.children[0]')
        self.assertEqual(tape.get_script_id(child1),
                         'child1')


    def test_write_script_id_in_namespace(self):
        "Test the write_script_id_in_namespace method."
        tape = self.tape
        tape.recording = True
        # This should not cause an error but insert the name 'foo' in the
        # namespace.
        tape.write_script_id_in_namespace('foo')

    def test_recorder_and_ignored(self):
        "Test if recorder trait is set and private traits are ignored."
        t = _Test()
        self.assertEqual(t.recorder, None)
        self.assertEqual(t._ignore, False)
        self.assertEqual(t.ignore_, False)
        tape = Recorder()
        tape.register(t)
        tape.recording = True

        self.assertEqual(t.recorder, tape)
        t._ignore = True
        t.ignore_ = True
        self.assertEqual(len(tape.script.strip()), 0)

    def test_record_function(self):
        "See if recordable function calls are handled correctly."
        # Note that the global recorder is set in setUp and removed in
        # tearDown.

        tape = self.tape
        c = self.p.children[0]
        tape.register(c)
        tape.recording = True

        # Setting the age should be recorded.
        c.age = 11
        self.assertEqual(tape.lines[-1], "child.age = 11.0")

        # This should also work without problems.
        c.f(c.toy)
        self.assertEqual(tape.lines[-2], "child.age = 11.0")
        self.assertEqual(tape.lines[-1], 'child.toy = child.f(child.toy)')

        # Calling f should be recorded.
        c.f(1)
        self.assertEqual(tape.lines[-1], "child.f(1)")

        # This should not record the call to f or the change to the age
        # trait inside grow.
        c.grow(1)
        self.assertEqual(c.age, 12.0)
        self.assertEqual(tape.lines[-2], "child.f(1)")
        self.assertEqual(tape.lines[-1], "child.grow(1)")

        # Non-recordable functions shouldn't be.
        c.not_recordable()
        self.assertEqual(tape.lines[-1], "child.grow(1)")

        # Test a simple recordable function.
        @recordable
        def func(x, y):
            return x, y

        result = func(1, 2)
        self.assertEqual(tape.lines[-1], "tuple0 = func(1, 2)")

    def test_non_has_traits(self):
        "Can classes not using traits be handled?"
        tape = self.tape
        p = self.p
        c = p.children[0]
        class A(object):
            @recordable
            def __init__(self, x, y=1):
                self.x = x
                self.y = y

            @recordable
            def f(self, x, y):
                return x, y

            @recordable
            def g(self, x):
                return x

            def not_recordable(self):
                pass

        tape.register(p)
        tape.recording = True
        # Test if __init__ is recorded correctly.
        a = A(x=1)

        # Should record.
        a.f(1, 'asd')
        self.assertEqual(tape.lines[-3][-8:],
                         "import A")
        self.assertEqual(tape.lines[-2],
                         "a = A(x=1)")
        self.assertEqual(tape.lines[-1], "tuple0 = a.f(1, 'asd')")

        result = a.f(p, c)
        # This should instantiate the parent first, get the child from
        # that and then record the call itself.
        self.assertEqual(tape.lines[-3], "parent = Parent()")
        self.assertEqual(tape.lines[-2], "child = parent.children[0]")
        self.assertEqual(tape.lines[-1], "tuple1 = a.f(parent, child)")

        # This should simply refer to the child.
        result = a.g(c)
        self.assertEqual(tape.lines[-1], "child = a.g(child)")

        # Should do nothing.
        a.not_recordable()
        self.assertEqual(tape.lines[-1], "child = a.g(child)")

        # When a function is called with unknown args it should attempt
        # to create the objects.
        r = a.g(Toy())
        self.assertEqual(tape.lines[-3][-10:], "import Toy",
                         '\n'.join(tape.lines[-5:]))
        self.assertEqual(tape.lines[-2], "toy = Toy()")
        self.assertEqual(tape.lines[-1], "toy = a.g(toy)")

    def test_set_script_id(self):
        "Test if setting script_id at registration time works."
        tape = self.tape
        p = self.p
        c = p.children[0]
        tape.register(p, script_id='child')
        tape.recording = True
        # Ask to be called child.
        self.assertEqual(tape.get_script_id(p), 'child')
        # Register another Child.
        c1 = Child()
        tape.register(c1)
        # Will be child2 since child1 is taken.
        self.assertEqual(tape.get_script_id(c1), 'child2')

        # Test if recording works correctly with the changed script_id.
        p.children.append(c1)
        self.assertEqual(tape.lines[-1],
                         "child.children[1:1] = [child2]")


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

        import io
        f = io.StringIO()
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
