.. _running-mlab-scripts:

Running mlab scripts
---------------------

Mlab, like the rest of Mayavi, is an interactive application. If you are
not already in an interactive environment (see next paragraph), to
interact with the figures or the rest of the drawing elements, you need
to use the :func:`show` function. For instance, if you are writing a
script, you need to call :func:`show` each time you want to display one
or more figures and allow the user to interact with them.

Using mlab interactively
~~~~~~~~~~~~~~~~~~~~~~~~~

Using IPython_, mlab instructions can be run interactively, or in
scripts using IPython_'s ``%run`` command::

    In [1]: %run my_script

You need to start IPython_ with the `-wthread` option, that became `--gui=wx` in the recent IPython versions (when installed
with `EPD`_, the `pylab` start-menu link does this for you). In this
environment, the plotting commands are interactive: they have an
immediate effect on the figure, alleviating the need to use the
:func:`show` function. 

.. _EPD: http://www.enthought.com/products/epd.php

Mlab can also be used interactively in the Python shell of the mayavi2
application, or in any interactive Python shell of wxPython-based
application (such as other Envisage-based applications, or SPE, Stani's
Python Editor).

Using together with Matplotlib's pylab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use Matplotlib's pylab with Mayavi's mlab in IPython you
should:

    * if your IPython version is greater than 0.11: start IPython with::

        $ ipython --gui=wx --pylab=wx

    * else, if your IPython version is greater than 0.8.4: start IPython with
      the following options::

        $ ipython -pylab -wthread

    * elsewhere, start IPython with the `-wthread` option::

        $ ipython -wthread

      and **before** importing pylab, enter the following Python
      commands::

        >>> import matplotlib
        >>> matplotlib.use('WxAgg')
        >>> matplotlib.interactive(True)

If you want matplotlib and mlab to work together by default in IPython,
you can change you default matplotlib backend, by editing the
`~/.matplotlib/matplotlibrc` to add the following line::

    backend     : WXAgg

.. topic:: Capturing mlab plots to integrate in pylab

    Starting from Mayavi version 3.4.0, the mlab :func:`screenshot` can
    be used to take a screenshot of the current figure, to integrate in a
    matplotlib plot.

In scripts
~~~~~~~~~~~~~~~~~

Mlab commands can be written to a file, to form a script. This script
can be loaded in the Mayavi application using the *File->Open file* menu
entry, and executed using the *File->Refresh code* menu entry or by
pressing ``Control-r``.  It can also be executed during the start of the
Mayavi application using the ``-x`` command line switch.

As mentioned above, when running outside of an interactive environment,
for instance with `python myscript.py`, you need to call the
:func:`show` function (as shown in the demo_ above) to pause your script
and have the user interact with the figure.

.. _demo:
    :ref:`mlab-demo`

You can also use :func:`show` to decorate a function, and have it run in
the event-loop, which gives you more flexibility::

 from mayavi import mlab
 from numpy import random
 
 @mlab.show
 def image():
    mlab.imshow(random.random((10, 10)))

With this decorator, each time the `image` function is called, `mlab`
makes sure an interactive environment is running before executing the
`image` function. If an interactive environment is not running, `mlab`
will start one and the image function will not return until it is closed.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

