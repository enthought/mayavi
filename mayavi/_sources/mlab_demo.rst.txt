.. _mlab_demo:

A demo
-------

To get you started, here is a pretty example showing a spherical harmonic
as a surface::

 # Create the data.
 from numpy import pi, sin, cos, mgrid
 dphi, dtheta = pi/250.0, pi/250.0
 [phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
 m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
 r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
 x = r*sin(phi)*cos(theta)
 y = r*cos(phi)
 z = r*sin(phi)*sin(theta)

 # View it.
 from mayavi import mlab
 s = mlab.mesh(x, y, z)
 mlab.show()

Bulk of the code in the above example is to create the data.  One line
suffices to visualize it.  This produces the following visualization:

.. image:: images/mlab_surf_example.jpg
    :align: center

The visualization is created by the single function :func:`mesh` in the above.

Several examples of this kind are provided with mlab (see
`test_contour3d`, `test_points3d`, `test_plot3d_anim` etc.).  The above
demo is available as `test_mesh`.  Under IPython these may be found by
tab completing on `mlab.test`.  You can also inspect the source in
IPython via the handy `mlab.test_contour3d??`.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

