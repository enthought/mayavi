

.. currentmodule:: enthought.mayavi.mlab

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Other functions
===============

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
    
        :line_width:  The with of the lines, if any used. Must be a float.
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
    
     stop : bool -- Specifies if a UI dialog is displayed which allows
                    the event loop to be stopped.
    
    **Examples**
    
    Here is a simple example demonstrating the use of show::
    
      >>> from enthought.mayavi import mlab
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
    
    

    


text
~~~~

.. function:: text(*args, **kwargs)

    Adds a text on the figure.
    
    **Function signature**::
    
        text(x, y, text, ...)
    
    x, and y are the position of the origin of the text on the 2D
    projection of the figure. If a z keyword argument is given, the
    text is positionned in 3D, in figure coordinnates.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :line_width:  The with of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :width: width of the text.
    
        :z: Optional z position. When specified, the
            text is positioned in 3D
    

    


orientation_axes
~~~~~~~~~~~~~~~~

.. function:: orientation_axes(*args, **kwargs)

    Applies the OrientationAxes mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :line_width:  The with of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :xlabel: the label of the x axis
    
        :ylabel: the label of the y axis
    
        :zlabel: the label of the z axis
    

    


set_engine
~~~~~~~~~~

.. function:: set_engine(self, engine)

    Sets the mlab engine.
    

    


animate
~~~~~~~

.. function:: animate(func=None, delay=500, ui=True)

    A convenient decorator to animate a generator that performs an
    animation.  The `delay` parameter specifies the delay (in
    milliseconds) between calls to the decorated function. If `ui` is
    True, then a simple UI for the animator is also popped up.  The
    decorated function will return the `Animator` instance used and a
    user may call its `Stop` method to stop the animation.
    
    If an ordinary function is decorated a `TypeError` will be raised.
    
    
    **Parameters**
    
      delay : int -- Time interval in milliseconds between calls to the
                     function.
    
      ui : bool : -- Specifies if a UI controlling the animation is to
                     be provided.
    
    **Returns**
    
      The decorated function returns an `Animator` instance.
    
    
    **Examples**
    
    Here is the example provided in the Animator class documentation::
    
        >>> from enthought.mayavi import mlab
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
    
        >>> from enthought.mayavi import mlab
        >>> @mlab.animate(delay=500, ui=False)
        ... def anim():
        ...     f = mlab.gcf()
        ...     while 1:
        ...         f.scene.camera.azimuth(10)
        ...         f.scene.render()
        ...         yield
        ...
        >>> a = anim() # Starts the animation without a UI.
    
    

    


show_engine
~~~~~~~~~~~

.. function:: show_engine()

    This function is depreciated, please use show_pipeline.
    

    


get_engine
~~~~~~~~~~

.. function:: get_engine(self)

    Returns an engine in agreement with the options.
    

    


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
    
        :line_width:  The with of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    

    


show_pipeline
~~~~~~~~~~~~~

.. function:: show_pipeline(self, engine=None)

    Show a dialog with the mayavi pipeline. This dialog allows to
    edit graphicaly the properties of the different objects on
    the scenes.
    

    


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
    
        :height: height of the title, in portion of the
                 figure height
    
        :line_width:  The with of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :size: the size of the title
    

    

