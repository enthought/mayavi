

.. _example_zzz_reader:

Zzz reader example
--------------------------------------------

This is a simple example that shows how to create a reader factory
and register that reader with mayavi.

To use this:

    - put this in ~/.mayavi2/
    - then import this module in your ~/.mayavi2/user_mayavi.py.

that's it.

What you should get:

    - Options to open .zzz files from the file->open menu.
    - Open .zzz files via right click.
    - Open .zzz files from the engine or mlab (via open)
    - do mayavi2 -d foo.zzz.



**Python source code:** :download:`zzz_reader.py`

.. literalinclude:: zzz_reader.py
    :lines: 19-


    