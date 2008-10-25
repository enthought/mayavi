Miscellaneous
=============


Tests for Mayavi2
-----------------

Mayavi consists of two main packages, ``enthought.tvtk`` and
``enthought.mayavi``.  ETS uses nose_ to gather and run tests.  To run
the unit tests of both packages simply do the following from the root of
the mayavi source directory::

  $ nosetests
  ----------------------------------------------------------------------
  Ran 170 tests in 39.254s

  OK (SKIP=1)

If you get an "ERROR" regarding the unavailability of coverage you may
safely ignore it.  If for some reason nose is having difficulty running
the tests, the tests may be found inside ``enthought/tvtk/tests`` and
``enthought/mayavi/tests``.  You can run each of the ``test_*.py`` files
in these directories manually, or change your current directory to these
directories and run ``nosetests`` there.

In addition to these unittests mayavi also has several integration
tests.  These are in the ``integrationtests/mayavi`` directory.  You may
run the tests there like so::

 $ ./run.py

These tests are intrusive and will create several mayavi windows and
also take a while to complete.  Some of them may fail on your machine
for various reasons.


.. _nose: http://somethingaboutorange.com/mrl/projects/nose/

.. _getting-help:

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

The Mayavi wiki page: https://svn.enthought.com/enthought/wiki/MayaVi

is a trac page where one can also enter bug reports and feature
requests.

If this manual, the mayavi web page, the wiki page and google are of no
help feel free to post on the enthought-dev mailing list for help.


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

