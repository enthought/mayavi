

.. currentmodule:: mayavi.mlab

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Other functions
===============

animate
~~~~~~~

.. function:: animate(func=None, delay=500, ui=True, support_movie=True)

    
    ::
    A convenient decorator to animate a generator performing an animation.
    
        The `delay` parameter specifies the delay (in milliseconds) between calls
        to the decorated function. If `ui` is True, then a simple UI for the
        animator is also popped up.  The decorated function will return the
        `Animator` instance used and a user may call its `Stop` method to stop the
        animation.  The `support_movie` parameter is True by default and this
        makes it easy to record a movie with the decorator.  If this is turned
        off, one cannot record a movie of the animation.
    
        If an ordinary function is decorated a `TypeError` will be raised.
    
        **Parameters**
    
        :delay: int specifying the time interval in milliseconds between
                calls to the function.
    
        :ui: bool specifying if a UI controlling the animation is to be
             provided.
    
        :support_movie: bool specifying if the animation will support
                        recording of a movie.
    
        **Returns**
    
        The decorated function returns an `Animator` instance.
    
        **Examples**
    
        Here is the example provided in the Animator class documentation::
    
            >>> from mayavi import mlab
            >>> @mlab.animate
            ... def anim():
            ...     f = mlab.gcf()
            ...     while 1:
            ...         f.scene.camera.azimuth(10)
            ...         f.scene.render()
            ...         yield
            ...
            >>> a = anim() # Starts the animation.
    
        For more specialized use you can pass arguments to the decorator::
    
            >>> from mayavi import mlab
            >>> @mlab.animate(delay=500, ui=False)
            ... def anim():
            ...     f = mlab.gcf()
            ...     while 1:
            ...         f.scene.camera.azimuth(10)
            ...         f.scene.render()
            ...         yield
            ...
            >>> a = anim() # Starts the animation without a UI.
    
        **Notes**
    
        If you want to modify the data plotted by an `mlab` function call,
        please refer to the section on: :ref:`mlab-animating-data`.
    
    

    


axes
~~~~

.. function:: axes(*args, **kwargs)

    Creates axes for the current (or given) object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :nb_labels: The number of labels along each direction Must be a legal
                    value. Default: 2
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :ranges: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Ranges of the labels displayed on the axes.
                 Default is the object's extents.
    
        :x_axis_visibility: Whether or not the x axis is visible (boolean)
    
        :xlabel: the label of the x axis
    
        :y_axis_visibility: Whether or not the y axis is visible (boolean)
    
        :ylabel: the label of the y axis
    
        :z_axis_visibility: Whether or not the z axis is visible (boolean)
    
        :zlabel: the label of the z axis
    

    


get_engine
~~~~~~~~~~

.. function:: get_engine(self)

    Returns an engine in agreement with the options.
    

    


init_notebook
~~~~~~~~~~~~~

.. function:: init_notebook(backend='ipy', width=None, height=None, local=True)

    Initialize a suitable backend for Jupyter notebooks.
    
    **Parameters**
    
    backend :str: one of ('png', 'x3d', 'ipy')
    width :int: suggested default width of the element
    height :int: suggested default height of the element
    local :bool: Use local copy of x3dom.js instead of online version.
    

    


orientation_axes
~~~~~~~~~~~~~~~~

.. function:: orientation_axes(*args, **kwargs)

    Applies the OrientationAxes mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :xlabel: the label of the x axis
    
        :ylabel: the label of the y axis
    
        :zlabel: the label of the z axis
    

    


outline
~~~~~~~

.. function:: outline(*args, **kwargs)

    Creates an outline for the current (or given) object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    

    


process_ui_events
~~~~~~~~~~~~~~~~~

.. function:: process_ui_events()

    Process GUI events.
    
    This function merely abstracts the function so nothing is done when
    no UI is running.
    

    


set_engine
~~~~~~~~~~

.. function:: set_engine(self, engine)

    Sets the mlab engine.
    

    


show
~~~~

.. function:: show(func=None, stop=False)

    Start interacting with the figure.
    
    By default, this function simply creates a GUI and starts its
    event loop if needed.
    
    If it is used as a decorator, then it may be used to decorate a
    function which requires a UI.   If the GUI event loop is already
    running it simply runs the function.  If not the event loop is
    started and function is run in the toolkit's event loop.  The choice
    of UI is via `ETSConfig.toolkit`.
    
    If the argument stop is set to True then it pops up a UI where the
    user can stop the event loop.  Subsequent calls to `show` will
    restart the event loop.
    
    **Parameters**
    
      :stop:  A boolean which specifies if a UI dialog is displayed which
              allows the event loop to be stopped.
    
    **Examples**
    
    Here is a simple example demonstrating the use of show::
    
      >>> from mayavi import mlab
      >>> mlab.test_contour3d()
      >>> mlab.show()
    
    You can stop interaction via a simple pop up UI like so::
    
      >>> mlab.test_contour3d()
      >>> mlab.show(stop=True)
    
    The decorator can be used like so::
    
      >>> @mlab.show
      ... def do():
      ...    mlab.test_contour3d()
      ...
      >>> do()
    
    The decorator can also be passed the stop argument::
    
      >>> @mlab.show(stop=True)
      ... def do():
      ...    mlab.test_contour3d()
      ...
      >>> do()
    
    

    


show_engine
~~~~~~~~~~~

.. function:: show_engine()

    This function is deprecated, please use show_pipeline.
    

    


show_pipeline
~~~~~~~~~~~~~

.. function:: show_pipeline(self, engine=None, rich_view=True)

    Show a dialog with the mayavi pipeline. This dialog allows to
    edit graphically the properties of the different objects on
    the scenes.
    

    


start_recording
~~~~~~~~~~~~~~~

.. function:: start_recording(ui=True)

    Start automatic script recording.  If the `ui` parameter is
    `True`, it creates a recorder with a user interface, if not it
    creates a vanilla recorder without a UI.
    
    **Returns**
        The `Recorder` instance created.
    

    


stop_recording
~~~~~~~~~~~~~~

.. function:: stop_recording(file=None)

    Stop the automatic script recording.
    
    **Parameters**
    
     :file: An open file or a filename or `None`.  If this is `None`,
            nothing is saved.
    
    

    


text
~~~~

.. function:: text(*args, **kwargs)

    Adds a text on the figure.
    
    **Function signature**::
    
        text(x, y, text, ...)
    
    x, and y are the position of the origin of the text. If no z
    keyword argument is given, x and y are the 2D projection of the
    figure, they belong to [0, 1]. If a z keyword  argument is given, the
    text is positioned in 3D, in figure coordinates.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The opacity of the text.
    
        :width: width of the text.
    
        :z: Optional z position. When specified, the
            text is positioned in 3D
    

    


text3d
~~~~~~

.. function:: text3d(*args, **kwargs)

    Positions text at a 3D location in the scene.
    
    **Function signature**::
    
        text3d(x, y, z, text, ...)
    
    x, y, and z are the position of the origin of the text. The
    text is positioned in 3D, in figure coordinates.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :orient_to_camera: if the text is kept oriented to the
                           camera, or is pointing in a specific direction,
                           regardless of the camera position. Must be a
                           boolean. Default: True
    
        :orientation: the angles giving the orientation of the
                      text. If the text is oriented to the camera,
                      these angles are referenced to the axis of the
                      camera. If not, these angles are referenced to
                      the z axis. Must be an array with shape (3,).
    
        :scale: The scale of the text, in figure units.
                Either a float, or 3-tuple of floats.
    

    


title
~~~~~

.. function:: title(*args, **kwargs)

    Creates a title for the figure.
    
    **Function signature**::
    
        title(text, ...)
    
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :figure:  Must be a Scene or None.
    
        :height: height of the title, in portion of the
                 figure height
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :size: the size of the title
    

    

