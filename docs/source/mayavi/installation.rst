.. _installation:

Installation
============

.. topic:: Section summary

    This section details the various ways of installing Mayavi.

    If you already have Mayavi up and running, you can skip this section.


By itself Mayavi is not a difficult package to install but its dependencies
are unfortunately rather heavy. Fortunately, many of these dependencies are now
available as wheels on PyPI.  The two critical dependencies are,

  1. VTK_
  2. A GUI toolkit, either PyQt4_, PySide_, PyQt5_ or wxPython_.

The latest VTK wheels are available on all the major platforms (Windows,
MacOS, and Linux), but only for 64 bit machines. Python 3.x is fully supported
on all these operating systems and Python 2.7.x on MacOS and Linux. If you are
out of luck, and your platform is not supported then you will need to install
VTK yourself using your particular distribution as discussed in the `General
Build and Installation instructions
<http://docs.enthought.com/mayavi/mayavi/installation.html#installing-ready-made-distributions>`_

On Python 3.x you will need to install PyQt5_ and wheels are available for
this. On 2.7.x you have more options, and can use PySide_, PyQt4_, and
wxPython_. These can be installed from pip or from your package manager.

Currently, Mayavi itself should work with the new wxPython 4.x. However,
traitsui_, pyface_, and other ETS packages do not yet support it so the UI
will not work correctly. Older versions should work. PyQt/PySide should work
largely out of the box. PySide2 is still young so YMMV.


.. _PyQt5: https://pypi.org/project/PyQt5/
.. _PySide: https://pypi.org/project/PySide
.. _PyQt4: https://pypi.org/project/PyQt4/
.. _wxPython: https://pypi.org/project/wxPython/
.. _VTK: https://www.vtk.org
.. _traitsui: https://github.com/enthought/traitsui
.. _pyface: https://github.com/enthought/pyface


.. _install-with-pip:

Installing with `pip`
---------------------

pip_ is the PyPA_ recommended tool for installing Python packages from PyPI_.
The latest version of Mayavi available on PyPI can be found
`here <https://pypi.python.org/pypi/mayavi>`_.

Required python packages can be automatically fetched and installed with pip_.

Latest stable release
~~~~~~~~~~~~~~~~~~~~~

As of the latest release, i.e. 4.6.0 and above, if you are using Python 3.x
and are on a 64 bit machine, installation via pip_ is the easiest and is as
follows::

  $ pip install mayavi

  $ pip install PyQt5

Thats it!

If you are unable to do this, read the documentation above and find a way to
install VTK and a suitable UI toolkit and then repeat the above.

If you are interested in the jupyter notebook support as well, do the
following (after ensuring that you have jupyter_ installed of course)::

  $ jupyter nbextension install --py mayavi --user
  $ jupyter nbextension enable --py mayavi --user

You will also need to have ipywidgets_ and ipyevents_ installed. These can be
installed via pip or your favorite package manager.

.. _ipywidgets: https://ipywidgets.readthedocs.io
.. _ipyevents: https://github.com/mwcraig/ipyevents


.. _installing_git:

Bleeding edge
--------------

If you want to install the latest version of Mayavi from github, you can
simply do the following::

  $ git clone https://github.com/enthought/mayavi.git
  $ cd mayavi
  $ pip install -r requirements.txt
  $ pip install PyQt5  # replace this with any supported toolkit
  $ python setup.py install  # or develop

Add the jupyter nbextensions using the instructions in the section above and
you should be good to go.

Mayavi depends on several packages that are part of ETS.  Sometimes it
is possible that the in-development mayavi version may depend on some
feature of an unreleased component.  The ETS packages that Mayavi
depends on are apptools_, traits_, traitsui_, pyface_, and envisage_.
In case one of these are required these can also be installed via git.
They are all relatively easy to install packages.


.. _traits: https://github.com/enthought/traits
.. _apptools: https://github.com/enthought/apptools
.. _envisage: https://github.com/enthought/envisage



Installing ready-made distributions
------------------------------------

:Windows:
     Under Windows the best way to install Mayavi is to install a full
     Python distribution, such as `Enthought Canopy`_, Pythonxy_, or Anaconda_.
     Note that for Pythonxy, you need to check in 'ETS' in the installer, when
     selecting components. If you want to reduce the disk space used by
     Pythonxy, you can uncheck other components.

:MacOSX:
    The full Python distribution `Enthought Canopy`_ (that includes
    Mayavi) or Anaconda_ are also available for MacOSX.

:Ubuntu or Debian:
     Mayavi is packaged in Debian_ and Ubuntu_ and can be installed via
     ``apt``.

:RedHat EL3 and EL4:
    The full Python distribution `Enthought Canopy`_ (that includes Mayavi) is also
    available for RHEL3 and 4.



.. _jupyter: https://jupyter.org
.. _Mayavi: http://docs.enthought.com/mayavi/mayavi
.. _TVTK: http://docs.enthought.com/mayavi/tvtk
.. _envisage: http://docs.enthought.com/envisage
.. _Traits: http://docs.enthought.com/traits
.. _Debian: http://www.debian.org
.. _Ubuntu: http://www.ubuntu.com
.. _numpy: http://numpy.scipy.org
.. _Enthought Canopy: https://www.enthought.com/products/canopy/
.. _Pythonxy: https://python-xy.github.io/
.. _Anaconda: https://store.continuum.io/cshop/anaconda/
.. _pip: https://pip.pypa.io/en/stable/
.. _PyPA: https://packaging.python.org/en/latest/current/
.. _PyPI: https://pypi.python.org/pypi

.. _install-with-edm:

Installing with `Enthought Deployment Manager(EDM)`
...................................................

EDM is Enthought's freely available python environment manager. It
allows new python users to create light-weight and custom python
environments. A major advantage of EDM is its robust state-of-the-art
management of package dependencies, with support for resolving
conflicts and ensuring consistent package version sets. It can be
downloaded from `edmInstaller
<https://www.enthought.com/products/edm/installers/>`_.

EDM provides Python 2.7.x as well as Python 3.x runtimes. Python 2.7
is the default version. After installing EDM, mayavi can be easily
installed from the terminal by using `edm`::

  $ edm install mayavi pyqt

This will install mayavi along with 'pyqt'. After this, you can start a shell with the default python version by running::

  $ edm shell

This should set Mayavi for the default python 2.7.

For python 3.6.x, you can install it by running:

  $ edm environments create --version 3.6 py3

Where 'py3' is the name of the environment. You may change this name to something else if you wish. Once you create the environment, you can activate it as follows::

  $ edm shell -e py3

You can now install mayavi as follows::

  $ edm install mayavi pyqt

Note that 'pyqt' needs to be installed explicitly for python 3.6 as well as for python 2.7.

.. _installing-with-conda

Installing with `Conda`
.......................

Conda is an open source package management environment management
system for installing multiple versions of software packages and their
dependencies. Conda is included in Anaconda and Miniconda.

Miniconda is a small "bootstrap" version that includes conda, python,
and the packages they depend on. Depending on your operating system,
you can download the `MinicondaInstaller
<https://conda.io/miniconda.html>`_


After installing conda you need to run the following from command line::

  $ conda create -n pyconda python=3.5 pyqt=4
  $ source activate pyconda
  $ conda install -c menpo mayavi

You should be all set with this.  As of Mayavi 4.6.0 you can also use ``pyqt=5``.


.. Installing with conda-forge

Installing with `Conda-forge`
-----------------------------

Conda-forge is a community-led conda channel of installable packages. For more information on conda-forge, you can vist their their website_.

.. _website: https://conda-forge.org

Follow these steps to install using conda-forge:

First, clone the environment or build one from scratch::

	$ conda create --name pyforge --clone root
 	or
 	$ conda create --name pyforge python=2.7

Then add the conda-forge channel::

	$ conda config --add channels conda-forge

Activate the 'pyforge' environment::

	$ source activate pyforge

You will need to install these dependencies for Mayavi::

	$ conda install vtk
	$ conda install pyqt=4

Finally, Mayavi can be installed as::

	$ conda install mayavi


Testing your installation
-------------------------

The easiest way to test if your installation is OK is to run the mayavi2
application like so::

 mayavi2

To get more help on the command try this::

 mayavi2 -h

``mayavi2`` is the mayavi application.  On some platforms like win32
you will need to double click on the ``mayavi2.exe`` program found in
your ``PythonXY\Scripts`` folder.  Make sure this directory is in your
path.

.. note::
  Mayavi can be used in a variety of other ways but the ``mayavi2``
  application is the easiest to start with.

If you have the source tarball of mayavi or have checked out the sources
from the github repository, you can run the examples in
``mayavi*/examples``.  There are plenty of example scripts
illustrating various features.  Tests are available in the
``mayavi*/tests`` sub-directory.

Test suite
~~~~~~~~~~

The basic test suites for tvtk and mayavi can be run using nose::

  nosetests -v tvtk/tests
  nosetests -v mayavi

The integration tests can be run as::

  cd integrationtests/mayavi
  python run.py


Troubleshooting
----------------

If you are having trouble with the installation you may want to check
the :ref:`getting-help` page for more details on how you can search for
information or email the mailing list.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
