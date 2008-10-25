Tips and Tricks
===============

Below are a few tips and tricks that you may find useful when you use
Mayavi2.


Extending Mayavi with customizations
-------------------------------------

A developer may wish to customize mayavi by adding new sources, filters
or modules.  These can be done by writing the respective filters and
exposing them via a ``user_mayavi.py`` or a ``site_mayavi.py`` as
described in `Customizing Mayavi2`_.   A more flexible and
reusable mechanism for doing this is to create a full fledged Mayavi
contrib package in the following manner.

  1. Create a Python package, lets call it ``mv_iitb`` (for IIT Bombay
     specific extensions/customizations).  The directory structure of
     this package can be something like so::

        mv_iitb/
                __init__.py
                user_mayavi.py
                sources/
                        ...
                filters/
                        ...
                modules/
                        ...
                docs/
                    ...

     The two key points to note in the above are the fact that
     ``mv_iitb`` is a proper Python package (notice the ``__init__.py``)
     and the ``user_mayavi.py`` is the file that adds whatever new
     sources/filters/modules etc. to mayavi.  The other part of the
     structure is really up to the developer.  At the moment these
     packages can add new sources, filters, modules and contribute any
     Envisage plugins that the ``mayavi2`` application will load.

  2. This package should then be installed somewhere on ``sys.path``.
     Once this is done, users can find these packages and enable them
     from the Tools->Preferences (the UI will automatically detect the
     package).  The ``user_mayavi.py`` of each selected package will
     then be imported next time mayavi is started, note that this will
     be usable even from ``mlab``.
         
Any number of such packages may be created and distributed.  If they are
installed, users can choose to enable them.  Internally, the list of
selected packages is stored as the ``enthought.mayavi.contrib_packages``
preference option.  The following code shows how this may be accessed
from a Python script::

   >>> from enthought.mayavi.preferences.api import preference_manager
   >>> print preference_manager.root.contrib_packages
   []
   >>> preference_manager.configure_traits() # Pop up a UI.

For more details on how best to write ``user_mayavi.py`` files and what
you can do in them, please refer to the
`examples/mayavi/user_mayavi.py`_ example.  Please pay particular
attention to the warnings in that file.  It is a very good idea to
ensure that the ``user_mayavi.py`` does not implement any
sources/modules/filters and only registers the metadata.  This will
avoid issues with circular imports. 


.. _`examples/mayavi/user_mayavi.py`: https://svn.enthought.com/enthought/browser/Mayavi/trunk/examples/mayavi/user_mayavi.py


Customizing Mayavi2
--------------------

There are three ways a user can customize mayavi:

  1. Via mayavi contributions installed on the system.  This may be done
     by enabling any found contributions from the Tools->Preferences
     menu on the Mayavi component, look for the "contribution settings".
     Any selected contributions will be imported the next time mayavi
     starts.  For more details see the `Extending Mayavi with
     customizations`_ section.

  2. At a global, system wide level via a ``site_mayavi.py``.  This file
     is to be placed anywhere on ``sys.path``.

  3. At a local, user level.  This is achieved by placing a
     ``user_mayavi.py`` in the users ``~/.mayavi2/`` directory.  If a 
     ``~/.mayavi2/user_mayavi.py`` is found, the directory is placed in
     ``sys.path``.

The files are similar in their content.  Two things may be done in this
file:

  1. Registering new sources, modules or filters in the mayavi registry
     (``enthought.mayavi.core.registry.registry``).  This is done by
     registering metadata for the new class in the registry.  See
     ``examples/mayavi/user_mayavi.py`` to see an example.

  2. Adding additional envisage plugins to the mayavi2 application.
     This is done by defining a function called ``get_plugins()`` that
     returns a list of plugins that you wish to add to the mayavi2
     application.


The ``examples/mayavi/user_mayavi.py`` example documents and shows how
this can be done.  To see it, copy the file to the ``~/.mayavi2``
directory.  If you are unsure where ``~`` is on your platform, just run
the example and it should print out the directory.

.. warning::

 In the ``user_mayavi.py`` or ``site_mayavi.py``, avoid mayavi imports
 like  ``from enthought.mayavi.modules.outline import Outline`` etc.
 This is because ``user_mayavi`` is imported at a time when many of the
 imports are not complete and this will cause hard-to-debug circular
 import problems.  The ``registry`` is given only metadata mostly in the
 form of strings and this will cause no problem.  Therefore to define
 new modules, we strongly recommend that the modules be defined in
 another module or be defined in a factory function as done in the
 example ``user_mayavi.py`` provided.


Off screen rendering
--------------------

Often you write Mayavi scripts to render a whole batch of images to make
an animation or so and find that each time you save an image, Mayavi
"raises" the window to make it the active window thus disrupting your
work.  This is needed since VTK internally grabs the window to make a
picture. 

If you already have a Python script, say ``script.py`` that sets up your
visualization that you run like so::

    $ mayavi2 -x script.py

Then it is very easy to have this script run offscreen.  Simply run it
like so::

    $ mayavi2 -x script.py -o

This will run the script in an offscreen, standalone window.  On Linux,
this works best with VTK-5.2 and above.  For more details on the command
line arguments supported by the ``mayavi2`` application, see the
:ref:`command-line-arguments` section.


Another option for offscreen rendering would be to click on the scene
and set the "Off screen rendering" option on.  Or from a script::

  mayavi.engine.current_scene.scene.off_screen_rendering = True

This will stop raising the window.  However, this may not be enough.  If
you are using win32 then off screen rendering should work well out of
the box.  On Linux and the Mac you will need VTK-5.2  to get this
working properly.

If upgrading VTK is a problem there is another approach for any OS
that supports X11.  This option should work irrespective of the
version of VTK you are using.  The idea is to use the virtual
framebuffer X server for X11 like so:

  * Make sure you have the ``xvfb`` package installed.

  * Create the virtual framebuffer X server like so::

      xvfb :1 -screen 0 1280x1024x24

    This creates the display ":1" and creates a screen of size
    1280x1024 with 24 bpp.  For more options check your ``xvfb`` man
    page.

  * Export display to :1 like so (on bash)::

      $ export DISPLAY=:1

  * Now run your mayavi script.  It should run uninterrupted on this X
    server and produce your saved images.
  
This probably will have to be fine tuned to suit your taste.

Note that if you want to use mayavi without the envisage UI or even a
traits UI (i.e. with a pure TVTK window) and do off screen rendering
with Python scripts you may be interested in the
``examples/offscreen.py`` example.  This simple example shows how you
can use MayaVi without using Envisage or the MayaVi envisage
application and still do off screen rendering.


Using ``mlab`` with the full envisage UI
----------------------------------------

Sometimes it is convenient to write an mlab script but still use the
full envisage application so you can click on the menus and use other
modules etc.  To do this you may do the following before you create an
mlab figure::

    from enthought.mayavi import mlab
    mlab.options.backend = 'envisage'
    f = mlab.figure()
    # ...

This will give you the full-fledged UI instead of the default simple
window.

Scripting mayavi without using Envisage
----------------------------------------

The example ``examples/standalone.py`` demonstrates how one can use
Mayavi without using Envisage.  This is useful when you want to minimize
dependencies.  ``examples/offscreen.py`` demonstrates how to use mayavi
without the envisage UI or even a traits UI (i.e. with a pure TVTK
window) and do off screen rendering.  


Embedding mayavi in your own traits UI
---------------------------------------

You've written your traits based application complete with a nice UI and
now you want to do some 3D plotting and embed that UI inside your own
UI.   This can be easily done.  ``examples/mayavi_traits_ui.py`` is a
fairly comprehensive example that demonstrates how you can embed almost
the entire mayavi UI into your traits based UI.
``examples/mlab_traits_ui.py`` demonstrates how you can do some simple
mlab based visualization.


Computing in a thread
----------------------

``examples/compute_in_thread.py`` demonstrates how to visualize a 2D
numpy array and visualize it as image data using a few modules.  It also
shows how one can do a computation in another thread and update the
mayavi pipeline once the computation is done.  This allows a user to
interact with  the user interface when the computation is performed in
another thread.


Polling a file and auto-updating mayavi
----------------------------------------

Sometimes you have a separate computational process that generates data
suitable for visualization.  You'd like mayavi to visualize the data but
automatically update the data when the data file is updated by the
computation.  This is easily achieved by polling the data file and
checking if it has been modified.  The ``examples/poll_file.py``
demonstrates this.  To see it in action will require that you edit the
scalar data in the ``examples/data/heart.vtk`` data file.  


..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

