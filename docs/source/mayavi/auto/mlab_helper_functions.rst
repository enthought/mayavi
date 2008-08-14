

.. currentmodule:: enthought.mayavi.mlab

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Plotting functions
==================

imshow
~~~~~~

.. function:: imshow(*args, **kwargs)

    
    Allows one to view a 2D Numeric array as an image.  This works
    best for very large arrays (like 1024x1024 arrays).
    
    **Function signatures**::
    
        imshow(2darray, ...)
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :representation: the representation type used for the surface. Must be
                         'surface' or 'wireframe' or 'points'. Default:
                         surface
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :figure: Figure to populate.
    
        :name: the name of the vtk object created.
    

    

.. image:: ../images/enthought_mayavi_mlab_imshow.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_imshow():
        return imshow(numpy.random.random((10,10)), colormap='gist_earth')
    
                



quiver3d
~~~~~~~~

.. function:: quiver3d(*args, **kwargs)

    
    Plots glyphs (like arrows) indicating the direction of the vectors
    for a 3D volume of data supplied as arguments.
    
    **Function signatures**::
    
        quiver3d(u, v, w, ...)
        quiver3d(x, y, z, u, v, w, ...)
        quiver3d(x, y, z, f, ...)
    
    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :scale_factor: the scaling applied to the glyphs. The
                       size of the glyph is by default in drawing
                       units. Must be a float. Default: 1.0
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :scalars: optional scalar data.
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'cone' or 'cube' or
               'cylinder' or 'point' or 'sphere'. Default: 2darrow
    
        :figure: Figure to populate.
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi.
    

    

.. image:: ../images/enthought_mayavi_mlab_quiver3d.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_quiver3d():
        dims = [8, 8, 8]
        xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
        x, y, z = numpy.mgrid[xmin:xmax:dims[0]*1j,
                              ymin:ymax:dims[1]*1j,
                              zmin:zmax:dims[2]*1j]
        x = x.astype('f')
        y = y.astype('f')
        z = z.astype('f')
    
        sin = numpy.sin
        cos = numpy.cos
        u = cos(x)
        v = sin(y)
        w = sin(x*z)
    
        obj = quiver3d(x, y, z, u, v, w, mode='cone', extent=(0,1, 0,1, 0,1),
                       scale_factor=0.9)
    
        return u, v, w, obj
    
                



plot3d
~~~~~~

.. function:: plot3d(*args, **kwargs)

    
    Draws lines between points.
    
    **Function signatures**::
    
        plot3d(x, y, z, ...)
        plot3d(x, y, z, s, ...)
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :tube_radius: radius of the tubes used to represent the
                      lines Must be a float. Default: 0.025
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :figure: Figure to populate.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :representation: the representation type used for the surface. Must be
                         'surface' or 'wireframe' or 'points'. Default:
                         surface
    
        :tube_sides: number of sides of the tubes used to
                     represent the lines. Must be an integer. Default: 6
    

    

.. image:: ../images/enthought_mayavi_mlab_plot3d.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_plot3d():
        """Generates a pretty set of lines."""
        n_mer, n_long = 6, 11
        pi = numpy.pi
        dphi = pi/1000.0 
        phi = numpy.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
        mu = phi*n_mer
        x = numpy.cos(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
        y = numpy.sin(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
        z = numpy.sin(n_long*mu/n_mer)*0.5
    
        l = plot3d(x, y, z, numpy.sin(mu), tube_radius=0.025, colormap='Spectral')
        return l
    
                



surf
~~~~

.. function:: surf(*args, **kwargs)

    
    Plots a surface using regularly spaced elevation data supplied as a 2D
    array.
    
    **Function signatures**::
    
        surf(s, ...)
        surf(x, y, s, ...)
        surf(x, y, f, ...)
    
    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinnates of positions corresponding to the s values.
    
    z is the elevation matrix.
    
    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value. For
    arbitrary-shaped position arrays (non-orthogonal grids), see the mesh
    function.
    
    If only 1 array s is passed the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :figure: Figure to populate.
    
        :warp_scale: scale of the z axis (warped from
                     the value of the scalar). By default this scale
                     is calculated to give a pleasant aspect ratio to
                     the plot. You can overright this behavior by
                     specifying a float value.
                     If you specify a value for warp_scale in
                     addition to an extent, the warp scale will be
                     determined by the warp_scale, and the plot be
                     positioned along the z axis with the zero of the
                     data centered on the center of the extent.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :mask: boolean mask array to suppress some data points.
    
        :representation: the representation type used for the surface. Must be
                         'surface' or 'wireframe' or 'points'. Default:
                         surface
    

    

.. image:: ../images/enthought_mayavi_mlab_surf.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_surf():
        """Test surf on regularly spaced co-ordinates like MayaVi."""
        def f(x, y):
            sin, cos = numpy.sin, numpy.cos
            return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
    
        x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
        s = surf(x, y, f)
        #cs = contour_surf(x, y, f, contour_z=0)
        return s
    
                



mesh
~~~~

.. function:: mesh(*args, **kwargs)

    
    Plots a surface using grid-spaced data supplied as 2D arrays.
    
    **Function signatures**::
    
        mesh(x, y, z, ...)
    
    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is implied by the connectivity on
    the arrays.
    
    For simple structures (such as orthogonal grids) prefer the surf function,
    as it will create more efficient data structures.
    
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :scale_factor: scale factor of the glyphs used to represent
                       the vertices, in fancy_mesh mode. Must be a float.
                       Default: 0.05
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :tube_radius: radius of the tubes used to represent the
                      lines, in mesh mode. If None, simple lines are used.
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :figure: Figure to populate.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :mask: boolean mask array to suppress some data points.
    
        :scalars: optional scalar data.
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'cone' or 'cube' or
               'cylinder' or 'point' or 'sphere'. Default: sphere
    
        :representation: the representation type used for the surface. Must be
                         'surface' or 'wireframe' or 'points' or 'mesh' or
                         'fancymesh'. Default: surface
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi.
    
        :tube_sides: number of sides of the tubes used to
                     represent the lines. Must be an integer. Default: 6
    

    

.. image:: ../images/enthought_mayavi_mlab_mesh.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_mesh():
        """A very pretty picture of spherical harmonics translated from
        the octaviz example."""
        pi = numpy.pi
        cos = numpy.cos
        sin = numpy.sin
        dphi, dtheta = pi/250.0, pi/250.0
        [phi,theta] = numpy.mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
        m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
        r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
        x = r*sin(phi)*cos(theta)
        y = r*cos(phi)
        z = r*sin(phi)*sin(theta);
    
        return mesh(x, y, z, colormap="bone")
    
                



contour3d
~~~~~~~~~

.. function:: contour3d(*args, **kwargs)

    
    Plots iso-surfaces for a 3D volume of data suplied as arguments.
    
    **Function signatures**::
    
        contour3d(scalars, ...)
        contour3d(scalarfield, ...)
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :name: the name of the vtk object created.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :colormap: type of colormap to use.
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying 0 shows no contours.
                   Specifying a list of values will only give the
                   requested contours asked for.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :figure: Figure to populate.
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    

    

.. image:: ../images/enthought_mayavi_mlab_contour3d.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_contour3d():
        dims = [64, 64, 64]
        xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
        x, y, z = numpy.ogrid[xmin:xmax:dims[0]*1j,
                              ymin:ymax:dims[1]*1j,
                              zmin:zmax:dims[2]*1j]
        x = x.astype('f')
        y = y.astype('f')
        z = z.astype('f')
    
        sin = numpy.sin
        scalars = x*x*0.5 + y*y + z*z*2.0
    
        obj = contour3d(scalars, contours=4, transparent=True)
        return obj, scalars
    
                



points3d
~~~~~~~~

.. function:: points3d(*args, **kwargs)

    
    Plots glyphs (like points) at the position of the supplied data.
    
    **Function signatures**::
    
        points3d(scalardata, ...)
        points3d(x, y, z...)
        points3d(x, y, z, s, ...)
        points3d(x, y, z, f, ...)
    
    If only one positional argument is passed, it should be VTK data
    object with scalar data.
    
    If only 3 arrays x, y, z all the points are drawn with the same size
    and color
    
    If 4 positional arguments are passed the last one can be an array s
    or a callable f that gives the size and color of the glyph.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :scale_factor: the scaling applied to the glyphs. The
                       size of the glyph is by default in drawing
                       units. Must be a float. Default: 1.0
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :scale_mode: the scaling mode for the glyphs
                     ('vector', 'scalar', or 'none').
    
        :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
               '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
               '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
               '2dtriangle' or '2dvertex' or 'arrow' or 'cone' or 'cube' or
               'cylinder' or 'point' or 'sphere'. Default: sphere
    
        :figure: Figure to populate.
    
        :resolution: The resolution of the glyph created. For spheres, for
                     instance, this is the number of divisions along theta and
                     phi.
    

    

.. image:: ../images/enthought_mayavi_mlab_points3d.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_points3d():
        t = numpy.linspace(0, 4*numpy.pi, 20)
        cos = numpy.cos
        sin = numpy.sin
    
        x = sin(2*t)
        y = cos(t)
        z = cos(2*t)
        s = 2+sin(t)
    
        return points3d(x, y, z, s, colormap="copper", scale_factor=.25)
    
                



flow
~~~~

.. function:: flow(*args, **kwargs)

    
    Creates streamlines following the flow of a vector field.
    
    **Function signatures**::
    
        flow(u, v, w, ...)
        flow(x, y, z, u, v, w, ...)
        flow(x, y, z, f, ...)
    
    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.
    
    If the x, y and z arrays are passed they are supposed to have been
    generated by `numpy.mgrid`. The function builds a scalar field assuming
    the points are regularily spaced.
    
    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :colormap: type of colormap to use.
    
        :seedtype: the widget used as a seed for the streamlines. Must be
                   'line' or 'plane' or 'point' or 'sphere'. Default: sphere
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :linetype: the type of line-like object used to display the
                   streamline. Must be 'line' or 'ribbon' or 'tube'. Default:
                   line
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :scalars: optional scalar data.
    
        :figure: Figure to populate.
    

    

.. image:: ../images/enthought_mayavi_mlab_flow.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_flow():
        dims = [32, 32, 32]
        xmin, xmax, ymin, ymax, zmin, zmax = [-5,5,-5,5,-5,5]
        x, y, z = numpy.mgrid[xmin:xmax:dims[0]*1j,
                              ymin:ymax:dims[1]*1j,
                              zmin:zmax:dims[2]*1j]
        x = x.astype('f')
        y = y.astype('f')
        z = z.astype('f')
    
        sin = numpy.sin
        cos = numpy.cos
        u = cos(x/2.)
        v = sin(y/2.)
        w = sin(x*z/4.)
    
        obj = flow(x, y, z, u, v, w, linetype='tube')
        return u, v, w, obj
    
                



contour_surf
~~~~~~~~~~~~

.. function:: contour_surf(*args, **kwargs)

    
    Plots a the contours of asurface using grid spaced data supplied as 2D
    arrays.
    
    **Function signatures**::
    
        contour_surf(s, ...)
        contour_surf(x, y, s, ...)
        contour_surf(x, y, f, ...)
    
    If only one array s is passed the x and y arrays are assumed to be made
    of the indices of s.
    s is the elevation matrix.
    
    **Keyword arguments:**
    
        :opacity: The overall opacity of the vtk object.
    
        :colormap: type of colormap to use.
    
        :color: the color of the vtk object. Overides the colormap,
                if any, when specified.
    
        :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
                 Default is the x, y, z arrays extents.
    
        :vmax: vmax is used to scale the colormap
               If None, the max of the data will be used
    
        :transparent: make the opacity of the actor depend on the
                      scalar.
    
        :warp_scale: scale of the warp scalar
    
        :name: the name of the vtk object created.
    
        :vmin: vmin is used to scale the colormap
               If None, the min of the data will be used
    
        :contours: Integer/list specifying number/list of
                   contours. Specifying 0 shows no contours.
                   Specifying a list of values will only give the
                   requested contours asked for.
    
        :figure: Figure to populate.
    

    

.. image:: ../images/enthought_mayavi_mlab_contour_surf.jpg


**Example** (run in ``ipython -wthread`` or in the mayavi2 interactive shell,
see :ref:`running-mlab-scripts` for more info)::

    
    import numpy
    from enthought.mayavi.mlab import *
    
    def test_contour_surf():
        """Test contour_surf on regularly spaced co-ordinates like MayaVi."""
        def f(x, y):
            sin, cos = numpy.sin, numpy.cos
            return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
    
        x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
        s = contour_surf(x, y, f)
        return s
    
                


