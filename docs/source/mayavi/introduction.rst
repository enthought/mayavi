Introduction
============

.. topic:: Section summary

    This section gives a quick summary of what is Mayavi, and should help
    you understand where, in this manual, find relevent information to
    your use case.

Mayavi2_ seeks to provide easy and interactive visualization of 3D
data.  It does this by the following:

    * an (optional) rich user interface with dialogs to interact with
      all data and objects in the visualization.

    * a simple and clean scripting interface in Python_, including ready
      to use 3D visualization functionality similar to matlab or
      `matplotlib`_ (using :ref:`mlab <simple-scripting-with-mlab>`), or 
      an object-oriented programming interface.

    * harnesses the power of VTK_ without forcing you to learn it.

Additionally, Mayavi2 strives to be a reusable tool that can be embedded
in your libraries and applications in different ways or be combined with
the Envisage_ application-building framework to assemble domain-specific
tools.

.. _Mayavi2: https://svn.enthought.com/enthought/wiki/MayaVi
.. _Mayavi: https://svn.enthought.com/enthought/wiki/MayaVi
.. _Python: http://www.python.org
.. _VTK: http://www.vtk.org
.. _envisage: https://svn.enthought.com/enthought/wiki/Envisage
.. _matplotlib: http://matplotlib.sf.net

What is Mayavi2?
----------------

Mayavi2 is a general purpose, cross-platform tool for 3-D scientific
data visualization. Its features include:

    * Visualization of scalar, vector and tensor data in 2 and 3
      dimensions.

    * Easy scriptability using Python.

    * Easy extendability via custom sources, modules, and data filters.

    * Reading several file formats: VTK_ (legacy and XML), PLOT3D,
      etc.

    * Saving of visualizations.

    * Saving rendered visualization in a variety of image formats.

    * Convenient functionality for rapid scientific plotting via mlab
      (see :ref:`simple-scripting-with-mlab`).

Unlike its predecessor Mayavi1_, Mayavi2 has been designed with
scriptability and extensibility in mind from the ground up.  Mayavi2
provides a ``mayavi2`` application which is usable by itself.  However,
Mayavi2 may also be used as a plotting engine, in scripts, like with
matplotlib or gnuplot, as well as a library for interactive
visualizations in any other application.  It may also be used as an
`Envisage`_ plugin which allows it to be embedded in other `Envisage`_
based applications natively.

.. _Mayavi1: http://mayavi.sourceforge.net


Technical details
-----------------

Mayavi2 provides a general purpose visualization engine based on a
pipeline architecture similar to that used in VTK.  Mayavi2 also provides
an `Envisage`_ plug-in for 2D/3D scientific data visualization. Mayavi2
uses the Enthought Tool Suite (ETS_) in the form of Traits_, TVTK_ and
Envisage_. Here are some of its features:

    * Pythonic API which takes full advantage of Traits_.

    * Mayavi can work natively and transparently with numpy_ arrays
      (this is thanks to its use of TVTK_).

    * Easier to script than Mayavi-1 due to a much cleaner MVC_ design.

    * Easy to extend with added sources, components, modules and data
      filters.

    * Provides an `Envisage`_ plugin. This implies that it is:

          - easy to use other Envisage plugins in Mayavi.  For
            example, Mayavi provides an embedded Python shell.  This
            is an Envisage plugin and requires one line of code to
            include in Mayavi.

          - easy to use Mayavi inside Envisage based applications.
            Thus, any envisage based application can readily use
            the mayavi plugin and script it to visualize data.

    * wxPython/Qt4 based GUI (thanks entirely to Traits, PyFace and
      Envisage).  It is important to note that there is no wxPython or
      Qt4 code used directly in the Mayavi source. 

    * A non-intrusive reusable design. It is possible to use Mayavi
      without a wxPython or Qt4 based UI.


.. _ETS: http://code.enthought.com/projects/tool-suite.php
.. _Traits: https://svn.enthought.com/enthought/wiki/Traits
.. _TVTK: https://svn.enthought.com/enthought/wiki/TVTK
.. _MVC: http://en.wikipedia.org/wiki/Model-view-controller
.. _numpy: http://numpy.scipy.org

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

