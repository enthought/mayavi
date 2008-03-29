
surf
~~~~


Plots a surface using regularly spaced elevation data supplied as a 2D
array.

**Function signatures**::

    surf(s, ...)
    surf(x, y, s, ...)
    surf(x, y, f, ...)

If only one array z is passed the x and y arrays are assumed to be made
of the indices of z.
z is the elevation matrix.

**Keyword arguments:**

    :opacity: The overall opactiy of the vtk object.

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

    :representation: the representation type used for the surface. Must be
                     'surface' or 'wireframe' or 'points'. Default:
                     surface


.. image:: images/mlab_surf.jpg

Example::

    def test_surf():
        """Test surf on regularly spaced co-ordinates like MayaVi."""
        def f(x, y):
            sin, cos = numpy.sin, numpy.cos
            return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
    
        x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
        s = surf(x, y, f)
        #cs = contour_surf(x, y, f, contour_z=0)
        return s
    

    