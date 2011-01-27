.. _known_bugs:

Known bugs and issues
======================

Here we list several known bugs along with potential solutions when
available and also those that are currently unresolved with links to the
appropriate tickets.

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

  * **Crash when adding list items**
    https://svn.enthought.com/enthought/ticket/1813 : Crashing list
    editor on Linux with wx backend when adding or removing list items.
    In Mayavi this happens for instance when adding or removing contours.

