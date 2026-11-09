"""Tiny assertion helpers so tests run without pytest installed."""


def raises(exc_type, fn, *args, **kwargs):
    """Fail unless fn(*args, **kwargs) raises exc_type."""
    try:
        fn(*args, **kwargs)
    except exc_type:
        return
    except Exception as other:  # wrong exception type
        raise AssertionError(f"expected {exc_type.__name__}, got {type(other).__name__}")
    raise AssertionError(f"expected {exc_type.__name__} to be raised")
