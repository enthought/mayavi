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


Tutorial videos
----------------

Here are some tutorial videos that you can watch to learn Mayavi:

- SciPy 2018 Mayavi tutorial (3 hrs):

  - Video: https://www.youtube.com/watch?v=r6OD07Qq2mw
  - Material: https://github.com/prabhuramachandran/mayavi-tutorial


.. _getting-help:

Getting help
------------

Bug reports should be submitted to the `issue tracker`_. Please make sure to
provide enough information so that the issue can be reproduced. For
other requests, if this manual, the Mayavi web page, the wiki page,
stack overflow and google are of no help, feel free to ask on the
`issue tracker`_.

If you have questions you could ask on the `Mayavi-users mailing list
<https://sourceforge.net/p/mayavi/mailman/mayavi-users/>`_. This is used by
some folks and is not too active. Another mailing list that may be of use is
the `ETS Users mailing list
<https://groups.google.com/forum/#!forum/ets-users>`_. This is a more general
list where a lot of folks experienced with the Enthought Tool Suite are
available.

Tests for Mayavi
-----------------

Running the tests is useful to find out if Mayavi works well on your
particular system. Indeed, the systems can vary from one to another: in
addition to the variety of existing operating systems, different versions of
the libraries can be installed. The Mayavi developers do their best to
support many different configuration, but you can help them by running the
test suite and reporting any errors.

The tests need `pytest`_ and are run from the root of a source checkout, one
suite per package, exactly as continuous integration runs them::

  $ pytest -v --timeout=10 mayavi
  $ pytest -sv --timeout=60 tvtk

A single file or a single test works the usual way::

  $ pytest mayavi/tests/test_contour.py
  $ pytest mayavi/tests/test_contour.py::TestContour::test_contour

In addition to these unit tests mayavi also has several integration tests,
in the ``integrationtests`` directory of the source distribution::

  $ pytest -v --timeout=360 integrationtests

These tests are intrusive: each one stands the Mayavi application up in a
subprocess of its own, so they create several mayavi windows and take a while
to complete.  Some of them may fail on your machine for various reasons.

Helping out
-----------

We are always on the lookout for people to help this project grow.  If
you need a functionality added to Mayavi, open an new feature request
issue in `issue tracker`_.

To submit bug fixes or new functionality, this is the recommended
workflow:

1. Fork the Repo on github.
2. If you are adding functionality or fixing a bug, please add a test!
3. Push to your fork and submit a **pull request to the main branch**.

The **main** branch is a 100% stable (should be).  The pull request is merged
only after it is certain that things are working out, which means that
`Travis`_ and `Appveyor`_ tests pass.

Please note that we aim to improve the overall testing of the Mayavi codebase,
so tests are also important.

Development quick start
~~~~~~~~~~~~~~~~~~~~~~~~

To help improve Mayavi, you first need to install the development
version, see :ref:`installing_git`. You can then modify your local
installation of Mayavi to add the functionality you are interested in
(make sure the tests still run after your modifications).  Once you
are done, you can generate a github `pull request`_ to get your changes
into the next stable release.

Improving the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation of a project is incredibly important. It also takes a lot
of time to write and improve. You can easily help us with documentation.

You will find the documentation sources in ``docs/sources/mayavi``. The
documentation is written in `sphinx`_. It is
easy to edit the `.rst` files to modify or extend the text. Once you have
done your modifications, you can build the documentation by
running::

    python setup.py build_docs

in the base directory of your checkout. You will need `sphinx`_ installed for
that. The documentation is then built as an HTML documentation that you can
find in the sub directory ``build/docs/html/mayavi``. Once you are comfortable
with the modifications, just generate a github pull request to integrate
your changes into the next stable release.

Translating the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way for new contributors to translate mayavi reference is to
join the translation team on Transifex.

There is a `mayavi translation page`_ for mayavi (main) documentation.

1. Login to transifex_ service.
2. Go to `mayavi translation page`_.
3. Click ``Request language`` and fill form.
4. Wait acceptance by transifex mayavi translation maintainers.
5. (After acceptance) Translate on transifex.
6. You can see the translated document in `Read The Docs`_.

Detail is here: https://docs.transifex.com/getting-started-1/translators

.. _pytest: https://docs.pytest.org
.. _github: https://github.com/enthought/mayavi
.. _issue tracker: https://github.com/enthought/mayavi/issues
.. _pull request: https://help.github.com/articles/using-pull-requests
.. _sphinx: https://www.sphinx-doc.org
.. _Travis: https://travis-ci.org/enthought/mayavi
.. _Appveyor: https://ci.appveyor.com/project/itziakos/mayavi
.. _`mayavi translation page`: https://www.transifex.com/tkoyama010/mayavi/
.. _Transifex: https://www.transifex.com/
.. _`Read The Docs`: https://mayavi.readthedocs.io/en/latest

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
