
contour_surf
~~~~~~~~~~~~


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

    :contours: Integer/list specifying number/list of
               contours. Specifying 0 shows no contours.
               Specifying a list of values will only give the
               requested contours asked for.


.. image:: images/mlab_contour_surf.jpg

Example::

    def test_contour_surf():
        """Test contour_surf on regularly spaced co-ordinates like MayaVi."""
        def f(x, y):
            sin, cos = numpy.sin, numpy.cos
            return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
    
        x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
        s = contour_surf(x, y, f)
        return s
    

    