"""
Viewing MRI data with cut plane and iso surface.

This example downloads an MRI scan, turns it into a 3D numpy array and
visualizes it.

First we extract some internal structures of the brain by defining a
volume of interest around them, and using iso surfaces.

Then we display two cut planes to show the raw MRI data itself.

Finally we display the outer surface, but we restrict it to volume of
interest to leave a cut for the cut planes.

"""

### Download the data, if not already on disk ##################################
import os
if not os.path.exists('mri_data.tar.gz'):
    # Download the data
    import urllib
    print "Downloading data, Please Wait (7.8MB)"
    opener = urllib.urlopen(
                'http://www-graphics.stanford.edu/data/voldata/MRbrain.tar.gz')
    open('mri_data.tar.gz', 'wb').write(opener.read())

# Extract the data
import tarfile
tar_file = tarfile.open('mri_data.tar.gz')
try:
    os.mkdir('mri_data')
except:
    pass
tar_file.extractall('mri_data')
tar_file.close()


### Read the data in a numpy 3D array ##########################################
import numpy as np
data = np.array([np.fromfile(os.path.join('mri_data', 'MRbrain.%i' % i),
                                        dtype='>u2') for i in range(1, 110)])
data.shape = (109, 256, 256)
data = data.T

# Display the data #############################################################
from enthought.mayavi import mlab

mlab.figure(bgcolor=(0, 0, 0), size=(400, 400))

src = mlab.pipeline.scalar_field(data)
# Our data is not equally spaced in all directions:
src.spacing = [1, 1, 1.5]
src.update_image_data = True

def user_defined(parent, filter_name):
    """ A function to add a TVTK filter not already in Mayavi.
    """
    from enthought.mayavi.filters.user_defined import UserDefined
    from enthought.tvtk.api import tvtk
    filter = UserDefined(filter=getattr(tvtk, filter_name)())
    parent.add_child(filter)
    return filter

# Extract some inner structures: the ventricles and the inter-hemisphere
# fibers. We define a VOI (volume of interest) that restricts the
# iso-surfaces to the inner of the brain.
blur = user_defined(src, 'ImageGaussianSmooth')
voi = user_defined(blur, 'ExtractVOI')
voi.filter.voi = [125, 193, 92, 125, 34, 75]

mlab.pipeline.iso_surface(voi, contours=[1610, 2480], colormap='Spectral')

# Add two cut planes to show the raw MRI data. We use a threshold filter
# to remove cut the planes outside the brain.
thr = mlab.pipeline.threshold(src, low=1120)
cut_plane = mlab.pipeline.scalar_cut_plane(thr,
                                plane_orientation='y_axes',
                                colormap='black-white',
                                vmin=1400,
                                vmax=2600)
cut_plane.implicit_plane.origin = (136, 111.5, 82)
cut_plane.implicit_plane.widget.enabled = False

cut_plane2 = mlab.pipeline.scalar_cut_plane(thr,
                                plane_orientation='z_axes',
                                colormap='black-white',
                                vmin=1400,
                                vmax=2600)
cut_plane2.implicit_plane.origin = (136, 111.5, 82)
cut_plane2.implicit_plane.widget.enabled = False

# Extract two views of the outside surface. We need to define VOIs in
# order to leave out a cut in the head.
voi2 = user_defined(src, 'ExtractVOI')
voi2.filter.voi = [0, 300, 112, 200, 0, 200]
outer = mlab.pipeline.iso_surface(voi2, contours=[1776, ], 
                                        color=(0.8, 0.7, 0.6))

voi3 = user_defined(src, 'ExtractVOI')
voi3.filter.voi = [0, 300, 0, 112, 0, 53]
outer3 = mlab.pipeline.iso_surface(voi3, contours=[1776, ],
                                         color=(0.8, 0.7, 0.6))


mlab.view(-125, 54, 326, (145.5, 138, 66.5))
mlab.roll(-175)

mlab.show()

import shutil
shutil.rmtree('mri_data')
