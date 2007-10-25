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
ENVISAGE = etsdep('enthought.envisage', '2.0.1b1', '3.0')
PYFACE_TVTK = etsdep('enthought.pyface[tvtk]', '2.0.1b1', '3.0')
TRAITS_UI = etsdep('enthought.traits[ui]', '2.0.1b1', '3.0')
TRAITSUIWX = etsdep('enthought.traits.ui.wx', '2.0.1b1', '3.0')


setup(
    author = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    cmdclass = {
        # Work around a numpy distutils bug by forcing the use of the
        # setuptools' sdist command.
        'sdist': setuptools.command.sdist.sdist,
        },
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = "Traited VTK",
    extras_require = {
        'plugin': [
            ENVISAGE,
            ],
        'wx': [
            TRAITSUIWX,
            ],

        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            # 'VTK',  # fixme: VTK is not available as an egg on all platforms.
            'numpy >= 1.0.3',
            ],
        },
    install_requires = [
        PYFACE_TVTK,
        TRAITS_UI,
        ],
    license = "BSD",
    name = 'enthought.tvtk',
    namespace_packages = [
        "enthought",
        ],
    tests_require = [
        'nose >= 0.9',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/tvtk/',
    version = '2.0.0b2',
    zip_safe = False,
    **configuration().todict()
    )
