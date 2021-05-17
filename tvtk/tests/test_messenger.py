"""Tests for messenger.py

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2020,  Enthought, Inc.
# License: BSD Style.

from importlib import reload
import unittest

from tvtk import messenger


#################################################################
# Support code.
#################################################################

class A:
    def __init__(self):
        self.event = None
        self.args = None
        self.kw = None
        self.did_catch_all = 0

    def callback(self, obj, event, *args, **kw):
        self.event = event
        self.args = args
        self.kw = kw

    def catch_all_cb(self, obj, event, *args, **kw):
        self.did_catch_all = 1

ret = None

def callback(obj, event, *args, **kw):
    global ret
    ret  = event, args, kw

class B:
    def __init__(self):
        self.a = A()
        messenger.connect(self, 'method', self.a.callback)
        messenger.connect(self, 'function', callback)
    def __del__(self):
        messenger.disconnect(self)

    def send(self, *args, **kw):
        messenger.send(self, 'method', *args, **kw)
        messenger.send(self, 'function', *args, **kw)


#################################################################
# The test case.
#################################################################

class TestMessenger(unittest.TestCase):
    def test_basic(self):
        """Test basic functionality of the messenger."""
        m = messenger.Messenger()
        orig_len = len(m._signals)
        b = B()
        b.send(1, test=1)
        self.assertEqual(b.a.event, 'method')
        self.assertEqual(ret[0], 'function')
        self.assertEqual(b.a.args, (1,))
        self.assertEqual(ret[1], (1,))
        self.assertEqual(b.a.kw, {'test':1})
        self.assertEqual(ret[2], {'test':1})
        # Ensures that disconnect works and also that there are no
        # reference cycles.
        self.assertEqual(len(m._signals) > orig_len, True)
        del b
        self.assertEqual(len(m._signals), orig_len)

    def test_reload(self):
        """Tests if module is reload safe."""
        b = B()
        m = messenger.Messenger()
        orig_len = len(m._signals)
        reload(messenger)
        m = messenger.Messenger()
        self.assertEqual(len(m._signals), orig_len)
        b.send(1, test=1)
        self.assertEqual(b.a.event, 'method')
        self.assertEqual(ret[0], 'function')
        self.assertEqual(b.a.args, (1,))
        self.assertEqual(ret[1], (1,))
        self.assertEqual(b.a.kw, {'test':1})
        self.assertEqual(ret[2], {'test':1})

    def test_catchall(self):
        """Tests if catch all handlers are called."""
        b = B()
        b.send()
        self.assertEqual(b.a.event, 'method')
        self.assertEqual(b.a.args, ())
        self.assertEqual(b.a.kw, {})
        self.assertEqual(b.a.did_catch_all, 0)
        messenger.connect(b, 'AnyEvent', b.a.catch_all_cb)
        b.send(1, test=1)
        self.assertEqual(b.a.event, 'method')
        self.assertEqual(b.a.args, (1,))
        self.assertEqual(b.a.kw, {'test':1})
        self.assertEqual(b.a.did_catch_all, 1)
        b.a.did_catch_all = 0
        messenger.disconnect(b, 'AnyEvent')
        b.send(1, test=1)
        self.assertEqual(b.a.did_catch_all, 0)

    def test_disconnect(self):
        """Tests if disconnection works correctly."""
        global ret
        ret = None
        b = B()
        messenger.disconnect(b)
        b.send(1, test=1)
        self.assertEqual(b.a.event, None)
        self.assertEqual(b.a.args, None)
        self.assertEqual(b.a.kw, None)
        self.assertEqual(b.a.did_catch_all, 0)
        self.assertEqual(ret, None)

    def test_send_on_dead_ref(self):
        """Test if sending to a gc'd callback works gracefully."""
        class C:
            def foo(self, o, e):
                pass
        c = C()
        c1 = C()
        messenger.connect(c1, 'foo', c.foo)
        messenger.send(c1, 'foo')

        # Test if things behave sanely if a message was sent and one
        # of the callbacks has been gc'd.
        m = messenger.Messenger()
        l1 = len(m._signals[hash(c1)]['foo'])
        #
        del c
        messenger.send(c1, 'foo')
        #
        l2 = len(m._signals[hash(c1)]['foo'])
        # Since 'c' is gc'd this callback should have been cleared
        # out.
        self.assertEqual(l2, l1 - 1)

        # Clean up.
        messenger.disconnect(c1)


if __name__ == "__main__":
    unittest.main()
