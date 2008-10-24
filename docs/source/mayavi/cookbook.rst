Mayavi2 Cookbook
=================

These are a collection of useful hints and recipes for various tasks.


Animating a series of images
-----------------------------

Lets say you have a stack of PNG or JPEG files that are numbered
serially that you want to animate on a mayavi scene.  Here is a simple
script (called ``img_movie.py``)::
    
    # img_movie.py
    from enthought.pyface.timer.api import Timer

    def animate(src, N=10):
        for j in range(N):
            for i in range(len(src.file_list)):
                src.timestep = i
                yield

    if __name__ == '__main__':
        src = mayavi.engine.scenes[0].children[0]
        animator = animate(src)
        t = Timer(250, animator.next)

The ``Timer`` class lets you call a function without blocking the
running user interface.  The first argument is the time after which the
function is to be called again in milliseconds.  The ``animate``
function is a generator and changes the timestep of the source.  This
script will animate the stack of images 10 times.  The script animates
the first data source by default.  This may be changed easily.

To use this script do this::
    
    $ mayavi2 -d your_image000.png -m ImageActor -x img_movie.py


Scripting from the command line
--------------------------------

The mayavi application allows for very powerful
:ref:`command-line-arguments` that lets you build a complex
visualization from your shell.  What follow is a bunch of simple
examples illustrating these.

The following example creates a ``ParametricSurface`` source and then
visualizes glyphs on its surface colored red::

    $ mayavi2 -d ParametricSurface -m Glyph \
    -s"glyph.glyph.scale_factor=0.1" \
    -s"glyph.color_mode='no_coloring'" \
    -s"actor.property.color = (1,0,0)"

Note that ``-s"string"`` applies the string on the last object (also
available as ``last_obj``), which is the glyph. 

This example turns off coloring of the glyph and changes the glyph to
display::

    $ mayavi2 -d ParametricSurface -m Glyph\
    -s"glyph.glyph.scale_factor=0.1" \
    -s"glyph.color_mode='no_coloring'" \
    -s"glyph.glyph_source.glyph_source = last_obj.glyph.glyph_source.glyph_list[-1]"

Note the use of ``last_obj`` in the above.


Texture mapping actors
-----------------------

Here is a simple example showing how to texture map an iso-surface with
the data that ships with the mayavi sources (the data files are in the
examples directory)::

    $ mayavi2 -d examples/tvtk/images/masonry.jpg \
     -d examples/mayavi/data/heart.vti \
     -m IsoSurface \
     -s"actor.mapper.scalar_visibility=False" \
     -s"actor.enable_texture=True"\
     -s"actor.tcoord_generator_mode='cylinder'"\
     -s"actor.texture_source_object=script.engine.current_scene.children[0]"

It should be relatively straightforward to change this example to use a
``ParametricSurface`` instead and any other image of your choice.
Notice how the texture image (``masonry.jpg``) is set in the last line
of the above.  The image reader is the first child of the current scene
and we set it as the ``texture_source_object`` of the isosurface actor.


Shifting data and plotting
---------------------------

Sometimes you need to shift/transform your input data in space and
visualize that in addition to the original data.  This is useful when
you'd like to do different things to the same data and see them on the
same plot.  This can be done with Mayavi using the ``TransformData`` filter
for ``StructuredGrid``, ``PolyData`` and ``UnstructuredGrid`` datasets.
Here is an example using the ``ParametricSurface`` data source::

   $ mayavi2 -d ParametricSurface \
     -m Outline -m Surface \
     -f TransformData -s "transform.translate(1,1,1)" \
     -s "widget.set_transform(last_obj.transform)" \
     -m Outline -m Surface

If you have an ``ImageData`` dataset then you can change the origin,
spacing and extents alone by using the ``ImageChangeInformation``
filter.  Here is a simple example with the standard mayavi image data::

    $ mayavi2 -d examples/mayavi/heart.vti -m Outline \
    -m ImagePlaneWidget \
    -f ImageChangeInformation \ 
    -s "filter.origin_translation=(20,20,20)" \
    -m Outline -m ImagePlaneWidget

