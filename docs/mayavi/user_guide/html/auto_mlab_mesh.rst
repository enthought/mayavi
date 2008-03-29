
mesh
~~~~


Plots a surface using-grid spaced data supplied as 2D arrays.

**Function signatures**::

    mesh(x, y, z, ...)



**Keyword arguments:**

    :opacity: The overall opactiy of the vtk object.

    :scale_factor: scale factor of the glyphs used to represent
                   the vertices, in fancy_mesh mode. Default: 0.05

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
           'cylinder' or 'point' or 'sphere'. Default: sphere

    :representation: the representation type used for the surface. Must be
                     'surface' or 'wireframe' or 'points' or 'mesh' or
                     'fancymesh'. Default: surface

    :tube_sides: number of sides of the tubes used to
                 represent the lines. Default: 6


.. image:: images/mlab_mesh.jpg

Example::

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
    

    