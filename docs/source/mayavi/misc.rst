Miscellaneous
=============

.. _getting-help:

Getting help
------------

Most of the user and developer discussion for Mayavi occurs on the
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

If this manual, the Mayavi web page, the wiki page and google are of no
help feel free to post on the enthought-dev mailing list for help.


Tests for Mayavi
-----------------

You can easily run the Mayavi test suite using `mayavi2 -t` from the
command line. Running tests is useful to find out if Mayavi works well on
your particular system. Indeed, the systems can vary from one to another:
in addition to the variety of existing operative system, different
versions of the libraries can be installed. The Mayavi developers do
their best to support many different configuration, but you can help them
by running the test suite and reporting any errors.

ETS uses nose_ to gather and run tests. You can also run the unit tests
of both packages by doing the following from the root of the Mayavi
source directory::

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

In addition to these unittests mayavi also has several integration tests.
These are in the ``integrationtests/mayavi`` directory of the source
distribution.  You may run the tests there like so::

 $ ./run.py

These tests are intrusive and will create several mayavi windows and
also take a while to complete.  Some of them may fail on your machine
for various reasons.

.. _nose: http://somethingaboutorange.com/mrl/projects/nose/

Helping out
-----------

We are always on the lookout for people to help this project grow.
If you need a functionnality added to Mayavi, just pitch in on the
enthought-dev mailing and we'll help you code it.

Development quick start
~~~~~~~~~~~~~~~~~~~~~~~~

To help improve Mayavi, you first need to install the development version
(see :ref:`installing_svn`). You can then modify your local installation
of Mayavi to add the functionality you are interested in (make sure the
tests still run after your modifications). To keep track of your changes,
you need to use subversion, if you have never used it, see
http://svnbook.red-bean.com/en/1.1/ch01s07.html. Once you are done, you
can generate a path that sums up your changes via by executing the
following command in the root of the Mayavi source::

    svn diff > my_patch.patch

Feel free to send us patches via the mailing list.  Thanks!


..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

