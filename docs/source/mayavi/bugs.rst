.. _known_bugs:

Known bugs and issues
======================

The Known Issues section contains those items that are big and
important but are not currently actively worked on, because they need
a lot of effort or there is no solution yet for them. For a more detailed
list of issues and bugs please check the list in github_


  * **Display bugs:** Mayavi, and VTK, heavily use hardware rendering, as a
    result are very sensitive to hardware rendering bugs. Common
    issues include surfaces showing up as black instead of colored
    (mostly on windows or in virtual machines, I believe), z-ordering
    bugs where hidden triangles are displayed in front of the triangles
    that should hide them (a common bug on Linux with intel graphics
    cards), or the rendering windows becoming grey when the focus is
    moved out (often seen on Linux, when compiz is enabled). The
    solution is most often simply to turn off hardware rendering in the
    system settings (turn off compiz under Linux) or change
    graphics-card drivers (under Linux, try switching between the open
    source one, and the proprietary one).

.. _github: https://github.com/enthought/mayavi/issues
