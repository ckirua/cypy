"""Public :mod:`cypy.cyiterobject` stubs."""

def seqiter_check(op: object) -> bool:
    """Return True if ``op`` is a sequence iterator (``PySeqIter_Check``)."""
    ...

def seqiter_new(seq: object) -> object:
    """Return a sequence iterator via ``PySeqIter_New``."""
    ...

def calliter_check(op: object) -> bool:
    """Return True if ``op`` is a callable iterator (``PyCallIter_Check``)."""
    ...

def calliter_new(callable: object, sentinel: object) -> object:
    """Return ``iter(callable, sentinel)`` via ``PyCallIter_New``."""
    ...
