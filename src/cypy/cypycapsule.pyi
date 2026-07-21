"""Public :mod:`cypy.cypycapsule` stubs."""
def capsule_check_exact(o: object) -> bool:
    """Return True if ``type(o) is types.CapsuleType`` (``PyCapsule_CheckExact``)."""
    ...
def capsule_is_valid(capsule: object, name: bytes) -> bool:
    """Return True if ``capsule`` is a valid capsule named ``name``."""
    ...
