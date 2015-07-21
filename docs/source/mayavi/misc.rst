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

Bug reports should be submitted to the `github issue tracker
<https://github.com/enthought/mayavi/issues>`_. Please make sure to
provide enough information so that the issue can be reproduced. For
other request, if this manual, the Mayavi web page, the wiki page,
stack overflow and google are of no help feel free to ask on the
`issue tracker <https://github.com/enthought/mayavi/issues>`_.


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

Helping out
-----------

We are always on the lookout for people to help this project grow.  If
you need a functionality added to Mayavi, open an new feature request
issue in github_ and feel free to make suggestions through `pull
request <https://help.github.com/articles/using-pull-requests/>`_.
Please note that we aim to improve the overall testing of the Mayavi
codebase, so tests are also important.

Development quick start
~~~~~~~~~~~~~~~~~~~~~~~~

To help improve Mayavi, you first need to install the development
version (see :ref:`installing_git`). You can then modify your local
installation of Mayavi to add the functionality you are interested in
(make sure the tests still run after your modifications).  Once you
are done, you can generate a github `pull request <pull_requests>`_ to
get your changes into the next stable release.

Improving the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation of a project is incredibly important. It also takes a lot
of time to write and improve. You can easily help us with documentation.

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
with the modifications, just generate a github pool request to integrate
your changes into the next stable release.

.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _github: https://github.com/enthought/mayavi
.. _github_issues:

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
