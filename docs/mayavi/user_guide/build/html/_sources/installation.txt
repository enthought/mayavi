.. _installation:

Installation
============

Up-to-date install instructions are always available at the Mayavi2_
web page.  The following instructions are likely not up-to-date but
should give you a good idea of the general installation procedure and
a start on where to look.

.. _Mayavi2: https://svn.enthought.com/enthought/wiki/MayaVi

Requirements
------------

Mayavi requires at the very minimum the following packages:

    * VTK_ >= 4.4 (5.x is ideal)
    * numpy_ >= 1.0.1
    * setuptools_ (for installation and egg builds)
    * TVTK_ (`enthought.tvtk`)
    * Traits_ >= 2.0 (`enthought.traits`)

The following requirements are really optional but strongly recommended,
especially if you are new to mayavi:

    * Envisage_ == 2.x (`enthought.envisage`)
    * wxPython_ 2.6.x or 2.8.x

One can install the requirements in several ways.  

   * Win32: Under Win32 the best way to get all the dependencies is to
     use Enthought's enstaller_.  This will also let you install mayavi.

   * Linux: Most Linux distributions will have installable binaries
     available for the some of the above.  For example, under Debian_ or
     Ubuntu_ you would need ``python-vtk``, ``python-wxgtk2.6``,
     ``python-setuptools``, ``python-numpy``.  More information on
     specific distributions and how you can get the requirements for
     each of these should be available from the list of distributions
     here:

        https://svn.enthought.com/enthought/wiki/Install

   * Mac OS X: The best available instructions for this platform are
     available on the IntelMacPython25_ page.


There are several ways to install TVTK_, Traits_ and Mayavi.  These
are described in the following.

.. _TVTK: https://svn.enthought.com/enthought/wiki/TVTK
.. _VTK: http://www.vtk.org
.. _envisage: https://svn.enthought.com/enthought/wiki/Envisage
.. _Traits: https://svn.enthought.com/enthought/wiki/Traits
.. _wxPython: http://www.wxpython.org
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _enstaller: http://code.enthought.com/enstaller
.. _Debian: http://www.debian.org
.. _Ubuntu: http://www.ubuntu.com
.. _IntelMacPython25: https://svn.enthought.com/enthought/wiki/IntelMacPython25
.. _numpy: http://numpy.scipy.org

Python packages: Eggs
-----------------------

Mayavi2_ is part of the Enthought Tool Suite (ETS_).  As such, it is
distributed as part of ETS and therefore binary packages and source
packages of ETS will contain Mayavi2. Mayavi releases are almost always
made along with an ETS release.  You may choose to install all of ETS or
just Mayavi2 alone from a release. 

ETS has been organized into several different Python packages.  These
packages are distributed as Python Eggs_.  Python eggs are fairly
sophisticated and carry information on dependencies with other eggs.  As
such they are rapidly becoming the standard for distributing Python
packages.

There are primarily two ways to use ETS eggs.
 
  1. The first and easiest is to use pre-built eggs built for your
     particular platform.  More instructions on this are below. 

  2. The second is to build the eggs from the source tarballs.  This is
     also fairly easy to do if you have a proper build environment.

Given this background please see the following:

  * `Enthought Install`_ describes how ETS can be installed with eggs.
    Check this page first.  It contains information on how to install
    the prebuilt binary eggs for various platforms along with any
    dependencies.

  * If there aren't any pre-built eggs for your platform, first make
    sure the requirements are installed, and then build and install
    the eggs like so::

     $ easy_install -f http://code.enthought.com/enstaller/eggs/source \
         > enthought.mayavi

    This one command will download, build and install all the required
    ETS related modules that mayavi needs for the latest ETS release.
    If you run into trouble please check the `Enthought Install`_ pages.
    Note that the above is really one line, it has been split with the
    ``\`` character into two lines in order to fit on the printed
    version of this document.


.. _Eggs: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _Enthought Install: https://svn.enthought.com/enthought/wiki/Install
.. _ETS: http://code.enthought.com/ets

The bleeding edge: SVN
----------------------

If you want to get the latest development version of Mayavi, we
recommend that you check it out from SVN.  Mayavi depends on several
packages that are part of ETS.  It is highly likely that the
in-development mayavi version may depend on some feature of an as yet
unreleased component.  Therefore, it is very convenient to get all the
relevant ETS projects that mayavi recursively depends on in one single
checkout.  In order to do this easily, Dave Peterson has created a
package called ETSProjectTools_.  This must first be installed and then
any of ETS related repositories may be checked out.  Here is how you can
get the latest development sources.

 1. Install ETSProjectTools_ like so::

     $ svn co https://svn.enthought.com/svn/enthought/ETSProjectTools/trunk \
            ETSProjectTools
     $ cd ETSProjectTools
     $ python setup.py install

    This will give you several useful scripts like ``etsco``, ``etsup``,
    ``etsdevelop`` etc.

 2. To get just the sources for mayavi and all its dependencies do this::

      $ etsco enthought.mayavi

    This will look at the latest available mayavi, parse its ETS
    dependencies and check out the relevant sources.  If you want a
    particular mayavi release you may do::

      $ etsco "enthought.mayavi==2.0.2"

    If you'd like to get the sources for an entire ETS release do this
    for example::

      $ etsco "ets==2.7.0"

    This will checkout all the relevant sources from SVN.  Be patient,
    this will take a while.  More options for the ``etsco`` tool are
    available in the ETSProjectTools_ page.

 3. Once the sources are checked out you may either do an::
    
        $ etsdevelop

    This will  install all the checked out sources via a ``setup.py
    develop`` applied to each package.  
 
 4. Alternatively, you may want to build binary eggs, of the sources.
    At this time ETSProjectTools does not provide a build script,
    however you can use the ``egg_builder.py`` script from here::

      $ svn cat https://svn.enthought.com/svn/enthought/sandbox/egg_builder.py \
            > egg_builder.py

    This script can be used to build eggs like so (here we assume that
    ``etsco`` checked out the sources into ``ets-2.7.0``)::

      $ cd ets-2.7.0
      $ python ../egg_builder.py

    This will build all the eggs and put them inside a ``dist``
    subdirectory.  The mayavi development egg and its dependencies  may
    be installed via::

      $ easy_install -f dist enthought.mayavi

    Alternatively, if you'd like just ``enthought.mayavi`` installed via
    ``setup.py develop`` with the rest as binary eggs you may do::

      $ cd enthought.mayavi_x.y.z
      $ python setup.py develop -f ../dist

    This will pull in any dependencies from the built eggs.

You should now have the latest version of Mayavi installed and usable.

.. _ETSProjectTools: https://svn.enthought.com/enthought/wiki/SVNScripts 


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
from the SVN repository, you can run the examples in
``enthought.mayavi*/examples``.  There are plenty of example scripts
illustrating various features.  Tests are available in the
``enthought.mayavi*/tests`` sub-directory.



..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

