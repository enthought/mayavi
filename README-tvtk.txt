===================
TVTK: Traited VTK
===================


Description
-----------

TVTK_ provides a Traits enabled version of VTK_.  TVTK objects wrap around VTK
objects but additionally support Traits_, support numpy arrays transparently
and provide a convenient Pythonic API. TVTK is implemented mostly in pure
Python (except for a small extension module).  TVTK is distributed under
a liberal BSD style license with the Mayavi_ package, which is part of the
Enthought Tool Suite (ETS) and is distributed.  License
information is available in the LICENSE.txt file in this same directory.

.. _VTK: http://www.vtk.org
.. _Traits: https://docs.enthought.com/traits
.. _TVTK: https://docs.enthought.com/mayavi/tvtk
.. _Mayavi: https://docs.enthought.com/mayavi/mayavi


Getting the package
-------------------

The source for TVTK should be acquired with the source for Mayavi here:

 http://pypi.python.org/pypi/mayavi


Documentation
--------------

Documentation is hosted here: http://docs.enthought.com/mayavi/tvtk


Examples
--------

Examples are all in the `examples` directory of the source or the SVN checkout.
The docs and examples do not ship with the binary eggs.


Test suite
----------

The test suite may be run like so (on a bash shell)::

 cd enthought/tvtk/tests
 for i in test*.py; do python $i; done

Use a similar line for your particular shell.


Bug tracker, mailing list etc.
-------------------------------

The bug tracker is available here:

 https://github.com/enthought/mayavi/issues

To submit a bug you will necessarily have to register on Github.
Alternatively, you can post on the info@enthought.com mailing list.


Authors and Contributors
------------------------

Prabhu Ramachandran: main author.

Gerald Knizia: Initial version of Tkinter based gradient editor.
Pete Schmitt: wxPython version of gradient editor.
Raashid Baig: `visual` module.
Phil Thompson: PyQt4 versions of pyface widgets.

Many thanks to all those who have submitted bug reports and suggestions for
further enhancements.

