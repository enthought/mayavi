"""
Script to generate the preview images for the mayavi2 LUTs.

Requires ImageMagick.
"""
import os

from mayavi import mlab
from mayavi.core.lut_manager import lut_mode_list, lut_image_dir

import numpy as np

# Create some data
X = np.arange(0, 255)
X = X * np.ones((200, 1))

mlab.clf()
image = mlab.imshow(X.T)
mlab.view(0, 0, 118)
# Make a preview for each possible lut
for lut in lut_mode_list():
    filebasename = os.path.join(lut_image_dir, lut.lower())
    if not lut == 'file':
        image.module_manager.scalar_lut_manager.lut_mode = lut
        mlab.savefig(filebasename + '.png', size=(80, 20))
        #os.system('convert %s.png %s.gif &' %(filebasename, filebasename))
        os.system('montage -geometry -0-0 -label "%s"  %s.png   %s.gif &'
                        % (lut, filebasename, filebasename) )
