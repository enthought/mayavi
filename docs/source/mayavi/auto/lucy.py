"""
Viewing Stanford 3D Scanning Repository lucy model
"""
# Copyright (c) 2014-2020, Enthought, Inc.
# Standard library imports
import os
from os.path import join

# Enthought library imports
from mayavi import mlab

### Download the lucy data, if not already on disk ############################
if not os.path.exists('lucy.tar.gz'):
    # Download the data
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
    print("Downloading lucy model, Please Wait (307MB)")
    opener = urlopen(
            'http://graphics.stanford.edu/data/3Dscanrep/lucy.tar.gz')
    open('lucy.tar.gz', 'wb').write(opener.read())

# Extract the data
import tarfile
lucy_tar_file = tarfile.open('lucy.tar.gz')
try:
    os.mkdir('lucy_data')
except:
    pass
lucy_tar_file.extractall('lucy_data')
lucy_tar_file.close()

# Path to the lucy ply file
lucy_ply_file = join('lucy_data', 'lucy.ply')

# Render the lucy ply file
mlab.pipeline.surface(mlab.pipeline.open(lucy_ply_file))
mlab.show()

import shutil
shutil.rmtree('lucy_data')
