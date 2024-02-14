# Wrapped in a try/except in those situations where someone hasn't installed
# as an egg.  What do we do then?  For now, we just punt since we don't want
# to define the version number in two places.
import importlib.metadata

try:
    version = importlib.metadata.version('mayavi')
except Exception:
    version = ''
