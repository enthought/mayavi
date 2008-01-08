"""
Script to generate the preview images for the mayavi2 LUTs.

Requires ImageMagick.
"""
from enthought.mayavi.tools import mlab
from enthought.mayavi.core.lut_manager import lut_mode_list
from enthought.mayavi.core import lut as destination_module
import os
target_dir = os.path.dirname(destination_module.__file__)


from numpy import arange, ones, atleast_2d

# Create some data
X = arange(0, 255)
X = X * ones((200, 1))

mlab.clf()
image = mlab.imshow(X.T)
mlab.view(0,0, 118)
# Make a preview for each possible lut
for lut in lut_mode_list():
    filebasename = target_dir + os.path.sep + lut.lower()
    if not lut == 'file':
        image.module_manager.scalar_lut_manager.lut_mode = lut
        mlab.savefig(filebasename + '.png', size=(80, 20))
    #os.system('convert %s.png %s.gif &' %(filebasename, filebasename))
    os.system('montage -geometry -0-0 -label "%s"  %s.png   %s.gif &' 
                    % (lut, filebasename, filebasename) )
