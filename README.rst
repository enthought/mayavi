=======================================================
MayaVi2: 3D visualization of scientific data in Python
=======================================================

Mayavi doc: http://docs.enthought.com/mayavi/mayavi/
TVTK doc: http://docs.enthought.com/mayavi/tvtk

.. image:: https://api.travis-ci.org/enthought/mayavi.png?branch=master
   :target: https://travis-ci.org/enthought/mayavi
   :alt: Build status

.. image:: http://codecov.io/github/enthought/mayavi/coverage.svg?branch=master
   :target: http://codecov.io/github/enthought/mayavi?branch=master


Vision
======

MayaVi2 seeks to provide easy and interactive visualization of 3D data. It does
this by the following:

    - an (optional) rich user interface with dialogs to interact with all data
      and objects in the visualization.

    - a simple and clean scripting interface in Python, including one-liners,
      a-la mlab, or object-oriented programming interface.

    - harnesses the power of the VTK toolkit without forcing you to learn it.

Additionally Mayavi2 strives to be a reusable tool that can be embedded in your
applications in different ways or combined with the envisage
application-building framework to assemble domain-specific tools.

Mayavi is part of the Enthought Tool Suite (ETS).


Features
===========

MayaVi2 is a general purpose, cross-platform tool for 2-D and 3-D scientific
data visualization. Its features include:

    * Visualization of scalar, vector and tensor data in 2 and 3 dimensions

    * Easy scriptability using Python

    * Easy extendability via custom sources, modules, and data filters

    * Reading several file formats: VTK (legacy and XML), PLOT3D, etc.

    * Saving of visualizations

    * Saving rendered visualization in a variety of image formats

    * Convenient functionality for rapid scientific plotting via mlab (see mlab
      documentation)

    * See the MayaVi2 Users Guide for more information.

Unlike its predecessor MayaVi1_, Mayavi2 has been designed with scriptability
and extensibility in mind from the ground up.  While the mayavi2 application is
usable by itself, it may be used as an Envisage plugin which allows it to be
embedded in user applications natively. Alternatively, it may be used as a
visualization engine for any application.

.. _MayaVi1: http://mayavi.sf.net


Quick start
===========

If you are new to mayavi it is a good idea to read the users guide which should
introduce you to how to install and use it.  The user guide is available in the
`docs` directory and also available from the mayavi home page.

If you have installed `mayavi` as described in the previous section
you should be able to launch the `mayavi2` application and also run any of the
examples in the examples directory.


Getting the package
===================

The mayavi codebase can be found in github:

https://github.com/enthought/mayavi

General Build and Installation instructions are available `here
<http://docs.enthought.com/mayavi/mayavi/installation.html#installing-ready-made-distributions>`_

Source tarballs for necessary stable ETS packages are available through pypi

- `traits <https://pypi.python.org/pypi/traits>`_
- `traitsui <https://pypi.python.org/pypi/traitsui>`_
- `pyface <https://pypi.python.org/pypi/pyface>`_
- `apptools <https://pypi.python.org/pypi/apptools>`_
- `envisage <https://pypi.python.org/pypi/envisage>`_
- `mayavi <https://pypi.python.org/pypi/mayavi>`_

Development versions exist in the github `Enthought organization <https://github.com/enthought>`_


Documentation
==============

More documentation is available in the `online user manual
<http://docs.enthought.com/mayavi/mayavi/>`_ or in ``docs`` directory
of the sources.  This includes a man page for the ``mayavi2``
application, a users guide in HTML and PDF format and documentation
for `mlab`.


Examples
========

Examples are all in the ``examples`` directory of the source or the SVN checkout.
The docs and examples do not ship with the binary eggs.  The examples directory
also contains some sample data.


Test suite
==========

The basic test suites for tvtk and mayavi can be run using nose::

  nosettests -v tvtk/tests
  nosettests -v mayavi

The integration tests::

  cd integrationtests/mayavi
  python run.py


Bug tracker, mailing list etc.
==============================

The bug tracker is available in `github <https://github.com/enthought/mayavi/issues>`_ Please provide info and details on platform, python, vtk and gui backends and their versions. If possible, a small example replicating the the problem.

Authors and Contributors
========================

* Core contribtuors:

  Prabhu Ramachandran: primary author.

  Gaël Varoquaux: mlab, icons, many general improvements and maintainance.

  Deepak Surti: Upgrade to VTK 5.10.1, VTK 6.x with new pipeline.

* Support and code contributions from Enthought Inc.

* Patches from many people (see the release notes), including K K Rai and
  R A Ambareesha for tensor support, parametric source and image data.

  Many thanks to all those who have submitted bug reports and suggestions for
  further enhancements.
