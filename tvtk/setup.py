#!/usr/bin/env python
# Setup script for TVTK, numpy.distutils based.
#
#
from __future__ import print_function

import os
import sys


def can_compile_extensions():
    from distutils.dist import Distribution
    from distutils.errors import DistutilsError
    sargs = {'script_name': None, 'script_args': ["--build-ext"]}
    d = Distribution(sargs)
    cfg = d.get_command_obj('config')
    cfg.dump_source = 0
    cfg.noisy = 0
    cfg.finalize_options()
    build_ext = d.get_command_obj('build_ext')
    build_ext.finalize_options()
    try:
        result = cfg.try_compile(
            'int main(void) {return 0;}',
            headers=['Python.h'],
            include_dirs=build_ext.include_dirs,
            lang='c'
        )
    except DistutilsError:
        return False
    else:
        return result


def configuration(parent_package=None, top_path=None):
    from os.path import join
    from numpy.distutils.misc_util import Configuration
    config = Configuration('tvtk', parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('custom')
    config.add_subpackage('pipeline')
    config.add_subpackage('pyface')
    config.add_subpackage('pyface.*')
    config.add_subpackage('pyface.*.*')
    config.add_subpackage('view')

    config.add_data_dir('pipeline/images')
    config.add_data_dir('pyface/images')
    config.add_data_dir('tools/images')

    config.add_subpackage('plugins')
    config.add_subpackage('plugins.*')
    config.add_subpackage('plugins.*.*')

    config.add_subpackage('tools')
    config.add_subpackage('util')

    config.add_subpackage('tests')

    # Add any extensions.  These are optional.
    if can_compile_extensions():
        config.add_extension(
            'array_ext',
            sources=[join('src', 'array_ext.c')],
            depends=[join('src', 'array_ext.pyx')],
        )

    tvtk_classes_zip_depends = config.paths(
        'code_gen.py', 'wrapper_gen.py', 'special_gen.py',
        'tvtk_base.py', 'indenter.py', 'vtk_parser.py'
    )

    return config


def gen_tvtk_classes_zip():
    MY_DIR = os.path.dirname(__file__)
    sys.path.append(MY_DIR)
    from tvtk.code_gen import TVTKGenerator
    target = os.path.join(MY_DIR, 'tvtk_classes.zip')
    output_dir = os.path.dirname(target)
    try:
        os.mkdir(output_dir)
    except:
        pass
    print('-'*70)
    if os.path.exists(target):
        print('Deleting possibly old TVTK classes')
        os.unlink(target)
    print("Building TVTK classes...", end=' ')
    sys.stdout.flush()
    cwd = os.getcwd()
    os.chdir(output_dir)
    gen = TVTKGenerator('')
    gen.generate_code()
    gen.build_zip(True)
    os.chdir(cwd)
    print("Done.")
    print('-'*70)
    sys.path.remove(MY_DIR)


def vtk_version_changed(zipfile):
    """Checks the ZIP file's VTK build version versus the current
    installed version of VTK and returns `True` if the versions are
    different.

    """
    result = True
    if os.path.exists(zipfile):
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
