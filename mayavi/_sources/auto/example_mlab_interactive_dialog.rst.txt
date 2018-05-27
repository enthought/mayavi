

.. _example_mlab_interactive_dialog:

Mlab interactive dialog example
--------------------------------------------


An example of how to modify the data visualized  via an interactive dialog.

A dialog is created via `TraitsUI
<http://code.enthought.com/projects/traits/>`_ from an object (MyModel).
Some attributes of the objects are represented on the dialog: first a
Mayavi scene, that will host our visualization, and two parameters that
control the data plotted.

A curve is plotted in the embedded scene using the associated
mlab.points3d function. The visualization object created is stored
as an attribute on the main MyModel object, to modify it inplace later.

When the `n_meridional` and `n_longitudinal` attributes are modified, eg via
the slide bars on the dialog, the curve is recomputed, and the
visualization is updated by modifying inplace the stored plot
object (see :ref:`mlab-animating-data`).

This example is discussed in details in the section
:ref:`embedding_mayavi_traits`.


.. image:: ../images/example_mlab_interactive_dialog.jpg
    :align: center



**Python source code:** :download:`mlab_interactive_dialog.py`

.. literalinclude:: mlab_interactive_dialog.py
    :lines: 23-


    