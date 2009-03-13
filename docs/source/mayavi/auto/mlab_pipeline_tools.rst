

.. currentmodule:: enthought.mayavi.tools.pipeline

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Tools
=====

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
    functionnality.
    

    


add_dataset
~~~~~~~~~~~

.. function:: add_dataset(dataset, name='', **kwargs)

    Add a dataset object to the Mayavi pipeline.
    
    The dataset can be either a tvtk dataset, or a mayavi source.
    
    If no `figure` keyword argument is given, the data is added to the
    current figure (a new figure if created if necessary).
    
    If a `figure` keyword argument is given, it should either the name
    name or the number of the figure the dataset should be added to, or None,
    in which case the data is not added to the pipeline.
    
    The corresponding Mayavi source is returned.
    

    


traverse
~~~~~~~~

.. function:: traverse(node)

    
    ::
     Generator to traverse a tree accessing the nodes children
            attribute.
    
            **Example**
    
            ::
                for obj in mlab.pipeline.traverse(mlab.gcf()):
                    print obj.name
    
    

    


add_module_manager
~~~~~~~~~~~~~~~~~~

.. function:: add_module_manager(object)

    Add a module-manager, to control colors and legend bars to the
    given object.
    

    

