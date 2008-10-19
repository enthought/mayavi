

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
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object.
    
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

.. function:: show(func=None)

    Start interacting with the figure.
    
    By default, this function simply creates a GUI and starts its
    event loop if needed.
    
    If it is used as a decorator, then it may be used to decorate a
    function which requires a UI.   If the GUI event loop is already
    running it simply runs the function.  If not the event loop is
    started and function is run in the toolkit's event loop.  The choice
    of UI is via `ETSConfig.toolkit`.
    
    

    


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
                if any, when specified.
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object.
    
        :width: width of the text.
    
        :z: Optional z position. When specified, the
            text is positioned in 3D
    

    


set_engine
~~~~~~~~~~

.. function:: set_engine(self, engine)

    Sets the mlab engine.
    

    


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
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object.
    

    


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
                if any, when specified.
    
        :height: height of the title, in portion of the
                 figure height
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object.
    
        :size: the size of the title
    

    


orientationaxes
~~~~~~~~~~~~~~~

.. function:: orientationaxes(*args, **kwargs)

    Applies the OrientationAxes mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object.
    
        :xlabel: the label of the x axis
    
        :ylabel: the label of the y axis
    
        :zlabel: the label of the z axis
    

    

