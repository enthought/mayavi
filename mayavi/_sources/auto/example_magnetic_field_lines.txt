

.. _example_magnetic_field_lines:

Magnetic field lines example
--------------------------------------------------------------------


This example uses the streamline module to display field lines of a
magnetic dipole (a current loop).

This example requires scipy.

The magnetic field from an arbitrary current loop is calculated from
eqns (1) and (2) in Phys Rev A Vol. 35, N 4, pp. 1535-1546; 1987.

To get a prettier result, we use a fairly large grid to sample the
field. As a consequence, we need to clear temporary arrays as soon as
possible.

For a more thorough example of magnetic field calculation and
visualization with Mayavi and scipy, see
:ref:`example_magnetic_field`.


.. image:: ../generated_images/example_magnetic_field_lines.jpg
    :align: center



**Python source code:** :download:`magnetic_field_lines.py`

.. literalinclude:: magnetic_field_lines.py
    :lines: 18-


    