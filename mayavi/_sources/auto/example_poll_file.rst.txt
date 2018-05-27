

.. _example_poll_file:

Poll file example
--------------------------------------------

A simple script that polls a data file for changes and then updates
the mayavi pipeline automatically.

This script is to be run like so::

 $ mayavi2 -x poll_file.py

Or::

 $ python poll_file.py

The script currently defaults to using the example data in
examples/data/heart.vtk.  You can try editing that data file or change
this script to point to other data which you can edit.


**Python source code:** :download:`poll_file.py`

.. literalinclude:: poll_file.py
    :lines: 17-


    