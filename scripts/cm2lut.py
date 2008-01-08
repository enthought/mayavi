#!/usr/bin/env python
"""
Script used to create lut lists used by mayavi from matplotlib colormaps.
This requires matlplotlib to be installed and should not be ran by the
user, but only once in a while to synchronize with MPL developpement.
"""
# Authors: Frederic Petit <fredmfp@gmail.com>, 
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from matplotlib.cm import datad, get_cmap
from numpy import linspace
from enthought.mayavi.core import lut as destination_module
import os
target_dir = os.path.dirname(destination_module.__file__)

values = linspace(0, 1, 256)

lut_dic = {}

for name in datad.keys():
    lut_dic[name] = get_cmap(name)(values).tolist()

module_string = """
# Lookup tables imported from pylab automaticaly by "cm2lut" script.
# Do not modify manually

# These colormaps are borrowed from matplotlib. See matplotlib license
# for license agreement (http://matplotlib.sourceforge.net/license.html)

# 34 of the colormaps are based on color specifications and designs
# developed by Cynthia Brewer (http://colorbrewer.org). The ColorBrewer
# palettes have been included under the terms of an Apache-stype license
# (for details, see the file LICENSE_COLORBREWER in the base directory of
# enthought.mayavi source).

# 7 palettes are from the Yorick scientific visalisation package, an
# evolution of the GIST package, both by David H. Munro. They are
# released under a BSD-like license (see LICENSE_YORICK in the base
# directory of enthought.mayavi source).

lut_dic = %s 

""" % lut_dic.__str__()

out_file = file(target_dir + os.path.sep + 'pylab_luts.py', 'w')

out_file.write(module_string)

out_file.close()

