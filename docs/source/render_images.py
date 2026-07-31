"""
Script to render the images for the Mayavi user guide.

"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) Enthought, Inc.
# License: BSD Style.


import os
import subprocess
import sys


#############################################################################
def use_ci_image_size():
    """ Renders at 1x, so images match the ones CI produces.

        savefig multiplies by the screen's device pixel ratio, and neither
        magnification nor an explicit size overrides it, so a HiDPI display
        yields 2x images.  QT_SCALE_FACTOR cancels it, but Qt reads it while
        building the QApplication -- hence the subprocess to learn the ratio
        before this process starts Qt.
    """
    if 'QT_SCALE_FACTOR' in os.environ:
        return
    probe = ('from pyface.qt import QtGui\n'
             'app = QtGui.QApplication([])\n'
             'print(app.primaryScreen().devicePixelRatio())\n')
    try:
        out = subprocess.run([sys.executable, '-c', probe], check=True,
                             capture_output=True, text=True).stdout
        ratio = float(out.strip().splitlines()[-1])
    except Exception as exc:
        print('Could not determine the device pixel ratio (%s); images may '
              'not match the ones CI renders' % exc)
        return
    if ratio != 1:
        print('Rendering at 1/%g to undo HiDPI scaling' % ratio)
        os.environ['QT_SCALE_FACTOR'] = str(1 / ratio)


# has to happen before the imports below, which build the QApplication; skipped
# when mlab_reference.py execs this file just to read IMAGE_DIR
if __name__ == '__main__':
    use_ci_image_size()

from mayavi import mlab                                            # noqa: E402
from mayavi.scripts import mayavi2                                 # noqa: E402

import numpy as np                                                 # noqa: E402
from inspect import getmembers                                     # noqa: E402
from PIL import Image, ImageChops                                  # noqa: E402

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'mayavi', 'generated_images')



def trim(filename):
    """ Crops the uniform border off an image, like ``convert -trim``.

        Raises if what is left is too small to be a real figure: a scene that
        renders blank otherwise trims to a couple of pixels and ships as an
        illustration, which is how mlab.test_simple_surf went unnoticed for
        years.
    """
    with Image.open(filename) as img:
        img = img.convert('RGB')
        # the border colour is whatever the top-left pixel is, as ImageMagick
        # assumes with a fuzz of 0
        border = Image.new('RGB', img.size, img.getpixel((0, 0)))
        bbox = ImageChops.difference(img, border).getbbox()
        if bbox is None or min(bbox[2] - bbox[0], bbox[3] - bbox[1]) < 32:
            raise RuntimeError(
                '%s came out blank (drawn area %s in a %dx%d image); the scene '
                'probably renders nothing, or nothing the camera can see'
                % (filename, bbox, img.size[0], img.size[1]))
        if bbox != (0, 0) + img.size:
            img.crop(bbox).save(filename)


def capture_image(func, filename):
    """ Runs a function doing some mayavi drawing and save the resulting
        scene to a file.
    """
    mlab.clf()
    # several of the test functions plot random data, which would otherwise give
    # a different figure on every run
    np.random.seed(0)
    func()
    if not filename[-4:] in ('.jpg', '.png'):
        filename = '%s.jpg' % filename
    mlab.savefig(filename , size=(400, 400) )
    trim(filename)


def illustrate_module(module, directory=IMAGE_DIR):
    """ Uses the test functions of the modules (discovery ala nose) to
        create images for each function tested.
    """
    for name, func in getmembers(module):
        if not callable(func) or not name.lower().startswith('test'):
            continue
        if name.lower().endswith('anim'):
            continue
        # LaTeX doesn't like '.' in filename (sucks), so we replace them.
        filename = directory + os.sep + module.__name__.replace('.', '_') \
                        + '_' + name[5:]
        capture_image(func, filename=filename)

#############################################################################
# Entry point
@mlab.show
def main():
    mlab.figure(bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 400))
    print("Generating the mlab images...")
    illustrate_module(mlab)
    mayavi2.close()
    print("Done generating the mlab images")
    print("Generating the example pages")
    from render_examples import render_examples
    render_examples(render_images=True)
    print("Done generating the example pages")

if __name__ == '__main__':
    main()

