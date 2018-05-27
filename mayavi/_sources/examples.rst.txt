.. _learning-mayavi-by-example:

Tutorial examples to learn Mayavi
-----------------------------------

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

We give a few detailed examples of how you can use the Mayavi application
to tour some of its features. Before proceeding to the examples, it can
be useful to locate some data to experiment with. Two of the examples
below make use of data shipped with the mayavi sources ship.  These may
be found in the ``examples/data`` directory inside the root of the mayavi
source tree. If these are not installed, the sources may be downloaded
from here: https://github.com/enthought/mayavi

.. topic:: **Examples**:

    .. toctree::

        example_parametric_surface.rst
        example_heart.rst
        example_fire.rst
        example_using_with_scipy.rst  
        example_exploring_a_vector_field.rst

