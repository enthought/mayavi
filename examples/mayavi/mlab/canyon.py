"""
Retrieve radar data from the NASA and plot a view of the Grand Canyon
landscape.

We cannot display the whole data, as it would be too big. To display
more, see the canyon decimation example.

This example is interesting as it shows how numpy can be used to load
and crop data completly foreign to Mayavi.
"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Retrieve the grand Canyon topological data ##################################
import os
if not os.path.exists('N36W113.hgt.zip'):
    # Download the data
    import urllib
    print 'Downloading data, please wait (10M)'
    opener = urllib.urlopen(
    'http://staging.enthought.com/projects/mayavi/N36W113.hgt.zip'
        )
    open('N36W113.hgt.zip', 'wb').write(opener.read())

# Load the data (signed 2 byte integers, big endian) ##########################
import zipfile
import numpy as np

data = np.fromstring(zipfile.ZipFile('N36W113.hgt.zip').read('N36W113.hgt'),
                    '>i2')
data.shape = (3601, 3601)
data = data.astype(np.float32)

# Plot an interesting section #################################################
from mayavi import mlab
data = data[:1000, 900:1900]
# Convert missing values into something more sensible.
data[data == -32768] = data[data > 0].min()

mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
mlab.surf(data, colormap='gist_earth', warp_scale=0.2,
            vmin=1200, vmax=1610)
# The data takes a lot of memory, and the surf command has created a
# copy. We free the inital memory.
del data

# A view of the canyon
mlab.view(-5.9, 83, 570, [5.3, 20, 238])
mlab.show()
