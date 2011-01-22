
Figures, legends, camera and decorations
-----------------------------------------

Handling several figures
~~~~~~~~~~~~~~~~~~~~~~~~~

All mlab functions operate on the current scene, that we also call
:func:`figure`, for compatibility with matlab and pylab. The different
figures are indexed by key that can be an integer or a string. A call to
the :func:`figure` function giving a key will either return the corresponding
figure, if it exists, or create a new one. The current figure can be
retrieved with the :func:`gcf` function. It can be refreshed using the
:func:`draw` function, saved to a picture file using :func:`savefig` and 
cleared using :func:`clf`.


Figure decorations
~~~~~~~~~~~~~~~~~~~~

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
:func:`orientation_axes`. 

.. warning:: The :func:`orientation_axes` was named `orientationaxes`
   before release 3.2.

Moving the camera
~~~~~~~~~~~~~~~~~~~~

The position and direction of the camera can be set using the :func:`view`
function. They are described in terms of Euler angles and distance to a
focal point. The :func:`view` function tries to guess the right roll angle 
of the camera for a pleasing view, but it sometimes fails. The :func:`roll`
explicitly sets the roll angle of the camera (this can be achieve
interactively in the scene by pressing down the control key, while
dragging the mouse, see :ref:`interaction-with-the-scene`).

The :func:`view` and :func:`roll` functions return the current values of
the different angles and distances they take as arguments. As a result, the
view point obtained interactively can be stored and reset using::

    # Store the information
    view = mlab.view()
    roll = mlab.roll()

    # Reposition the camera
    mlab.view(*view)
    mlab.roll(roll)

.. topic:: Rotating the camera around itself

    You can also rotate the camera around itself using the `roll`, `yaw`
    and `pitch` methods of the camera object. This moves the focal point::

        f = mlab.gcf()
        camera = f.scene.camera
        camera.yaw(45)

   Unlike the :func:`view` and :func:`roll` function, the angles
   are incremental, and not absolute.

.. topic:: Modifying zoom and view angle

   The camera is entirely defined by its position, its focal point, and
   its view angle (attributes 'position', 'focal_point', 'view_angle').
   The camera method 'zoom' changes the view angle incrementally by the 
   specify ratio, where as the method 'dolly' translates the camera along
   its axis while keeping the focal point constant. The :func:`move`
   function can also be useful in these regards.

.. note:: Camera parallel scale

    In addition to the information returned and set by mlab.view and
    mlab.roll, a last parameter is needed to fully define the view point:
    the parallel scale of the camera, that control its view angle. It can
    be read (or set) with the following code::

        f = mlab.gcf()
        camera = f.scene.camera
        cam.parallel_scale = 9

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

