

.. _example_wx_embedding:

Wx embedding example
--------------------------------------------


This example shows to embed a Mayavi view in a wx frame.

The trick is to create a `HasTraits` object, as in the
mlab_traits_ui.py, mayavi_traits_ui.py, or the modifying_mlab_source.py
examples (:ref:`example_mlab_traits_ui`, :ref:`example_mayavi_traits_ui`,
:ref:`example_mlab_interactive_dialog`).

Calling the `edit_traits` method returns a `ui` object whose
`control` attribute is the wx widget. It can thus be embedded in a
standard wx application.

In this example, the wx part is very simple. See
:ref:`example_wx_mayavi_embed_in_notebook` for an example of more complex
embedding of Mayavi scenes in Wx applications.


**Python source code:** :download:`wx_embedding.py`

.. literalinclude:: wx_embedding.py
    :lines: 17-


    