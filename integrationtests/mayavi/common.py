"""MayaVi test related utilities.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports
import gc
import os
import os.path
import sys
import logging
import traceback
from optparse import OptionParser

# Enthought library imports
from traits.etsconfig.api import ETSConfig
from traits.api import  Any, Bool, Instance
from pyface.api import GUI
from tvtk.api import tvtk
from tvtk.common import configure_input
from mayavi.plugins.app import Mayavi, setup_logger

# The TVTK window.
from tvtk.pyface.tvtk_scene import TVTKWindow

# Global variables.
VERBOSE = False
logger = logging.getLogger()


def off_screen_viewer():
    """A factory that creates an offscreen viewer."""
    win = TVTKWindow(off_screen_rendering=True)
    # Need to set some non-zero size for the off screen window.  If
    # not we get VTK errors on Linux.
    win.scene.set_size((300,300))
    return win


class MayaviTestError(Exception):
    pass

###########################################################################
# `MemoryAssistant` class.
###########################################################################

class MemoryAssistant(object):
    """ Assistant methods to assert memory usage and memory leaks.
    """
    def assertMemoryUsage(self, process, usage, slack=0, msg=None):
        """ Assert that the memory usage does not exceed the provided limit.

        Parameters
        ----------
        process : psutil.Process
            The process to check.
        usage : float
            The target memory usage. This is used as a soft-limit.
        msg : str
            The message to show on AssertionError.
        slack : float
            The percentage (relative to `usage`) that we allow the
            process memory usage to exceed the soft limit. The default is 0.0

        Raises
        ------
        AssertionError :
            if the current memory usage of the process is higher than
            :math:`usage * (1 + slack)`.

        """
        current_usage = self._memory_usage(process)
        hard_limit = usage * (1 + slack)
        if  hard_limit < current_usage:
            if msg is None:
                difference = (current_usage - usage) / usage
                msg = "Memory leak of {:.2%}".format(difference)
            raise AssertionError(msg)

    def assertReturnsMemory(self, function, args=None, iterations=100,
                            slack=0.0, msg=None):
        """ Assert that the function does not retain memory over a number of
        runs.

        Parameters
        ----------
        func : callable
            The function to check. The function should take no arguments.
        args : tuple
            The tuple of arguments to pass to the callable.
        iterations : int
            The number of times to run the function. Default is 100.
        msg : str
            The message to show on AssertionError.
        slack : float
            The percentage (relative to the first run) that we allow the
            process memory usage to exceed the expected. The default is 0.0

        Note
        ----
        The function is executed in-process thus any memory leaks will be
        there to cause problems to other tests that are part of the currently
        running test suite.

        """
        try:
            import psutil
        except ImportError:
            msg = "Please install psutil to check memory usage"
            raise ImportError(msg)

        process = psutil.Process(os.getpid())

        def test_function():
            if args is None:
                function()
            else:
                function(*args)

        gc.collect()
        baseline = self._memory_usage(process)
        samples_msg   = "Samples           : {}"
        mem_usage_msg = "Memory growth (MB): {:5.1f} to {:5.1f}"
        mem_leak_msg =  "Memory leak   (%) : {:5.1f}"

        try:
            print('Profiling', end=' ')
            sys.stdout.flush()
            for index in range(iterations):
                test_function()
                print('.', end=' ')
                sys.stdout.flush()
                gc.collect()
                self.assertMemoryUsage(process, baseline, slack=slack)
            ##########################################
            # If we have come this far, we are golden!
            ##########################################
            final = self._memory_usage(process)
            leak = (final - baseline) / baseline
            print()
            print(samples_msg.format(index + 1))
            print(mem_usage_msg.format(baseline, final))
            print(mem_leak_msg.format(leak * 100.0, index + 1))
        except AssertionError:
            final = self._memory_usage(process)
            leak = (final - baseline) / baseline
            if msg is None:
                msg = 'Memory Leak!!!\n'
                msg += samples_msg.format(index + 1)
                msg += '\n'
                msg += mem_usage_msg.format(baseline, final)
                msg += '\n'
                msg += mem_leak_msg.format(leak * 100.0, index + 1)
                raise AssertionError(msg)
            else:
                raise AssertionError(msg)

    def _memory_usage(self, process):
        return float(process.get_memory_info().rss) / (1024 ** 2)

######################################################################
# Image comparison utility functions.
######################################################################


# Much of this code is translated from `vtk.test.Testing`.
def _print_image_error(img_err, err_index, img_base):
    """Prints out image related error information."""
    msg = """Failed image test with error: %(img_err)f
             Baseline image, error index: %(img_base)s, %(err_index)s
             Test image:  %(img_base)s.test.small.jpg
             Difference image: %(img_base)s.diff.small.jpg
             Valid image: %(img_base)s.small.jpg"""%locals()
    logger.error(msg)
    if VERBOSE:
        print(msg)


def _print_image_success(img_err, err_index):
    "Prints XML data for Dart when image test succeeded."
    msg = "Image Error, image_index: %s, %s"%(img_err, err_index)
    logger.debug(msg)
    if VERBOSE:
        print(msg)


def _handle_failed_image(idiff, src_img, pngr, img_fname):
    """Writes all the necessary images when an image comparison
    failed."""
    f_base, f_ext = os.path.splitext(img_fname)

    # write out the difference file in full.
    pngw = tvtk.PNGWriter(file_name=f_base + ".diff.png")
    configure_input(pngw, idiff)
    pngw.write()

    # write the difference image scaled and gamma adjusted for the
    # dashboard.
    sz = pngr.output.dimensions
    if sz[1] <= 250.0:
        mag = 1.0
    else:
        mag = 250.0/sz[1]

    shrink = tvtk.ImageResample(interpolate=1)
    configure_input(shrink, idiff.output)
    shrink.set_axis_magnification_factor(0, mag)
    shrink.set_axis_magnification_factor(1, mag)

    gamma = tvtk.ImageShiftScale(shift=0, scale=10)
    configure_input(gamma, shrink)

    jpegw = tvtk.JPEGWriter(file_name=f_base + ".diff.small.jpg",
                            quality=85)
    configure_input(jpegw, gamma)
    jpegw.write()

    # write out the image that was generated.
    pngw.trait_set(file_name=f_base + ".test.png")
    configure_input(pngw, src_img)
    pngw.write()

    # write out a smaller version of the image that was generated.
    configure_input(shrink, idiff.input)
    jpegw.trait_set(file_name=f_base + ".test.small.jpg")
    configure_input(jpegw, shrink)
    jpegw.write()

    # write out the valid image that matched.
    configure_input(shrink, idiff.image)
    jpegw.trait_set(file_name=f_base + ".small.jpg")
    configure_input(jpegw, shrink)
    jpegw.write()


def _set_scale(r1, r2):
    """Given two instances of tvtk.ImageResample, this sets the scale
    of the two such that their outputs are of the same.  The final
    size is chosen as the minumum of the height and width of each
    image.
    """
    img1, img2 = r1.input, r2.input
    if hasattr(img1, 'whole_extent'):
        ex1 = img1.whole_extent
    else:
        ex1 = img1.extent
    w1, h1 = ex1[1] + 1, ex1[3] + 1
    if hasattr(img2, 'whole_extent'):
        ex2 = img2.whole_extent
    else:
        ex2 = img2.extent
    w2, h2 = ex2[1] + 1, ex2[3] + 1
    w = min(w1, w2)
    h = min(h1, h2)
    r1.set_axis_magnification_factor(0, float(w)/w1)
    r1.set_axis_magnification_factor(1, float(h)/h1)
    r1.update()
    r2.set_axis_magnification_factor(0, float(w)/w2)
    r2.set_axis_magnification_factor(1, float(h)/h2)
    r2.update()


def compare_image_with_saved_image(src_img, img_fname, threshold=10,
                                   allow_resize=True):
    """Compares a source image (src_img, which is a tvtk.ImageData)
    with the saved image file whose name is given in the second
    argument.  If the image file does not exist the image is generated
    and stored.  If not the source image is compared to that of the
    figure.  This function also handles multiple images and finds the
    best matching image.  If `allow_resize` is True then the images
    are rescaled if they are not of the same size.
    """
    f_base, f_ext = os.path.splitext(os.path.abspath(img_fname))

    if not os.path.isfile(img_fname):
        # generate the image
        pngw = tvtk.PNGWriter(file_name=img_fname, input=src_img)
        pngw.write()
        if VERBOSE:
            print("Creating baseline image '%s'."%img_fname)
        return

    pngr = tvtk.PNGReader(file_name=img_fname)
    pngr.update()

    if allow_resize:
        src_resample = tvtk.ImageResample(interpolate=1,
                                          interpolation_mode='cubic')
        configure_input(src_resample, src_img)
        img_resample = tvtk.ImageResample(interpolate=1,
                                          interpolation_mode='cubic')
        configure_input(img_resample, pngr)
        _set_scale(src_resample, img_resample)
        idiff = tvtk.ImageDifference()
        configure_input(idiff, src_resample.output)
        if hasattr(idiff, 'set_image_data'):
            idiff.set_image_data(img_resample.output)
        else:
            idiff.image = img_resample.output
    else:
        idiff = tvtk.ImageDifference()
        configure_input(idiff, src_img)
        if hasattr(idiff, 'set_image_data'):
            idiff.set_image_data(pngr.output)
        else:
            idiff.image = pngr.output
    idiff.update()

    min_err = idiff.thresholded_error
    img_err = min_err
    best_img = img_fname

    err_index = 0
    count = 0
    if min_err > threshold:
        count = 1
        test_failed = 1
        err_index = -1
        while 1: # keep trying images till we get the best match.
            new_fname = f_base + "_%d.png"%count
            if not os.path.exists(new_fname):
                # no other image exists.
                break
            # since file exists check if it matches.
            pngr.file_name = new_fname
            pngr.update()
            if allow_resize:
                _set_scale(src_resample, img_resample)
            idiff.update()
            alt_err = idiff.thresholded_error
            if alt_err < threshold:
                # matched,
                err_index = count
                test_failed = 0
                min_err = alt_err
                img_err = alt_err
                best_img = new_fname
                break
            else:
                if alt_err < min_err:
                    # image is a better match.
                    err_index = count
                    min_err = alt_err
                    img_err = alt_err
                    best_img = new_fname

            count = count + 1
        # closes while loop.

        if test_failed:
            _handle_failed_image(idiff, src_img, pngr, best_img)
            _print_image_error(img_err, err_index, f_base)
            msg = "Failed image test: %f\n"%idiff.thresholded_error
            raise AssertionError(msg)
    # output the image error even if a test passed
    _print_image_success(img_err, err_index)


def compare_image_raw(renwin, img_fname, threshold=10, allow_resize=True):
    """Compares renwin's (a tvtk.RenderWindow) contents with the image
    file whose name is given in the second argument.  If the image
    file does not exist the image is generated and stored.  If not the
    image in the render window is compared to that of the figure.
    This function also handles multiple images and finds the best
    matching image.  If `allow_resize` is True then the images are
    rescaled if they are not of the same size.
    """
    # If this is not done the window may not be parented correctly.
    GUI.process_events()

    w2if = tvtk.WindowToImageFilter(read_front_buffer=False, input=renwin)
    w2if.update()
    return compare_image_with_saved_image(w2if.output, img_fname,
                                          threshold, allow_resize)


def compare_image_offscreen(scene, img_path):
    """Given a MayaVi scene and a path to a valid image, this
    compares the image rendered on the scene to that saved as the
    image.

    This functionality relies on the off screen rendering
    capabilities of VTK.  Under Linux and Mac OS X this only works
    with VTK from CVS (i.e. VTK-5.1.x).  It definitely works with
    a CVS checkout later than March 2006.
    """
    abs_img_path = img_path
    if not os.path.isabs(img_path):
        abs_img_path = fixpath(img_path)

    s = scene.scene
    saved = s.off_screen_rendering
    s.off_screen_rendering = True
    s.render_window.size = (300, 300)
    s.reset_zoom()
    s.render()
    try:
        compare_image_raw(s.render_window, abs_img_path)
    finally:
        s.off_screen_rendering = saved
        s.render()


def compare_image(scene, img_path):
    """Given a MayaVi scene and a path to a valid image, this
    compares the image rendered on the scene to that saved as the
    image.

    This will pop up a new tvtk render window and use that to
    perform the image comparison.
    """
    abs_img_path = img_path
    if not os.path.isabs(img_path):
        abs_img_path = fixpath(img_path)

    s = scene.scene
    s.disable_render = True
    ren = s.renderer
    s.render_window.remove_renderer(ren)
    rw = tvtk.RenderWindow(size=(300,300))
    rw.add_renderer(ren)
    ren.reset_camera()
    rw.render()
    try:
        compare_image_raw(rw, abs_img_path)
    finally:
        rw.remove_renderer(ren)
        s.render_window.add_renderer(ren)
        s.disable_render = False
        ren.reset_camera()
        s.render()


def is_running_with_nose():
    """Returns True if we are being run via nosetests.

    This tests if `nosetests` is used or if we are invoked via
    `python -m nose.core`.
    """
    argv0 = sys.argv[0]
    nose_core = os.path.join('nose', 'core.py')
    if argv0.endswith('nosetests') or argv0.endswith(nose_core):
        return True
    return False


###########################################################################
# `TestCase` class.
###########################################################################
class TestCase(Mayavi):
    """
    This class is to be subclassed when you write a test.
    """

    # Interact with the user after test is done?  Normally tests just
    # exit after completion, this prevents that.
    interact = Bool(False)

    # Always use offscreen rendering to generate images -- even if
    # `self.compare_image` was called in the test..
    offscreen = Bool(False)

    # Profile for memory usage.
    profile = Bool(False)

    # Use the standalone mode. This mode does not use the envisage Mayavi
    # application.
    standalone = Bool(True)

    app_window = Instance('pyface.api.ApplicationWindow')

    gui = Instance('pyface.gui.GUI')

    # An exception info if an exception was raised by a test.
    exception_info = Any

    ######################################################################
    # `Mayavi` interface.
    ######################################################################
    def main(self, argv=None, plugins=None):
        """Overridden main method that sets the argv to sys.argv[1:] by
        default.  Call this to run the test.
        """
        if argv is None:
            argv = sys.argv[1:]

        if not is_running_with_nose():
            self.parse_command_line(argv)

        if self.standalone:
            self.run_standalone()
        else:
            # Call the superclass main method.
            super(TestCase, self).main(argv, plugins)

    def setup_logger(self):
        """Overridden logger setup."""
        if self.standalone:
            path = os.path.join(ETSConfig.application_data,
                                'mayavi_e3', 'mayavi-test.log')
            path = os.path.abspath(path)
            log_path = os.path.dirname(path)
            if not os.path.exists(log_path):
                os.makedirs(log_path)
        else:
            path = 'mayavi-test.log'
        setup_logger(logger, path, mode=self.log_mode)

    def run_standalone(self):
        from mayavi.core.engine import Engine
        from mayavi.plugins.script import Script
        from pyface.api import ApplicationWindow, GUI

        self.setup_logger()
        if self.offscreen:
            engine = Engine(scene_factory=off_screen_viewer)
        else:
            engine = Engine()
        engine.start()

        self.exception_info = None
        self.script = Script(engine=engine)
        self.gui = g = GUI()
        self.app_window = a = ApplicationWindow()
        a.open()
        a.show(False)
        g.invoke_later(self.run)
        g.start_event_loop()
        if self.exception_info is not None:
            type, value, tb = self.exception_info
            raise type(value).with_traceback(tb)

    def run(self):
        """This starts everything up and runs the test.  Call main to
        run the test."""
        # Calls the users test code.
        try:
            if self.profile:
                memory_assistant = MemoryAssistant()
                memory_assistant.assertReturnsMemory(self.do_profile,
                                                     slack = 1.0)
            else:
                self.do()
        except Exception as e:
            type, value, tb = sys.exc_info()
            if is_running_with_nose():
                self.exception_info = type, value, tb
            else:
                # To mimic behavior of unittest.
                sys.stderr.write('\nfailures=1\n')
                info = traceback.extract_tb(tb)
                filename, lineno, function, text = info[-1] # last line only
                exc_msg = "%s\nIn %s:%d\n%s: %s (in %s)" %\
                        ('Exception', filename, lineno, type.__name__, str(value),
                        function)
                sys.stderr.write(exc_msg + '\n')
                # Log the message.
                logger.exception(exc_msg)
                if not self.interact:
                    sys.exit(1)
        finally:
            if not self.interact:
                if self.standalone:
                    # Close all existing viewers.
                    e = self.script.engine
                    for scene in e.scenes:
                        viewer = e.get_viewer(scene)
                        if viewer is not None:
                            if self.offscreen:
                                viewer.scene.close()
                            else:
                                viewer.close()
                    GUI.process_events()
                    # Shut down the app and the event loop.
                    self.app_window.close()
                    self.gui.stop_event_loop()
                else:
                    self.application.gui.invoke_later(self.application.exit)

    def parse_command_line(self, argv):
        """Parse command line options."""
        usage = "usage: %prog [options]"
        parser = OptionParser(usage)
        parser.add_option("-v", "--verbose", action="store_true",
                          dest="verbose", help="Print verbose output")
        parser.add_option("-i", "--interact", action="store_true",
                          dest="interact", default=False,
                          help="Allow interaction after test (default: False)")
        parser.add_option("-p", "--profile", action="store_true",
                          dest="profile", default=False,
                          help="Profile for memory usage and leaks "\
                               "(default:False). [Long Running] ")
        parser.add_option("-s", "--nostandalone", action="store_true",
                          dest="standalone", default=False,
                          help="Run test using envisage without standalone "\
                          "(default: False)")
        parser.add_option("-o", "--offscreen", action="store_true",
                          dest="offscreen", default=False,
                          help="Always use offscreen rendering when "\
                               "generating images (default: False)")

        (options, args) = parser.parse_args(argv)
        global VERBOSE
        if options.verbose:
            VERBOSE = True
            self.log_mode = logging.DEBUG
        self.offscreen = options.offscreen
        self.interact = options.interact
        self.profile = options.profile
        self.standalone = not options.standalone

    ######################################################################
    # `TestCase` interface.
    ######################################################################

    def do(self):
        """Override this to do whatever you want to do as your test
        code.

        *Make sure all other MayaVi specific imports are made here!*

        If you import MayaVi related code earlier you will run into
        difficulties.
        """
        raise NotImplementedError

    def do_profile(self):
        """Override this to profile for memory usage.

        *Make sure all other MayaVi specific imports are made here!*

        If you import MayaVi related code earlier you will run into
        difficulties.
        """
        raise NotImplementedError

    def new_scene(self):
        """Creates a new TVTK scene, sets its size to that prescribed
        and returns the scene.
        """
        script = self.script
        # Create a new VTK scene.
        script.new_scene()
        # Set its background.
        if self.standalone:
            GUI.process_events()
        s = script.engine.current_scene
        s.scene.background = (0.5, 0.5, 0.5)
        return s

    def compare_image_offscreen(self, scene, img_path):
        """Given a MayaVi scene and a path to a valid image, this
        compares the image rendered on the scene to that saved as the
        image.

        This functionality relies on the off screen rendering
        capabilities of VTK.  Under Linux and Mac OS X this only works
        with VTK from CVS (i.e. VTK-5.1.x).  It definitely works with
        a CVS checkout later than March 2006.
        """
        return compare_image_offscreen(scene, img_path)

    def compare_image(self, scene, img_path):
        """Given a MayaVi scene and a path to a valid image, this
        compares the image rendered on the scene to that saved as the
        image.

        This will pop up a new tvtk render window and use that to
        perform the image comparison.
        """
        if self.offscreen:
            return self.compare_image_offscreen(scene, img_path)
        else:
            return compare_image(scene, img_path)

    def failUnlessRaises(self, excClass, callableObj, *args, **kwargs):
        """Fail unless an exception of class excClass is thrown by
        callableObj when invoked with arguments args and keyword
        arguments kwargs. If a different type of exception is thrown,
        it will not be caught, and the test case will be deemed to
        have suffered an error, exactly as for an unexpected
        exception.
        """
        try:
            callableObj(*args, **kwargs)
        except excClass:
            return
        else:
            if hasattr(excClass,'__name__'):
                excName = excClass.__name__
            else:
                excName = str(excClass)
            raise MayaviTestError(excName)
    assertRaises = failUnlessRaises


def fixpath(filename):
    """Given a relative file path it sets the path relative to this
    directory.  This allows us to run the tests from other directories
    as well.
    """
    return os.path.join(os.path.dirname(__file__), filename)


def get_example_data(fname):
    """Given a relative path to data inside the examples directory,
    obtains the full path to the file.
    """
    p = os.path.join(os.pardir, os.pardir,
                     'examples', 'mayavi', 'data', fname)
    return os.path.abspath(fixpath(p))


def test(function):
    """A decorator to make a simple mayavi2 script function into a
    test case.  Note that this will not work with nosetests.
    """
    class MyTest(TestCase):
        def do(self):
            g = sys.modules['__main__'].__dict__
            if 'mayavi' not in g:
                g['mayavi'] = self.script
            if 'application' not in g:
                g['application'] = self.application
            # Call the test.
            function()
        def __call__(self):
           self.main()

    test = MyTest()
    return test
