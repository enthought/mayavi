#!/usr/bin/env python
# Setup script for TVTK, numpy.distutils based.
#
#
import os, sys

def configuration(parent_package='enthought',top_path=None):
    import numpy
    from os.path import join
    from numpy.distutils.misc_util import Configuration
    config = Configuration('tvtk',parent_package,top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)


    config.add_subpackage('custom')
    config.add_subpackage('pipeline')
    config.add_data_dir('pipeline/images')
    config.add_data_dir('pyface/images')
    config.add_data_dir('tools/images')

    config.add_subpackage('plugins')
    config.add_subpackage('plugins.*')

    config.add_subpackage('tools')
    config.add_subpackage('util')

    config.add_subpackage('tests')

    # Numpy support.
    config.add_extension('array_ext',
                         sources = [join('src','array_ext.c')],
                         depends = [join('src','array_ext.pyx')],
                         )

    tvtk_classes_zip_depends = config.paths(
        'code_gen.py','wrapper_gen.py', 'special_gen.py',
        'tvtk_base.py', 'indenter.py', 'vtk_parser.py')
    from code_gen import TVTKGenerator
    def gen_tvtk_classes_zip(build_dir):
        import os, sys
        from distutils.dep_util import newer_group
        from distutils.dir_util import mkpath
        target = join(build_dir,'tvtk_classes.zip')
        if newer_group(tvtk_classes_zip_depends ,target) \
               or vtk_version_changed(target):
            output_dir = os.path.dirname(target)
            mkpath(output_dir, verbose=1)
            print '-'*70
            print "Building TVTK classes...",
            sys.stdout.flush()
            cwd = os.getcwd()
            os.chdir(output_dir)
            gen = TVTKGenerator('')
            gen.generate_code()
            gen.build_zip(True)
            gen.clean()
            os.chdir(cwd)
            print "Done."
            print '-'*70
        return target
    
    binaries = ('bdist', 'build', 'develop', 'install', 'bdist_egg')
    for arg in sys.argv:
        print arg
        if arg in binaries:
            print "HERE"
    #sys.exit()
    config.add_data_files(gen_tvtk_classes_zip)
#    print dir()
#    print dir(config)
#    print config

    return config

def vtk_version_changed(zipfile):
    """Checks the ZIP file's VTK build version versus the current
    installed version of VTK and returns `True` if the versions are
    different.

    """
    import os, sys
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

