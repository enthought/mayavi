#!/usr/bin/env python
"""
Script used to create lut lists used by mayavi from matplotlib colormaps.
This requires matlplotlib to be installed and should not be ran by the
user, but only once in a while to synchronize with MPL developpement.
"""
# Authors: Frederic Petit <fredmfp@gmail.com>,
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007-2009, Enthought, Inc.
# License: BSD Style.

import os
import numpy as np

from matplotlib.cm import datad, get_cmap
from mayavi.core import lut as destination_module
from apptools.persistence import state_pickler
target_dir = os.path.dirname(destination_module.__file__)

values = np.linspace(0., 1., 256)

lut_dic = {}

for name in datad.keys():
    if name.endswith('_r'):
        continue
    lut_dic[name] = get_cmap(name)(values.copy())

out_name = os.path.join(target_dir, 'pylab_luts.pkl')
state_pickler.dump(lut_dic, out_name)

