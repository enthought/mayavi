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
    config.add_data_files('enthought/__init__.py')

    return config


# Function to convert simple ETS component names and versions to a requirements
# spec that works for both development builds and stable builds.
def gendeps(list):
    return ['%s >=%s.dev, <=%s.dev' % (p,min,max) for p,min,max in list]

# Declare our installation requirements.
install_requires = gendeps([
    ("enthought.pyface", "2.0b1", "3"),
    ("enthought.persistence", "2.0b1", "3"),
    ])
print 'install_requires:\n\t%s' % '\n\t'.join(install_requires)


setup(
    name = 'enthought.tvtk',
    version      = '2.0b1',
    description  = "Traited VTK",
    author       = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    url          = 'http://www.enthought.com/enthought/wiki/TVTK',
    license = "BSD",
    install_requires = install_requires,
    extras_require = {
        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            # 'VTK',  # fixme: VTK is not available as an egg on all platforms.
            ],
    },
    namespace_packages = [
        "enthought",
    ],
    **configuration().todict()
)
