Tips and Tricks
===============

Below are a few tips and tricks that you may find useful when you use
Mayavi2.

.. _jupyter_notebook:

Using Mayavi in Jupyter notebooks
---------------------------------

There are three different ways in which one can embed Mayavi
visualizations in a Jupyter notebook.  The best way is to use the
``'ipy'`` backend (which is the default).  This backend was first
introduced in Mayavi 4.7.0.  This backend requires that the
ipywidgets_ and ipyevents_ packages be installed.  It behaves almost
exactly like a normal Mayavi UI window and supports any Mayavi/VTK
visualization and is fully interactive.  This backend relies on VTK's
off screen support and depending on how your VTK is configured may
require a windowing system.

.. _ipywidgets: https://ipywidgets.readthedocs.io
.. _ipyevents: https://github.com/mwcraig/ipyevents

There are two other backends, the simplest one is the ``'png'``
backend which produces images that can be embedded in the notebook.
These are static and not interactive.

In between these two extremes is the ``'x3d'`` backend which displays
X3D_ elements on the notebook.  The X3D output produces a fully
interactive 3D scene, however, this will not support VTK's interactive
widgets.  It does not support transparency and other advanced
visualizations either.  For information on how to interact with the
X3D scene, see here: http://www.x3dom.org/documentation/interaction/

Mayavi ships with some javascript files that can be installed as::

  $ jupyter nbextension install --py mayavi --user

This will install the x3dom Javascript and CSS files locally.  Note
that you do not need to "enable" the extension or anything after you
run the above.  For more instructions and options see the
`Installation of Jupyter Extensions`_.  Doing this allows one to view
X3D files without a network connection.

.. _Installation of Jupyter Extensions: http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Installation-of-Jupyter-Extensions

To view Mayavi visualizations on the notebook one should first do::

    from mayavi import mlab
    mlab.init_notebook()

Subequently, one may simply do::

    s = mlab.test_plot3d()
    s

When the ``init_notebook`` method is called it configures the Mayavi
objects so they can be rendered on the Jupyter notebook.

.. note::

   One can call ``init_notebook`` multiple times if one wishes to
   change the backend between ``ipy``, ``png``, and ``x3d`` for some
   reason.

There are several optional arguments to ``init_notebook``.

- The first is the backend which defaults to ``'ipy'``, and can also
  be set to ``'x3d'`` or ``'png'``.
- One can set the pixel width and height of the figure to create (as
  integers) (for example ``mlab.init_notebook('x3d', 800, 800)``).
  This only applies to the ``x3d`` backend.  For the ``ipy`` backend
  this can be set when creating a new ``figure`` with the ``size``
  keyword argument.
- The last keyword argument ``local`` defaults to ``True``.
  When ``local=True`` it uses javascript files that are distributed
  along with Mayavi otherwise will require an internet connection
  to use the x3dom files online.  If for some reason the installation
  of the jupyter nbextension is not working, using ``local=False``
  with an internet connection should work on a modern browser that
  supports WebGL.

The X3D data is embedded in the notebook and can be shared but if the
scenes have a lot of polygons, these files can be large.  With the PNG
backend, the PNG's are also embedded and these are smaller files.  The
PNG backend relies on offscreen rendering working correctly on your
platform.


.. _X3D: http://www.x3dom.org


.. _offscreen_rendering:

Off screen rendering
--------------------

Avoiding the rendering window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often you write Mayavi scripts to render a whole batch of images to make
an animation or so and find that each time you save an image, Mayavi
"raises" the window to make it the active window thus disrupting your
work.  This is needed since VTK internally grabs the window to make a
picture.  Occluding the window will also produce either blank or
incorrect images.

If you already have a Python script, say ``script.py`` that sets up your
visualization that you run likes so::

    $ mayavi2 -x script.py

Then it is very easy to have this script run offscreen.  Simply run it
like so::

    $ mayavi2 -x script.py -o

This will run the script in an offscreen, standalone window.  On Linux,
this works best with VTK-5.2 and above.  For more details on the command
line arguments supported by the ``mayavi2`` application, see the
:ref:`command-line-arguments` section.

When using ``mlab`` you will want to do this::

   mlab.options.offscreen = True

before you create a figure and it will use an offscreen window for the
rendering.

Another option for offscreen rendering would be to click on the scene
and set the "Off screen rendering" option on.  Or from a script::

  mayavi.engine.current_scene.scene.off_screen_rendering = True

This will stop raising the window.  However, this may not be enough.
Please see below on the situation on different platforms.

Platform Summary
~~~~~~~~~~~~~~~~~

* **Windows**: If you are using win32 then off screen rendering should work
  well out of the box.  All you will need to do is what is given above.

* **Linux and the Mac**: there are several options to get this working
  correctly and some major issues to consider:

  If you have VTK-5.2 the offscreen rendering option should let you
  generate the pictures without worrying about occluding the window.
  However, you will need VTK-5.2 to get this working properly.  There
  are also situations when this does not always work -- try it and if
  you get blank windows, you have a problem.  For example::

      from mayavi import mlab
      mlab.options.offscreen = True
      mlab.test_contour3d()
      mlab.savefig('example.png')

  If this produces a clean image (even if you switch desktops or cover
  any windows produced), you should be golden.  If not you should
  consider either using a virtual framebuffer or building VTK with Mesa
  + OSMesa to give you a pure software rendering approach.



Rendering using the virtual framebuffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VTK uses openGL for all its rendering. Under any conventional Unix
(including Linux), you need an Xserver running to open a GL context
(especially if you want hardware acceleration). This might be a problem
when rendering on a headless server. As mentioned in the above
paragraph, on a desktop, using the default server may also be a problem
as it interferes with your ongoing work.

A good workaround is to use the virtual framebuffer X server for X11 like
so:

  * Make sure you have the ``Xvfb`` package installed.  For example
    under Debian and derivatives this is called the ``xvfb`` package.

  * Create the virtual framebuffer X server like so::

      Xvfb :1 -screen 0 1280x1024x24 -auth localhost

    This creates the display ":1" and creates a screen of size 1280x1024
    with 24 bpp (the 24bpp is important).  For more options check your
    ``Xvfb`` man page.

  * Export display to :1 like so (on bash)::

      $ export DISPLAY=:1

  * Now run your Mayavi script.  It should run uninterrupted on this X
    server and produce your saved images.

This probably will have to be fine tuned to suit your taste.

If you want to do this in python. You can use `pyvirtualdisplay <https://pypi.org/project/PyVirtualDisplay/>`_ ::

   from pyvirtualdisplay import Display
   import os
   display = Display(visible=0, size=(1280, 1024))
   display.start()

Many Linux systems (including Ubuntu and Debian) ship with a helper
script `xvfb-run` for running headless. The following command can run a
Python script with Mayavi2 visualizations headless::

    xvfb-run --server-args="-screen 0 1024x768x24" python my_script.py

Beware that you shouldn't call `mlab.show` or start the mainloop in the
script, elsewhere the script will run endlessly, waiting for interaction
in a hidden window.

.. note::

    If you want to use Mayavi without the envisage UI or even a traits UI
    (i.e. with a pure TVTK window) and do off screen rendering with
    Python scripts you may be interested in the
    :ref:`example_offscreen`. This simple example shows how you can use
    Mayavi without using Envisage or the Mayavi envisage application and
    still do off screen rendering.

    If you are using mlab, outside of the Mayavi2 application, simply set::

        mlab.options.offscreen = True


Using VTK with Mesa for pure software rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you might want to run Mayavi/VTK completely headless on a
machine with no X server at all and are interested in pure offscreen
rendering (for example for usage on the Sage_ notebook interface).  In
these cases one could use Mesa's OSMesa library to render offscreen.
The downside is that you will not get any hardware acceleration in this
case.  Here are brief instructions on how to build VTK to do this.

 * Build a recent version of mesa.  7.0.4 (as of this time) should work
   as would 7.2.  We assume you download MesaLib-7.0.4.tar.bz2.

 * Untar, and change directory to the new directory created. We call
   this directory ``$MESA`` henceforth.

 * Run ``make configs/linux-x86``,  change file as per your
   configuration. Run ``make`` to see list of options.  Note: 7.2 has a
   ``./configure`` script that you can run.

 * Get VTK-5.2 or later (CVS will also work)..

 * Run ``ccmake path/to/VTK``.

   * Now select advanced options 't'.

   * Set ``VTK_OPENGL_HAS_OSMESA ON``

   * Configure: press 'c'

   * Set the ``OSMESA_INCLUDE_DIR`` to the ``$MESA/include dir``

   * Set ``OSMESA_LIBRARY`` to ``$MESA/lib/libOSMesa.so``

   * Similarly set the ``OPENGL_INCLUDE_DIR``,
     ``OPENGL_gl_LIBRARY=$MESA/lib/libGL.so``,
     ``OPENGL_glu_LIBRARY``, and ``OPENGL_xmesa_INCLUDE_DIR``.

   * Set ``VTK_USE_OFFSCREEN`` to ``ON`` if you want offscreen all the
     time, this will never produce an actual mapped VTK window since the
     default value of the render window's offscreen rendering ivar will
     be set to True in this case.

   * Any other settings like ``VTK_USE_GL2PS, USE_RPATH`` etc.

   * Configure again (press 'c') and then generate 'g'.


   * Note that if you do not want to use ``ccmake`` and would like to do
     this from the command line you may also do (for example)::

        cmake \
        -DVTK_OPENGL_HAS_OSMESA=ON \
        -DVTK_USE_OFFSCREEN=ON \
        -DCMAKE_INSTALL_PREFIX=/path/to/vtk-offscreen \
        -DVTK_WRAP_PYTHON=ON \
        -DPYTHON_EXECUTABLE=/usr/bin/python2.5 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.5.so \
        -DBUILD_SHARED_LIBS=ON \
        -DVTK_USE_GL2PS=ON \
        -DOSMESA_INCLUDE_DIR=/path/to/Mesa-7.2/include/ \
        -DOSMESA_LIBRARY=/home/path/to/Mesa-7.2/lib64/libOSMesa.so \
        -DOPENGL_INCLUDE_DIR=/path/to/Mesa-7.2/include \
        -DOPENGL_gl_LIBRARY=/path/to/Mesa-7.2/lib64/libGL.so \
        -DOPENGL_glu_LIBRARY=/path/to/Mesa-7.2/lib64/libGLU.so \
        path/to/VTK/

 * Run ``make`` and wait till VTK has built.  Let us say the build is in
   ``$VTK_BUILD``.

 * Now install VTK or set the ``PYTHONPATH`` and ``LD_LIBRARY_PATH``
   suitably.  Also ensure that ``LD_LIBRARY_PATH`` points to
   ``$MESA/lib`` (if the mesa libs are not installed on the system) this
   ensures that VTK links to the right GL libs.  For example::

        $ export PYTHONPATH=$VTK_BUILD/bin:$VTK_BUILD/Wrapping/Python``
        $ export LD_LIBRARY_PATH=$VTK_BUILD/bin:$MESA/lib

   Now, you should be all set.

Once this is done you should be able to run mlab examples offscreen.
This will work without an X display even.

With such a VTK built and running, one could simply build and install
mayavi2.  To use it in a Sage notebook for example you'd want to set
``ETS_TOOLKIT='null'`` and set ``mlab.options.offscreen = True``.  Thats
it.  Everything should now work offscreen.

Note that if you set ``VTK_USE_OFFSCREEN`` to ``ON`` then you'll by
default only get offscreen contexts.  If you do want a UI you will want
to explicitly set the render window's ``off_screen_rendering`` ivar to
``False`` to force a mapped window.  For this reason if you might need
to popup a full UI, it might be better to *not set*
``VTK_USE_OFFSCREEN=ON``.



.. _Sage: http://www.sagemath.org



Extending Mayavi with customizations
-------------------------------------

A developer may wish to customize Mayavi by adding new sources, filters
or modules.  These can be done by writing the respective filters and
exposing them via a ``user_mayavi.py`` or a ``site_mayavi.py`` as
described in `Customizing Mayavi2`_.   A more flexible and
reusable mechanism for doing this is to create a full fledged Mayavi
contrib package in the following manner.

  1. Create a Python package, let's call it ``mv_iitb`` (for IIT Bombay
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
     sources/filters/modules etc. to Mayavi.  The other part of the
     structure is really up to the developer.  At the moment these
     packages can add new sources, filters, modules and contribute any
     Envisage plugins that the ``mayavi2`` application will load.

  2. This package should then be installed somewhere on ``sys.path``.
     Once this is done, users can find these packages and enable them
     from the Tools->Preferences (the UI will automatically detect the
     package).  The ``user_mayavi.py`` of each selected package will
     then be imported next time Mayavi is started, note that this will
     be usable even from ``mlab``.

Any number of such packages may be created and distributed.  If they are
installed, users can choose to enable them.  Internally, the list of
selected packages is stored as the ``mayavi.contrib_packages``
preference option.  The following code shows how this may be accessed
from a Python script::

   >>> from mayavi.preferences.api import preference_manager
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


.. _`examples/mayavi/user_mayavi.py`: https://raw.githubusercontent.com/enthought/mayavi/4.4.4/examples/mayavi/user_mayavi.py


Customizing Mayavi2
--------------------

There are three ways a user can customize Mayavi:

  1. Via Mayavi contributions installed on the system.  This may be done
     by enabling any found contributions from the Tools->Preferences
     menu on the Mayavi component, look for the "contribution settings".
     Any selected contributions will be imported the next time Mayavi
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

  1. Registering new sources, modules or filters in the Mayavi registry
     (``mayavi.core.registry.registry``).  This is done by
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

 In the ``user_mayavi.py`` or ``site_mayavi.py``, avoid Mayavi imports
 like  ``from mayavi.modules.outline import Outline`` etc.
 This is because ``user_mayavi`` is imported at a time when many of the
 imports are not complete and this will cause hard-to-debug circular
 import problems.  The ``registry`` is given only metadata mostly in the
 form of strings and this will cause no problem.  Therefore to define
 new modules, we strongly recommend that the modules be defined in
 another module or be defined in a factory function as done in the
 example ``user_mayavi.py`` provided.


Scripting Mayavi without using Envisage
----------------------------------------

The :ref:`example_standalone` demonstrates how one can use the core
Mayavi API without using Envisage.  This is useful when you want to
minimize dependencies.  :ref:`example_offscreen` demonstrates how to use
Mayavi without the envisage UI or even a traits UI (i.e. with a pure TVTK
window) and do off screen rendering.

Computing in a thread
----------------------

:ref:`example_compute_in_thread` demonstrates how to visualize a 2D
numpy array and visualize it as image data using a few modules.  It also
shows how one can do a computation in another thread and update the
Mayavi pipeline once the computation is done.  This allows a user to
interact with  the user interface when the computation is performed in
another thread.


Polling a file and auto-updating Mayavi
----------------------------------------

Sometimes you have a separate computational process that generates data
suitable for visualization.  You'd like Mayavi to visualize the data but
automatically update the data when the data file is updated by the
computation.  This is easily achieved by polling the data file and
checking if it has been modified.  The :ref:`example_poll_file`
demonstrates this.  To see it in action will require that you edit the
scalar data in the ``examples/data/heart.vtk`` data file.


Serving Mayavi on the network
-------------------------------

.. currentmodule:: mayavi.tools.server

Say you have a little visualization script and you'd like to run some
kind of server where you can script the running Mayavi UI from a TCP/UDP
connection.  It turns out there is a simple way to do this  if you have
Twisted_ installed.  Here is a trivial example::

    from mayavi import mlab
    from mayavi.tools import server
    mlab.test_plot3d()
    server.serve_tcp()

There is no need to call ``mlab.show()`` in the above.  The TCP server
will listen on port 8007 by default in the above (this can be changed
with suitable arguments to :func:`serve_tcp`).  Any data sent to the server
is simply exec'd, meaning you can do pretty much anything you want.  The
names ``engine``, ``scene``, ``camera`` and ``mlab`` are all available
and can be scripted with Python code.  For example after running the
above you can do this::

    $ telnet localhost 8007
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    scene.camera.azimuth(45)
    mlab.clf()
    mlab.test_contour3d()
    scene.camera.zoom(1.5)

The nice thing about this is that you do not loose any interactivity of
the application and can continue to use its UI as before, any network
commands will be simply run on top of this.  To serve on a UDP port use
the :func:`serve_udp` function.  For more details on the ``server`` module
please look at the source code -- it is thoroughly documented.

.. warning::
    While this is very powerful it is also a huge security hole
    since the remote user can do pretty much anything they want once
    connected to the server.


.. _Twisted: http://www.twistedmatrix.com

TCP server: the `serve_tcp` function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: serve_tcp

..
 _____

 .. autoclass:: M2TCP
    :members:


UDP server: the `serve_udp` function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: serve_udp

..
 _____

 .. autoclass:: M2UDP
    :members:


.. _animating_a_timeseries:

Animating a timeseries
-----------------------

If a file that mayavi can load has the form ``some_name[0-9]*.ext``,
then it is treated as part of a timeseries.  For example let us say
you have the following files:

.. code-block:: bash

  $ ls
  data_01.vti data_02.vti ... data_10.vti

If one loads the file using Mayavi, a slider will show up on the file
reader object which can be used to choose an appropriate timestep.
There are also buttons to automatically change the timestep. To do
this, select the play checkbox.  This can also be done
programmatically as follows::

   from mayavi import mlab
   src = mlab.pipeline.open('data_01.vti')
   src.play = True

Selecting the "loop" checkbox will loop over the files continuously.
If you have multiple files that are part of a timeseries, you can
choose the "sync timestep" option.  This will sync all the timesteps
of the other files that have the same number of timesteps as the
current reader. The "Rescan files" button will rescan the files on the
disc to find newer ones that are part of the timeseries.


.. _animating_a_visualization:

Animating a visualization
--------------------------

.. currentmodule:: mayavi.mlab

Often users like to animate visualization without affecting the
interactive capabilities of the view.  For example you may want to
rotate the camera continuously, take a snapshot while continuing to
interact with the Mayavi UI.  To do this one can use the very convenient
:func:`animate` decorator provided with Mayavi.  Here is a simple
example::

    from mayavi import mlab
    @mlab.animate
    def anim():
        f = mlab.gcf()
        while 1:
            f.scene.camera.azimuth(10)
            f.scene.render()
            yield

    a = anim() # Starts the animation.

Notice the use of ``yield`` in the above, this is *very* crucial to this
working.  This example will continuously rotate the camera without
affecting the UI's interactivity.  It also pops up a little UI that lets
you start and stop the animation and change the time interval between
calls to your function.  For more specialized use you can pass arguments
to the decorator::

    from mayavi import mlab
    @mlab.animate(delay=500, ui=False)
    def anim():
        # ...

    a = anim() # Starts the animation without a UI.

If you don't want to import all of ``mlab``, the animate
decorator is available from::

    from mayavi.tools.animator import animate

Note that to start the event loop, *i.e.* to get the animation running,
you will need to call :func:`show` if you do not already have a GUI
environment running.

Here is another example illustrating the use of the decorator::

    import numpy as np
    from mayavi import mlab

    @mlab.animate(delay = 100)
    def updateAnimation():
        t = 0.0
        while True:
            ball.mlab_source.set(x = np.cos(t), y = np.sin(t), z = 0)
            t += 0.1
            yield

    ball = mlab.points3d(np.array(1.), np.array(0.), np.array(0.))

    updateAnimation()
    mlab.show()

For more details check the documentation of the :func:`animate` decorator
available in the :ref:`mlab-reference`. For an example using it,
alongside with the `visual` handy for object-movement animation, see
:ref:`example_mlab_visual`.

.. note::

    If you want to change the data of an object in an animation, see
    :ref:`mlab-animating-data`


Creating a movie from an animation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is easy to create a movie from either an animation or by playing a
timeseries.  To do this on the UI, select the Mayavi Scene and
navigate to the Movie tab and select the record checkbox.  After this,
if one animates a timestep via the "play" checkbox referred to in
:ref:`animating_a_timeseries`, then a stack of images will be created
in the directory specified in the movie UI.  This will also happen if
one runs an animation as discussed in :ref:`animating_a_visualization`.

This can also be scripted with mlab for example as follows::

   from mayavi import mlab
   f = mlab.figure()
   f.scene.movie_maker.record = True
   mlab.test_mesh_sphere_anim()

This will create a set of images, one for each step of the animation.
The ``movie_maker`` instance is available on each created scene.


Animating a series of images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you have a stack of PNG or JPEG files that are numbered
serially that you want to animate on a Mayavi scene.  Here is a simple
script (called ``img_movie.py``)::

    # img_movie.py
    from pyface.timer.api import Timer

    def animate(src, N=10):
        for j in range(N):
            for i in range(len(src.file_list)):
                src.timestep = i
                yield

    if __name__ == '__main__':
        src = mayavi.engine.scenes[0].children[0]
        animator = animate(src)
        t = Timer(250, animator.next)

The ``Timer`` class lets you call a function without blocking the
running user interface.  The first argument is the time after which the
function is to be called again in milliseconds.  The ``animate``
function is a generator and changes the timestep of the source.  This
script will animate the stack of images 10 times.  The script animates
the first data source by default.  This may be changed easily.

To use this script do this::

    $ mayavi2 -d your_image000.png -m ImageActor -x img_movie.py


Making movies from a stack of images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This isn't really related to Mayavi but is a useful trick nonetheless.
Let's say you generate a stack of images using Mayavi say of the form
``anim%03d.png`` (i.e. ``anim000.png``, ``anim001.png`` and so on), you
can make this into a movie.  If you have ``mencoder`` installed try
this::

  $ mencoder "mf://anim%03d.png" -mf fps=10 -o anim.avi \
    -ovc lavc -lavcopts vcodec=msmpeg4v2:vbitrate=500

If you have ffmpeg installed you may try this::

  $ ffmpeg -f image2 -r 10 -i anim%03d.png -sameq anim.mov -pass 2

.. _mencoder: http://www.mplayerhq.hu/
.. _ffmpeg: http://ffmpeg.mplayerhq.hu/


Scripting from the command line
--------------------------------

The Mayavi application allows for very powerful
:ref:`command-line-arguments` that lets you build a complex
visualization from your shell.  What follow is a bunch of simple
examples illustrating these.

The following example creates a ``ParametricSurface`` source and then
visualizes glyphs on its surface colored red::

    $ mayavi2 -d ParametricSurface -m Glyph \
    -s"glyph.glyph.scale_factor=0.1" \
    -s"glyph.color_mode='no_coloring'" \
    -s"actor.property.color = (1,0,0)"

Note that ``-s"string"`` applies the string on the last object (also
available as ``last_obj``), which is the glyph.

This example turns off coloring of the glyph and changes the glyph to
display::

    $ mayavi2 -d ParametricSurface -m Glyph\
    -s"glyph.glyph.scale_factor=0.1" \
    -s"glyph.color_mode='no_coloring'" \
    -s"glyph.glyph_source.glyph_source = last_obj.glyph.glyph_source.glyph_list[-1]"

Note the use of ``last_obj`` in the above.


Texture mapping actors
-----------------------

Here is a simple example showing how to texture map an iso-surface with
the data that ships with the Mayavi sources (the data files are in the
examples directory)::

    $ mayavi2 -d examples/tvtk/images/masonry.jpg \
     -d examples/mayavi/data/heart.vti \
     -m IsoSurface \
     -s"actor.mapper.scalar_visibility=False" \
     -s"actor.enable_texture=True"\
     -s"actor.tcoord_generator_mode='cylinder'"\
     -s"actor.texture_source_object=script.engine.current_scene.children[0]"

It should be relatively straightforward to change this example to use a
``ParametricSurface`` instead and any other image of your choice.
Notice how the texture image (``masonry.jpg``) is set in the last line
of the above.  The image reader is the first child of the current scene
and we set it as the ``texture_source_object`` of the isosurface actor.


Shifting data and plotting
---------------------------

Sometimes you need to shift/transform your input data in space and
visualize that in addition to the original data.  This is useful when
you'd like to do different things to the same data and see them on the
same plot.  This can be done with Mayavi using the ``TransformData`` filter
for ``StructuredGrid``, ``PolyData`` and ``UnstructuredGrid`` datasets.
Here is an example using the ``ParametricSurface`` data source::

   $ mayavi2 -d ParametricSurface \
     -m Outline -m Surface \
     -f TransformData -s "transform.translate(1,1,1)" \
     -s "widget.set_transform(last_obj.transform)" \
     -m Outline -m Surface

If you have an ``ImageData`` dataset then you can change the origin,
spacing and extents alone by using the ``ImageChangeInformation``
filter.  Here is a simple example with the standard Mayavi image data::

    $ mayavi2 -d examples/mayavi/data/heart.vti -m Outline \
    -m ImagePlaneWidget \
    -f ImageChangeInformation \
    -s "filter.origin_translation=(20,20,20)" \
    -m Outline -m ImagePlaneWidget

.. _using_userdefined_filter:

Using the ``UserDefined`` filter
---------------------------------

The ``UserDefined`` filter in Mayavi lets you wrap around existing VTK
filters easily.  Here are a few examples::

    $ mayavi2 -d ParametricSurface -s "function='dini'" \
    -f UserDefined:GeometryFilter \
    -s "filter.extent_clipping=True" \
    -s "filter.extent = [-1,1,-1,1,0,5]" \
    -f UserDefined:CleanPolyData \
    -m Surface \
    -s "actor.property.representation = 'p'" \
    -s "actor.property.point_size=2"

This one uses a ``tvtk.GeometryFilter`` to perform extent based clipping of
the parametric surface generated.  Note the specification of the ``-f
UserDefined:GeometryFilter``.  This data is then cleaned using the
``tvtk.CleanPolyData`` filter.

Under :ref:`mlab <simple-scripting-with-mlab>`, the `Userdefined` can be
used to wrap eg a `GeometryFilter` VTK filter with::

    filtered_obj = mlab.pipeline.user_defined(obj, filter='GeometryFilter')

With :ref:`mlab <simple-scripting-with-mlab>`, the `user_defined`
function can either take as a filter argument the name of the VTK filter
to be used, or an already-instanciated instance of the filter.

.. note::

    With the `UserDefined` filter, as with most Mayavi filter, the raw
    TVTK object can be accessed as the `filter` attribute of the Mayavi
    filter object.

The :ref:`example_image_cursor_filter` gives a full example of using the
UserDefined filter. The :ref:`example_tvtk_segmentation` is a full
example of building a complex VTK pipeline with a heavy use of the
UserDefined filter.

.. _sharing_data_between_scenes:

Sharing the same data between scenes
-------------------------------------

If you want to display different views of the same data on different, you
will have to create different Mayavi data sources, as a data source can
belong on to one scene. However, this does not mean that you need to copy
the data, or recreate the source from scratch. The trick is to create a
second Mayavi data source pointing to the same underlying VTK dataset,
and attach it to another scene (see :ref:`data-structures-used-by-mayavi`
for the difference between a Mayavi source and a VTK dataset).

Using mlab
~~~~~~~~~~~~

Every visualization object returned by :ref:`mlab
<simple-scripting-with-mlab>` has a `mlab_source` attribute, which
exposes the VTK dataset as `dataset`. In addition, the :ref:`mlab
pipeline <controlling-the-pipeline-with-mlab-scripts>` functions for
adding modules know how to use raw VTK datasets. Thus exposing the
dataset in a new figure can simply by done by feeding the
`mlab_source.dataset` attribute of a visualization object created by mlab
to an `mlab.pipeline` function::

    from mayavi import mlab
    ctr = mlab.test_contour3d()
    mlab.figure()
    ipw = mlab.pipeline.image_plane_widget(ctr.mlab_source.dataset)
    mlab.show()

The above example creates two figures displaying the same data, one with
iso-surfaces, and the other with an image plane widget.

Alternatively, it can be useful to be explicit about the figure that the
new module is added onto, rather than using the `mlab` current figure.
This is important to make the code easier to read in situations where the
current figure is not clear, for instance in an interactive application,
rather than a script::

    new_fig = mlab.figure()
    ipw = mlab.pipeline.image_plane_widget(ctr.mlab_source.dataset, figure=new_fig)

The :ref:`example_volume_slicer` shows a complex dialog exposing the same
data through different views via `mlab.pipeline`.

Using the core Mayavi API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also do this fully explicitly by creating the objects yourself
through the Mayavi core api, and adding them to the pipeline, rather than
using factories::

    import numpy as np
    a = np.random.random((3, 3, 3))
    from mayavi.sources.api import ArraySource, VTKDataSource
    src1 = ArraySource(scalar_data=a)
    engine.add_source(src1)
    engine.new_scene()
    scene2 = engine.current_scene

    # Now create a second data source viewing the same data:
    src2 = VTKDataSource(data=src1.image_data)
    scene2.add_child(src2)

Changing the interaction with a scene
--------------------------------------

The default 3D interaction with the scene (left click on the background
rotates the scene, right click scales, middle click pans) is not suited
for every visualization. For instance, in can be interesting to restrict
the movement to 2D, e.g. when viewing an object in the 'x' direction.
This is done by changing the `interactor_style` of a scene. Here is an
example to use Mayavi as a 2D image viewer::

    from mayavi import mlab
    mlab.test_imshow()
    mlab.view(0, 0)
    fig = mlab.gcf()
    from tvtk.api import tvtk
    fig.scene.interactor.interactor_style = tvtk.InteractorStyleImage()
    mlab.show()

Another useful interactor is the 'terrain' interactor, handy to have
natural movement in scenes where you want the 'up' vector to be always
pointing in the 'z' direction::

    from mayavi import mlab
    mlab.test_surf()
    fig = mlab.gcf()
    from tvtk.api import tvtk
    fig.scene.interactor.interactor_style = tvtk.InteractorStyleTerrain()
    mlab.show()

VTK has many different interactors. An easy way to list them is to
display the VTK class browser (via the help menu, in the `mayavi2`
application) and to search for "Interactor". Another option is to tab
complete on Ipython, on `tvtk.InteractorStyle`.


.. _acceleration_mayavi_scripts:

Accelerating a Mayavi script
------------------------------

You've just created a nice Mayavi/mlab script and now want to generate
an animation or a series of images.  You realize that it is way too slow
rendering the images and takes ages to finish.  There are two simple
ways to speed up the rendering.  Let's assume that ``obj`` is any Mayavi
pipeline object that has a ``scene`` attribute::

    obj.scene.disable_render = True
    # Do all your scripting that takes ages.
    # ...
    # Once done, do the following:
    obj.scene.disable_render = False

This will speed things up for complex visualizations sometimes by an
order of magnitude.

While saving the visualization to an image you can speed up the image
generation at the cost of loosing out on anti-aliasing by doing the
following::

    obj.scene.anti_aliasing_frames = 0

The default value is typically 8 and the rendered image will be nicely
anti-aliased.  Setting it to zero will not produce too much difference
in the rendered image but any smooth lines will now appear slightly
jagged. However, the rendering will be much faster.  So if this is
acceptable (try it) this is a mechanism to speed up the generation of
images.



..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
