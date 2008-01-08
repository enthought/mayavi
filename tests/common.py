"""MayaVi test related utilities.  This only works with
wxPython-2.6.x.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports
import os.path
import sys
from optparse import OptionParser

# Enthought library imports
from enthought.traits.api import HasTraits, Bool, Instance
from enthought.pyface.timer.api import do_later
from enthought.pyface.api import GUI
from enthought.tvtk.api import tvtk
from enthought.mayavi.app import Application, PLUGIN_DEFINITIONS, IMAYAVI

VERBOSE = False

class MayaviTestError(Exception):
    pass

######################################################################
# Image comparison utility functions.
######################################################################

# Much of this code is translated from `vtk.test.Testing`.
def _print_image_error(img_err, err_index, img_base):
    """Prints out image related error information."""
    print "Failed image test with error: %f"%img_err
    print "Baseline image, error index:", img_base, err_index
    print "Test image: ", img_base + '.test.small.jpg'
    print "Difference image: ", img_base + '.diff.small.jpg'
    print "Valid image: ", img_base + '.small.jpg'


def _print_image_success(img_err, err_index):
    "Prints XML data for Dart when image test succeeded."
    print "Image Error, image_index: ", img_err, err_index
    

def _handle_failed_image(idiff, src_img, pngr, img_fname):
    """Writes all the necessary images when an image comparison
    failed."""
    f_base, f_ext = os.path.splitext(img_fname)

    # write out the difference file in full.
    pngw = tvtk.PNGWriter(file_name=f_base + ".diff.png",
                          input=idiff.output)
    pngw.write()
    
    # write the difference image scaled and gamma adjusted for the
    # dashboard.
    sz = pngr.output.dimensions
    if sz[1] <= 250.0:
        mag = 1.0
    else:
        mag = 250.0/sz[1]

    shrink = tvtk.ImageResample(input=idiff.output, interpolate=1)
    shrink.set_axis_magnification_factor(0, mag)
    shrink.set_axis_magnification_factor(1, mag)

    gamma = tvtk.ImageShiftScale(input=shrink.output, shift=0, scale=10)

    jpegw = tvtk.JPEGWriter(file_name=f_base + ".diff.small.jpg",
                            input=gamma.output, quality=85)
    jpegw.write()

    # write out the image that was generated.
    pngw.set(input=src_img, file_name=f_base + ".test.png")
    pngw.write()
    
    # write out a smaller version of the image that was generated.
    shrink.input = idiff.input
    jpegw.set(input=shrink.output, file_name=f_base + ".test.small.jpg")
    jpegw.write()

    # write out the valid image that matched.
    shrink.input = idiff.image
    jpegw.set(input=shrink.output, file_name=f_base + ".small.jpg")
    jpegw.write()

def _set_scale(r1, r2):
    """Given two instances of tvtk.ImageResample, this sets the scale
    of the two such that their outputs are of the same.  The final
    size is chosen as the minumum of the height and width of each
    image.
    """
    img1, img2 = r1.input, r2.input
    ex1 = img1.whole_extent
    w1, h1 = ex1[1] + 1, ex1[3] + 1
    ex2 = img2.whole_extent
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
            print "Creating baseline image '%s'."%img_fname
        return 
        
    pngr = tvtk.PNGReader(file_name=img_fname)
    pngr.update()

    if allow_resize:
        src_resample = tvtk.ImageResample(input=src_img, interpolate=1,
                                          interpolation_mode='cubic')    
        img_resample = tvtk.ImageResample(input=pngr.output, interpolate=1,
                                          interpolation_mode='cubic')
        _set_scale(src_resample, img_resample)
        idiff = tvtk.ImageDifference(input=src_resample.output,
                                     image=img_resample.output)
    else:
        idiff = tvtk.ImageDifference(input=src_img,
                                     image=pngr.output)
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
            if VERBOSE:
                _print_image_error(img_err, err_index, f_base)
            msg = "Failed image test: %f\n"%idiff.thresholded_error
            raise AssertionError, msg
    # output the image error even if a test passed
    if VERBOSE:
        _print_image_success(img_err, err_index)


def compare_image(renwin, img_fname, threshold=10, allow_resize=True):
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


###########################################################################
# `TestCase` class.
###########################################################################
class TestCase(HasTraits):

    interact = Bool(False)

    # The main envisage application.
    application = Instance('enthought.envisage.core.application.Application')

    # The MayaVi Script instance.
    script = Instance('enthought.mayavi.script.Script')

    def run(self):
        """This starts everything up and runs the test."""

        # Parse any cmd line args.
        self._parse_options()

        from enthought.pyface.api import GUI
        gui = GUI()
        
        # Create the application.
        self.application = app = Application(argv=sys.argv,
                                             gui=gui,
                                             id='enthought.mayavi',
                                             plugin_definitions=PLUGIN_DEFINITIONS,
                                             requires_gui=False)

        # Arrange for the callback to be called on application's started event.
        app.on_trait_change(self._start, 'started')

        # Start the application.
        app.start()

        # Start the GUI event loop (this call does not return until the GUI is
        # closed).
        gui.start_event_loop()

        # Stop the application.
        app.stop()

    def new_scene(self):
        """Creates a new TVTK scene, sets its size to that prescribed
        and returns the scene.
        """
        script = self.script
        # Create a new VTK scene.
        script.new_scene()
        # Set its background.
        s = script.engine.current_scene
        s.scene.background = (0.5, 0.5, 0.5)
        return s

    def test(self):
        """Override this to do whatever you want to do as your test
        code.

        *Make sure all other MayaVi specific imports are made here!*

        If you import MayaVi related code earlier you will run into
        difficulties.
        """        
        raise NotImplementedError

    def compare_image_offscreen(self, scene, img_path):
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
        s.off_screen_rendering = True
        s.render_window.size = (300, 300)
        s.reset_zoom()
        s.render()
        try:
            compare_image(s.render_window, abs_img_path)
        finally:
            s.off_screen_rendering = False
            s.render()
    
    def compare_image(self, scene, img_path):
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
            compare_image(rw, abs_img_path)
        finally:
            rw.remove_renderer(ren)
            s.render_window.add_renderer(ren)
            s.disable_render = False
            ren.reset_camera()
            s.render()

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
            raise MayaviTestError, excName
    assertRaises = failUnlessRaises

    ######################################################################
    # Non-public interface.    
    ######################################################################
    def _start(self, app):
        """This callback is called as soon as Envisage starts up.  The
        argument to this function is the
        enthought.envisage.Application singleton instance.
        """
        # Setup the script instances.
        self.script = app.get_service(IMAYAVI)
        # This in turn calls the testing code once the GUI mainloop is
        # running.
        g = app.gui
        g.on_trait_change(lambda : do_later(self._test), 'started')

    def _test(self):
        # Calls the users test code.
        self.test()
        if not self.interact:
            self.application.gui.ExitMainLoop()

    def _parse_options(self):
        """Parse command line options."""
        usage = "usage: %prog [options]"
        parser = OptionParser(usage)
        parser.add_option("-v", "--verbose", action="store_true",
                          dest="verbose", help="Print verbose output")
        parser.add_option("-i", "--interact", action="store_true",
                          dest="interact", default=False,
                          help="Allow interaction after test (default: False)")

        (options, args) = parser.parse_args()
        global VERBOSE
        if options.verbose:
            VERBOSE = True
        self.interact = options.interact


def fixpath(filename):
    """Given a relative file path it sets the path relative to this
    directory.  This allows us to run the tests from other directories
    as well.
    """
    return os.path.join(os.path.dirname(__file__), filename)
