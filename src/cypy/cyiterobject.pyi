"""Public :mod:`cypy.cyiterobject` stubs.

Tier A losers (ratio > 1.02 vs Python) are omitted from stubs but remain
``cpdef`` on the extension for Cython / future work.
"""

def seqiter_check(op: object) -> bool:
    """Return True if ``op`` is a sequence iterator (``PySeqIter_Check``)."""
    ...

def calliter_check(op: object) -> bool:
    """Return True if ``op`` is a callable iterator (``PyCallIter_Check``)."""
    ...

