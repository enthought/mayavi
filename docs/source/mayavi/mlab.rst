.. _simple-scripting-with-mlab:

``mlab``: Python scripting for 3D plotting
============================================

.. topic:: Section summary

    This section describes the `mlab` API, for use of Mayavi as a simple
    plotting in scripts or interactive sessions. This is the main entry
    point for people interested in doing 3D plotting à la Matlab or IDL
    in Python. If you are interested in a list of all the
    functions exposed in mlab, see the :ref:`mlab-reference`.

.. currentmodule:: mayavi.mlab

The :mod:`mayavi.mlab` module, that we call mlab, provides an easy
way to visualize data in a script or from an interactive prompt with 
one-liners as done in the matplotlib_ ``pylab`` interface but with an
emphasis on 3D visualization using Mayavi2. This allows users to perform
quick 3D visualization while being able to use Mayavi's powerful
features.

Mayavi's mlab is designed to be used in a manner well-suited to
scripting and does not present a fully object-oriented API.
It is can be used interactively with IPython_.

.. warning:: 

    When using IPython with mlab, as in the following examples, IPython must 
    be invoked with the ``-wthread`` command line option like so::

         $ ipython -wthread

    Or, for IPython recent version (0.11 and above)::

         $ ipython --gui=wx

    If you are using the `Enthought Python Distribution
    <http://www.enthought.com/products/epd.php>`_, or the latest 
    `Python(x,y) <http://www.pythonxy.com>`_ distribution, the Pylab menu
    entry will start ipython with the right switch. In older release of
    Python(x,y) you need to start "Interactive Console (wxPython)".

    For more details on using mlab and running scripts, read the section
    :ref:`running-mlab-scripts`

.. _matplotlib: http://matplotlib.sf.net

.. _IPython: http://ipython.scipy.org

In this section, we first introduce simple plotting functions, to create
3D objects as representations of `numpy` arrays. Then we explain how
properties such as color or glyph size can be modified or used to
represent data, we show how the visualization created through `mlab` can
be modified interactively with dialogs, we show how scripts and
animations can be ran. Finally, we expose a more advanced use of `mlab`
in which full visualization pipeline are built in scripts, and we give
some detailed examples of applying these tools to visualizing volumetric
scalar and vector data.

.. contents:: Section contents
    :depth: 1
    :local:

..
 .. topic:: **Section contents**
 
    .. toctree::
 
        mlab_demo
        mlab_3d_plotting_functions
        mlab_changing_object_looks
        mlab_figures_decorations
        mlab_running_scripts
        mlab_animating
        mlab_pipeline
        mlab_case_studies

.. include:: mlab_demo.rst

.. include:: mlab_3d_plotting_functions.rst

.. include:: mlab_changing_object_looks.rst

.. include:: mlab_figures_decorations.rst

.. include:: mlab_running_scripts.rst

.. include:: mlab_animating.rst

.. include:: mlab_pipeline.rst

.. include:: mlab_case_studies.rst

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

