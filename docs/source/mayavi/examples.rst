.. _learning-mayavi-by-example:

Tutorial examples to learn Mayavi
==================================

.. topic:: Section summary

    In this section, we give a few detailed examples of how you can use the
    Mayavi application to tour some of its features.

    This section is mainly interested with the Mayavi application, but it
    is a good introduction to the ideas behind using Mayavi as a library.
    However, if you are only interested in a quick start to use Mayavi as
    a simple, Matlab-like, plotting library, you can jump directly to the 
    :ref:`simple-scripting-with-mlab` section, and come back later for a
    deeper understanding.

To get acquainted with mayavi you may start up the Mayavi2 application,
``mayavi2`` in the command line, like so::

  $ mayavi2

On Windows you can double click on the installed ``mayavi2.exe``
executable (usually in the ``Python2X\Scripts`` directory), or use the
start menu entry, if you installed python(x,y) or EPD.

Once Mayavi starts, you may resize the various panes of the user
interface to get a comfortable layout.  These settings will become the
default "perspective" of the mayavi application.  More details on the
UI are available in the :ref:`general-layout-of-ui` section.

Before proceeding on the quick tour, it can be useful to locate some data
to experiment with. Two of the examples below make use of data shipped
with the mayavi sources ship.  These may be found in the
``examples/data`` directory inside the root of the mayavi source tree. If
these are not installed, the sources may be downloaded from here:
http://code.enthought.com/enstaller/eggs/source/

**Examples**:

.. toctree::

    example_parametric_surface.rst
    example_heart.rst
    example_fire.rst
    example_using_with_scipy.rst  
    example_exploring_a_vector_field.rst

