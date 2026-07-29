======================================================
Mayavi: 3D visualization of scientific data in Python
======================================================

Mayavi docs: https://mayavi.readthedocs.io/en/latest/
TVTK docs: https://tvtk.readthedocs.io/en/latest/

.. image:: https://img.shields.io/pypi/v/mayavi.svg
   :target: https://pypi.org/project/mayavi/
   :alt: Package on PyPI

.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
   :alt: BSD 3 Clause

Vision
======

Mayavi seeks to provide easy and interactive visualization of 3D data. It does
this by the following:

    - an (optional) rich user interface with dialogs to interact with all data
      and objects in the visualization.

    - a simple and clean scripting interface in Python, including one-liners,
      a-la mlab, or object-oriented programming interface.

    - harnesses the power of the VTK toolkit without forcing you to learn it.

Additionally Mayavi strives to be a reusable tool that can be embedded in your
applications in different ways or combined with the envisage
application-building framework to assemble domain-specific tools.

Mayavi is part of the Enthought Tool Suite (ETS).


Features
===========

Mayavi is a general purpose, cross-platform tool for 2-D and 3-D scientific
data visualization. Its features include:

    * Visualization of scalar, vector and tensor data in 2 and 3 dimensions

    * Easy scriptability using Python

    * Easy extendability via custom sources, modules, and data filters

    * Reading several file formats: VTK (legacy and XML), PLOT3D, etc.

    * Saving of visualizations

    * Saving rendered visualization in a variety of image formats

    * Convenient functionality for rapid scientific plotting via mlab (see mlab
      documentation)

    * See the Mayavi Users Guide for more information.

Unlike its predecessor MayaVi1_, Mayavi has been designed with scriptability
and extensibility in mind from the ground up.  While the mayavi2 application
is usable by itself, it may be used as an Envisage plugin which allows it to
be embedded in user applications natively. Alternatively, it may be used as a
visualization engine for any application.

.. _MayaVi1: http://mayavi.sf.net


Quick start
===========

If you are new to Mayavi it is a good idea to read the `online user manual`_
which should introduce you to how to install and use it.

If you have installed Mayavi as described in the next section, you should be
able to launch the ``mayavi2`` application and also run any of the examples
in the examples directory.


.. _online user manual: https://mayavi.readthedocs.io/en/latest/

Installation
=============

By itself Mayavi is not a difficult package to install but its dependencies
are unfortunately rather heavy. However, many of these dependencies are now
available as wheels on PyPI.  The two critical dependencies are,

  1. VTK_ >= 9.0
  2. A GUI toolkit, either PySide6_, PyQt6_, or wxPython_.

The latest VTK wheels are available on all the major platforms (Windows,
MacOS, and Linux). If you are
out of luck, and your platform is not supported then you will need to install
VTK yourself using your particular distribution as discussed in the `General
Build and Installation instructions
<https://mayavi.readthedocs.io/en/latest/installation.html#installing-ready-made-distributions>`_.

If you have trouble installing the Mayavi wheels, you can install the old way from the
source distribution and your current VTK version with::

  $ pip install --no-binary=mayavi --no-build-isolation mayavi

Currently, Mayavi itself should work with the new wxPython 4.x. However,
traitsui_, pyface_, and other ETS packages do not yet support it so the UI
will not work correctly. Older versions should work. PyQt6 and PySide6
should work out of the box.


.. _PyQt6: https://pypi.org/project/PyQt6/
.. _PySide6: https://pypi.org/project/PySide6/
.. _wxPython: https://pypi.org/project/wxPython/
.. _VTK: https://www.vtk.org
.. _traitsui: https://github.com/enthought/traitsui
.. _pyface: https://github.com/enthought/pyface

Latest stable release
-----------------------

As of the latest release, i.e. 4.6.0 and above, if you are using Python 3.x
and are on a 64 bit machine, installation via pip_ is the easiest and is as
follows::

  $ pip install mayavi
  $ pip install PySide6

Thats it!

If you are unable to do this, read the documentation above and find a way to
install VTK and a suitable UI toolkit and then repeat the above.

If you are interested in the jupyter notebook support as well, do the
following (after ensuring that you have jupyter installed of course.
**Note, the Jupyter notebook function is only supported starting mayavi
version 4.5.0**)::

  $ jupyter nbextension install --py mayavi --user
  $ jupyter nbextension enable --py mayavi --user

You will also need to have ipywidgets_ and ipyevents_ installed. These can be
installed via pip_ or your favorite package manager.

.. _pip: https://pip.pypa.io/en/stable/
.. _ipywidgets: https://ipywidgets.readthedocs.io
.. _ipyevents: https://github.com/mwcraig/ipyevents

Bleeding edge
--------------

If you want to install the latest version of Mayavi from github, you can
simply do the following::

  $ git clone https://github.com/enthought/mayavi.git
  $ cd mayavi
  $ pip install PySide6  # replace this with any supported toolkit
  $ pip install -v .  # or -e for editable install

Add the jupyter nbextensions using the instructions in the section above and
you should be good to go.

Documentation
==============

More documentation is available in the `online user manual`_ or in ``docs``
directory of the sources. This includes a man page for the ``mayavi2``
application, a users guide in HTML and PDF format and documentation for
``mlab``.

More documentation in the form of workshop/tutorial material is available
here:

- https://github.com/prabhuramachandran/mayavi-tutorial
- https://github.com/prabhuramachandran/mayavi-workshop

Tutorial Videos
===============

Here are some tutorial videos that you can watch to learn Mayavi:

- SciPy 2018 Mayavi tutorial (3 hrs):

  - Video: https://www.youtube.com/watch?v=r6OD07Qq2mw
  - Material: https://github.com/prabhuramachandran/mayavi-tutorial


Examples
========

Examples are all in the ``examples`` directory of the source or the git clone.
The docs and examples do not ship with the binary eggs. The examples directory
also contains some sample data.


Test suite
==========

The basic test suites for tvtk and mayavi can be run using nose::

  pytest -v tvtk/tests
  pytest -v mayavi

The integration tests::

  cd integrationtests/mayavi
  python run.py


Bug tracker, mailing list etc.
==============================

The bug tracker is available in `github
<https://github.com/enthought/mayavi/issues>`_ Please provide info and details
on platform, python, vtk and gui backends and their versions. If possible, a
small example replicating the the problem.

If you have questions you could ask on the `Mayavi-users mailing list
<https://sourceforge.net/p/mayavi/mailman/mayavi-users/>`_. This is used by
some folks and is not too active. Another mailing list that may be of use is
the `ETS Users mailing list
<https://groups.google.com/forum/#!forum/ets-users>`_. This is a more general
list where a lot of folks experienced with the Enthought Tool Suite are
available.

Authors and Contributors
========================

* Core contributors:

  Prabhu Ramachandran: primary author.

* Previous contributors:

  Gaël Varoquaux: mlab, icons, many general improvements and maintenance.

  Deepak Surti: Upgrade to VTK 5.10.1, VTK 6.x with new pipeline.

* Support and code contributions from Enthought Inc.

* Patches from many people (see the release notes), including K K Rai and
  R A Ambareesha for tensor support, parametric source and image data.

  Many thanks to all those who have submitted bug reports and suggestions for
  further enhancements.
