import setuptools
from numpy.distutils.core import setup


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


# Function to convert simple ETS project names and versions to a requirements
# spec that works for both development builds and stable builds.  Allows
# a caller to specify a max version, which is intended to work along with
# Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdep(p, min, max=None, literal=False):
    require = '%s >=%s.dev' % (p, min)
    if max is not None:
        if literal is False:
            require = '%s, <%sa' % (require, max)
        else:
            require = '%s, <%s' % (require, max)
    return require


# Declare our ETS project dependencies.
APPTOOLS = etsdep('AppTools', '3.0.0b1')
ENTHOUGHTBASE = etsdep('EnthoughtBase', '3.0.0b1')    # The 'plugin' extra is required by loose-coupling in the mayavi ui plugin definition's default pespective.
ENVISAGECORE = etsdep('EnvisageCore', '3.0.0b1')
ENVISAGEPLUGINS = etsdep('EnvisagePlugins', '3.0.0b1')
TRAITSBACKENDQT = etsdep('TraitsBackendQt', '3.0.0b1')
TRAITSBACKENDWX = etsdep('TraitsBackendWX', '3.0.0b1')
TRAITSGUI = etsdep('TraitsGUI[tvtk]', '3.0.0b1')
TRAITS_UI = etsdep('Traits[ui]', '3.0.0b1', '3.1')


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
    extras_require = {
        'plugin': [
            ENVISAGECORE,
            ],
        'ui': [
            APPTOOLS,
            ENVISAGECORE,
            ENVISAGEPLUGINS,
            ],
        'qt': [
            TRAITSBACKENDQT,
            ],
        'wx': [
            TRAITSBACKENDWX,
            ],

        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            'numpy >= 1.0.3',
            "scipy >=0.5.2",
            # 'VTK',  # fixme: VTK is not available as an egg on all platforms.
            ],
        },
    include_package_data = True,
    install_requires = [
        ENTHOUGHTBASE,
        TRAITSGUI,
        TRAITS_UI,
        ],
    license = "BSD",
    name = 'Mayavi',
    namespace_packages = [
        "enthought",
        ],
    packages = find_packages(exclude=['docs', 'examples']),
    tests_require = [
        'nose >= 0.9',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/ets/',
    version = '2.0.3a1',
    zip_safe = False,
    **configuration().todict()
    )

