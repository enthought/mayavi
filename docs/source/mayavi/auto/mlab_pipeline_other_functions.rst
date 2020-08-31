

.. currentmodule:: mayavi.tools.pipeline

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Filters, modules, other functions
=================================

cell_derivatives
~~~~~~~~~~~~~~~~

.. function:: cell_derivatives(*args, **kwargs)

    Calculate derivatives of input point/vector data and output these as cell data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


cell_to_point_data
~~~~~~~~~~~~~~~~~~

.. function:: cell_to_point_data(*args, **kwargs)

    Convert cell data to point data for the active data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


contour
~~~~~~~

.. function:: contour(*args, **kwargs)

    Compute contours of the input dataset
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


contour_grid_plane
~~~~~~~~~~~~~~~~~~

.. function:: contour_grid_plane(*args, **kwargs)

    
    ::
     Applies the ContourGridPlane mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying a list of values will only
                   give the requested contours asked for.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


contour_surface
~~~~~~~~~~~~~~~

.. function:: contour_surface(*args, **kwargs)

    Applies the Surface mayavi module to the given data
    source (Mayavi source, or VTK dataset) and turns contours on.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying a list of values will only
                   give the requested contours asked for.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


custom_grid_plane
~~~~~~~~~~~~~~~~~

.. function:: custom_grid_plane(*args, **kwargs)

    
    ::
     Applies the CustomGridPlane mayavi module to the given VTK data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying a list of values will only
                   give the requested contours asked for.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


cut_plane
~~~~~~~~~

.. function:: cut_plane(*args, **kwargs)

    Slice the input dataset with a cut plane
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


data_set_clipper
~~~~~~~~~~~~~~~~

.. function:: data_set_clipper(*args, **kwargs)

    Clip the input dataset
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


decimate_pro
~~~~~~~~~~~~

.. function:: decimate_pro(*args, **kwargs)

    Simpilies a mesh using the DecimatePro filter
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


delaunay2d
~~~~~~~~~~

.. function:: delaunay2d(*args, **kwargs)

    Perform a 2D Delaunay triangulation for the given data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


delaunay3d
~~~~~~~~~~

.. function:: delaunay3d(*args, **kwargs)

    Perform a 3D Delaunay triangulation for the given data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


elevation
~~~~~~~~~

.. function:: elevation(*args, **kwargs)

    Creates scalar data from the elevation along a direction
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


elevation_filter
~~~~~~~~~~~~~~~~

.. function:: elevation_filter(*args, **kwargs)

    Applies the Elevation Filter mayavi filter to the given VTK object.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :high_point: The end point of the projection line
    
        :low_point: The start point of the projection line
    
        :name: the name of the vtk object created.
    

    


extract_edges
~~~~~~~~~~~~~

.. function:: extract_edges(*args, **kwargs)

    Turns edges into lines.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


extract_grid
~~~~~~~~~~~~

.. function:: extract_grid(*args, **kwargs)

    Extract/subsample part of any structured grid
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


extract_tensor_components
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: extract_tensor_components(*args, **kwargs)

    Extract tensor components from tensor data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


extract_unstructured_grid
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: extract_unstructured_grid(*args, **kwargs)

    Extract part of an unstructured grid
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


extract_vector_components
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: extract_vector_components(*args, **kwargs)

    Extract vector components from vector data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


extract_vector_norm
~~~~~~~~~~~~~~~~~~~

.. function:: extract_vector_norm(*args, **kwargs)

    Compute the vector norm for the current vector data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


gaussian_splatter
~~~~~~~~~~~~~~~~~

.. function:: gaussian_splatter(*args, **kwargs)

    Builds a structured set of points from a cloud of points,
    the local density defining the scalar.  It is essentially equivalent
    to a 3D Gaussian kernel density estimate.
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


glyph
~~~~~

.. function:: glyph(*args, **kwargs)

    Applies the Glyph mayavi module to the given VTK data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :mask_points: If supplied, only one out of 'mask_points' data point is
                      displayed. This option is useful to reduce the number of
                      points displayed on large datasets Must be an integer or
                      None.
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'axes' or 'cone' or
               'cube' or 'cylinder' or 'point' or 'sphere'. Default: sphere
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi. Must be an integer. Default: 8
    
        :scale_factor: the scaling applied to the glyphs. The
                       size of the glyph is by default in drawing
                       units. Must be a float. Default: 1.0
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


greedy_terrain_decimation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: greedy_terrain_decimation(*args, **kwargs)

    Simplifies image data and performs a triangulation
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


grid_plane
~~~~~~~~~~

.. function:: grid_plane(*args, **kwargs)

    Shows a grid plane for the given input
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


hyper_streamline
~~~~~~~~~~~~~~~~

.. function:: hyper_streamline(*args, **kwargs)

    Shows hyper streamlines for tensor data
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


image_actor
~~~~~~~~~~~

.. function:: image_actor(*args, **kwargs)

    Applies the ImageActor mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :interpolate: if the pixels in the image are to be
                      interpolated or not. Must be a boolean. Default: True
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: the opacity of the image. Must be a legal value. Default:
                  1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


image_change_information
~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: image_change_information(*args, **kwargs)

    Change the origin, spacing and extents of an image dataset
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


image_data_probe
~~~~~~~~~~~~~~~~

.. function:: image_data_probe(*args, **kwargs)

    Samples arbitrary datasets onto an image dataset (cube of data)
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


image_plane_widget
~~~~~~~~~~~~~~~~~~

.. function:: image_plane_widget(*args, **kwargs)

    
    ::
     Applies the ImagePlaneWidget mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :plane_opacity: the opacity of the plane actor. Must be a legal value.
                        Default: 1.0
    
        :plane_orientation: the orientation of the plane Must be a legal
                            value. Default: x_axes
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :slice_index: The index along with the
                      image is sliced.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


iso_surface
~~~~~~~~~~~

.. function:: iso_surface(*args, **kwargs)

    Applies the IsoSurface mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying a list of values will only
                   give the requested contours asked for.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


labels
~~~~~~

.. function:: labels(*args, **kwargs)

    Display labels for active dataset or active module
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


mask_points
~~~~~~~~~~~

.. function:: mask_points(*args, **kwargs)

    Mask the input points in the data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


outline
~~~~~~~

.. function:: outline(*args, **kwargs)

    Draw an outline for given input
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


point_to_cell_data
~~~~~~~~~~~~~~~~~~

.. function:: point_to_cell_data(*args, **kwargs)

    Convert point data to cell data for the active data
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


poly_data_normals
~~~~~~~~~~~~~~~~~

.. function:: poly_data_normals(*args, **kwargs)

    Compute normals and smooth the appearance
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


quadric_decimation
~~~~~~~~~~~~~~~~~~

.. function:: quadric_decimation(*args, **kwargs)

    Simplifies a triangular mesh
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


scalar_cut_plane
~~~~~~~~~~~~~~~~

.. function:: scalar_cut_plane(*args, **kwargs)

    
    ::
     Applies the ScalarCutPlane mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :plane_orientation: the orientation of the plane Must be a legal
                            value. Default: x_axes
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :view_controls: Whether or not the controls of the cut plane are
                        shown. Must be a boolean. Default: True
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


select_output
~~~~~~~~~~~~~

.. function:: select_output(*args, **kwargs)

    Choose the output of the source that should be used
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


set_active_attribute
~~~~~~~~~~~~~~~~~~~~

.. function:: set_active_attribute(*args, **kwargs)

    
    ::
     Applies the SetActiveAttribute Filter mayavi filter to the given
    VTK object.
    
    **Keyword arguments:**
    
        :cell_scalars: The name of the active cell scalars
    
        :cell_tensors: The name of the active cell tensors
    
        :cell_vectors: The name of the active cell vectors
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    
        :point_scalars: The name of the active point scalars
    
        :point_tensors: The name of the active point tensors
    
        :point_vectors: The name of the active point vectors
    

    


slice_unstructured_grid
~~~~~~~~~~~~~~~~~~~~~~~

.. function:: slice_unstructured_grid(*args, **kwargs)

    Slice an unstructured grid to show cells
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


streamline
~~~~~~~~~~

.. function:: streamline(*args, **kwargs)

    Applies the Streamline mayavi module to the given VTK data object.
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :integration_direction: The direction of the integration. Must be
                                'forward' or 'backward' or 'both'. Default:
                                forward
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :linetype: the type of line-like object used to display the
                   streamline. Must be 'line' or 'ribbon' or 'tube'. Default:
                   line
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :seed_resolution: The resolution of the seed. Determines the number of
                          seed points Must be an integer or None.
    
        :seed_scale: Scales the seed around its default center Must be a
                     float. Default: 1.0
    
        :seed_visible: Control the visibility of the seed. Must be a boolean.
                       Default: True
    
        :seedtype: the widget used as a seed for the streamlines. Must be
                   'line' or 'plane' or 'point' or 'sphere'. Default: sphere
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


stripper
~~~~~~~~

.. function:: stripper(*args, **kwargs)

    Regularizes surfaces by creating triangle strips
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


structured_grid_outline
~~~~~~~~~~~~~~~~~~~~~~~

.. function:: structured_grid_outline(*args, **kwargs)

    Draw a grid-conforming outline for structured grids
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


surface
~~~~~~~

.. function:: surface(*args, **kwargs)

    Applies the Surface mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :representation: the representation type used for the surface. Must be
                         'surface' or 'wireframe' or 'points'. Default:
                         surface
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


tensor_glyph
~~~~~~~~~~~~

.. function:: tensor_glyph(*args, **kwargs)

    Displays glyphs scaled and oriented as per tensor data
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


text3d
~~~~~~

.. function:: text3d(*args, **kwargs)

    Displays user-specified text at a 3D location in the scene
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


threshold
~~~~~~~~~

.. function:: threshold(*args, **kwargs)

    Applies the Threshold mayavi filter to the given VTK object.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :filter_type: If threshold is put on cells or points
    
        :low: The lower threshold
    
        :name: the name of the vtk object created.
    
        :up: The upper threshold
    

    


transform_data
~~~~~~~~~~~~~~

.. function:: transform_data(*args, **kwargs)

    Transform (rotate/translate/scale) non ImageData datasets
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


triangle_filter
~~~~~~~~~~~~~~~

.. function:: triangle_filter(*args, **kwargs)

    Convert input polygons and triangle strips to triangles
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


tube
~~~~

.. function:: tube(*args, **kwargs)

    Applies the Tube mayavi filter to the given VTK object.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    
        :tube_radius: radius of the tubes used to represent the
                      lines. Must be a float. Default: 0.05
    
        :tube_sides: number of sides of the tubes used to
                     represent the lines. Must be an integer. Default: 6
    

    


user_defined
~~~~~~~~~~~~

.. function:: user_defined(*args, **kwargs)

    Applies the UserDefined mayavi filter to the given TVTK object.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :filter: the tvtk filter to adapt. Thisbe either an instance of the
                 filter, or thename of this filter.
    
        :name: the name of the vtk object created.
    

    


vector_cut_plane
~~~~~~~~~~~~~~~~

.. function:: vector_cut_plane(*args, **kwargs)

    
    ::
     Applies the VectorCutPlane mayavi module to the given data
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :mask_points: If supplied, only one out of 'mask_points' data point is
                      displayed. This option is useful to reduce the number of
                      points displayed on large datasets Must be an integer or
                      None.
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'axes' or 'cone' or
               'cube' or 'cylinder' or 'point' or 'sphere'. Default: 2darrow
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :plane_orientation: the orientation of the plane Must be a legal
                            value. Default: x_axes
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi. Must be an integer. Default: 8
    
        :scale_factor: the scaling applied to the glyphs. The
                       size of the glyph is by default in drawing
                       units. Must be a float. Default: 1.0
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :view_controls: Whether or not the controls of the cut plane are
                        shown. Must be a boolean. Default: True
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


vectors
~~~~~~~

.. function:: vectors(*args, **kwargs)

    Applies the Vectors mayavi module to the given data object
    source (Mayavi source, or VTK dataset).
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :mask_points: If supplied, only one out of 'mask_points' data point is
                      displayed. This option is useful to reduce the number of
                      points displayed on large datasets Must be an integer or
                      None.
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'axes' or 'cone' or
               'cube' or 'cylinder' or 'point' or 'sphere'. Default: 2darrow
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi. Must be an integer. Default: 8
    
        :scale_factor: the scaling applied to the glyphs. The
                       size of the glyph is by default in drawing
                       units. Must be a float. Default: 1.0
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    


volume
~~~~~~

.. function:: volume(*args, **kwargs)

    
    ::
     Applies the Volume mayavi module to the given VTK data
    source (Mayavi source, or VTK dataset).
    
    **Note**
    
    The range of the colormap can be changed simply using the
    vmin/vmax parameters (see below). For more complex modifications of
    the colormap, here is some pseudo code to change the ctf (color
    transfer function), or the otf (opacity transfer function)::
    
        vol = mlab.pipeline.volume(src)
    
        # Changing the ctf:
        from tvtk.util.ctf import ColorTransferFunction
        ctf = ColorTransferFunction()
        ctf.add_rgb_point(value, r, g, b)  # r, g, and b are float
                                           # between 0 and 1
        ctf.add_hsv_point(value, h, s, v)
        # ...
        vol._volume_property.set_color(ctf)
        vol._ctf = ctf
        vol.update_ctf = True
    
        # Changing the otf:
        from tvtk.util.ctf import PiecewiseFunction
        otf = PiecewiseFunction()
        otf.add_point(value, opacity)
        vol._otf = otf
        vol._volume_property.set_scalar_opacity(otf)
    
    Also, it might be useful to change the range of the ctf::
    
        ctf.range = [0, 1]
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    
        :vmax: vmax is used to scale the transparency
               gradient. If None, the max of the data will be
               used
    
        :vmin: vmin is used to scale the transparency
               gradient. If None, the min of the data will be
               used
    

    


vorticity
~~~~~~~~~

.. function:: vorticity(*args, **kwargs)

    Calculate the vorticity (curl) of input vector field
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


warp_scalar
~~~~~~~~~~~

.. function:: warp_scalar(*args, **kwargs)

    Applies the WarpScalar mayavi filter to the given VTK object.
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    
        :warp_scale: scale of the warp scalar
    

    


warp_vector
~~~~~~~~~~~

.. function:: warp_vector(*args, **kwargs)

    Move points of data along the vector data at point
    
    **Keyword arguments:**
    
        :figure:  Must be a Scene or None.
    
        :name: the name of the vtk object created.
    

    


warp_vector_cut_plane
~~~~~~~~~~~~~~~~~~~~~

.. function:: warp_vector_cut_plane(*args, **kwargs)

    Warp cut plane along scaled input vectors
    
    **Keyword arguments:**
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified. This is specified as a
                triplet of float ranging from 0 to 1, eg (1, 1,
                1) for white.
    
        :colormap: type of colormap to use.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extent. Use
                 this to change the extent of the object
                 created.
    
        :figure:  Must be a Scene or None.
    
        :line_width:  The width of the lines, if any used. Must be a float.
                     Default: 2.0
    
        :name: the name of the vtk object created.
    
        :opacity: The overall opacity of the vtk object. Must be a float.
                  Default: 1.0
    
        :reset_zoom: Reset the zoom to accomodate the data newly
                     added to the scene. Defaults to True.
    
        :transparent: make the opacity of the actor depend on
                      the scalar.
    
        :vmax: vmax is used to scale the colormap.
               If None, the max of the data will be used
    
        :vmin: vmin is used to scale the colormap.
               If None, the min of the data will be used
    

    

