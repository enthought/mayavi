

.. _example_multiple_engines:

Multiple engines example
--------------------------------------------


An example to show how you can have multiple engines in one application.

Mutliple engines can be useful for more separation, eg to script each
engine separately, or to avoid side effects between scenes.

This example shows how to explicitly set the engine for an embedded
scene.

To define default arguments, it makes use of the Traits initialization
style, rather than overriding the __init__.


**Python source code:** :download:`multiple_engines.py`

.. literalinclude:: multiple_engines.py
    :lines: 13-


    