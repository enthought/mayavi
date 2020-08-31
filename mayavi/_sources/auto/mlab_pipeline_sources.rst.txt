

.. currentmodule:: mayavi.tools.pipeline

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Sources
=======

array2d_source
~~~~~~~~~~~~~~

.. function:: array2d_source(*args, **kwargs)

    
    Creates structured 2D data from a 2D array.
    
    **Function signatures**::
    
        array2d_source(s, ...)
        array2d_source(x, y, s, ...)
        array2d_source(x, y, f, ...)
    
    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinates of positions corresponding to the s values.
    
    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value.
    
    If only 1 array s is passed the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
    
        :mask: Mask points specified in a boolean masking array.
    

    


builtin_image
~~~~~~~~~~~~~

.. function:: builtin_image(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a1888>)

    Create a vtk image data source
    

    


builtin_surface
~~~~~~~~~~~~~~~

.. function:: builtin_surface(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a17d8>)

    Create a vtk poly data source
    

    


chaco_file
~~~~~~~~~~

.. function:: chaco_file(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a1a40>)

    Open a Chaco file
    

    


grid_source
~~~~~~~~~~~

.. function:: grid_source(x, y, z, **kwargs)

    
    Creates 2D grid data.
    
    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is implied by the connectivity on
    the arrays.
    
    For simple structures (such as orthogonal grids) prefer the array2dsource
    function, as it will create more efficient data structures.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :scalars: optional scalar data.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
    
        :mask: Mask points specified in a boolean masking array.
    
    

    


line_source
~~~~~~~~~~~

.. function:: line_source(*args, **kwargs)

    
    Creates line data.
    
    **Function signatures**::
    
        line_source(x, y, z, ...)
        line_source(x, y, z, s, ...)
        line_source(x, y, z, f, ...)
    
        If 4 positional arguments are passed the last one must be an array s,
        or a callable, f, that returns an array.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

    


open
~~~~

.. function:: open(filename, figure=None)

    Open a supported data file given a filename.  Returns the source
    object if a suitable reader was found for the file.
    
    If 'figure' is False, no view is opened, and the code does not need
    GUI or openGL context.
    

    


parametric_surface
~~~~~~~~~~~~~~~~~~

.. function:: parametric_surface(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a1620>)

    Create a parametric surface source
    

    


point_load
~~~~~~~~~~

.. function:: point_load(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a1728>)

    Simulates a point load on a cube of data (for tensors)
    

    


scalar_field
~~~~~~~~~~~~

.. function:: scalar_field(*args, **kwargs)

    
    Creates a scalar field data.
    
    **Function signatures**::
    
        scalar_field(s, ...)
        scalar_field(x, y, z, s, ...)
        scalar_field(x, y, z, f, ...)
    
    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of arrays.
    
    If the x, y and z arrays are passed they are supposed to have been
    generated by `numpy.mgrid`. The function builds a scalar field assuming
    the points are regularily spaced.
    
    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

    


scalar_scatter
~~~~~~~~~~~~~~

.. function:: scalar_scatter(*args, **kwargs)

    
    Creates scattered scalar data.
    
    **Function signatures**::
    
        scalar_scatter(s, ...)
        scalar_scatter(x, y, z, s, ...)
        scalar_scatter(x, y, z, s, ...)
        scalar_scatter(x, y, z, f, ...)
    
    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

    


triangular_mesh_source
~~~~~~~~~~~~~~~~~~~~~~

.. function:: triangular_mesh_source(x, y, z, triangles, **kwargs)

    
    Creates 2D mesh by specifying points and triangle connectivity.
    
    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is given by listing triplets of
    vertices inter-connected. These vertices are designed by there
    position index.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :scalars: optional scalar data.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
    

    


vector_field
~~~~~~~~~~~~

.. function:: vector_field(*args, **kwargs)

    Creates vector field data.
    
    **Function signatures**::
    
        vector_field(u, v, w, ...)
        vector_field(x, y, z, u, v, w, ...)
        vector_field(x, y, z, f, ...)
    
    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If the x, y and z arrays are passed, they should have been generated
    by `numpy.mgrid` or `numpy.ogrid`. The function builds a scalar field
    assuming the points are regularily spaced on an orthogonal grid.
    
    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :scalars: optional scalar data.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

    


vector_scatter
~~~~~~~~~~~~~~

.. function:: vector_scatter(*args, **kwargs)

    Creates scattered vector data.
    
    **Function signatures**::
    
        vector_scatter(u, v, w, ...)
        vector_scatter(x, y, z, u, v, w, ...)
        vector_scatter(x, y, z, f, ...)
    
    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :scalars: optional scalar data.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

    


vertical_vectors_source
~~~~~~~~~~~~~~~~~~~~~~~

.. function:: vertical_vectors_source(*args, **kwargs)

    
    Creates a set of vectors pointing upward, useful eg for bar graphs.
    
    **Function signatures**::
    
        vertical_vectors_source(s, ...)
        vertical_vectors_source(x, y, s, ...)
        vertical_vectors_source(x, y, f, ...)
        vertical_vectors_source(x, y, z, s, ...)
        vertical_vectors_source(x, y, z, f, ...)
    
    If only one positional argument is passed, it can be a 1D, 2D, or 3D
    array giving the length of the vectors. The positions of the data
    points are deducted from the indices of array, and an
    uniformly-spaced data set is created.
    
    If 3 positional arguments (x, y, s) are passed the last one must be
    an array s, or a callable, f, that returns an array. x and y give the
    2D coordinates of positions corresponding to the s values. The
    vertical position is assumed to be 0.
    
    If 4 positional arguments (x, y, z, s) are passed, the 3 first are
    arrays giving the 3D coordinates of the data points, and the last one
    is an array s, or a callable, f, that returns an array giving the
    data value.
    
    **Keyword arguments**:
    
        :name: the name of the vtk object created.
    
        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
    

    


volume_file
~~~~~~~~~~~

.. function:: volume_file(metadata=<mayavi.core.metadata.SourceMetadata object at 0x13b8a1938>)

    Open a Volume file
    

    

