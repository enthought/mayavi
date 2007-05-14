#!/usr/bin/env python
# Setup script for TVTK, numpy.distutils based.
#
#
import os

build_numeric = False
build_numarray = False

minimum_numpy_version = '0.9.7.2467'
def configuration(parent_package='enthought',top_path=None):
    import numpy
    if numpy.__version__ < minimum_numpy_version:
        raise RuntimeError, 'numpy version %s or higher required, but got %s'\
              % (minimum_numpy_version, numpy.__version__)
    from os.path import join
    from numpy.distutils.misc_util import Configuration
    config = Configuration('tvtk',parent_package,top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)


    #add the parent __init__.py to allow for importing
    config.add_data_files(('..', os.path.abspath(os.path.join('..','__init__.py'))))

    config.add_subpackage('custom')
    config.add_subpackage('pipeline')
    config.add_data_dir('pipeline/images')

    config.add_subpackage('plugins')
    config.add_subpackage('plugins.*')

    config.add_subpackage('tools')
    config.add_subpackage('util')
    
    config.add_data_dir('doc')
    config.add_data_dir('examples')
    config.add_data_dir('tests')

    # Numpy support.
    config.add_extension('array_ext_sp',
                         sources = [join('src','array_ext_sp.c')],
                         depends = [join('src','array_ext_sp.pyx')],
                         )

    # Numeric support.
    if build_numeric:
        array_ext_c = config.paths('src/array_ext.c')[0]
        def get_array_ext_c(ext, build_dir):
            try:
                import Numeric
            except ImportError, msg:
                print 'Skip building %s: %s' % (ext.name, msg)
                return None
            return array_ext_c
        config.add_extension('array_ext',
                             sources = [get_array_ext_c],
                             depends = ['src/array_ext.*']
                             )

    # Numarray support.
    if build_numarray:
        array_ext_na_c = config.paths('src/array_ext_na.c')[0]
        def get_array_ext_na_c(ext, build_dir):
            try:
                import numarray
            except ImportError, msg:
                print 'Skip building %s: %s' % (ext.name, msg)
                return None
            return array_ext_na_c
        config.add_extension('array_ext_na',
                             sources = [get_array_ext_na_c],
                             depends = ['src/array_ext_na.*']
                             )
    
    tvtk_classes_zip_depends = config.paths(
        'code_gen.py','wrapper_gen.py', 'special_gen.py',
        'tvtk_base.py', 'indenter.py')
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
    config.add_data_files(gen_tvtk_classes_zip)

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

if __name__ == "__main__":
    try:
        from numpy.distutils.core import setup
    except ImportError:
        # Fall back to scipy_distutils based setup script.
        execfile('setup_tvtk.py')
    else:
        setup(
            version      = '1.0.0',
            description  = "Traited VTK",
            author       = "Prabhu Ramachandran",
            author_email = "prabhu_r@users.sf.net",
            install_requires = ['vtk', 'enthought.pyface.tvtk'],
            url          = 'http://www.enthought.com/enthought/wiki/TVTK',
            license      = "BSD",
            zip_safe     = False,
            configuration=configuration)

