

.. currentmodule:: mayavi.mlab

.. note::

    This section is only a reference describing the function, please see
    the chapter on :ref:`simple-scripting-with-mlab` for an introduction to
    mlab and how to interact with and assemble the functions of `mlab`.

    Please see the section on :ref:`running-mlab-scripts` for
    instructions on running the examples.

Figure handling functions
=========================

clf
~~~

.. function:: clf(figure=None)

    Clear the current figure.
    
    You can also supply the figure that you want to clear.
    

    


close
~~~~~

.. function:: close(scene=None, all=False)

    Close a figure window
    
    close() by itself closes the current figure.
    
    close(num) closes figure number num.
    
    close(name) closes figure named name.
    
    close(figure), where figure is a scene instance, closes that
    figure.
    
    close(all=True) closes all figures controlled by mlab
    

    


draw
~~~~

.. function:: draw(figure=None)

    Forces a redraw of the current figure.
    

    


figure
~~~~~~

.. function:: figure(figure=None, bgcolor=None, fgcolor=None, engine=None, size=(400, 350))

    Creates a new scene or retrieves an existing scene. If the mayavi
    engine is not running this also starts it.
    
    **Keyword arguments**
    
        :figure: The name of the figure, or handle to it.
    
        :bgcolor: The color of the background (None is default).
    
        :fgcolor: The color of the foreground, that is the color of all text
                  annotation labels (axes, orientation axes, scalar bar
                  labels). It should be sufficiently far from `bgcolor`
                  to see the annotation texts. (None is default).
    
        :engine: The mayavi engine that controls the figure.
    
        :size: The size of the scene created, in pixels. May not apply
               for certain scene viewer.
    

    


gcf
~~~

.. function:: gcf(engine=None)

    Return a handle to the current figure.
    
    You can supply the engine from which you want to retrieve the
    current figure, if you have several mayavi engines.
    

    


savefig
~~~~~~~

.. function:: savefig(filename, size=None, figure=None, magnification='auto', **kwargs)

    Save the current scene.
    The output format are deduced by the extension to filename.
    Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
    oogl (geomview), iv (OpenInventor), wrl, vrml, obj (wavefront),
    x3d, pov (povray).
    
    **Parameters**
    
    :size: the size of the image created (unless magnification is
           set, in which case it is the size of the window used
           for rendering).
    
    :figure: the figure instance to save to a file.
    
    :magnification: the magnification is the scaling between the
                    pixels on the screen, and the pixels in the
                    file saved. If you do not specify it, it will be
                    calculated so that the file is saved with the
                    specified size. If you specify a magnification,
                    Mayavi will use the given size as a screen size,
                    and the file size will be 'magnification * size'.
    
    **Notes**
    
    If the size specified is larger than the window size, and no
    magnification parameter is passed, the magnification of the scene
    is changed so that the image created has the requested size.
    Please note that if you are trying to save images with sizes
    larger than the window size, there will be additional computation
    cost.
    
    Any extra keyword arguments are passed along to the respective
    image format's save method.
    

    


screenshot
~~~~~~~~~~

.. function:: screenshot(figure=None, mode='rgb', antialiased=False)

    Return the current figure pixmap as an array.
    
    **Parameters**
    
    :figure: a figure instance or None, optional
        If specified, the figure instance to capture the view of.
    :mode: {'rgb', 'rgba'}
        The color mode of the array captured.
    :antialiased: {True, False}
        Use anti-aliasing for rendering the screenshot.
        Uses the number of aa frames set by
        figure.scene.anti_aliasing_frames
    
    **Notes**
    
    On most systems, this works similarly to taking a screenshot of
    the rendering window. Thus if it is hidden by another window, you
    will capture the other window. This limitation is due to the
    heavy use of the hardware graphics system.
    
    **Examples**
    
    This function can be useful for integrating 3D plotting with
    Mayavi in a 2D plot created by matplotlib.
    
    >>> from mayavi import mlab
    >>> mlab.test_plot3d()
    >>> arr = mlab.screenshot()
    >>> import pylab as pl
    >>> pl.imshow(arr)
    >>> pl.axis('off')
    >>> pl.show()
    
    

    


sync_camera
~~~~~~~~~~~

.. function:: sync_camera(reference_figure, target_figure)

    Synchronise the camera of the target_figure on the camera of the
    reference_figure.
    

    

