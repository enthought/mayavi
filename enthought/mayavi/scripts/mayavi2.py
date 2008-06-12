#!/usr/bin/env python
"""The MayaVi application standalone script.

This script parses the command line arguments and launches MayaVi2
suitably.  It is meant to be used by those using MayaVi2 as a
standalone application.

MayaVi2 wiki page: http://svn.enthought.com/enthought/wiki/MayaVi

Author: Prabhu Ramachandran <prabhu_r@users.sf.net>

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys
import types
import getopt
import logging
from os.path import splitext, exists

# Local imports.
from enthought.mayavi.__version__ import __version__
from enthought.mayavi.scripts.util import get_data_dir

# Globals.
OFFSCREEN = False

# A global mayavi instance so we can close it correctly.
mayavi = None


###########################################################################
# Utility functions.
###########################################################################
def usage ():
    msg="""Usage:\n\nmayavi2 [options] ... [arg1] [arg2] ...

Where arg1, arg2 ... are optional file names that correspond to saved
MayaVi2 visualizations (file.mv2) or MayaVi2 scripts (file.py).  Valid
options are one or more of the following:

-d vtk-file.[vt*,xml]
--vtk vtk-file.[vt*,xml]

     vtk-file.vt* can be any VTK file (old style or XML).

-p plot3d-xyz-file
--plot3d-xyz plot3d-xyz-file

     The plot3d-xyz-file must be a PLOT3D single block co-ordinate
     file.  

-q plot3d-q-file
--plot3d-q plot3d-q-file

     The plot3d-q-file must be a PLOT3D single block solution file.
     The -q option is optional but must always follow the
     -p/--plot3d-xyz option.

-e ensight-case-file [FIXME]
--ensight ensight-case-file

     ensight-case-file must be a valid EnSight case file.  EnSightGold
     and EnSight6 formats are supported.

-w vrml-file
--vrml vrml-file

     Imports a VRML2 scene given an appropriate file.

-3 3DStudio-file
--3ds 3dStudio-file

     Imports a 3D Studio scene given an appropriate file.

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

     Starts up a new module manager on the MayaVi pipeline.

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
     that the name 'mayavi' is MayaVi's script instance -- just like
     in the embedded Python interpreter.

     **WARNING**: Note that this uses `execfile`, so please note that
                  this can be dangerous if the script does something
                  nasty!

-z saved-visualization-file
--viz saved-visualization-file
--visualization saved-visualization-file

     Loads a previously saved MayaVi2 visualization file passed as the
     argument.

-v
--verbose

     Prints verbose logs on the console.

-V 
--version

     Prints the MayaVi version.

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
    if type(arguments) in types.StringTypes:
        arguments = arguments.split()
        
    options = "d:p:q:e:m:f:z:w:3:x:nMvo"
    
    long_opts = ['vtk=',
                 'plot3d-xyz=', 'plot3d-q=',
                 'ensight=',
                 'module=', 'filter=',
                 'visualization=', 'viz=', 
                 'vrml=',
                 '3ds=',
                 'exec=',
                 'verbose',
                 'module-mgr', 'new-scene', 'offscreen']

    try:
        opts, args = getopt.getopt (arguments, options, long_opts)
    except getopt.error, msg:
        print msg
        print usage ()
        print '-'*70
        print msg
        sys.exit (1)
        
    return opts, args


def process_cmd_line(app, opts, args):
    """ Processes the passed command line arguments.

    Input Arguments:
      app -- A MayaVi application instance.

      opts -- The list of options returned by getopt.

      args -- The remaining arguments returned by getopt.
    """    

    from enthought.mayavi.core.common import error, exception
    from enthought.tvtk.common import camel2enthought

    script = app.script
    in_plot3d = False
    xyz_file = ""

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
            script.new_scene()
        
    for o, a in opts:
        if o in ('-d', '--vtk'):
            base, ext = splitext(a)
            if not exists(a):
                error("File %s does not exist!"%a)
                return
            if ext in ['.xml', '.vti', '.vtr', '.vts', '.vtp', '.vtu',
                       '.pvti', '.pvtr', '.pvts', '.pvtp', '.pvtu']:
                from enthought.mayavi.sources.vtk_xml_file_reader \
                     import VTKXMLFileReader
                r = VTKXMLFileReader()
                r.initialize(a)
                script.add_source(r)
            elif ext == '.vtk':
                from enthought.mayavi.sources.vtk_file_reader \
                     import VTKFileReader
                r = VTKFileReader()
                r.initialize(a)
                script.add_source(r)
            else:
                error("File %s does not appear to be a VTK file!"%a)
                return
        if in_plot3d:
            from enthought.mayavi.sources.plot3d_reader \
                 import PLOT3DReader
            r = PLOT3DReader()
            if o in ('-q', '--plot3d-q'):
                r.initialize(xyz_file, a)
            else:
                r.initialize(xyz_file)
            script.add_source(r)
            in_plot3d = False
        else:
            if o in ('-q', '--plot3d-q'):
                error("Sorry, the -q/--plot3d-q option must follow "\
                      "a -p/--plot3d-xyz option.")
        
        if o in ('-p', '--plot3d-xyz'):
            in_plot3d = True
            xyz_file = a

        # FIXME.
        if o in ('-e', '--ensight'):
            error('Feature not implemented!  Patches welcome! ;-)')
            #script.open_ensight(a, config=0)

        if o in ('-w', '--vrml'):
            from enthought.mayavi.sources.vrml_importer import VRMLImporter
            r = VRMLImporter()
            r.initialize(a)
            script.add_source(r)

        if o in ('-3', '--3ds'):
            from enthought.mayavi.sources.three_ds_importer import ThreeDSImporter
            r = ThreeDSImporter()
            r.initialize(a)
            script.add_source(r)

        if o in ('-m', '--module'):
            if '.' in a:
                idx = a.rfind('.')
                modname = a[:idx]
                classname = a[idx+1:]
            else:
                modname = 'enthought.mayavi.modules.%s'%camel2enthought(a)
                classname = a
            try:
                mod = __import__(modname, globals(), locals(), [classname])
            except ImportError, msg:
                exception(str(msg))
                return
            else:
                m = getattr(mod, classname)()
                if classname == 'Labels':
                    m.object = script.engine.current_object
                script.add_module(m)

        if o in ('-f', '--filter'):
            if '.' in a:
                idx = a.rfind('.')
                modname = a[:idx]
                classname = a[idx+1:]
            else:
                if a[:12] == 'UserDefined:':
                    modname = 'enthought.mayavi.filters.user_defined'
                    classname = 'UserDefined'
                    # Create the wrapped filter.
                    fname = a[12:]
                    from enthought.tvtk.api import tvtk
                    try:
                        extra = getattr(tvtk, fname)()
                    except (AttributeError, TypeError):
                        # Don't worry about errors.
                        extra = None
                else:
                    modname = 'enthought.mayavi.filters.%s'%camel2enthought(a)
                    classname = a
                    extra = None
            try:
                mod = __import__(modname, globals(), locals(), [classname])
            except ImportError, msg:
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

        if o in ('-M', '--module-mgr'):
            from enthought.mayavi.core.module_manager \
                 import ModuleManager
            mm = ModuleManager()            
            script.add_filter(mm)

        if o in ('-n', '--new-scene'):
            script.new_scene()
            e = script.engine
            s = e.scenes[-1]
            e.set(current_scene=s, current_object=s)

        if o in ('-x', '--exec' ):
            err = run_script(script, a)
            if err: # stop processing options.
                return

        if o in ('-z', '--visualization', '--viz'):
            script.load_visualization(a)

    # for remaining arguments simply load saved visualizations.
    for arg in args:
        base, ext = splitext (arg)
        if ext == '.mv2':
            script.load_visualization(arg)
        elif ext == '.py':
            err = run_script(script, arg)
            if err: # stop processing arguments.
                return            
        else:
            err =  "Please specify a MayaVi file with a '.mv2' extension. "\
                   "Or a MayaVi script with a '.py' extension. "\
                   "For details on how to load other files please read the "\
                   "usage documentation using mayavi2 --help."
            error(err)
            print usage()
            print "*"*70
            print err
            print "*"*70


def run_script(mayavi, script_name):
    """Execfiles a given script.  The name `mayavi` is bound to the
    mayavi script instance just like in the embedded interpreter.
    `script_name` is the name of the script to execute.

    Note that this function uses `execfile`. You should be careful
    when using this.

    It returns `False` if everything was OK and `True` if not.
    """
    from enthought.mayavi.core.common import exception

    g = sys.modules['__main__'].__dict__
    if 'mayavi' not in g:
        g['mayavi'] = mayavi
    error = False
    # Do execfile
    try:
        # If we don't pass globals twice we get NameErrors and nope,
        # using exec open(script_name).read() does not fix it.
        execfile(script_name, g, g)
    except Exception, msg:
        exception(str(msg))
        error = True

    return error


# If the user just wants help messages.  Print them before importing
# any of the big modules.
if ('-h' in sys.argv[1:]) or ('--help' in sys.argv[1:]):
    print usage()
    sys.exit(0)

if ('-V' in sys.argv[1:]) or ('--version' in sys.argv[1:]):
    print 'MayaVi %s'%__version__
    sys.exit(0)

if ('-o' in sys.argv[1:]) or ('--offscreen' in sys.argv[1:]):
    OFFSCREEN = True

# Importing here to avoid time-consuming import when user only wanted
# version/help information.
from enthought.mayavi.plugins.app import Mayavi

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


################################################################################
# `MayaviOffscreen` class.
################################################################################ 
class MayaviOffscreen(MayaviApp):
    """
    The mayavi application used for offscreen rendering.
    """

    def _script_default(self):
        from enthought.mayavi.plugins.script import Script
        from enthought.mayavi.core.engine import Engine
        engine = Engine(scene_factory=off_screen_viewer)
        s = Script(engine=engine)
        return s

    def main(self, argv=None):
        if argv is None:
            argv = []
        self.parse_command_line(argv)
        self.run()


##########################################################################
# Helper functions
##########################################################################
def off_screen_viewer():
    """A factory that creates an offscreen viewer."""
    from enthought.pyface.tvtk.tvtk_scene import TVTKWindow
    win = TVTKWindow(off_screen_rendering=True)
    # Need to set some non-zero size for the off screen window.  If
    # not we get VTK errors on Linux.
    win.scene.set_size((300,300))
    return win

def standalone(globals_dict):
    """This could be optionally called at the top of stand-alone
    scripts so that the script runs either as::
    
     $ mayavi2 script.py

    or::

     $ python script.py

    The script is typically passed the result of globals().
    For example:
    >>> from enthought.mayavi.scripts import mayavi2
    >>> mayavi2.standalone(globals())
    """
    if 'mayavi' not in globals_dict.keys():
        sys.argv.insert(0, 'mayavi2')
        # Main will execute the script for us via run_script.
        main()
        # Exit after mayavi has run.  If this is not done the rest of
        # the script will be executed which will cause errors.
        sys.exit(0)

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
