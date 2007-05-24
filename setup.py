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


setup(
    name = 'enthought.tvtk',
    version      = '2.0',
    description  = "Traited VTK",
    author       = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    url          = 'http://www.enthought.com/enthought/wiki/TVTK',
    license = "BSD",
    install_requires = [
        # 'VTK',  # fixme: VTK is not available as an egg on all platforms.
        'enthought.pyface==2.0',
    ],
    namespace_packages = [
        "enthought",
    ],
    **configuration().todict()
)
