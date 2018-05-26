

.. _example_superquad_with_gui:

Superquad with gui example
--------------------------------------------


This example uses MayaVi to show the evolution of a superquadric
(http://en.wikipedia.org/wiki/Superquadrics), which are ellipsoidal surfaces parametrised
by two parameters,lpha and eta. The equations that are used to determine the superquadric are 
(in spherical-polar coordinates):

  \(x = A(\sin^{lpha}(\phi)*\cos^{eta}(	heta))\)
  \(y = B(\sin^{lpha}(\phi)*\sin^{eta}(	heta))\)
  \(z = C(\cos^{lpha}(\phi))\)

Note that when we set A=B=C=r, and lpha =  eta = 1, we get the 
equation for a sphere in spherical polar coordinate.

Use the controls at the bottom of the plot to adjust lpha and eta,
and watch as the figure transforms accordingly!



**Python source code:** :download:`superquad_with_gui.py`

.. literalinclude:: superquad_with_gui.py
    :lines: 18-


    