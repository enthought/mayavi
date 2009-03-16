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


Avoiding the rendering window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often you write Mayavi scripts to render a whole batch of images to make
an animation or so and find that each time you save an image, Mayavi
"raises" the window to make it the active window thus disrupting your
work.  This is needed since VTK internally grabs the window to make a
picture.  Occluding the window will also produce either blank or
incorrect images. 

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

      from enthought.mayavi import mlab
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

  * Now run your mayavi script.  It should run uninterrupted on this X
    server and produce your saved images.
  
This probably will have to be fine tuned to suit your taste.

Many Linux systems (including Ubuntu and Debian) ship with a helper
script `xvfb-run` for running headless. The following command can run a
Python script with Mayavi2 visualizations headless::

    xvfb-run --server-args="-screen 0 1024x768x24" python my_script.py

Beware that you shouldn't call `mlab.show` or start the mainloop in the
script, elsewhere the script will run endlessly, waiting for interaction
in a hidden window.

.. note:: 

    If you want to use mayavi without the envisage UI or even a traits
    UI (i.e. with a pure TVTK window) and do off screen rendering with
    Python scripts you may be interested in the
    ``examples/offscreen.py`` or the ``examples/offscreen_mlab.py``
    example.  This simple example shows how you can use Mayavi without
    using Envisage or the Mayavi envisage application and still do off
    screen rendering.


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


Using ``mlab`` with the full Envisage UI
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


Serving mayavi on the network
-------------------------------

.. currentmodule:: enthought.mayavi.tools.server

Say you have a little visualization script and you'd like to run some
kind of server where you can script the running mayavi UI from a TCP/UDP
connection.  It turns out there is a simple way to do this  if you have
Twisted_ installed.  Here is a trivial example::

    from enthought.mayavi import mlab
    from enthought.mayavi.tools import server
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


Common problems
----------------

:Display bugs:
    Mayavi, and VTK, uses heavily hardware rendering, as a result it is
    very sensitive on hardware rendering bugs. Common issues include
    surfaces showing up as black instead of colored (mostly on windows or
    in virtual machines, I believe), z-ordering bugs where hidden triangles 
    are displayed in front of the triangles that should hide them (a
    common bug on Linux with intel graphics cards), or the rendering
    windows becomming grey when the focus is moved out (often seen on
    Linux, when compiz is enabled). The solution is most often simply to
    turn off hardware rendering in the system settings (turn off compiz
    under Linux) or change graphics-card drivers (under Linux, try
    switching between the open source one, and the proprietary one).

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

