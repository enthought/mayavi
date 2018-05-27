

.. _example_user_mayavi:

User mayavi example
--------------------------------------------


Sample Mayavi customization file.

This code is not to be executed as `mayavi2 -x user_mayavi.py` or
`python user_mayavi.py`.

Put this file in ~/.mayavi2/user_mayavi.py and rerun mayavi2 to see what
it does -- the worker view may not show up by default so you will have
to go to View->Other and in the Show View dialog, activate the "Custom
Mayavi2 View".

The added modules should show up in the menus (Look for UserOutline in
the Modules)

____

This module demonstrates how to extend Mayavi.  It extends the  modules
provided by mayavi by adding these to the Mayavi registry.  Note that
the registry imports customize which in turn imports this file.

It also defines an Envisage plugin that is added to the default list of
plugins to extend the running mayavi application.  This plugin is
returned by the `get_plugins()` function.

This file must be placed inside the `~/.mayavi2` directory and called
`user_mayavi.py`.  Please note that `~/.mayavi2` is placed in `sys.path`
(if the directory exists) so make sure that you choose your module names
carefully (so as not to override any common module names).

The file may also be placed anywhere on sys.path and called
`site_mayavi.py` for global system level customizations.



**Python source code:** :download:`user_mayavi.py`

.. literalinclude:: user_mayavi.py
    :lines: 34-


    