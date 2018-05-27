

.. _example_multiple_mlab_scene_models:

Multiple mlab scene models example
--------------------------------------------

 Example showing a dialog with multiple embedded scenes.

When using several embedded scenes with mlab, you should be very careful
always to pass the scene you want to use for plotting to the mlab
function used, elsewhere it uses the current scene. In this example,
failing to do so would result in only one scene being used, the last
one created.

The trick is to use the 'mayavi_scene' attribute of the MlabSceneModel,
and pass it as a keyword argument to the mlab functions.

For more examples on embedding mlab scenes in dialog, see also:
the examples :ref:`example_mlab_interactive_dialog`, and
:ref:`example_lorenz_ui`, as well as the section of the user manual
:ref:`embedding_mayavi_traits`.


**Python source code:** :download:`multiple_mlab_scene_models.py`

.. literalinclude:: multiple_mlab_scene_models.py
    :lines: 17-


    