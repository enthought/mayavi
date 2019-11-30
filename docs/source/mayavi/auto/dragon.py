"""
Viewing Stanford 3D Scanning Repository dragon model
"""
# Copyright (c) 2014-2015, Enthought, Inc.
# Standard library imports
import shutil
import tarfile
import os
from os.path import join

# Enthought library imports
from mayavi import mlab

### Download the dragon data, if not already on disk ############################
if not os.path.exists("dragon.tar.gz"):
    # Download the data
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
    print("Downloading dragon model, Please Wait (11MB)")
    opener = urlopen(
        "http://graphics.stanford.edu/pub/3Dscanrep/dragon/dragon_recon.tar.gz"
    )
    open("dragon.tar.gz", "wb").write(opener.read())

# Extract the data

dragon_tar_file = tarfile.open("dragon.tar.gz")
try:
    os.mkdir("dragon_data")
except:
    pass
dragon_tar_file.extractall("dragon_data")
dragon_tar_file.close()

# Path to the dragon ply file
dragon_ply_file = join("dragon_data", "dragon_recon", "dragon_vrip.ply")

# Render the dragon ply file
mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
mlab.show()


shutil.rmtree("dragon_data")
