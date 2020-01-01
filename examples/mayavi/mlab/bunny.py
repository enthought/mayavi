"""
Viewing Stanford 3D Scanning Repository bunny model
"""
# Copyright (c) 2014-2020, Enthought, Inc.
# Standard library imports
import os
from os.path import join

# Enthought library imports
from mayavi import mlab

### Download the bunny data, if not already on disk ############################
if not os.path.exists('bunny.tar.gz'):
    # Download the data
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
    print("Downloading bunny model, Please Wait (3MB)")
    opener = urlopen(
                'http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz')
    open('bunny.tar.gz', 'wb').write(opener.read())

# Extract the data
import tarfile
bunny_tar_file = tarfile.open('bunny.tar.gz')
try:
    os.mkdir('bunny_data')
except:
    pass
bunny_tar_file.extractall('bunny_data')
bunny_tar_file.close()

# Path to the bunny ply file
bunny_ply_file = join('bunny_data', 'bunny', 'reconstruction', 'bun_zipper.ply')

# Render the bunny ply file
mlab.pipeline.surface(mlab.pipeline.open(bunny_ply_file))
mlab.show()

import shutil
shutil.rmtree('bunny_data')
