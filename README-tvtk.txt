===================
TVTK: Traited VTK
===================


Description
-----------

TVTK_ provides a Traits enabled version of VTK_.  TVTK objects wrap around VTK
objects but additionally support Traits_, support numpy arrays transparently
and provide a convenient Pythonic API. TVTK is implemented mostly in pure
Python (except for a small extension module).  TVTK is part of the Enthought
Tool Suite (ETS) and is distributed under a liberal BSD style license.  License
information is available in the LICENSE.txt file in this same directory.

.. _VTK: http://www.vtk.org
.. _Traits: https://svn.enthought.com/enthought/wiki/Traits
.. _TVTK: https://svn.enthought.com/enthought/wiki/TVTK



Getting the package
-------------------

Source tarballs for all stable ETS packages are available at

 http://code.enthought.com/enstaller/eggs/source

General Build and Installation instructions for ETS are available here:

 https://svn.enthought.com/enthought/wiki/Build
 https://svn.enthought.com/enthought/wiki/Install


Documentation
--------------

The TVTK home page is: http://code.enthought.com/projects/mayavi

More detailed information on TVTK is available in `docs/README.txt` which
covers installation, requirements, examples of usage etc.  This document is
also available on the web from
http://code.enthought.com/projects/mayavi/docs/development/html/tvtk/


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

The bug tracker is available as part of the trac interface here:

 https://svn.enthought.com/enthought/

To submit a bug you will necessarily have to register at the site.  Click on
the "register" link at the top right on the above page to register.  Or login
if you already have registered.  Once you are registered you may file a bug by
creating a new ticket.

Alternatively, you can post on the enthought-dev@mail.enthought.com mailing list.


Authors and Contributors
------------------------

Prabhu Ramachandran: main author.

Gerald Knizia: Initial version of Tkinter based gradient editor.
Pete Schmitt: wxPython version of gradient editor.
Raashid Baig: `visual` module.
Phil Thompson: PyQt4 versions of pyface widgets.

Many thanks to all those who have submitted bug reports and suggestions for
further enhancements.

