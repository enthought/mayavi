
plot3d
~~~~~~


Draws lines between points.

**Function signatures**::

    plot3d(x, y, z, ...)
    plot3d(x, y, z, s, ...)

**Keyword arguments:**

    :opacity: The overall opactiy of the vtk object.

    :tube_radius: radius of the tubes used to represent the
                  lines Default: 0.025

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

    :representation: the representation type used for the surface. Must be
                     'surface' or 'wireframe' or 'points'. Default:
                     surface

    :tube_sides: number of sides of the tubes used to
                 represent the lines. Default: 6


.. image:: images/mlab_plot3d.jpg

Example::

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
    

    