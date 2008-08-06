

.. currentmodule:: enthought.mayavi.mlab

.. note::

    This section is only a reference, please see chapter on
    :ref:`simple-scripting-with-mlab` for an introduction to mlab.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Figure handling functions
=========================

figure
~~~~~~

.. function:: figure(name=None, bgcolor=None, fgcolor=None, engine=None, size=(400, 350))

    Creates a new scene or retrieves an existing scene. If the mayavi
    engine is not running this also starts it.
    
    **Keyword arguments**
    
        :name: The name of the scene.
    
        :bgcolor: The color of the background (None is default).
    
        :fgcolor: The color of the foreground (None is default).
    
        :engine: The mayavi engine that controls the figure.
    
        :size: The size of the scene created, in pixels. May not apply
               for certain scene viewer.
    

    


savefig
~~~~~~~

.. function:: savefig(filename, size=None, figure=None, **kwargs)

    Save the current scene.
    The output format are deduced by the extension to filename.
    Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
    oogl (geomview), iv (OpenInventor), vrml, obj (wavefront)
    
    If an additional size (2-tuple) argument is passed the window
    is resized to the specified size in order to produce a
    suitably sized output image.  Please note that when the window
    is resized, the window may be obscured by other widgets and
    the camera zoom is not reset which is likely to produce an
    image that does not reflect what is seen on screen.
    
    Any extra keyword arguments are passed along to the respective
    image format's save method.
    

    


gcf
~~~

.. function:: gcf(engine=None)

    Return a handle to the current figure.
    
    You can supply the engine from which you want to retrieve the
    current figure, if you have several mayavi engines.
    

    


clf
~~~

.. function:: clf(figure=None)

    Clear the current figure.
    
    You can also supply the figure that you want to clear.
    

    


draw
~~~~

.. function:: draw(figure=None)

    Forces a redraw of the current figure.
    

    

