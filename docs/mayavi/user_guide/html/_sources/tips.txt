Tips and Tricks
===============

Below are a few useful tips and tricks that you may find useful when you
use Mayavi2.


Customizing the Mayavi2 UI
---------------------------

See the ``examples/mayavi_custom_ui.py`` example that documents and
shows how the UI of the ``mayavi2`` application can be modified.  The
module documents how this can be done and provides a simple example.


Off screen rendering
--------------------

Often you write Mayavi scripts to render a whole batch of images to
make an animation or so and find that each time you save an image,
Mayavi "raises" the window to make it the active window thus
disrupting your work.  This is needed since VTK internally grabs the
window to make a picture.  To get around this behavior you may click
on the scene and set the "Off screen rendering" option on.  Or from a
script::

  mayavi.engine.current_scene.scene.off_screen_rendering = True

This will stop raising the window.  However, this may not be enough.
If you are using win32 then off screen rendering should work well out
of the box.  On Linux and the Mac you will need VTK-5.1 (currently
from CVS) to get this working properly.

If upgrading VTK is a problem there is another approach for any OS
that supports X11.  This option should work irrespective of the
version of VTK you are using.  The idea is to use the virtual
framebuffer X server for X11 like so:

  * Make sure you have the `xvfb` package installed.

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

