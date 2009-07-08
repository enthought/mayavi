"""
Simple utility code for animations.
"""
# Author: Prabhu Ramachandran <prabhu at aerodotiitbdotacdotin>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

import types

from enthought.pyface.timer.api import Timer
from enthought.traits.api import HasTraits, Button, Instance, Range
from enthought.traits.ui.api import View, Group, Item

################################################################################
# `Animator` class.
################################################################################ 
class Animator(HasTraits):

    """ Convenience class to manage a timer and present a convenient
        UI.  This is based on the code in `enthought.tvtk.tools.visual`.
        Here is a simple example of using this class::
        
            >>> from enthought.mayavi import mlab
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
    timer = Instance(Timer)

    ######################################################################
    # User interface view 

    traits_view = View(Group(Item('start'),
                             Item('stop'),
                             show_labels = False
                             ),
                             Item('_'),
                       Item(name = 'delay'),
                       title = 'Animation Controller', 
                       buttons = ['OK'])

    ######################################################################
    # Initialize object 
    def __init__(self, millisec, callable, *args, **kwargs):
        """Constructor.

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
        self.timer = Timer(millisec, callable, *args, **kwargs)

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



################################################################################ 
# Decorators.

def animate(func=None, delay=500, ui=True):
    """ A convenient decorator to animate a generator that performs an
        animation.  The `delay` parameter specifies the delay (in
        milliseconds) between calls to the decorated function. If `ui` is
        True, then a simple UI for the animator is also popped up.  The
        decorated function will return the `Animator` instance used and a
        user may call its `Stop` method to stop the animation.  
        
        If an ordinary function is decorated a `TypeError` will be raised.
        
        **Parameters**
        
        :delay: int specifying the time interval in milliseconds between
                calls to the function.
        
        :ui: bool specifying if a UI controlling the animation is to be
             provided.
        
        **Returns**
        
        The decorated function returns an `Animator` instance.
        
        **Examples**
        
        Here is the example provided in the Animator class documentation::

            >>> from enthought.mayavi import mlab
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

            >>> from enthought.mayavi import mlab
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
        def __call__(self, *args, **kw):
            f = self.func(*args, **kw)
            if isinstance(f, types.GeneratorType):
                a = Animator(self.delay, f.next)
                if self.ui:
                    a.edit_traits()
                return a
            else:
                msg = 'The function "%s" must be a generator '\
                      '(use yield)!'%(self.func.__name__)
                raise TypeError(msg)

    def _wrapper1(function):
        # Needed to create the Wrapper in the right scope.
        w = Wrapper(function)
        return w
        
    if func is None:
        return _wrapper1
    else:
        return _wrapper1(func)

