import contextlib
import gc

@contextlib.contextmanager
def restore_gc_state():
    """Ensure that gc state is restored on exit of the with statement."""
    originally_enabled = gc.isenabled()
    try:
        yield
    finally:
        if originally_enabled:
            gc.enable()
        else:
            gc.disable()
