#!/usr/bin/env python
"""The Mayavi application standalone script.

This script parses the command line arguments and launches Mayavi2
suitably.  It is meant to be used by those using Mayavi2 as a
standalone application.

Mayavi2: http://docs.enthought.com/mayavi/mayavi/overview.html

"""
# Author: Prabhu Ramachandran <prabhu@enthought.com>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys
import getopt
import logging
from os.path import splitext, exists, join, abspath

# Local imports.
from mayavi.__version__ import __version__
from mayavi.scripts.util import get_data_dir

# Globals.
OFFSCREEN = False

# A global mayavi instance so we can close it correctly.
mayavi = None


###########################################################################
# Utility functions.
###########################################################################
def usage():
    msg = """Usage:\n\nmayavi2 [options] ... [arg1] [arg2] ...

Where arg1, arg2 ... are optional file names that correspond to saved
Mayavi2 visualizations (file.mv2) or Mayavi2 scripts (file.py) or any
data files supported by Mayavi.  Valid options are one or more of the
following:

-d datafile.ext
--data datafile.ext

     datafile.ext can be any of the supported data file formats.  This
     includes VTK file formats (*.vtk, *.xml, *.vt[i,p,r,s,u],
     *.pvt[i,p,r,s,u]), VRML2 (*.wrl), 3D Studio (*.3ds), PLOT3D
     (*.xyz), STL, BYU, RAW, PLY,  PDB,  SLC,  FACET,  OBJ,  AVSUCD
     (*.inp),  GAMBIT (*.neu),  Exodus  (*.exii),  PNG,  JPEG,  BMP,
     PNM, DCM, DEM, MHA, MHD, MINC, XIMG, TIFF, and various others that
     are supported.  datafile.ext can also be a source object not
     associated with a file, for example ParametricSurface or PointLoad
     will load the corresponding data sources into Mayavi.

--filter filter-name
-f filter-name

     The passed filter name is loaded with respect to the current
     source/filter object.  The filter name must be a valid one if not
     you will get an error message.

     If the filter is specified as 'package.sub.filter.SomeFilter'
     then the filter (`SomeFilter`) is imported from
     'package.sub.filter'.  Standard modules provided with mayavi2 do
     not need the full path specification.

     Example::
         mayavi2 -d data.vtk -f ExtractVectorNorm -f m2_user_filters.TestFilter

     In this example 'ExtractVectorNorm' is a standard filter and
     'm2_user_filters.TestFilter' is some user defined filter.

-m module-name
--module module-name

     The passed module name is loaded in the current ModuleManager.
     The module name must be a valid one if not you will get an error
     message.

     If a module is specified as 'package.sub.module.SomeModule' then
     the module (`SomeModule`) is imported from 'package.sub.module'.
     Standard modules provided with mayavi2 do not need the full path
     specification.

     Example::
         mayavi2 -d data.vtk -m Outline -m m2_user_modules.TestModule

     In this example 'Outline' is a standard module and
     'm2_user_modules.TestModule' is some user defined module.

-M
--module-mgr

     Starts up a new module manager on the Mayavi pipeline.

-n
--new-scene

     Creates a new TVTK scene.  Any options passed after this will
     apply to this newly created scene.

-o
--offscreen

     Run Mayavi in offscreen mode without any graphical user interface.
     This is most useful for scripts that need to render images
     offscreen.

-x script-file
--exec script-file

     This executes the given script in a namespace where we guarantee
     that the name 'mayavi' is Mayavi's script instance -- just like
     in the embedded Python interpreter.

     **WARNING**: Note that this uses `execfile`, so please note that
                  this can be dangerous if the script does something
                  nasty!

-s python-expression
--set python-expression

     Execute the expression on the last created object.  For example,
     lets say the previous object was a module.  If you want to set the
     color of that object and save the scene you may do::

      $ mayavi2 [...] -m Outline -s"actor.property.color = (1,0,0)" \
        -s "scene.save('test.png', size=(800, 800))"

     You should use quotes for the expression.

     **WARNING**: Note that this uses `exec`, so please note that
                  this can be dangerous!

-z saved-visualization-file
--viz saved-visualization-file
--visualization saved-visualization-file

     Loads a previously saved Mayavi2 visualization file passed as the
     argument.

-t
--test

     Runs the mayavi2 test suite and exits.  If run as such, this runs
     both the TVTK and Mayavi2 unittests.  If any additional arguments
     are passed they are passed along to the test runner.  So this may
     be used to run other tests as well.  For example::

        mayavi2 -t apptools.persistence

     This will run just the tests inside the apptools.persistence
     package.  You can also specify a directory with test files to run
     with this, for example::

        mayavi2 -t relative_path_to/integrationtests/mayavi

     will run the integration tests from the mayavi sources.

-v
--verbose

     Prints verbose logs on the console.

-V
--version

     Prints the Mayavi version.

-h
--help

     Prints this help message.

Examples::

     mayavi2 test.mv2 (or mayavi2 -z test.mv2)

     mayavi2 test.py (or mayavi2 -x test.py)

     mayavi2 test.mv2 other.mv2 (or mayavi2 -z test.mv2 -z other.mv2)

     mayavi2 -d test.vtk -m Axes -m GridPlane \\
     -f Threshold -m IsoSurface \\
     -n -d heart.vtk -m Outline -m ContourGridPlane
"""
    return msg


def parse_cmd_line(arguments):
    """Returns the options and arguments parsed via getopts.

    Due to the special needs (order of args is important and repeated
    options will be supplied) of this command line parser we must use
    getopts and not optparse.

    Input Arguments:
      arguments -- This can be either a list of arguments as in
                   sys.argv[1:] or a string that is similar to the one
                   passed on the command line.  If it is a string the
                   string is split to create a list of arguments.
    """
    if type(arguments) is str:
        arguments = arguments.split()

    options = "d:m:f:z:x:s:nMvo"

    long_opts = ['data=',
                 'module=', 'filter=',
                 'visualization=', 'viz=',
                 'exec=',
                 'set=',
                 'verbose',
                 'module-mgr', 'new-scene', 'offscreen']

    try:
        opts, args = getopt.getopt(arguments, options, long_opts)
    except getopt.error as msg:
        print(msg)
        print(usage())
        print('-'*70)
        print(msg)
        sys.exit(1)

    return opts, args


def _get_non_file_sources():
    """Returns a dict indexed on the name of non-file related sources
    ids with the value being the corresponding metadata object.
    """
    from mayavi.core.registry import registry
    data = {}
    for src in registry.sources:
        if len(src.extensions) == 0:
            name = src.id[:-6]
            data[name] = src
    return data


def process_cmd_line(app, opts, args):
    """ Processes the passed command line arguments.

    Input Arguments:
      app -- A Mayavi application instance.

      opts -- The list of options returned by getopt.

      args -- The remaining arguments returned by getopt.
    """

    from mayavi.core.common import error, exception
    from tvtk.common import camel2enthought

    sources = _get_non_file_sources()
    script = app.script
    last_obj = None

    # Start a new scene by default if there is none currently and none
    # was specified at the start of the command line arguments.
    if script.engine.current_scene is None:
        new_scene = False
        if len(opts) == 0:
            if len(args) == 0:
                new_scene = True
        elif (opts[0][0] not in ('-n', '--new-scene', '-z',
                                 '--visualization', '--viz',
                                 '-x', '--exec')):
            new_scene = True
        if new_scene:
            last_obj = script.new_scene()

    for o, a in opts:
        if o in ('-d', '--data'):
            base, ext = splitext(a)
            if exists(a):
                last_obj = script.open(a)
            elif a in sources:
                md = sources[a]
                src = md.get_callable()()
                script.add_source(src)
                last_obj = src
            else:
                error("File/Source %s does not exist!" % a)
                return

        if o in ('-m', '--module'):
            if '.' in a:
                idx = a.rfind('.')
                modname = a[:idx]
                classname = a[idx+1:]
            else:
                modname = 'mayavi.modules.%s' % camel2enthought(a)
                classname = a
            try:
                mod = __import__(modname, globals(), locals(), [classname])
            except ImportError as msg:
                exception(str(msg))
                return
            else:
                m = getattr(mod, classname)()
                if classname == 'Labels':
                    m.object = script.engine.current_object
                script.add_module(m)
                last_obj = m

        if o in ('-f', '--filter'):
            if '.' in a:
                idx = a.rfind('.')
                modname = a[:idx]
                classname = a[idx+1:]
            else:
                if a[:12] == 'UserDefined:':
                    modname = 'mayavi.filters.user_defined'
                    classname = 'UserDefined'
                    # Create the wrapped filter.
                    fname = a[12:]
                    from tvtk.api import tvtk
                    try:
                        extra = getattr(tvtk, fname)()
                    except (AttributeError, TypeError):
                        # Don't worry about errors.
                        extra = None
                else:
                    modname = 'mayavi.filters.%s' % camel2enthought(a)
                    classname = a
                    extra = None
            try:
                mod = __import__(modname, globals(), locals(), [classname])
            except ImportError as msg:
                exception(str(msg))
                return
            else:
                klass = getattr(mod, classname)
                if classname != 'UserDefined':
                    f = klass()
                else:
                    if extra is not None:
                        f = klass(filter=extra)
                    else:
                        f = klass()
                    f.setup_filter()
                script.add_filter(f)
                last_obj = f

        if o in ('-M', '--module-mgr'):
            from mayavi.core.module_manager \
                 import ModuleManager
            mm = ModuleManager()
            script.add_filter(mm)
            last_obj = mm

        if o in ('-n', '--new-scene'):
            script.new_scene()
            e = script.engine
            s = e.scenes[-1]
            e.trait_set(current_scene=s, current_object=s)
            last_obj = s

        if o in ('-x', '--exec'):
            err = run_script(script, a)
            if err:  # stop processing options.
                return

        if o in ('-s', '--set'):
            try:
                stmt = 'last_obj.' + a
                exec(stmt, locals(), globals())
            except Exception as msg:
                exception(str(msg))

        if o in ('-z', '--visualization', '--viz'):
            script.load_visualization(a)

    # for remaining arguments simply load saved visualizations.
    for arg in args:
        base, ext = splitext(arg)
        if ext == '.mv2':
            script.load_visualization(arg)
        elif ext == '.py':
            err = run_script(script, arg)
            if err:  # stop processing arguments.
                return
        else:
            script.open(arg)


def run_script(mayavi, script_name):
    """Execfiles a given script.  The name `mayavi` is bound to the
    mayavi script instance just like in the embedded interpreter.
    `script_name` is the name of the script to execute.

    Note that this function uses `execfile`. You should be careful
    when using this.

    It returns `False` if everything was OK and `True` if not.
    """
    from mayavi.core.common import exception

    g = sys.modules['__main__'].__dict__
    if 'mayavi' not in g:
        g['mayavi'] = mayavi
        g['engine'] = mayavi.engine
    g['__file__'] = script_name
    error = False
    # Do execfile
    try:
        # If we don't pass globals twice we get NameErrors and nope,
        # using exec open(script_name).read() does not fix it.
        exec(compile(open(script_name).read(), script_name, 'exec'), g, g)
    except Exception as msg:
        exception(str(msg))
        error = True

    return error


# This runs the runtests script and sends any args to it.
if ('-t' in sys.argv[1:]) or ('--test' in sys.argv[1:]):
    from mayavi.tests import runtests
    for arg in ('-t', '--test'):
        if arg in sys.argv[1:]:
            sys.argv.remove(arg)
    runtests.main()

# If the user just wants help messages.  Print them before importing
# any of the big modules.
if ('-h' in sys.argv[1:]) or ('--help' in sys.argv[1:]):
    print(usage())
    sys.exit(0)

if ('-V' in sys.argv[1:]) or ('--version' in sys.argv[1:]):
    print('Mayavi %s' % __version__)
    sys.exit(0)

for opt, arg in parse_cmd_line(sys.argv[1:])[0]:
    if opt in ('-o', '--offscreen'):
        OFFSCREEN = True
        break
# Create opt and arg to be able to delete them even if the previous loop
# is empty.
opt, arg = None, None
del opt, arg


# The vtk module is imported by the engine, so mayavi is never going to
# start without it. Let us capture the error early, and give a meaningful
# error message
try:
    import vtk
except ImportError as m:
    msg = '%s\n%s\nDo you have vtk installed properly?\n' \
        'VTK (and build instructions) can be obtained from '\
        'http://www.vtk.org\n' \
        % (m, '_'*80)
    raise ImportError(msg)


# Importing here to avoid time-consuming import when user only wanted
# version/help information.
from mayavi.plugins.app import Mayavi, setup_logger


##########################################################################
# `MayaviApp` class
##########################################################################
class MayaviApp(Mayavi):
    def parse_command_line(self, argv):
        """Parse command line options."""
        # Parse and store command line options to process once app has
        # started in `run`.
        options, args = parse_cmd_line(argv)
        self.cmd_line_opts = (options, args)
        # If the verbose option is set, change the log mode.
        for opts, args in options:
            if opts in ('-v', '--verbose'):
                self.log_mode = logging.DEBUG
                break

    def run(self):
        """Process the command line options and setup mayavi as per
        the users needs.
        """
        options, args = self.cmd_line_opts
        # Process the options.
        process_cmd_line(self, options, args)


###############################################################################
# `MayaviOffscreen` class.
###############################################################################
class MayaviOffscreen(MayaviApp):
    """
    The mayavi application used for offscreen rendering.
    """

    def _script_default(self):
        from mayavi.plugins.script import Script
        from mayavi.core.off_screen_engine import OffScreenEngine
        engine = OffScreenEngine()
        engine.start()
        s = Script(engine=engine)
        return s

    def setup_logger(self):
        from traits.etsconfig.api import ETSConfig
        path = join(ETSConfig.application_data,
                    'mayavi_e3', 'mayavi.log')
        path = abspath(path)
        logger = logging.getLogger()
        setup_logger(logger, path, mode=self.log_mode)

    def main(self, argv=None):
        if argv is None:
            argv = []

        self.parse_command_line(argv)
        self.setup_logger()
        self.run()


##########################################################################
# Helper functions
##########################################################################
def get_mayavi_script_instance():
    """Return the mayavi Script instance from the first available set of
    envisage engines registered in the registry.
    """
    from mayavi.core.registry import registry
    from mayavi.plugins.envisage_engine import EnvisageEngine
    from mayavi.plugins.script import Script
    for name, engine in registry.engines.items():
        if isinstance(engine, EnvisageEngine):
            return engine.window.get_service(Script)
    return


def contains_mayavi(namespace):
    """Returns if the given namespace contains a 'mayavi' name bound to
    a mayavi script instance.
    """
    from mayavi.plugins.script import Script
    if 'mayavi' in namespace:
        if isinstance(namespace.get('mayavi'), Script):
            return True
    return False


def standalone(func):
    """A decorator to run a function from within mayavi.  This lets
    users write a normal Python function and have that run from within
    mayavi.  It implicitly assumes that the name 'mayavi' refers the the
    Script instance and will overwrite it if not.
    """
    def wrapper(*args, **kw):
        script = get_mayavi_script_instance()
        if script is None and mayavi is not None:
            script = mayavi.script
        if script is None:
            def caller(script):
                """Callback that runs the function inside the mayavi
                app."""
                # Bind the 'mayavi' name to the script instance
                func.__globals__['mayavi'] = script
                # Run the function in the event loop.
                g = script.window.application.gui
                g.invoke_later(func, *args, **kw)

            # Start up mayavi and invoke caller when the script instance
            # is available.
            m = Mayavi()
            m.on_trait_change(caller, 'script')
            # Run the mayavi app.
            m.main()
        else:
            ns = func.__globals__
            if not contains_mayavi(ns):
                # Bind the 'mayavi' name to the script instance
                ns['mayavi'] = script
            # Now run the function.
            func(*args, **kw)

    return wrapper


def main():
    """This starts up the mayavi2 application.
    """
    global mayavi

    # Make sure '.' is in sys.path
    if '' not in sys.path:
        sys.path.insert(0, '')
    # Start the app.
    if OFFSCREEN:
        mayavi = MayaviOffscreen()
    else:
        mayavi = MayaviApp()
    mayavi.main(sys.argv[1:])


def close():
    """ This closes the mayavi2 application.
    """
    if mayavi is not None and not OFFSCREEN:
        mayavi.window.close()


if __name__ == '__main__':
    main()
