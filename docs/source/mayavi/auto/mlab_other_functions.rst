

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
    
        :width: width of the text.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    

    


show_engine
~~~~~~~~~~~

.. function:: show_engine()

    Show the UI for the mayavi engine used to create the
    visualisations.
    

    


get_engine
~~~~~~~~~~

.. function:: get_engine()

    Returns the mayavi engine used to create the visualisations.
    

    


outline
~~~~~~~

.. function:: outline(*args, **kwargs)

    Creates an outline for the current (or given) object.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :name: the name of the vtk object created.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the object's extents.
    

    


title
~~~~~

.. function:: title(*args, **kwargs)

    Creates a title for the figure.
    
    **Function signature**::
    
        title(text, ...)
    
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :height: height of the title, in portion of the
                 figure height
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
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
    

    

