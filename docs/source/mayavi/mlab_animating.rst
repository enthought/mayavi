
.. _mlab-animating-data:

Animating the data
------------------

Often it isn't sufficient to just plot the data.  You may also want to
change the data of the plot and update the plot without having to
recreate the entire visualization, for instance to do animations, or in
an interactive application. Indeed, recreating the entire visualization
is very inefficient and leads to very jerky looking
animations. To do this, mlab provides a very convenient way to change
the data of an existing mlab visualization.  Consider a very simple
example.  The `mlab.test_simple_surf_anim` function has this code::

    import numpy as np
    from mayavi import mlab
    x, y = np.mgrid[0:3:1,0:3:1]
    s = mlab.surf(x, y, np.asarray(x*0.1, 'd'))

    for i in range(10):
        s.mlab_source.scalars = np.asarray(x*0.1*(i+1), 'd')

The first two lines define a simple plane and view that.  The next three
lines animate that data by changing the scalars producing a plane that
rotates about the origin.  The key here is that the `s` object above has
a special attribute called `mlab_source`.  This sub-object allows us to
manipulate the points and scalars.  If we wanted to change the `x` values
we could set that too by::

    s.mlab_source.x = new_x

The only thing to keep in mind here is that the shape of `x` should not
be changed.

Note that many of the examples discussed here may not appear to be
animated at all and you may just see the final state of the animation.
If you save a screenshot of the image at each stage of the animation,
you would get the correct result.  However, you will not get the
visual effect on screen.  See the section
:ref:`animating_a_visualization` to learn more on the use of the
`@animate` decorator (:func:`mayavi.mlab.animate`) to achieve this.
We show a small example here, where we rewrite the above to animate
nicely::

    import numpy as np
    from mayavi import mlab
    x, y = np.mgrid[0:3:1,0:3:1]
    s = mlab.surf(x, y, np.asarray(x*0.1, 'd'))

    @mlab.animate
    def anim():
        for i in range(10):
            s.mlab_source.scalars = np.asarray(x*0.1*(i+1), 'd')
            yield

    anim()
    mlab.show()


In the above, note that we wrap the iteration in a function which is a
generator and decorate it with the `@mlab.animate` decorator.

If multiple values have to be changed, you can use the `set` method of
the `mlab_source` to set them as shown in the more complicated example
below::

    # Produce some nice data.
    n_mer, n_long = 6, 11
    pi = np.pi
    dphi = pi/1000.0
    phi = np.arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
    mu = phi*n_mer
    x = np.cos(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
    y = np.sin(mu)*(1+np.cos(n_long*mu/n_mer)*0.5)
    z = np.sin(n_long*mu/n_mer)*0.5

    # View it.
    l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')

    # Now animate the data.
    ms = l.mlab_source
    for i in range(10):
        x = np.cos(mu)*(1+np.cos(n_long*mu/n_mer +
                                          np.pi*(i+1)/5.)*0.5)
        scalars = np.sin(mu + np.pi*(i+1)/5)
        ms.trait_set(x=x, scalars=scalars)

Notice the use of the `set` method above. With this method, the
visualization is recomputed only once.  In this case, the shape of the
new arrays has not changed, only their values have.  If the shape of the
array changes then one should use the `reset` method as shown below::

    x, y = np.mgrid[0:3:1,0:3:1]
    s = mlab.surf(x, y, np.asarray(x*0.1, 'd'),
                  representation='wireframe')
    # Animate the data.
    fig = mlab.gcf()
    ms = s.mlab_source
    for i in range(5):
        x, y = np.mgrid[0:3:1.0/(i+2),0:3:1.0/(i+2)]
        sc = np.asarray(x*x*0.05*(i+1), 'd')
        ms.reset(x=x, y=y, scalars=sc)
        fig.scene.reset_zoom()

Many standard examples for animating data are provided with mlab.  Try
the examples with the name `mlab.test_<name>_anim`, i.e. where the name
ends with an `_anim` to see how these work and run.



.. note::

    It is important to remember distinction between `set` and `reset`.
    Use `set` or directly set the attributes (`x`, `y`, `scalars` etc.)
    when you are not changing the shape of the data but only the values.
    Use `reset` when the arrays are changing shape and size.  Reset
    usually regenerates all the data and can be inefficient when
    compared to `set` or directly setting the traits.

.. warning::

    When creating a Mayavi pipeline, as explained in the following
    subsection, instead of using ready-made plotting function, the
    `mlab_source` attribute is created only on sources created via
    `mlab`. Pipeline created entirely using `mlab` will present this
    attribute.

.. note::

    If you are animating several plot objects, each time you modify the
    data with there `mlab_source` attribute, Mayavi will trigger a
    refresh of the scene. This operation might take time, and thus slow
    your animation. In this case, the tip
    :ref:`acceleration_mayavi_scripts` may come in handy.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
