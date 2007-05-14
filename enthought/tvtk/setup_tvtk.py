#!/usr/bin/env python
"""Setup script for TVTK.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2005, Enthought, Inc.
# License: BSD.

import os
import sys
from os.path import join, exists, dirname
from glob import glob
try:
    from scipy_distutils.misc_util import get_path, default_config_dict, dot_join
    from scipy_distutils.core import Extension
except ImportError:
    from numpy.distutils.misc_util import get_path, default_config_dict, dot_join
    from numpy.distutils.core import Extension
    

# Set this to False if you don't want the ZIP file to contain the ``*.py``
# files.
INCLUDE_SRC=True


#################################################################
# Utility functions.
#################################################################
def target_outdated(target, deps):
    """Determine whether a target is out of date.

    target_outdated(target,deps) -> True/False

    deps: list of filenames which MUST exist.
    target: single filename which may or may not exist.

    If target doesn't exist or is older than any file listed in deps,
    return true, otherwise return false.

    This function is basically copied and modified from
    IPython/genutils.py.
    """
    try:
        target_time = os.path.getmtime(target)
    except os.error:
        return True
    for dep in deps:
        dep_time = os.path.getmtime(dep)
        if dep_time > target_time:
            return True
    return False

def vtk_version_changed(zipfile):
    """Checks the ZIP file's VTK build version versus the current
    installed version of VTK and returns `True` if the versions are
    different.
 
    """
    result = True
    if exists(zipfile):        
        import vtk
        vtk_version = vtk.vtkVersion().GetVTKVersion()[:3]
        sys.path.append(zipfile)
        try:
            from tvtk_classes.vtk_version import vtk_build_version
        except ImportError:
            result = True
        else:
            if vtk_version != vtk_build_version:
                result = True
            else:
                result = False
        sys.path.pop()

    return result


#################################################################
# Build the ZIP file:
#################################################################
def build_zip(parent_path=None):    
    local_path = get_path(__name__, parent_path)
    deps = ['code_gen.py', 'wrapper_gen.py', 'special_gen.py',
            'tvtk_base.py', 'indenter.py']

    deps = [join(local_path, x) for x in deps]
    target = join(local_path, 'tvtk_classes.zip')
    builder = join(local_path, 'tvtk_classes.zip')
    
    if INCLUDE_SRC:
        cmd = 'cd %s && python code_gen.py -s'%local_path
    else:
        cmd = 'cd %s && python code_gen.py'%local_path

    if target_outdated(target, deps) or vtk_version_changed(target):
        print '-'*70
        print "Building TVTK classes...",
        sys.stdout.flush()
        os.system(cmd)
        print "Done."
        print '-'*70

# This ensures that the ZIP file is built if necessary when
# `setup_tvtk` is imported from the main setup.py script.
if len(sys.argv) >= 2 and \
       sys.argv[1] not in ['clean', 'register'] and \
       not sys.argv[1].startswith('--'):
    build_zip(parent_path='')

#################################################################
#  Define the configuration information:
#################################################################
def configuration(parent_package='', parent_path=None):
    package = 'tvtk'
    config = default_config_dict(package, parent_package)

    local_path = get_path(__name__, parent_path)
    # Data files.    
    data_files = [
        (join(parent_package, package), 
         [join(local_path, 'tvtk_classes.zip')]),
        (join(parent_package, package, 'pipeline', 'images' ), 
         glob(join(local_path, 'pipeline', 'images', '*.png'))),
        (join(parent_package, package, 'examples' ), 
         glob(join(local_path, 'examples', '*.py'))),
        (join(parent_package, package, 'examples', 'images' ), 
         glob(join(local_path, 'examples', 'images', '*.jpg'))),
        (join(parent_package, package, 'examples', 'plugin' ), 
         glob(join(local_path, 'examples', 'plugin', '*.py'))),
        (join(parent_package, package, 'doc'), 
         glob(join(local_path, 'doc', '*.txt'))),
        ]
    if config.has_key('data_files'):
        config['data_files'].extend(data_files)
    else:
        config['data_files'] = data_files

    # Extension modules.
    ext_mods = []

    # Numeric support.
    ext_nc = Extension(dot_join(parent_package,package,'array_ext'),
                       sources=[join(local_path, 'src', 'array_ext.c')],
                       depends=[join(local_path, 'src', 'array_ext.pyx')])
    try:
        import Numeric
    except ImportError:
        pass
    else:
        ext_mods.append(ext_nc)

    # Numarray support.
    ext_na = Extension(dot_join(parent_package,package,'array_ext_na'),
                       sources=[join(local_path, 'src', 'array_ext_na.c')],
                       depends=[join(local_path, 'src', 'array_ext_na.pyx')])
    try:
        import numarray
    except ImportError:
        pass
    else:
        ext_mods.append(ext_na)
        
    # Numpy support.
    ext_sp = Extension(dot_join(parent_package,package,'array_ext_sp'),
                       sources=[join(local_path, 'src', 'array_ext_sp.c')],
                       depends=[join(local_path, 'src', 'array_ext_sp.pyx')])
    try:
        import numpy
    except ImportError:
        pass
    else:
        ext_mods.append(ext_sp)
        from numpy import get_numpy_include
        if config.has_key('include_dirs'):
            config['include_dirs'].append(get_numpy_include())
        else:
            config['include_dirs'] = [get_numpy_include()]
        
    if config.has_key('ext_modules'):
        config['ext_modules'].extend(ext_mods)
    else:
        config['ext_modules'] = ext_mods
    
    for package_name in [('custom',), ('pipeline',), ('tests',),
                         ('tools',), ('plugins',), ('plugins', 'browser'),
                         ('plugins', 'scene'), ('util',),]:
        package_cur = dot_join(parent_package, package, *package_name)
        config['packages'].append(package_cur)
        config['package_dir'][package_cur] = join(local_path,
                                                  *package_name)
  
    return config


#################################################################
#  Do the setup if we are run stand-alone:
#################################################################    
if __name__ == '__main__':
    try:
        from scipy_distutils.core import setup
    except ImportError:
        from numpy.distutils.core import setup        
    setup(version      = '1.0.0',
          description  = "Traited VTK",
          author       = "Prabhu Ramachandran",
          author_email = "prabhu_r@users.sf.net",
          url          = 'http://www.enthought.com/enthought/wiki/TVTK',
          license      = "BSD",
          **configuration(parent_package='enthought', parent_path=''))
