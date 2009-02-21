"""
Simple utility code for animations.
"""
# Author: Prabhu Ramachandran <prabhu at aerodotiitbdotacdotin>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

from enthought.pyface.timer.api import Timer
from enthought.traits.api import HasTraits, Button, Instance, Range
from enthought.traits.ui.api import View, Group, Item

################################################################################
# `Animator` class.
################################################################################ 
class Animator(HasTraits):

    """Convenience class to manage a timer and present a convenient
    UI.  This is based on the code in `enthought.tvtk.tools.visual`.
    Here is a simple example of using this class::

        >>> from enthought.mayavi import mlab
        >>> def animate():
        ...     f = mlab.gcf()
        ...     while 1:
        ...         f.scene.azimuth(10)
        ...         f.scene.render()
        ...         yield
        ...
        >>> anim = animate()
        >>> t = Animator(500, anim.next)
        >>> t.edit_traits()

    This makes it very easy to animate your visualizations and control
    it from a simple UI.

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

            -- millisec : int specifying the delay in milliseconds
               between calls to the callable.

            -- callable : callable function to call after the specified
               delay.

            -- *args : optional arguments to be passed to the callable.

            -- **kwargs : optional keyword arguments to be passed to the callable.

        """
        HasTraits.__init__(self)
        self.delay = millisec
        self.timer = Timer(millisec, callable, *args, **kwargs)

    ######################################################################
    # Non-public methods, Event handlers
    def _start_fired(self):
        self.timer.Start()        
        
    def _stop_fired(self):
        self.timer.Stop()

    def _delay_changed(self, value):
        t = self.timer
        if t is None:
            return
        if t.IsRunning():
            t.Stop()
            t.Start(value)

