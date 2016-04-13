#!/usr/bin/env python
"""
Script used to create lut lists used by mayavi from matplotlib colormaps.
This requires matlplotlib to be installed and should not be ran by the
user, but only once in a while to synchronize with MPL developpement.
"""
# Authors: Frederic Petit <fredmfp@gmail.com>,
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007-2016, Enthought, Inc.
# License: BSD Style.

import os

try:
    # Python 2
    import cPickle as pickle
except ImportError:
    # Python 3
    import pickle

import numpy as np

from matplotlib.cm import datad, get_cmap
from mayavi.core import lut as destination_module

target_dir = os.path.dirname(destination_module.__file__)

values = np.linspace(0., 1., 256)

lut_dic = {}

for name in datad.keys():
    if name.endswith('_r'):
        continue
    lut_dic[name] = get_cmap(name)(values.copy())

out_name = os.path.join(target_dir, 'pylab_luts.pkl')

with open(out_name, "wb") as fh:
    pickle.dump(lut_dic, fh, protocol=0)
