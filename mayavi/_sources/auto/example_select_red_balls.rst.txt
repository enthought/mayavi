

.. _example_select_red_balls:

Select red balls example
--------------------------------------------


This example shows how to use a callback to select a red ball amongst white
balls.

The example uses the figure method 'on_mouse_pick', added in Mayavi
3.4, to register a callback when the left mouse is pressed. The callback
is called with a picker, enabling to identify the object selected.
Specifically, actors are selected, each object is represented on the scene
via actors. The selected actors can be found in 'picker.actors'. In this
example, we have plotted red balls and white ball. We want to select the
red balls, and thus test if any actor in picker.actors corresponds to an
actor of red balls.

To identify which ball has been selected, we use the point id. However,
each ball is represented by several points. Thus we need to retrieve the
number of points per ball, and divide the point id by this number.

We use an outline to display which ball was selected by positioning it on
the corresponding ball.


**Python source code:** :download:`select_red_balls.py`

.. literalinclude:: select_red_balls.py
    :lines: 21-


    