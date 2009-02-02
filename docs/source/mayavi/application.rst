.. _using-the-mayavi-application:

Using the Mayavi application
=============================

.. topic:: Section summary


    This section primarily concerns using the ``mayavi2`` application.
    Some of the things mentioned here also apply when mayavi is scripted.
    We recommend that new users read this chapter to get a better
    knowledge of the interactive use of the library.

.. _general-layout-of-ui:

General layout of UI
--------------------

When the `mayavi2` application is started it will provide a user
interface that looks something like the figure shown below.

.. image:: images/mayavi_ui_first.png
   :alt: Figure of Mayavi's initial UI window.

*Figure of Mayavi's initial UI window.*


The UI features several sections described below.

  Menus
    The menus let you open files, load modules, set preferences etc.

  The Mayavi engine tree view
    This is a tree view of the mayavi pipeline.
      * Right click a tree node to rename, delete, copy the objects.

      * Left click on a node to edit its properties on the object
        editor below the tree.

      * It is possible to drag the nodes around on the tree.  For
        example it is possible to drag and move a module from one set
        of Modules to another, or to move a visualization from one
        scene to another.

  The object editor 
    This is where the properties of mayavi pipeline objects can be
    changed when an object on the engine's pipeline is clicked.

  TVTK scenes
    This is where the visualization of the data happens.  One can
    interact with this scene via the mouse and the keyboard.  More
    details are in the following sections.

  Python interpreter
    The built-in Python interpreter that can be used to script mayavi
    and do other things.  You can drag nodes from the mayavi tree and
    drop them on the interpreter and then script the object represented
    by the node!

  Logger
    Application log messages may be seen here.


Mayavi's UI layout is highly configurable:

 * the line in-between the sections can be dragged to resize
   particular views.

 * most of the "tabs" on the widgets can be dragged around to move
   them anywhere in the application.

 * Each view area (the mayavi engine view, object editor, python shell
   and logger) can be enabled and disabled in the 'View' menu.

Each time you change the appearance of mayavi it is saved and the next
time you start up the application it will have the same configuration.
In addition, you can save different layouts into different
"perspectives" using the `View->Perspectives` menu item.

Shown below is a specifically configured mayavi user interface view.
In this view the size of the various parts are changed.  The Python
shell is activated by default.

.. image:: images/mayavi_ui_second.png
   :alt: Figure of Mayavi's UI after being configured by a user.

*Figure of Mayavi's UI after being configured by a user.*


Visualizing data
----------------

Visualization data in Mayavi is performed by loading some data as `data
sources`, and applying visualization modules to these sources to
visualize the data as described in the :ref:`an-overview-of-mayavi`
section and the :ref:`learning-mayavi-by-example` section.  

One needs to have some data or the other loaded before a `Module` or
`Filter` may be used.  Mayavi supports several data file formats most
notably VTK data file formats. Alternatively, :ref:`mlab
<simple-scripting-with-mlab>` can be used to load data from `numpy`
arrays. For advanced information on data structures, refer to the
:ref:`data-structures-used-by-mayavi` section.

Once data is loaded one can optionally use a variety of :ref:`filters` to
filter or modify the data in some way or the other and then visualize
the data using several :ref:`modules`. 

Here we list all the Mayavi `modules` and `filters`. This list is useful
as a reference:

.. toctree::

    modules.rst
    filters.rst


.. _interaction-with-the-scene:

Interaction with the scene
--------------------------

The TVTK scenes on the UI can be closed by clicking on the little 'x'
icon on the tab.  Each scene features a toolbar that supports various
features:

  * Buttons to set the view to view along the positive or negative X,
    Y and Z axes or obtain an isometric view.

  * A button to turn on parallel projection instead of the default
    perspective projection.  This is particularly useful when one is
    looking at 2D plots.

  * A button to turn on an axes to indicate the x, y and z axes.

  * A button to turn on full-screen viewing.  Note that once
    full-screen mode is entered one must press 'q' or 'e' to get back
    a normal window.

  * A button to save the scene to a variety of image formats.  The
    image format to use is determined by the extension provided for
    the file.

  * A button that provides a UI to configure the scene properties.

The primary means to interact with the scene is to use the mouse and
keyboard.


Mouse interaction
~~~~~~~~~~~~~~~~~

There are two modes of mouse interaction:

  * Camera mode: the default, where the camera is operated on with
    mouse moves.  This mode is activated by pressing the 'c' key.

  * Actor mode: in this mode the mouse actions operate on the actor
    the mouse is currently above.  This mode is activated by pressing
    the 'a' key.

The view on the scene can be changed by using various mouse actions.
Usually these are accomplished by holding down a mouse button and
dragging.

  * holding the left mouse button down and dragging will rotate the
    camera/actor in the direction moved.

        - Holding down "SHIFT" when doing this will pan the scene --
          just like the middle button.

        - Holding down "CONTROL" will rotate about the camera's focal
          point.

        - Holding down "SHIFT" and "CONTROL" and dragging up will zoom
          in and dragging down will zoom out.  This is like the right
          button.

  * holding the right mouse button down and dragging upwards will zoom
    in (or increase the actors scale) and dragging downwards will zoom
    out (or reduce scale).

  * holding the middle mouse button down and dragging will pan the
    scene or translate the object.

  * Rotating the mouse wheel upwards will zoom in and downwards will
    zoom out.


Keyboard interaction
~~~~~~~~~~~~~~~~~~~~

The scene supports several features activated via keystrokes.  These
are:
 
 * '3': Turn on/off stereo rendering.  This may not work if the
   'stereo' preference item is not set to True.

 * 'a': Use actor mode for mouse interaction instead of camera mode.

 * 'c': Use camera mode for mouse interaction instead of actor mode.

 * 'e'/'q'/'Esc': Exit full-screen mode.

 * 'f': Move camera's focal point to current mouse location.  This
   will move the camera focus to center the view at the current mouse
   position.

 * 'j': Use joystick mode for the mouse interaction.  In joystick mode
   the mouse somewhat mimics a joystick.  For example, holding the
   mouse left button down when away from the center will rotate the
   scene.

 * 'l': Configure the lights that are illumining the scene.  This will
   pop-up a window to change the light configuration.

 * 'p': Pick the data at the current mouse point.  This will pop-up a
   window with information on the current pick.  The UI will also
   allow one to change the behavior of the picker to pick cells,
   points or arbitrary points.

 * 'r': Reset the camera focal point and position.  This is very handy.

 * 's': Save the scene to an image, this will first popup a file
   selection dialog box so you can choose the filename, the extension of
   the filename determines the image type.

 * 't': Use trackball mode for the mouse interaction.  This is the
   default mode for the mouse interaction.

 * '='/'+': Zoom in.

 * '-': Zoom out.

 * 'left'/'right'/'up'/'down' arrows: Pressing the left, right, up and
   down arrow let you rotate the camera in those directions.  When
   "SHIFT" modifier is also held down the camera is panned.

.. _the-embedded-python-interpreter:

The embedded Python interpreter
-------------------------------

The embedded Python interpreter offers extremely powerful
possibilities.  The interpreter features command completion, automatic
documentation, tooltips and some multi-line editing.  In addition it
supports the following features:

 * The name ``mayavi`` is automatically bound to the
   ``enthought.mayavi.script.Script`` instance.  This may be used to
   easily script mayavi.

 * The name ``application`` is bound to the envisage application.

 * If a Python file is opened via the ``File->Open File...`` menu item
   one can edit it with a color syntax capable editor.  To execute
   this script in the embedded Python interpreter, the user may type
   ``Control-r`` on the editor window.  To save the file press
   ``Control-s``.  This is a very handy feature when developing simple
   mayavi scripts. You can also increase and decrease the font size using
   ``Control-n`` and ``Control-s``.

 * As mentioned earlier, one may drag and drop nodes from the Mayavi
   engine tree view onto the Python shell.  The object may then be
   scripted as one normally would.  A commonly used pattern when this
   is done is the following::

     >>> tvtk_scene_1
     <enthought.mayavi.core.scene.Scene object at 0x9f4cbe3c>
     >>> s = _

   In this case the name ``s`` is bound to the dropped tvtk_scene
   object.  The ``_`` variable stores the last evaluated expression
   which is the dropped object.  Using ``tvtk_scene_1`` will also work
   but is a mouthful.

.. _command-line-arguments:

Command line arguments
----------------------

The ``mayavi2`` application features several useful command line
arguments that are described in the following section.  These options
are described in the ``mayavi2`` man page as well.

Mayavi can be run like so::

       mayavi2 [options] [args]

Where ``arg1``, ``arg2`` etc.  are optional file names that correspond
to saved Mayavi2 visualizations (``filename.mv2``),  Mayavi2 scripts
(``filename.py``) or any datafile supported by Mayavi.  If no options or
arguments are provided mayavi will start up with a default blank scene.

The options are:

-h
      This prints all the available command line options and exits.
      Also available through ``--help``.

-V
      This prints the Mayavi version on the command line and exits.
      Also available through ``--version``.

-z file_name
      This loads a previously saved Mayavi2 visualization.  Also
      available through ``--viz file_name`` or ``--visualization
      file_name``.

-d data_file
      Opens any of the supported data file formats or non-file
      associated data source objects.  This includes VTK file formats
      (*.vtk, *.xml, *.vt[i,p,r,s,u], *.pvt[i,p,r,s,u]), VRML2 (*.wrl),
      3D Studio (*.3ds), PLOT3D (*.xyz) and various others that are
      supported.

      ``data_file`` can also be a source object not associated with a file,
      for example ``ParametricSurface`` or ``PointLoad`` will load the
      corresponding data sources into Mayavi.  Also available through
      ``--data``.

-m module-name
      A module is an object that actually visualizes the data.  The
      given ``module-name`` is loaded in the current ``ModuleManager``.
      The module name must be a valid one if not you will get an error
      message.

      If a module is specified as ``package.sub.module.SomeModule``
      then the module (``SomeModule``) is imported from
      ``package.sub.module``.  Standard modules provided with
      ``mayavi2`` do not need the full path specification.  For
      example::

         mayavi2 -d data.vtk -m Outline -m user_modules.AModule

      In this example ``Outline`` is a standard module and
      ``user_modules.AModule`` is some user defined module.
      Also available through ``--module``.

-f filter-name
      A filter is an object that filters out the data in some way or
      the other.  The given ``filter-name`` is loaded with respect to
      the current source/filter object.  The filter name must be a
      valid one if not you will get an error message.

      If the filter is specified as ``package.sub.filter.SomeFilter``
      then the filter (``SomeFilter``) is imported from
      ``package.sub.filter``.  Standard modules provided with
      ``mayavi2`` do not need the full path specification.  For
      example::

         mayavi2 -d data.vtk -f ExtractVectorNorm -f user_filters.AFilter

      In this example ``ExtractVectorNorm`` is a standard filter and
      ``user_filters.AFilter`` is some user defined filter.
      Also available through ``--filter``.

-M
      Starts up a new module manager on the Mayavi pipeline. Also
      available through ``--module-mgr``.

-n
      Creates a new window/scene. Any options passed after this will
      apply to this newly created scene.  Also available through
      ``--new-window``.

-o
      Run Mayavi in offscreen mode without any graphical user interface.
      This is most useful for scripts that need to render images
      offscreen (for an animation say) in the background without an
      intrusive user interface popping up.  Mayavi scripts (run via the
      ``-x`` argument) should typically work fine in this mode.  Also
      available through, ``--offscreen``.

-x script-file
      This executes the given script in a namespace where we guarantee
      that the name 'mayavi' is Mayavi's script instance -- just like
      in the embedded Python interpreter.  Also available through
      ``--exec``.

-s python-expression
      Execute the python-expression on the last created object.  For
      example, lets say the previous object was a module.  If you want
      to set the color of that object and save the scene, you may do::

       $ mayavi2 [...] -m Outline -s"actor.property.color = (1,0,0)" \
        -s "scene.save('test.png', size=(800, 800))"

      You should use quotes for the expression.  This is also available
      through ``--set``.

.. warning::
 Note that ``-x`` or ``--exec`` uses `execfile`, so this can be
 dangerous if the script does something nasty!  Similarly, ``-s`` or
 ``--set`` uses `exec`, which can also be dangerous if abused.

It is important to note that mayavi's **command line arguments are
processed sequentially** in the same order they are given.  This
allows users to do interesting things.

Here are a few examples of the command line arguments::

  $ mayavi2 -d ParametricSurface -s "function='dini'" -m Surface \
    -s "module_manager.scalar_lut_manager.show_scalar_bar = True" \
    -s "scene.isometric_view()" -s "scene.save('snapshot.png')"

  $ mayavi2 -d heart.vtk -m Axes -m Outline -m GridPlane \
    -m ContourGridPlane -m IsoSurface

  $ mayavi2 -d fire_ug.vtu -m Axes -m Outline -m VectorCutPlane \
    -f MaskPoints -m Glyph

In the above examples, ``heart.vtk`` and ``fire_ug.vtu`` VTK files can
be found in the ``examples/data`` directory in the source.  They may
also be installed on your computer depending on your particular
platform.



..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

