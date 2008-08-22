# Function to convert simple ETS project names and versions to a requirements
# spec that works for both development builds and stable builds.  Allows
# a caller to specify a max version, which is intended to work along with
# Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdep(p, min, max=None, literal=False):
    require = '%s >=%s.dev' % (p, min)
    if max is not None:
        if literal is False:
            require = '%s, <%s.a' % (require, max)
        else:
            require = '%s, <%s' % (require, max)
    return require


# Declare our ETS project dependencies.
APPTOOLS = etsdep('AppTools', '3.0.1')  # -- imports of persistence and resource in many places
ENTHOUGHTBASE = etsdep('EnthoughtBase', '3.0.1')    # The 'plugin' extra is required by loose-coupling in the mayavi ui plugin definition's default pespective.
ENVISAGECORE = etsdep('EnvisageCore', '3.0.1')
ENVISAGEPLUGINS = etsdep('EnvisagePlugins', '3.0.1')
TRAITSBACKENDWX = etsdep('TraitsBackendWX', '3.0.2')
TRAITSGUI = etsdep('TraitsGUI', '3.0.2')
TRAITS_UI = etsdep('Traits[ui]', '3.0.2')


# A dictionary of the pre_setup information.
INFO = {
    'extras_require': {
        'app' : [
            ENVISAGECORE,
            ENVISAGEPLUGINS,
            TRAITSBACKENDWX,
            ],
        'ui': [
            ENVISAGECORE,
            ENVISAGEPLUGINS,
            ],
        'util': [
            TRAITSBACKENDWX,
            ],
            
        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            'numpy >= 1.1.0',
            'setuptools',
            #'VTK',  # fixme: VTK is not available as an egg on all platforms.
            #'wxPython',  # Not everyone uses WX.
            ],
        },
    'install_requires': [
        APPTOOLS,
        ENTHOUGHTBASE,
        TRAITSGUI,
        TRAITS_UI,
        ],
    'name': 'Mayavi',
    'version': '3.0.3',
    }
