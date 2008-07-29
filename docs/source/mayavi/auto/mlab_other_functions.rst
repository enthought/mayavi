

.. currentmodule:: enthought.mayavi.mlab

Other functions
===============

axes
~~~~

.. function:: axes(*args, **kwargs)

    Creates axes for the current (or given) object.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :zlabel: the label of the z axis
    
        :ranges: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Ranges of the labels displayed on the axes.
                 Default is the object's extents.
    
        :xlabel: the label of the x axis
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    
        :ylabel: the label of the y axis
    

    


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
    
    x, and y are the position of the origin of
    the text on the 2D projection of the figure.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :width: width of the text.
    

    


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
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    

    


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
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :height: height of the title, in portion of the
                 figure height
    
        :size: the size of the title
    

    


orientationaxes
~~~~~~~~~~~~~~~

.. function:: orientationaxes(*args, **kwargs)

    Applies the OrientationAxes mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :zlabel: the label of the z axis
    
        :xlabel: the label of the x axis
    
        :ylabel: the label of the y axis
    

    

