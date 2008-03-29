
quiver3d
~~~~~~~~


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

    :opacity: The overall opactiy of the vtk object.

    :scale_factor: the scaling applied to the glyphs. The
                   size of the glyph is by default in drawing
                   units. Default: 1.0

    :colormap: type of colormap to use.

    :vmin: vmin is used to scale the colormap
           If None, the min of the data will be used

    :color: the color of the vtk object. Overides the colormap,
            if any, when specified.

    :scale_mode: the scaling mode for the glyphs
                 ('vector', 'scalar', or 'none').

    :mode: the mode of the glyphs. Must be '2darrow' or '2dcircle' or
           '2dcross' or '2ddash' or '2ddiamond' or '2dhooked_arrow' or
           '2dsquare' or '2dthick_arrow' or '2dthick_cross' or
           '2dtriangle' or '2dvertex' or 'arrow' or 'cone' or 'cube' or
           'cylinder' or 'point' or 'sphere'. Default: 2darrow

    :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
             Default is the x, y, z arrays extents.

    :vmax: vmax is used to scale the colormap
           If None, the max of the data will be used

    :transparent: make the opacity of the actor depend on the
                  scalar.

    :name: the name of the vtk object created.


.. image:: images/mlab_quiver3d.jpg

Example::

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
    

    