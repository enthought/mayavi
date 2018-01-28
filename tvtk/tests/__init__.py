# Use faulthandler if available to provide more info on segfaults.
try:
    import faulthandler
except ImportError:
    pass
else:
    faulthandler.enable()
