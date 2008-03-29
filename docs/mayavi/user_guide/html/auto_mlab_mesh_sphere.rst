
mesh_sphere
~~~~~~~~~~~

Create a simple sphere and test the mesh.


.. image:: images/mlab_mesh_sphere.jpg

Example::

        def test_mesh_sphere():
        """Create a simple sphere and test the mesh."""
        pi = numpy.pi
        cos = numpy.cos
        sin = numpy.sin    
        du, dv = pi/20.0, pi/20.0
        phi, theta = numpy.mgrid[0.01:pi+du*1.5:du, 0:2*pi+dv*1.5:dv]
        r = 1.0
        x = r*sin(phi)*cos(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(phi)
        s = mesh(x, y, z, representation='mesh', colormap='jet',
                        tube_radius=None)
    

    