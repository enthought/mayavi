.. _installation:

Installation
============

.. topic:: Section summary

    This section details the various ways of installing and compiling
    Mayavi.

    If you already have Mayavi up and running, you can skip this section.

..
 Up-to-date install instructions for the latest version of Mayavi are
 always available from links at the Mayavi_ wiki page.  The following
 will give you a good idea of the general installation procedure and a
 start on where to look for more information.
 
Installing ready-made distributions
------------------------------------

:Windows:
     Under Windows the best way to install Mayavi is to install a full
     Python distribution, such as `Enthought Canopy`_, Pythonxy_, or Anaconda_. 
     Note that for Pythonxy, you need to check in 'ETS' in the installer, when
     selecting components. If you want to reduce the disk space used by
     Pythonxy, you can uncheck other components.
     
:MacOSX:
    The full Python distribution `Enthought Canopy`_ (that includes Mayavi) is also
    available for MacOSX.  Unless you really enjoy the intricacies of
    compilation; this is the best solution to install Mayavi.

:Ubuntu or Debian:
     Mayavi is packaged in Debian and Ubuntu. In addition, more up to
     date packages of Mayavi releases for old versions of Ubuntu are
     available at https://launchpad.net/~gael-varoquaux/+archive .
     Experimental Debian packages are also available at
     http://people.debian.org/~varun/ .

:RedHat EL3 and EL4:
    The full Python distribution `Enthought Canopy`_ (that includes Mayavi) is also
    available for RHEL3 and 4.


Doing it yourself
------------------

.. _requirements-for-install:

Requirements for manual installs
................................

If you are not using a full, ready-made, scientific Python distribution,
you need to satisfy Mayavi's requirements.  However, depending on your
installation procedure, these requirements may be automatically done
for you (see the following sections).

Mayavi requires at the very minimum the following packages:

    * VTK_ >= 5.0 with Python wrapper
    * numpy_ >= 1.1.1
    * setuptools_ (for installation and egg builds)
    * Traits_ >= 3.0 (`Traits`, `TraitsUI` and `TraitsBackendWX` or
      `TraitsBackendQt`, `EnthoughtBase`, `AppTools`)

.. note::

   As new versions of VTK_ become available, Mayavi is continuously
   updated to support the latest releases.  If your VTK version is
   newer than 6.2.0, please check the Changelog_ for the current status
   of Mayavi.

.. _Changelog: auto/changes.html

The following requirements are really optional but strongly recommended,
especially if you are new to Mayavi:

    * PySide_ or PyQt4_ or wxPython_ (2.8.x)
    * configobj_
    * Envisage_ == 3.x (`EnvisageCore` and `EnvisagePlugins`) 
      **Note** These last requirements can be automatically installed,
      see below.

One can install the requirements in several ways.  

   * Windows and MacOSX: even if you want to build from source, a good
     way to install the requirements is to install one of the
     distributions indicated above. Note that under Windows, 
     `Enthought Canopy`_ comes with a compiler (mingw) and facilitates 
     building Mayavi.

   * Linux: In addition to using `Enthought Canopy`_, most Linux
     distributions will have installable binaries
     available for the some of the above.  For example, under Debian_ or
     Ubuntu_ you would need ``python-vtk``, ``python-qt4``, ``python-qt4-gl``,
     ``python-setuptools``, ``python-numpy``, ``python-configobj``.


There are several ways to install TVTK_, Traits_ and Mayavi.  These
are described in the following.

.. _Mayavi: http://docs.enthought.com/mayavi/mayavi
.. _TVTK: http://docs.enthought.com/mayavi/tvtk
.. _VTK: http://www.vtk.org
.. _envisage: http://docs.enthought.com/envisage
.. _Traits: http://docs.enthought.com/traits
.. _PyQt4: http://pyqt.sourceforge.net/Docs/PyQt4/
.. _PySide: https://pypi.python.org/pypi/PySide/1.2.4
.. _PyQt4: http://pyqt.sourceforge.net/Docs/PyQt4/
.. _wxPython: http://www.wxpython.org
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _enstaller: https://pypi.python.org/pypi/enstaller
.. _Debian: http://www.debian.org
.. _Ubuntu: http://www.ubuntu.com
.. _IntelMacPython25: https://svn.enthought.com/enthought/wiki/IntelMacPython25
.. _numpy: http://numpy.scipy.org
.. _Enthought Canopy: https://www.enthought.com/products/canopy/
.. _Pythonxy: https://python-xy.github.io/
.. _Anaconda: https://store.continuum.io/cshop/anaconda/
.. _configobj: http://pypi.python.org/pypi/ConfigObj/


.. _install-with-pip:

Installing with `pip`
.....................

pip_ is the PyPA_ recommended tool for installing Python packages from PyPI_.
The latest version of Mayavi available on PyPI can be found
`here <https://pypi.python.org/pypi/mayavi>`_.

Required python packages can be automatically fetched and installed by `pip`.
However, VTK Python wrapper is not available from PyPI.
Therefore you will need to install it separately before proceeding;
e.g. it is available from `Enthought Canopy`_ or Linux installable binaries.

After installing VTK Python, you can install mayavi using `pip`::

  $ pip install mayavi

.. _pip: https://pip.pypa.io/en/stable/
.. _PyPA: https://packaging.python.org/en/latest/current/
.. _PyPI: https://pypi.python.org/pypi

.. _install-with-easy-install:

Installing with `easy_install`
...............................

First make sure you have the prerequisites for Mayavi installed, as
indicated in :ref:`requirements-for-install`.

Mayavi_ is part of the Enthought Tool Suite (ETS_).  As such, it is
distributed as part of ETS and therefore binary packages and source
packages of ETS will contain Mayavi. Mayavi releases are almost always
made along with an ETS release.  You may choose to install all of ETS or
just Mayavi alone from a release. 

ETS has been organized into several different Python packages.  These
packages are distributed as Python Eggs_.  Python eggs are fairly
sophisticated and carry information on dependencies with other eggs.  As
such they are rapidly becoming the standard for distributing Python
packages.

The easiest way to install Mayavi with eggs is to use pre-built eggs 
built for your particular platform and downloaded by `easy_install`. 
Alternatively `easy_install` can build the eggs from the source tarballs.
This is also fairly easy to do if you have a proper build environment.

To install eggs, first make sure the essential requirements are
installed, and then build and install the eggs like so::

 $ easy_install "Mayavi[app]" 

This one command will download, build and install all the required ETS
related modules that Mayavi needs for the latest ETS release, this means
that the `Traits` dependencies and the `Envisage` dependencies will be
installed automatically.

If you are running a unix system (such as Linux) we advice you not to
install the files in the system directories (`/usr`). An easy way to
avoid this is to run::

 $ easy_install --prefix "Mayavi[app]"

.. warning:: **Known issues**

  * One common sources of problems during an install, is the presence of
    older versions of packages such as Traits, Mayavi, Envisage or TVTK.
    Make sure that you clean your ``site-packages`` before installing a new
    version of Mayavi. 
    
  * Another problem often encountered is running into
    what is probably a bug of the build system that appears as a "sandbox
    violation". In this case, it can be useful to try the download and
    install command a few times.


.. note:: Automatic downloading of required eggs

    If you wish to download all the eggs fetched by `easy_install`, for
    instance to propagate to an offline PC, you can use virtualenv to
    create an empty site-packages, and install to it::

        virtualenv --no-site-packages temp
        cd temp
        source bin/activate
        mkdir temp_subdir
        easy_install -zmaxd temp_subdir "Mayavi[app,nonets]"


.. _step-by-step-window-installation:

Step-by-step instructions to install with eggs under Windows
...............................................................

If you do not wish to install a ready-made distribution under Windows,
these instructions (provided by Guillaume Duclaux) will guide you through
the necessary steps to configure a Windows environment in which Mayavi
will run.

1. Install Python 2.5. Add 'C:\\Python25;` to the PATH environment
   variables.

2. Install Mingw32, from the Download section of http://www.mingw.org/ ,
   use the MinGW5.1.4 installer. Add 'C:\\MinGW\\bin;' to the PATH
   environment variables.

3. Create a 'c:\\documents and settings\\USERNAME\\pydistutils.cfg' file(where 
   USERNAME is the login) with the following contents::

               [build]
               compiler=mingw32

4. Create the new environment variable HOME and set it to the value:
   'c:\\docume~1\\USERNAME' (where USERNAME is the login name)

5. Install Setuptools (0.6c9 binary) from its webpage, and
   'C:\Python25\Scripts;' to the PATH environment variables

6. Install VTK 5.2 (using Dr Charl P. Botha Windows binary
   http://cpbotha.net/2008/09/23/python-25-enabled-vtk-52-windows-binaries/
   )

    * Unzip the folder content in 'C:\\Program Files\\VTK5.2_cpbotha'
    * add 'C:\\Program Files\\VTK5.2_cpbotha\\bin;' to the PATH environment
      variables
    * create a new environment variable PYTHONPATH and set it to the
      value 'C:\\Program Files\\VTK5.2_cpbotha\\lib\\site-packages;'
    * If you are running an old version of windows (older than XP)
      download msvcr80.dll and msvcp80.dll from the www.dll-files.com
      website and copy them into C:\\winnt\\system32.

7. Install Numpy (binary from http://numpy.scipy.org/ )

8. Installing wxPython (2.8 binary from http://www.wxpython.org/ )

9. Run in cmd.exe::

     easy_install Sphinx EnvisageCore EnvisagePlugins configobj

10. Finally, run in cmd.exe::

     easy_install Mayavi[app]


.. _Eggs: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _ETS: http://code.enthought.com/

Downloading tarballs
.....................

Relase tarballs for Mayavi can be found on the PyPI page, under 'download
URL': http://pypi.python.org/pypi/mayavi/

.. _install-in-mac-snow-leopard:

Under Mac OSX Snow Leopard
..........................

Under Mac OSX Snow Leopard, you may need to build VTK yourself. Here are
instructions specific to Snow Leopard (thanks to Darren Dale for
providing the instructions):

#. Download the VTK tarball, unzip it, and make a build directory
   (vtkbuild) next to the resulting VTK directory

#. Then cd into vtkbuild and run "cmake ../VTK". Next, edit CMakeCache.txt 
   (in vtkbuild) and set::

      //Build Verdict with shared libraries.
      BUILD_SHARED_LIBS:BOOL=ON

      //Build architectures for OSX
      CMAKE_OSX_ARCHITECTURES:STRING=x86_64

      //Minimum OS X version to target for deployment (at runtime); newer
      // APIs weak linked. Set to empty string for default value.
      CMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.6

      //Wrap VTK classes into the Python language.
      VTK_WRAP_PYTHON:BOOL=ON

      //Arguments passed to "python setup.py install ..." during installation.
      VTK_PYTHON_SETUP_ARGS:STRING=

#. Run "cmake ../VTK" again.

#. Run "make -j 2" for a single cpu system. "make -j 9" will compile
   faster on an 8-core system.

#. Run "sudo make install"

#. Edit your ~/.profile and add the following line::

      export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:/usr/local/lib/vtk-5.4

#. Run "source ~/.profile" or open a new terminal so the DYLD_LIBRARY_PATH
   environment variable is available.

#. After that, install Mayavi in the usual way.

.. _installing_git:

The bleeding edge: Git
----------------------

If you want to get the latest development version of Mayavi (e.g. for
developing Mayavi or contributing to the documentation), we
recommend that you check it out from github: Mayavi is hosted on github
with its own repository: https://github.com/enthought/mayavi as part of the
Enthought open source packages (ETS): https://github.com/enthought/ets

Mayavi depends on several packages that are part of ETS.  It is highly
likely that the in-development mayavi version may depend on some feature
of an unreleased component.  It is very convenient to get all the
relevant ETS projects that Mayavi recursively depends on with a single
checkout.  The ETS repository provides an `ets` module, which allows
pulling all other ETS projects from github, and other useful features.

To install ETS, please follow the instruction
`here <https://github.com/enthought/ets>`_.

.. note::

   The `ets` utility downloads the entire ETS, which is more than you need
   to build Mayavi. As the extra packages have additional
   dependencies, they may render the build harder. You can remove
   safely the following directories::

     blockcanvas chaco codetools enable graphcanvas scimath


Testing your installation
-------------------------

The easiest way to test if your installation is OK is to run the mayavi2
application like so::

 mayavi2

To get more help on the command try this::

 mayavi2 -h

``mayavi2`` is the mayavi application.  On some platforms like win32
you will need to double click on the ``mayavi2.exe`` program found in
your ``Python2X\Scripts`` folder.  Make sure this directory is in your
path.

.. note::
  Mayavi can be used in a variety of other ways but the ``mayavi2``
  application is the easiest to start with.

If you have the source tarball of mayavi or have checked out the sources
from the github repository, you can run the examples in
``mayavi*/examples``.  There are plenty of example scripts
illustrating various features.  Tests are available in the
``mayavi*/tests`` sub-directory.


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

