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

