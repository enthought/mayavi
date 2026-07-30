

.. _example_superquad_with_gui:

Superquad with gui example
--------------------------------------------

This example uses MayaVi to show the evolution of a superquadric
(http://en.wikipedia.org/wiki/Superquadrics), which are ellipsoidal surfaces
parametrised by two parameters, *alpha* and *beta*.

The equations that determine the superquadric are, in spherical-polar
coordinates::

    x = A * sin(phi)**alpha * cos(theta)**beta
    y = B * sin(phi)**alpha * sin(theta)**beta
    z = C * cos(phi)**alpha

Note that when we set ``A = B = C = r`` and ``alpha = beta = 1``, we get the
equation for a sphere in spherical polar coordinates.

Use the controls at the bottom of the plot to adjust *alpha* and *beta*, and
watch as the figure transforms accordingly!

**Python source code:** :download:`superquad_with_gui.py`

.. literalinclude:: superquad_with_gui.py
    :lines: 19-


    