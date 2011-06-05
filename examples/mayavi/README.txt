This directory contains several mayavi2 examples.  There are two ways
to script mayavi2.

 1. The recommended way is to just write a script (script.py say) the
    way you'd write it out on the embedded interpreter.  Then you can
    execute this script by doing the following::

       $ mayavi2 -x script.py

    or

       $ mayavi2 script.py

    The advantages with this approach are:

      A. You can actually edit this script from inside mayavi2 (via
         File->Open Text File...) and then run it (by pressing Ctrl-r on
         the editor window).

      B. You can experiment on the embedded interpreter and cut/paste
         that code to make a script.

      C. The '-x' command line option is very powerful and can be
         invoked as many times as you want.  This lets you run
         multiple simulations.

      D. You get to use all the cool command line options of mayavi2.

      E. If you add the line::

              #!/usr/bin/env mayavi2

         to the start of the script, it even becomes standalone!

    Apart from the nongui.py and test.py scripts all the scripts in
    this directory use this approach.

 2. Subclass the `mayavi.plugins.app.Mayavi` application and
    override the `run` method.  While this is obviously very flexible
    it does involve quite a bit more work.  The only major benefit of
    this is that you can choose to use the non-GUI mayavi plugin as
    the nongui.py example demonstrates.


The explorer/ directory contains a simple 3D function explorer.  To
run it, change to the directory and then run python explorer3d.py.
