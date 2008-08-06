

.. currentmodule:: enthought.mayavi.mlab

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Figure decoration functions
===========================

zlabel
~~~~~~

.. function:: zlabel(text, object=None)

    
    Creates a set of axes if there isn't already one, and sets the z label
    
    **Keyword arguments**
    
        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    

    


ylabel
~~~~~~

.. function:: ylabel(text, object=None)

    
    Creates a set of axes if there isn't already one, and sets the y label
    
    **Keyword arguments**:
    
    
        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    

    


scalarbar
~~~~~~~~~

.. function:: scalarbar(object=None, title=None, orientation=None)

    Adds a colorbar for the scalar color mapping of the given object.
    
    If no object is specified, the first object with scalar data in the scene
    is used.
    
    **Keyword arguments**:
    
        :object: Optional object to get the scalar color map from
    
        :title: The title string
    
        :orientation: Can be 'horizontal' or 'vertical'
    

    


colorbar
~~~~~~~~

.. function:: colorbar(object=None, title=None, orientation=None)

    Adds a colorbar for the color mapping of the given object.
    
    If the object has scalar data, the scalar color mapping is
    represented. Elsewhere the vector color mapping is represented, if
    available.
    If no object is specified, the first object with a color map in the scene
    is used.
    
    **Keyword arguments**:
    
        :object: Optional object to get the color map from
    
        :title: The title string
    
        :orientation: Can be 'horizontal' or 'vertical'
    

    


xlabel
~~~~~~

.. function:: xlabel(text, object=None)

    
    Creates a set of axes if there isn't already one, and sets the x label
    
    **Keyword arguments**:
    
        :object:  The object to apply the module to, if not the whole scene
                  is searched for a suitable object.
    

    


vectorbar
~~~~~~~~~

.. function:: vectorbar(object=None, title=None, orientation=None)

    Adds a colorbar for the vector color mapping of the given object.
    
    If no object is specified, the first object with vector data in the scene
    is used.
    
    **Keyword arguments**
    
        :object: Optional object to get the vector color map from
    
        :title: The title string
    
        :orientation: Can be 'horizontal' or 'vertical'
    

    

