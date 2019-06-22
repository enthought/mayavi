"""
Simple utility code for animations.
"""
# Author: Prabhu Ramachandran <prabhu at aerodotiitbdotacdotin>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

import types
from functools import wraps
try:
    from decorator import decorator
    HAS_DECORATOR = True
except ImportError:
    HAS_DECORATOR = False

from pyface.timer.api import Timer
from traits.api import Any, HasTraits, Button, Instance, Range
from traitsui.api import View, Group, Item


###############################################################################
# `Animator` class.
###############################################################################
class Animator(HasTraits):
    """ Convenience class to manage a timer and present a convenient
        UI.  This is based on the code in `tvtk.tools.visual`.
        Here is a simple example of using this class::

            >>> from mayavi import mlab
            >>> def anim():
            ...     f = mlab.gcf()
            ...     while 1:
            ...         f.scene.camera.azimuth(10)
            ...         f.scene.render()
            ...         yield
            ...
            >>> anim = anim()
            >>> t = Animator(500, anim.next)
            >>> t.edit_traits()

        This makes it very easy to animate your visualizations and control
        it from a simple UI.

        **Notes**

        If you want to modify the data plotted by an `mlab` function call,
        please refer to the section on: :ref:`mlab-animating-data`
    """

    ########################################
    # Traits.

    start = Button('Start Animation')
    stop = Button('Stop Animation')
    delay = Range(10, 100000, 500,
                  desc='frequency with which timer is called')

    # The internal timer we manage.
    timer = Any

    ######################################################################
    # User interface view

    traits_view = View(Group(Item('start'),
                             Item('stop'),
                             show_labels=False),
                       Item('_'),
                       Item(name='delay'),
                       title='Animation Controller',
                       buttons=['OK'])

    ######################################################################
    # Initialize object
    def __init__(self, millisec, callable, *args, **kwargs):
        r"""Constructor.

        **Parameters**

          :millisec: int specifying the delay in milliseconds
                     between calls to the callable.

          :callable: callable function to call after the specified
                     delay.

          :\*args: optional arguments to be passed to the callable.

          :\*\*kwargs: optional keyword arguments to be passed to the callable.

        """
        HasTraits.__init__(self)
        self.delay = millisec
        self.ui = None
        self.timer = Timer(millisec, callable, *args, **kwargs)

    ######################################################################
    # `Animator` protocol.
    ######################################################################
    def show(self):
        """Show the animator UI.
        """
        self.ui = self.edit_traits()

    def close(self):
        """Close the animator UI.
        """
        if self.ui is not None:
            self.ui.dispose()

    ######################################################################
    # Non-public methods, Event handlers
    def _start_fired(self):
        self.timer.Start(self.delay)

    def _stop_fired(self):
        self.timer.Stop()

    def _delay_changed(self, value):
        t = self.timer
        if t is None:
            return
        if t.IsRunning():
            t.Stop()
            t.Start(value)


###############################################################################
# Decorators.

def animate(func=None, delay=500, ui=True, support_movie=True):
    """A convenient decorator to animate a generator performing an animation.

    The `delay` parameter specifies the delay (in milliseconds) between calls
    to the decorated function. If `ui` is True, then a simple UI for the
    animator is also popped up.  The decorated function will return the
    `Animator` instance used and a user may call its `Stop` method to stop the
    animation.  The `support_movie` parameter is True by default and this
    makes it easy to record a movie with the decorator.  If this is turned
    off, one cannot record a movie of the animation.

    If an ordinary function is decorated a `TypeError` will be raised.

    **Parameters**

    :delay: int specifying the time interval in milliseconds between
            calls to the function.

    :ui: bool specifying if a UI controlling the animation is to be
         provided.

    :support_movie: bool specifying if the animation will support
                    recording of a movie.

    **Returns**

    The decorated function returns an `Animator` instance.

    **Examples**

    Here is the example provided in the Animator class documentation::

        >>> from mayavi import mlab
        >>> @mlab.animate
        ... def anim():
        ...     f = mlab.gcf()
        ...     while 1:
        ...         f.scene.camera.azimuth(10)
        ...         f.scene.render()
        ...         yield
        ...
        >>> a = anim() # Starts the animation.

    For more specialized use you can pass arguments to the decorator::

        >>> from mayavi import mlab
        >>> @mlab.animate(delay=500, ui=False)
        ... def anim():
        ...     f = mlab.gcf()
        ...     while 1:
        ...         f.scene.camera.azimuth(10)
        ...         f.scene.render()
        ...         yield
        ...
        >>> a = anim() # Starts the animation without a UI.

    **Notes**

    If you want to modify the data plotted by an `mlab` function call,
    please refer to the section on: :ref:`mlab-animating-data`.

    """

    class Wrapper(object):
        # The wrapper which calls the decorated function.

        def __init__(self, function):
            self.func = function
            self.ui = ui
            self.delay = delay
            self._support_movie = support_movie
            self._movie_maker = None
            self._next = None

        def __call__(self, *args, **kw):
            if isinstance(self.func, types.GeneratorType):
                f = self.func
            else:
                f = self.func(*args, **kw)
            if isinstance(f, types.GeneratorType):
                _next = f.next if hasattr(f, 'next') else f.__next__
                self._next = _next
                self._movie_maker = None
                a = Animator(self.delay, self._step)
                if self.ui:
                    a.show()
                return a
            else:
                msg = 'The function "%s" must be a generator '\
                      '(use yield)!' % (self.func.__name__)
                raise TypeError(msg)

        def _step(self):
            try:
                self._next()
                if self._support_movie:
                    self._update_movie_maker()
            except StopIteration:
                if self._support_movie:
                    self._movie_maker.animation_stop()
                raise

        def _update_movie_maker(self):
            if self._movie_maker is None:
                from .engine_manager import get_engine
                scene = get_engine().current_scene.scene
                self._movie_maker = scene.movie_maker
                self._movie_maker.animation_start()
            else:
                self._movie_maker.animation_step()

        def decorator_call(self, func, *args, **kw):
            return self(*args, **kw)


    def _wrapper(function):
        # Needed to create the Wrapper in the right scope.
        if HAS_DECORATOR:
            # The decorator calls a callable with (func, *args, **kw) signature
            return decorator(Wrapper(function).decorator_call, function)
        else:
            return wraps(function)(Wrapper(function))

    if func is None:
        return _wrapper
    else:
        return _wrapper(func)
