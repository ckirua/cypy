"""Public :mod:`cypy.cymarshal` stubs."""
def marshal_dumps(value: object, version: int = 4) -> object:
    """Serialize ``value`` via ``PyMarshal_WriteObjectToString``."""
    ...
def marshal_loads(data: bytes) -> object:
    """Deserialize marshal bytes via ``PyMarshal_ReadObjectFromString``."""
    ...
