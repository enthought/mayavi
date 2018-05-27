

.. _example_spherical_harmonics:

Spherical harmonics example
--------------------------------------------------------------------


Plot spherical harmonics on the surface of the sphere, as well as a 3D
polar plot.

This example requires scipy.

In this example we use the mlab's mesh function:
:func:`mayavi.mlab.mesh`.
For plotting surfaces this is a very versatile function. The surfaces can
be defined as functions of a 2D grid.

For each spherical harmonic, we plot its value on the surface of a
sphere, and then in polar. The polar plot is simply obtained by varying
the radius of the previous sphere.


.. image:: ../generated_images/example_spherical_harmonics.jpg
    :align: center



**Python source code:** :download:`spherical_harmonics.py`

.. literalinclude:: spherical_harmonics.py
    :lines: 16-


    