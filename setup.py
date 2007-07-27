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
# spec that works for both development builds and stable builds.  This relies
# on the Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdeps(list):
    return ['%s >=%s.dev, <%s.a' % (p,ver,int(ver[:1])+1) for p,ver in list]


# Declare our installation requirements.
install_requires = etsdeps([
    ("enthought.pyface[tvtk]", "2.0b1"),
    ('enthought.traits[ui]', '2.0b1'),
    ('enthought.util', '2.0b1'),    # tools/visual.py imports from util.wx.timer
    ])
print 'install_requires:\n\t%s' % '\n\t'.join(install_requires)
plugin_requires = etsdeps([
    ('enthought.envisage', '2.0b1'),
    ])
print 'plugin_requires:\n\t%s' % '\n\t'.join(plugin_requires)
test_requires = [
    "nose >= 0.9, ",
    ] + etsdeps([
    ])
print 'test_requires:\n\t%s' % '\n\t'.join(test_requires)
wx_requires = etsdeps([
    ('enthought.traits.ui.wx', '2.0b1'),
    ])
print 'wx_requires:\n\t%s' % '\n\t'.join(wx_requires)


setup(
    author = "Prabhu Ramachandran",
    author_email = "prabhu_r@users.sf.net",
    description = "Traited VTK",
    extras_require = {
        'plugin': plugin_requires,
        'wx': wx_requires,

        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            # 'VTK',  # fixme: VTK is not available as an egg on all platforms.
            'numpy >= 1.0.3',
            ],
        },
    install_requires = install_requires,
    license = "BSD",
    name = 'enthought.tvtk',
    namespace_packages = [
        "enthought",
        ],
    tests_require = test_requires,
    test_suite = 'nose.collector',
    url = 'http://www.enthought.com/enthought/wiki/TVTK',
    version = '2.0b1',
    zip_safe = False,
    **configuration().todict()
)
