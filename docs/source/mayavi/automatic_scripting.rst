.. _automatic-script-generation:

Automatic script generation
===========================

Mayavi features a very handy and powerful script recording facility.
This can be used to:

 - record all actions performed on the Mayavi UI into a *human readable*,
   Python script that should be able to recreate your visualization.

 - easily learn the Mayavi code base and how to script it.

.. _recording-python-script:

Recording mayavi actions to a script
------------------------------------

Here is how you can use this feature:

 1. When you start the ``mayavi2`` application, on the Engine View (the
    tree view) toolbar you will find a red record icon next to the
    question mark icon.  Click it.  Note that this will also work from a
    standalone mlab session.

 2. You'll see a window popup with a few lines of boilerplate code so
    you can run your script standalone/with ``mayavi2 -x script.py ``or
    ``python script.py``.

 3. Now do anything you please on the UI.  As you perform those actions,
    you'll see the code needed to perform those actions.  For example,
    create a new source (either via the adder node dialog/view, the file
    menu or right click, i.e. any normal option), then add a
    module/filter etc.  Modify objects on the tree view.  
 
 4. Move the camera on the UI, rotate the camera, zoom, pan.  All of
    these will generate suitable Python code.  For the camera only the
    end position is stored (otherwise you'll see millions of useless
    lines of code).  The major keyboard actions on the scene are
    recorded (except for the 'c'/'t'/'j'/'a' keys).  This implies that
    it will record any left/right/up/down arrows the '+'/'-' keys etc.

    Since the code is updated as the actions are performed, this is a
    nice way to learn the mayavi API. 

 5. Once you are done, click on the record icon again, it will ask you
    to save the recorded script to a Python file.  Save it to some file,
    say ``script.py``.  If you are only interested in the code and not
    saving a file you may click cancel at this point.

 6. Close the recorder window and quit Mayavi (if you want to).

 7. Now from the shell do::

      $  mayavi2 -x script.py

    or even::

      $ python script.py

    These should run all the code to get you where you left.  You can
    feel free to edit this generated script -- in fact that is the whole
    point of automatic script generation!

It is important to understand that it is possible to script an existing
session of Mayavi too.  So, if after starting mayavi you did a few
things or ran a mayavi script and then want to record any further
actions, that is certainly possible.  Follow the same procedure as
before.  The only gotcha you have to remember in this case is that the
script recorder will not create the objects you already have setup on
the session.

.. note::

    You should also be able to delete/drag drop objects on the mayavi
    tree view.  However, these probably aren't things you'd want to do
    in an automatic script.

As noted earlier, script recording will work for an ``mlab`` session or
anywhere else where mayavi is used.  It will not generate any ``mlab``
specific code but write generic Mayavi code using the OO Mayavi API.

.. _recording-limitations:

Limitations
-----------

The script recorder works for most important actions.  At this point it
does not support the following actions:

  - On the scene, the 'c'/'t'/'j'/'a'/'p' keys are not recorded
    correctly since this is much more complicated to implement and
    typically not necessary for basic scripting.

  - Arbitrary scripting of the interface is obviously not going to work
    as you may expect.

  - Only trait changes and specific calls are recorded explicitly in the
    code.  So calling arbitrary methods on arbitrary mayavi objects will
    not record anything typically.  Only the mayavi engine is specially
    wired up to record specific methods.


.. _recorder-api:


The recorder API
----------------

The code used to perform the automatic script generation is itself
reusable outside of the context of Mayavi2 so long as you are using
Traits.  We do not document the full API here, the best place to look
for that is the ``enthought.mayavi.core.recorder`` module which is
reasonably well documented.  We provide a high level overview of the
library. 

The quickest way to get started is to look at a small example.


.. _recorder-api-example:

A tour by example
~~~~~~~~~~~~~~~~~~~

The following example is taken from the test suite.  Consider a set of
simple objects organized in a hierarchy::

    from enthought.traits.api import (HasTraits, Float, Instance,
            Str, List, Bool)
    from enthought.tvtk.api import tvtk
    from enthought.mayavi.core.recorder import recordable

    class Toy(HasTraits):
        color = Str
        type = Str
        # Note the use of the trait metadata to ignore this trait.
        ignore = Bool(False, record=False)

    class Child(HasTraits):
        name = Str('child')
        age = Float(10.0)
        # The recorder walks through sub-instances if they are marked
        # with record=True
        property = Instance(tvtk.Property, (), record=True)
        toy = Instance(Toy, record=True)
        friends = List(Str)

        # The decorator records the method.
        @recordable
        def grow(self, x):
            """Increase age by x years."""
            self.age += x

    class Parent(HasTraits):
        children = List(Child, record=True)
        recorder = Instance(Recorder, record=False)

Using these simple classes we first create a simple object hierarchy as
follows::

    p = Parent()
    c = Child()
    t = Toy()
    c.toy = t 
    p.children.append(c)

Given this hierarchy, we'd like to be able to record a script.  To do
this we setup the recording infrastructure::

    from enthought.mayavi.core.recorder import Recorder, set_recorder
    # Create a recorder.
    r = Recorder()
    # Set the global recorder so the decorator works.
    set_recorder(r)     
    r.register(p)
    r.recording = True

The key method here is the ``r.register(p)`` call above.  It looks at
the traits of ``p`` and finds all traits and nested objects that specify
a ``record=True`` in their trait metadata (all methods starting and
ending with ``_`` are ignored).  All sub-objects are in turn registered
with the recorder and so on.  Callbacks are attached to traits changes
and these are wired up to produce readable and executable code.  

Now lets test this out like so::

    # The following will be recorded.
    c.name = 'Shiva'
    c.property.representation = 'w'
    c.property.opacity = 0.4
    c.grow(1)

To see what's been recorded do this::

    print r.script

This prints::

    child = parent.children[0]
    child.name = 'Shiva'
    child.property.representation = 'wireframe'
    child.property.opacity = 0.40000000000000002
    child.grow(1)

The recorder internally maintains a mapping between objects and unique
names for each object.  It also stores the information about the
location of a particular object in the object hierarchy.  For example,
the path to the ``Toy`` instance in the hierarchy above is
``parent.children[0].toy``.  Since scripting with lists this way can be
tedious, the recorder first instantiates the ``child``::
    
    child = parent.children[0]

Subsequent lines use the ``child`` attribute.  The recorder always tries
to instantiate the object referred to using its path information in this
manner.

To record a function or method call one must simply decorate the
function/method with the ``recordable`` decorator.  Nested recordable
functions are not recorded and trait changes are also not recorded if
done inside a recordable function.  

.. note::

    1. It is very important to note that the global recorder must be set
       via the ``set_recorder`` method.  The ``recordable`` decorator
       relies on this being set to work.  
    
    2. The ``recordable`` decorator will work with plain Python classes
       and with functions too.

To stop recording do this::

    r.unregister(p)
    r.recording = False

The ``r.unregister(p)`` reverses the ``r.register(p)`` call and
unregisters all nested objects as well.


.. _recorder-advanced-uses:

Advanced use cases
~~~~~~~~~~~~~~~~~~~~

Here are a few advanced use cases.

 - Sometimes it is not enough to just record trait changes, one may want
   to pass an arbitrary string or command when recording is occuring.
   To allow for this, if one defines a ``recorder`` trait on the object,
   it is set to the current recorder.  One can then use this recorder to
   do whatever one wants.  This is very convenient.

 - To ignore specific traits one must specify either a ``record=False``
   metadata to the trait definition or specify a list of strings to the
   ``register`` method in the ``ignore`` keyword argument.

 - If you want to use a specific name for an object on the script you
   can pass the ``script_id`` parameter to the register function.


For more details on the recorder itself we suggest reading the module
source code.  It is fairly well documented and with the above background
should be enough to get you going.

