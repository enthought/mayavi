

.. currentmodule:: mayavi.tools.pipeline

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Tools
=====

add_dataset
~~~~~~~~~~~

.. function:: add_dataset(dataset, name='', **kwargs)

    Add a dataset object to the Mayavi pipeline.
    
    **Parameters**
    
    :dataset: a tvtk/vtk dataset/tvtk/VTK Algorithm, or a Mayavi source. The
              dataset added to the Mayavi pipeline
    
    :figure: a figure identifier number or string, None or False, optional.
    
            If no `figure` keyword argument is given, the data
            is added to the current figure (a new figure if created if
            necessary).
    
            If a `figure` keyword argument is given, it should either the name
            the number of the figure the dataset should be added to, or None,
            in which case the data is not added to the pipeline.
    
            If figure is False, a null engine is created. This null
            engine does not create figures, and is mainly usefull for
            tensting, or using the VTK algorithms without visualization.
    
    **Returns**
    
    The corresponding Mayavi source is returned.
    
    

    


add_module_manager
~~~~~~~~~~~~~~~~~~

.. function:: add_module_manager(object)

    Add a module-manager, to control colors and legend bars to the
    given object.
    

    


get_vtk_src
~~~~~~~~~~~

.. function:: get_vtk_src(mayavi_object, stop_at_filter=True)

    Goes up the Mayavi pipeline to find the data sources of a given
    object.
    
    **Parameters**
    
    :object: any Mayavi visualization object
    
    :stop_at_filter: optional boolean flag: if True, the first object
                     exposing data found going up the pipeline is
                     returned. If False, only the source itself
                     is returned.
    
    **Returns**
    
    :sources: List of vtk data sources (vtk data sources, and not
              Mayavi source objects).
    
    **Notes**
    
    This function traverses the Mayavi pipeline. Thus the input
    object 'mayavi_object' should already be added to the pipeline.
    

    


set_extent
~~~~~~~~~~

.. function:: set_extent(module, extents)

    Attempts to set the physical extents of the given module.
    
    The extents are given as (xmin, xmax, ymin, ymax, zmin, zmax).
    This does not work on an image plane widget, as this module does
    not have an actor.
    
    Once you use this function on a module, be aware that other
    modules applied on the same data source will not share the same
    scale. Thus for instance an outline module will not respect the
    outline of the actors whose extent you modified. You should pass
    in the same "extents" parameter for this to work.You can have a
    look at the wigner.py example for a heavy use of this
    functionality.
    
    **Note**
    
    This function does not work on some specific modules, such as
    Outline, Axes, or ImagePlaneWidget. For Outline and Axes, use the
    extent keyword argument of mlab.pipeline.outline and
    mlab.pipeline.axes.
    

    


traverse
~~~~~~~~

.. function:: traverse(node)

    Generator to traverse a tree accessing the nodes' children
    attribute.
    
    **Example**
    
    Here is a simple example printing the names of all the objects in
    the pipeline::
    
        for obj in mlab.pipeline.traverse(mlab.gcf()):
            print obj.name
    
    

    

