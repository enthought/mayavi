
Main view and UI objects
=========================

This is an API reference of the views for the main objects.
The section :ref:`builing_applications` gives some context on
how to use them.

.. currentmodule:: mayavi.core.ui.api

Scene UIs: :class:`DecoratedScene` and :class:`MayaviScene`
--------------------------------------------------------------

.. autoclass:: DecoratedScene
    :members:
    :show-inheritance:

.. autoclass:: MayaviScene
    :members:
    :show-inheritance:


:class:`SceneEditor`
---------------------
.. autoclass:: SceneEditor
    :members:
    :show-inheritance:

:class:`MlabSceneModel`
-----------------------
.. autoclass:: MlabSceneModel
    :members:
    :show-inheritance:

:class:`EngineView` and  :class:`EngineRichView`
--------------------------------------------------

These are two objects to be used as views for an engine::

   from mayavi.core.ui.api import EngineView
   view = EngineView(engine=engine)
   view.edit_traits()


.. autoclass:: EngineView
    :members:
    :show-inheritance:

.. autoclass:: EngineRichView
    :members:
    :show-inheritance:

