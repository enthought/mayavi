
imshow
~~~~~~


Allows one to view a 2D Numeric array as an image.  This works
best for very large arrays (like 1024x1024 arrays).

**Function signatures**::

    imshow(2darray, ...)

**Keyword arguments:**

    :opacity: The overall opactiy of the vtk object.

    :colormap: type of colormap to use.

    :vmin: vmin is used to scale the colormap
           If None, the min of the data will be used

    :color: the color of the vtk object. Overides the colormap,
            if any, when specified.

    :extent: [xmin, xmax, ymin, ymax, zmin, zmax]
             Default is the x, y, z arrays extents.

    :vmax: vmax is used to scale the colormap
           If None, the max of the data will be used

    :representation: the representation type used for the surface. Must be
                     'surface' or 'wireframe' or 'points'. Default:
                     surface

    :transparent: make the opacity of the actor depend on the
                  scalar.

    :name: the name of the vtk object created.


.. image:: images/mlab_imshow.jpg

Example::

    def test_imshow():
        return imshow(numpy.random.random((10,10)), colormap='gist_earth')
    

    