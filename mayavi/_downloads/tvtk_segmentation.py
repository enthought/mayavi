"""
Using VTK to assemble a pipeline for segmenting MRI images. This example
shows how to insert well-controled custom VTK filters in Mayavi.

This example downloads an MRI scan, turns it into a 3D numpy array,
applies a segmentation procedure made of VTK filters to extract the
gray-matter/white-matter boundary.

The segmentation algorithm used here is very naive and should, of course,
not be used as an example of segmentation.

"""

### Download the data, if not already on disk ##################################
import os
if not os.path.exists('MRbrain.tar.gz'):
    # Download the data
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
    print("Downloading data, Please Wait (7.8MB)")
    opener = urlopen(
                'http://graphics.stanford.edu/data/voldata/MRbrain.tar.gz')
    open('MRbrain.tar.gz', 'wb').write(opener.read())

# Extract the data
import tarfile
tar_file = tarfile.open('MRbrain.tar.gz')
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

################################################################################
# Heuristic for finding the threshold for the brain

# Exctract the percentile 20 and 80 (without using
# scipy.stats.scoreatpercentile)
sorted_data = np.sort(data.ravel())
l = len(sorted_data)
lower_thr = sorted_data[0.2*l]
upper_thr = sorted_data[0.8*l]

# The white matter boundary: find the densest part of the upper half
# of histogram, and take a value 10% higher, to cut _in_ the white matter
hist, bins = np.histogram(data[data > np.mean(data)], bins=50)
brain_thr_idx = np.argmax(hist)
brain_thr =  bins[brain_thr_idx + 4]

del hist, bins, brain_thr_idx

# Display the data #############################################################
from mayavi import mlab
from tvtk.api import tvtk

fig = mlab.figure(bgcolor=(0, 0, 0), size=(400, 500))
# to speed things up
fig.scene.disable_render = True

src = mlab.pipeline.scalar_field(data)
# Our data is not equally spaced in all directions:
src.spacing = [1, 1, 1.5]
src.update_image_data = True

#----------------------------------------------------------------------
# Brain extraction pipeline

# In the following, we create a Mayavi pipeline that strongly
# relies on VTK filters. For this, we make heavy use of the
# mlab.pipeline.user_defined function, to include VTK filters in
# the Mayavi pipeline.

# Apply image-based filters to clean up noise
thresh_filter = tvtk.ImageThreshold()
thresh_filter.threshold_between(lower_thr, upper_thr)
thresh = mlab.pipeline.user_defined(src, filter=thresh_filter)

median_filter = tvtk.ImageMedian3D()
median_filter.set_kernel_size(3, 3, 3)
median = mlab.pipeline.user_defined(thresh, filter=median_filter)

diffuse_filter = tvtk.ImageAnisotropicDiffusion3D(
                                    diffusion_factor=1.0,
                                    diffusion_threshold=100.0,
                                    number_of_iterations=5, )

diffuse = mlab.pipeline.user_defined(median, filter=diffuse_filter)

# Extract brain surface
contour = mlab.pipeline.contour(diffuse, )
contour.filter.contours = [brain_thr, ]

# Apply mesh filter to clean up the mesh (decimation and smoothing)
dec = mlab.pipeline.decimate_pro(contour)
dec.filter.feature_angle = 60.
dec.filter.target_reduction = 0.7

smooth_ = tvtk.SmoothPolyDataFilter(
                    number_of_iterations=10,
                    relaxation_factor=0.1,
                    feature_angle=60,
                    feature_edge_smoothing=False,
                    boundary_smoothing=False,
                    convergence=0.,
                )
smooth = mlab.pipeline.user_defined(dec, filter=smooth_)

# Get the largest connected region
connect_ = tvtk.PolyDataConnectivityFilter(extraction_mode=4)
connect = mlab.pipeline.user_defined(smooth, filter=connect_)

# Compute normals for shading the surface
compute_normals = mlab.pipeline.poly_data_normals(connect)
compute_normals.filter.feature_angle = 80

surf = mlab.pipeline.surface(compute_normals,
                                        color=(0.9, 0.72, 0.62))

#----------------------------------------------------------------------
# Display a cut plane of the raw data
ipw = mlab.pipeline.image_plane_widget(src, colormap='bone',
                plane_orientation='z_axes',
                slice_index=55)

mlab.view(-165, 32, 350, [143, 133, 73])
mlab.roll(180)

fig.scene.disable_render = False

#----------------------------------------------------------------------
# To make the link between the Mayavi pipeline and the much more
# complex VTK pipeline, we display both:
mlab.show_pipeline(rich_view=False)
from tvtk.pipeline.browser import PipelineBrowser
browser = PipelineBrowser(fig.scene)
browser.show()

mlab.show()
