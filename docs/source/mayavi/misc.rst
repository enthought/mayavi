Miscellaneous
=============

Citing Mayavi
---------------

The core developers of Mayavi are academics. Therefore they justify time and
resources spent developing Mayavi by the number of citations of the
software. If you publish scientific articles using Mayavi, please cite
the following article (bibtex entry :download:`citation.bib`):

  Ramachandran, P. and Varoquaux, G., *`Mayavi: 3D Visualization of 
  Scientific Data`* IEEE Computing in Science & Engineering, **13**
  (2), pp. 40-51 (2011)

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

The Mayavi documentation: http://docs.enthought.com/mayavi/mayavi

If this manual, the Mayavi web page, the wiki page and google are of no
help feel free to post on the enthought-dev mailing list for help.


Tests for Mayavi
-----------------

You can easily run the Mayavi test suite using `mayavi2 -t` from the
command line. Running tests is useful to find out if Mayavi works well on
your particular system. Indeed, the systems can vary from one to another:
in addition to the variety of existing operating systems, different
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
``mayavi/tests``.  You can run each of the ``test_*.py`` files
in these directories manually, or change your current directory to these
directories and run ``nosetests`` there.

In addition to these unit tests mayavi also has several integration tests.
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
If you need a functionality added to Mayavi, just pitch in on the
enthought-dev mailing and we'll help you code it.

Development quick start
~~~~~~~~~~~~~~~~~~~~~~~~

To help improve Mayavi, you first need to install the development version
(see :ref:`installing_git`). You can then modify your local installation
of Mayavi to add the functionality you are interested in (make sure the
tests still run after your modifications). To keep track of your changes,
you need to use subversion, if you have never used it, see
http://svnbook.red-bean.com/en/1.1/ch01s07.html. Once you are done, you
can generate a path that sums up your changes by executing the
following command in the root of the Mayavi source::

    svn diff > my_patch.patch

Feel free to send us patches via the `mailing list <https://mail.enthought.com/mailman/listinfo/enthought-dev>`__.  Thanks!

Improving the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation of a project is incredibly important. It also takes a lot
of time to write and improve. You can easily help us with documentation.

For that, you can check out only the subversion tree of Mayavi, using::

  svn co http://svn.enthought.com/svn/enthought/Mayavi/trunk/ mayavi

You will find the documentation sources in `docs/sources/mayavi`. The
documentation is written in `sphinx <http://sphinx.pocoo.org/>`__. It is
easy to edit the `.rst` files to modify or extend the text. Once you have
done your modifications, you can build the documentation using by
running::

    python setup.py build_docs

in the base directory of your checkout. You will need 
`sphinx <http://sphinx.pocoo.org/>`__ installed for that. The
documentation is then built as an HTML documentation that you can find
in the sub directory `build/docs/html/mayavi`. Once you are comfortable
with the modifications, just generate an SVN patch using::

    svn diff > my_patch.patch 

And send us the patch via the `mailing list <https://mail.enthought.com/mailman/listinfo/enthought-dev>`__.  Thanks!


..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

