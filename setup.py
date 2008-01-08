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

    return config


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
            'mayavi2 = enthought.mayavi.scripts.mayavi2:main'
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

