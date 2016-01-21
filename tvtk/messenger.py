"""
Implements a simple, robust, safe, Messenger class that allows one to
register callbacks for a signal/slot (or event/handler) kind of
messaging system.  One can basically register a callback
function/method to be called when an object sends a particular event.
The Messenger class is Borg.  So it is easy to instantiate and use.
This module is also reload-safe, so if the module is reloaded the
callback information is not lost.  Method callbacks do not have a
reference counting problem since weak references are used.

The main functionality of this module is provided by three functions,
`connect`, `disconnect` and `send`.

Here is example usage with VTK::

    >>> import messenger, vtk
    >>> def cb(obj, evt):
    ...  print obj.__class__.__name__, evt
    ...
    >>> o = vtk.vtkProperty()
    >>> o.AddObserver('ModifiedEvent', messenger.send)
    1
    >>> messenger.connect(o, 'ModifiedEvent', cb)
    >>>
    >>> o.SetRepresentation(1)
    vtkOpenGLProperty ModifiedEvent
    >>> messenger.connect(o, 'AnyEvent', cb)
    >>> o.SetRepresentation(2)
    vtkOpenGLProperty ModifiedEvent
    vtkOpenGLProperty ModifiedEvent
    >>>
    >>> messenger.send(o, 'foo')
    vtkOpenGLProperty foo
    >>> messenger.disconnect(o, 'AnyEvent')
    >>> messenger.send(o, 'foo')
    >>>

This approach is necessary if you don't want to be bitten by reference
cycles.  If you have a Python object holding a reference to a VTK
object and pass a method of the object to the AddObserver call, you
will get a reference cycle that cannot be collected by the garbage
collector.  Using this messenger module gets around the problem.

Also note that adding a connection for 'AnyEvent' will trigger a
callback no matter what event was generated.  The code above also
shows how disconnection works.

"""
# Author: Prabhu Ramachandran
# Copyright (c) 2004-2007, Enthought, Inc.
# License: BSD Style.

__all__ = ['Messenger', 'MessengerError',
           'connect', 'disconnect', 'send']

import types
import sys
import weakref


#################################################################
# This code makes the module reload-safe.
#################################################################
_saved = {}

for name in ['messenger', 'tvtk.messenger']:
    if name in sys.modules:
        mod = sys.modules[name]
        if hasattr(mod, 'Messenger'):
            _saved = mod.Messenger._shared_data
        del mod
        break


#################################################################
# `MessengerError` class for exceptions raised by Messenger.
#################################################################

class MessengerError(Exception):
    pass



#################################################################
# `Messenger` class.
#################################################################

class Messenger:

    """Implements a messenger class which deals with something like
    signals and slots.  Basically, an object can register a signal
    that it plans to emit.  Any other object can decide to handle that
    signal (of that particular object) by registering itself with the
    messenger.  When a signal is emitted the messenger calls all
    handlers.  This makes it totally easy to deal with communication
    between objects.  The class is Borg.  Rather than use this class,
    please use the 'connect' and 'disconnect' functions.

    """

    _shared_data = _saved

    def __init__(self):
        """Create the messenger.  This class is Borg.  So all
        instances are the same.

        """

        self.__dict__ = self._shared_data

        if not hasattr(self, '_signals'):
            # First instantiation.
            self._signals = {}
            self._catch_all = ['AnyEvent', 'all']

    #################################################################
    # 'Messenger' interface.
    #################################################################

    def connect(self, obj, event, callback):
        """ Registers a slot given an object and its signal to slot
        into and also given a bound method in `callback` that should
        have two arguments.  `send` will call the callback
        with the object that emitted the signal and the actual
        event/signal as arguments.

        Parameters
        ----------

        - obj :  Python object

          Any Python object that will generate the particular event.

        - event : An event (can be anything, usually strings)

          The event `obj` will generate.  If this is in the list
          `self._catch_all`, then any event will call this callback.

        - callback : `function` or `method`

          This callback will be called when the object generates the
          particular event.  The object, event and any other arguments
          and keyword arguments given by the `obj` are passed along to
          the callback.

        """
        typ = type(callback)
        key = hash(obj)
        if not key in self._signals:
            self._signals[key] = {}
        signals = self._signals[key]
        if not event in signals:
            signals[event] = {}

        slots = signals[event]

        callback_key = hash(callback)
        if typ is types.FunctionType:
            slots[callback_key] = (None, callback)
        elif typ is types.MethodType:
            obj = weakref.ref(callback.__self__)
            name = callback.__name__
            slots[callback_key] = (obj, name)
        else:
            raise MessengerError(
                "Callback must be a function or method. "\
                "You passed a %s."%(str(callback))
            )

    def disconnect(self, obj, event=None, callback=None, obj_is_hash=False):
        """Disconnects the object and its event handlers.

        Parameters
        ----------

        - obj : Object

          The object that generates events.

        - event : The event.  (defaults to None)

        - callback : `function` or `method`

          The event handler.

         If `event` and `callback` are None (the default) all the
         events and handlers for the object are removed.  If only
         `callback` is None, only this handler is removed.  If `obj`
         and 'event' alone are specified, all handlers for the event
         are removed.

        - obj_is_hash : `bool`

         Specifies if the object passed is a hash instead of the object itself.
         This is needed if the object is gc'd but only the hash exists and one
         wants to disconnect the object.

        """
        signals = self._signals
        if obj_is_hash:
            key = obj
        else:
            key = hash(obj)
        if not key in signals:
            return
        if callback is None:
            if event is None:
                del signals[key]
            else:
                del signals[key][event]
        else:
            del signals[key][event][hash(callback)]

    def send(self, source, event, *args, **kw_args):
        """To be called by the object `source` that desires to
        generate a particular event.  This function in turn invokes
        all the handlers for the event passing the `source` object,
        event and any additional arguments and keyword arguments.  If
        any connected callback is garbage collected without being
        disconnected, it is silently removed from the existing slots.

        Parameters
        ----------

        - source : Python object

          This is the object that generated the event.

        - event : The event.

          If there are handlers connected to events called 'AnyEvent'
          or 'all', then any event will invoke these.

        """
        try:
            sigs = self._get_signals(source)
        except (MessengerError, KeyError):
            return
        events = self._catch_all[:]
        if event not in events:
            events.append(event)
        for evt in events:
            if evt in sigs:
                slots = sigs[evt]
                for key in list(slots.keys()):
                    obj, meth = slots[key]
                    if obj: # instance method
                        inst = obj()
                        if inst:
                            getattr(inst, meth)(source, event, *args, **kw_args)
                        else:
                            # Oops, dead reference.
                            del slots[key]
                    else: # normal function
                        meth(source, event, *args, **kw_args)

    def is_registered(self, obj):
        """Returns if the given object has registered itself with the
        messenger.

        """
        try:
            sigs = self._get_signals(obj)
        except MessengerError:
            return 0
        else:
            return 1

    def get_signal_names(self, obj):
        """Returns a list of signal names the object passed has
        registered.

        """
        return list(self._get_signals(obj).keys())

    #################################################################
    # Non-public interface.
    #################################################################

    def _get_signals(self, obj):
        """Given an object `obj` it returns the signals of that
        object.

        """
        ret = self._signals.get(hash(obj))
        if ret is None:
            raise MessengerError(
                "No such object: %s, has registered itself "\
                "with the messenger."%obj
            )
        else:
            return ret


#################################################################
# Convenience functions.
#################################################################

_messenger = Messenger()

def connect(obj, event, callback):
    _messenger.connect(obj, event, callback)
connect.__doc__ = _messenger.connect.__doc__

def disconnect(obj, event=None, callback=None, obj_is_hash=False):
    _messenger.disconnect(obj, event, callback)
disconnect.__doc__ = _messenger.disconnect.__doc__

def send(obj, event, *args, **kw_args):
    _messenger.send(obj, event, *args, **kw_args)
send.__doc__ = _messenger.send.__doc__

del _saved
