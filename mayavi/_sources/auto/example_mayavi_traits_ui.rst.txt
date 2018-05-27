

.. _example_mayavi_traits_ui:

Mayavi traits ui example
--------------------------------------------


An example of how to create a UI similar to the complete Mayavi application
inside a Traits UI view.

This does not use Envisage and provides a similar UI as seen in the full
Mayavi application.

This example uses `traitsUI <http://code.enthought.com/projects/traits/>`_
to create a dialog mimicking the mayavi2 application: a scene on the
right, and on the left a pipeline tree view, and below it a panel to
edit the currently-selected object.


**Python source code:** :download:`mayavi_traits_ui.py`

.. literalinclude:: mayavi_traits_ui.py
    :lines: 14-


    