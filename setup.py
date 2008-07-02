import setuptools
from numpy.distutils.core import setup
from setup_data import INFO


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )

    config.add_subpackage('enthought.tvtk')
    config.add_subpackage('enthought')
    config.add_data_dir('enthought/mayavi/core/images')
    config.add_data_dir('enthought/mayavi/core/lut')
    config.add_data_dir('enthought/mayavi/images')
    config.add_data_dir('enthought/mayavi/view/images')

    # *.ini files.
    config.add_data_dir('enthought/tvtk/plugins/scene')
    config.add_data_dir('enthought/mayavi/preferences')

    # Add the documentation.
    config.add_data_files(('enthought/mayavi/html/*', ['docs/mayavi/user_guide/build/html/*']))    

    return config


# The following monkeypatching code comes from Numpy distutils.
#
# Monkeypatch the 'develop' command so that we build_src will execute
# inplace.  This is fixed in numpy 1.0.5 (svn r4569).
import numpy
if numpy.__version__[:5] < '1.0.5':

    # Replace setuptools's develop command with our own
    from setuptools.command import develop
    old_develop = develop.develop
    class develop(old_develop):
        __doc__ = old_develop.__doc__
        def install_for_development(self):
            self.reinitialize_command('build_src', inplace=1)
            old_develop.install_for_development(self)
    develop.develop = develop

    # Make numpy distutils use this develop.
    from numpy.distutils import core
    core.numpy_cmdclass['develop'] = develop


# Build the full set of packages by appending any found by setuptools'
# find_packages to those discovered by numpy.distutils.
config = configuration().todict()
packages = setuptools.find_packages(exclude=config['packages'] +
    ['docs', 'examples'])
config['packages'] += packages


# This renames the mayavi script to a MayaVi.pyw script on win32.
from setuptools.command.install_scripts import install_scripts
class my_install_scripts(install_scripts):
    def run(self):
        import os
        install_scripts.run(self)
        if os.name != 'posix':
            # Rename <script> to <script>.pyw. Executable bits
            # are already set in install_scripts.run().
            for file in self.get_outputs():
                if file[-4:] != '.pyw':
                    if file[-7:] == 'mayavi2':
                        new_file = file[:-7] + 'MayaVi2.pyw'
                    else:
                        new_file = os.path.splitext(file)[0] + '.pyw'
                    self.announce("renaming %s to %s" % (file, new_file))
                    if not self.dry_run:
                        if os.path.exists(new_file):
                            os.remove (new_file)
                        os.rename (file, new_file)


setup(
    author = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    cmdclass = {
        # Work around a numpy distutils bug by forcing the use of the
        # setuptools' sdist command.
        'sdist': setuptools.command.sdist.sdist,
        'install_scripts': my_install_scripts,
        },
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = "The MayaVi scientific data visualizer",
    entry_points = {
        'console_scripts': [
            'mayavi2 = enthought.mayavi.scripts.mayavi2:main',
            'tvtk_doc = enthought.tvtk.tools.tvtk_doc:main'
            ],

        'enthought.envisage.plugins': [
            'scene = enthought.tvtk.plugins.scene.scene_plugin:ScenePlugin',
            'scene_ui = enthought.tvtk.plugins.scene.ui.scene_ui_plugin:SceneUIPlugin',
            'browser = enthought.tvtk.plugins.browser.browser_plugin:BrowserPlugin',
            'mayavi = enthought.mayavi.plugins.mayavi_plugin:MayaviPlugin',
            'mayavi_ui = enthought.mayavi.plugins.mayavi_ui_plugin:MayaviUIPlugin'
            ],
        },
    extras_require = INFO['extras_require'],
    include_package_data = True,
    install_requires = INFO['install_requires'],
    license = "BSD",
    name = INFO['name'],
    namespace_packages = [
        "enthought",
        ],
    tests_require = [
        'nose >= 0.9',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/ets/',
    version = INFO['version'],
    zip_safe = False,
    **config
    )

