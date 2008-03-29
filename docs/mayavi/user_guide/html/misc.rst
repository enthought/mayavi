Miscellaneous
=============


Tests for Mayavi2
-----------------

Mayavi features a few simple tests.  These are in the ``tests``
directory.  The testing is performed using the same technique that
VTK_ employs.  Basically, a visualization is scripted and the
resulting visualization window is captured and compared with an
existing test image.  If there are differences in the images then
there is an error, if not the test passes.  The test cases are
themselves relatively simple and the magic of the actual generation of
test images etc. is all in the ``tests/common.py`` module.

To run a test you may do something like the following::

 $ cd tests
 $ python test_array_source.py


Getting help
------------

Most of the user and developer discussion for mayavi2 occurs on the
Enthought OSS developers mailing list
(enthought-dev@mail.enthought.com).  This list is also available via
gmane from here:
http://dir.gmane.org/gmane.comp.python.enthought.devel

Discussion and bug reports are also sometimes sent to the mayavi-users
mailing list (Mayavi-users@lists.sourceforge.net).  We recommend
sending messages to the enthought-dev list though.

The Mayavi web page: https://svn.enthought.com/enthought/wiki/MayaVi

is a trac page where one can also enter bug reports and feature
requests.

If this manual, the mayavi web page and google are of no help feel
free to post on the enthought-dev mailing list for help.


Helping out
-----------

We are always on the lookout for people to help this project grow.
Feel free to send us patches -- these are best sent to the mailing
list.  Thanks!


..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

