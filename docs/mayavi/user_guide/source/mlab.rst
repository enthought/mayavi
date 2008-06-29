.. _simple-scripting-with-mlab:

Simple Scripting with ``mlab``
===============================

.. currentmodule:: enthought.mayavi.mlab

The ``enthought.mayavi.mlab`` module, that we call mlab, provides quick
one-liners as done in the matplotlib_ ``pylab`` interface but with an
emphasis on 3D visualization using Mayavi2.  This allows users to perform
quick 3D visualization while being able to use Mayavi's powerful
features.

Mayavi's mlab is designed to be used in a manner well suited to
scripting and does not present a fully object-oriented API (this is
similar to matplotlib's ``pylab``).  It is best used interactively with
IPython_.  IPython must be invoked with the ``-wthread`` command line
option like so::

 $ ipython -wthread

.. _matplotlib: http://matplotlib.sf.net

.. _IPython: http://ipython.scipy.org

A demo
-------

Once started, here is a pretty example showing a spherical harmonic::

 from numpy import *
 from enthought.mayavi import mlab
 # Create the data.
 dphi, dtheta = pi/250.0, pi/250.0
 [phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
 m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
 r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
 x = r*sin(phi)*cos(theta)
 y = r*cos(phi)
 z = r*sin(phi)*sin(theta);
 # View it.
 f = mlab.figure()
 s = mlab.mesh(x, y, z)

Bulk of the code in the above example is to create the data.  One line
suffices to visualize it.  This produces the following visualization
in a Mayavi window.

.. image:: images/mlab_surf_example.jpg

The data and visualization modules are all created by the single
command ``mesh`` in the above. 
 
Plotting 
---------

The mlab plotting functions take numpy arrays as input, describing the
``x``, ``y``, and ``z`` coordinates of the data. They build full-blown
visualizations: they create the data source, filters if necessary, and
add the visualization modules. Their behavior, and thus the visualization
created, can be fine-tuned through keyword arguments, similarly to pylab.
In addition, they all return the visualization module created, thus
visualization can also be modified by changing the attributes of this
module.

0D and 1D data
~~~~~~~~~~~~~~~

    The :func:`plot3d` and :func:`points3d` functions are respectively used 
    to draw lines, and sets of points, specifying the ``x``, ``y`` and 
    ``z`` coordinates as numpy arrays.

2D data
~~~~~~~~

    A 2D array can be shown as a image using :func:`imshow`, or as a surface 
    with the elevation given by its values using :func:`surf`. The contours 
    (lines) of same values can be plotted using :func:`contour_surf`.

    The :func:`mesh` function also creates surfaces, however, unlike 
    :func:`surf`, the surface is defined by its ``x``, ``y`` and ``z`` 
    coordinates, and more complex surfaces can be created, as in the 
    above example.

3D data
~~~~~~~~

    To plot isosurfaces of a 3D scalar field use :func:`contour3d`. A
    vector field can be represented using :func:`quiver3d`, and the
    trajectories of particles along this field can plotted using :func:`flow`. 


Handling figures
-----------------

All mlab functions operate on the current scene, that we also call
:func:`figure`, for compatibility with matlab and pylab. The different
figures are indexed by key that can be an integer or a string. A call to
the :func:`figure` function giving a key will either return the corresponding
figure, if it exists, or create a new one. The current figure can be
retrieved with the :func:`gcf` function. It can be refreshed using the
:func:`draw` function, saved to a picture file using :func:`savefig` and 
cleared using :func:`clf`.


Figure decorations
-------------------

Axes can be added around a visualization object with the :func:`axes`
function, and the labels can be set using the :func:`xlabel`, :func:`ylabel`
and :func:`zlabel` functions. Similarly, :func:`outline` creates an 
outline around an object. :func:`title` adds a title to the figure.

Color bars can be used to reflect the color maps used to display values
(LUT, or lookup tables, in VTK parlance). :func:`colorbar` creates a color 
bar for the last object created, trying to guess whether to use the vector
data or the scalar data color maps. The :func:`scalarbar` and 
:func:`vectorbar` function scan be used to create color bars specifically 
for scalar or vector data. 

A small *xyz* triad can be added to the figure using 
:func:`orientationaxes`. 

Moving the camera
-------------------

The position and direction of the camera can be set using the :func:`view`
function. They are described in terms of Euler angles and distance to a
focal point. The :func:`view` function tries to guess the right roll angle 
of the camera for a pleasing view, but it sometimes fails. The :func:`roll`
explicitly sets the roll angle of the camera.


Interacting graphically with the visualization
-----------------------------------------------

The Mayavi pipeline tree can be displayed using :func:`show_engine`
command. One can now change the visualization using this dialog by
double-clicking on each object to edit its properties, as described in
other parts of this manual.

In addition, for every object returned by a mlab function,
``this_object.edit_traits()`` brings up a dialog that can be used to
interactively edit the object's properties.


Running Mlab scripts
---------------------

Interactively
~~~~~~~~~~~~~~~

Using `IPython`_ mlab instructions can be run interactively, or in
scripts using `IPython`_'s ``%run`` command.

Mlab can also be used interactively in the Python shell of the mayavi2
application, or in any interactive Python shell of wxPython-based
application (such as other Envisage-based applications, or Stani's
Python editor).

As batch scripts
~~~~~~~~~~~~~~~~~

Mlab commands can be written to a file, to form a script. This script
can be loaded in the Mayavi application using the *File->Open file* menu
entry, and executed using the *File->Refresh code* menu entry or by
pressing ``Control-r``.  It can also be executed during the start of the
Mayavi application using the ``-x`` command line switch.

You can also make your mlab script a normal Python script, that can be
run with ``python my_script.py`` by adding the following lines at the end
of your script::

    from enthought.pyface.api import GUI
    GUI().start_event_loop()

Don't do this when running it in an interactive environment, as it will
freeze your environment.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

