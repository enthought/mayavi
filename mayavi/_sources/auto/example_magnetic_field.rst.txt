

.. _example_magnetic_field:

Magnetic field example
--------------------------------------------


An example mixing numerical caculation and 3D visualization of the
magnetic field created by an arbitrary number of current loops.

The goal of this example is to show how Mayavi can be used with scipy to
debug and understand physics and electromagnetics computation.

The field is calculated for an arbitrary number of current loops using the
corresponding exact formula. The coils are plotted in 3D with a synthetic
view of the magnetic_field. A VectorCutPlane is used as it enables good
inspection of the magnetic field.

This example originated from a real-life case of coil design in Python (
Atomic sources for long-time-of-flight interferometric inertial sensors,
G. Varoquaux, http://tel.archives-ouvertes.fr/tel-00265714/, page 148).

For another visualization of magnetic field, see the
:ref:`example_magnetic_field_lines`.


**Python source code:** :download:`magnetic_field.py`

.. literalinclude:: magnetic_field.py
    :lines: 20-


    