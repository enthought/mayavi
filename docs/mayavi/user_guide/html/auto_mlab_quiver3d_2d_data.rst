
quiver3d_2d_data
~~~~~~~~~~~~~~~~




.. image:: images/mlab_quiver3d_2d_data.jpg

Example::

        def test_quiver3d_2d_data():
        dims = [32, 32]
        xmin, xmax, ymin, ymax = [-5,5,-5,5]
        x, y = numpy.mgrid[xmin:xmax:dims[0]*1j,
                           ymin:ymax:dims[1]*1j]
        x = x.astype('f')
        y = y.astype('f')
    
        sin = numpy.sin
        cos = numpy.cos
        u = cos(x)
        v = sin(y)
        w = numpy.zeros_like(x)
    
        return quiver3d(x, y, w, u, v, w, colormap="Purples",
                                    scale_factor=0.5, mode="2dthick_arrow")
    

    