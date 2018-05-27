

.. _example_offscreen:

Offscreen example
--------------------------------------------

A simple example of how you can use Mayavi without using Envisage
or the Mayavi Envisage application and do off screen rendering.

On Linux/Mac, with VTK < 5.2, you should see a small black window popup
and disappear, see the section :ref:`offscreen_rendering` to avoid this.
On Win32 you will not see any windows popping up at all. In the end you
should have an offscreen.png image in the same directory with the
rendered visualization.

It can be run as::

    $ python offscreen.py


**Python source code:** :download:`offscreen.py`

.. literalinclude:: offscreen.py
    :lines: 15-


    