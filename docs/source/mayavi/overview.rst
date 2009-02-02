.. _an-overview-of-mayavi:

An overview of Mayavi
=====================

All the following sections assume you have a working Mayavi
:ref:`installation`.

Using Mayavi as an application, or a library?
-----------------------------------------------

As a user there are three primary ways to use Mayavi:

  1. Use the ``mayavi2`` application completely graphically.  More
     information on this is in the :ref:`using-the-mayavi-application` 
     section.

  2. Use Mayavi as a plotting engine from simple Python scripts, for
     example from Ipython, in combination with numpy.  The
     ``mlab`` scripting API provides a simple way of using Mayavi in
     batch-processing scripts, see :ref:`simple-scripting-with-mlab` for
     more information on this.

  3. Script the Mayavi application from Python. The Mayavi application 
     itself features a powerful and general purpose scripting API that
     can be used to adapt it to your needs.

      a. You can script Mayavi while using the ``mayavi2`` application
         in order to automate tasks and extend Mayavi's behavior.

      b. You can script Mayavi from your own Python based application.

      c. You can embed Mayavi into your application in a variety of
         ways either using Envisage_ or otherwise.

     More details on this are available in the 
     :ref:`advanced-scripting-with-mayavi` chapter.


Scenes and visualization objects: the pipeline model
------------------------------------------------------

Mayavi uses a pipeline architecture like VTK_.  As far as a user is
concerned this basically boils down to a simple hierarchy.

  * The user visualizes data on a `Scene` -- this is an area
    where the 3D visualization is performed.  In the interactive
    application, new scenes may be created by using the 
    `File->New->VTK Scene` menu.

  * On each scene the user loads data (either using a file or created
    from a script). Any number of data files or data objects may be
    opened; these objects are called **data sources**.

  * This data is optionally processed using :ref:`filters` that operate on
    the data and visualized using visualization :ref:`modules`.  The
    Filters and Modules are accessible in the application via the 
    `Visualize` menu on the UI or context menus on the pipeline. They may 
    also be instantiated as Python objects when scripting Mayavi.


Loading data into Mayavi
-------------------------

Mayavi is a scientific data visualizer. There are two primary ways to
make your data available to it:

  1. Store your data in a supported file format like VTK legacy or 
     VTK XML files etc. See `VTK file formats`_ for more information on the 
     VTK formats. These files can be loaded in the interactive application 
     using the menus.

  2. Generate a TVTK dataset via numpy_ arrays or any other sequence.
     This is easiest done by using the scripting APIs, for instance `mlab`
     (see the paragraph on 
     :ref:`creating data sources with mlab <mlab_data_source>`, or simply
     the 3D plotting functions: :ref:`mlab_plotting_functions`).

Aternatively, if you whish to gain a deeper understanding by
creating VTK data structures or files, more information on datasets in general
is available in the :ref:`data-structures-used-by-mayavi` section.

.. _VTK file formats: http://www.vtk.org/pdf/file-formats.pdf
.. _numpy: http://numpy.scipy.org
.. _VTK: http://www.vtk.org
.. _envisage: https://svn.enthought.com/enthought/wiki/Envisage
.. _TVTK: https://svn.enthought.com/enthought/wiki/TVTK

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

