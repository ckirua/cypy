"""Public :mod:`cypy.cycodecs` stubs."""

def codec_register(search_function: object) -> int:
    """Register a codec search function (``PyCodec_Register``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def codec_known(encoding: bytes) -> bool:
    """Return True if ``encoding`` is a known codec (``PyCodec_KnownEncoding``; ``encoding`` must be ``bytes``, not ``str``)."""
    ...

def codec_encode(o: object, encoding: bytes, errors: bytes | None = None) -> object:
    """Encode ``o`` with ``encoding`` via ``PyCodec_Encode``."""
    ...

def codec_decode(o: object, encoding: bytes, errors: bytes | None = None) -> object:
    """Decode ``o`` with ``encoding`` via ``PyCodec_Decode``."""
    ...

def codec_encoder(encoding: bytes) -> object:
    """Return the encoder for ``encoding`` (``PyCodec_Encoder``)."""
    ...

def codec_decoder(encoding: bytes) -> object:
    """Return the decoder for ``encoding`` (``PyCodec_Decoder``)."""
    ...

def codec_incremental_encoder(encoding: bytes, errors: bytes | None = None) -> object:
    """Return an incremental encoder (``PyCodec_IncrementalEncoder``)."""
    ...

def codec_incremental_decoder(encoding: bytes, errors: bytes | None = None) -> object:
    """Return an incremental decoder (``PyCodec_IncrementalDecoder``)."""
    ...

def codec_stream_reader(encoding: bytes, stream: object, errors: bytes | None = None) -> object:
    """Return a stream reader (``PyCodec_StreamReader``)."""
    ...

def codec_stream_writer(encoding: bytes, stream: object, errors: bytes | None = None) -> object:
    """Return a stream writer (``PyCodec_StreamWriter``)."""
    ...

def codec_register_error(name: bytes, error: object) -> int:
    """Register a codec error callback (``PyCodec_RegisterError``). Returns 0 on success; errors raise — do not use as bool."""
    ...

def codec_lookup_error(name: bytes) -> object:
    """Lookup a codec error callback (``PyCodec_LookupError``)."""
    ...

def codec_strict_errors(exc: object) -> object:
    """Strict error handler (``PyCodec_StrictErrors``)."""
    ...

def codec_ignore_errors(exc: object) -> object:
    """Ignore error handler (``PyCodec_IgnoreErrors``)."""
    ...

def codec_replace_errors(exc: object) -> object:
    """Replace error handler (``PyCodec_ReplaceErrors``)."""
    ...

def codec_xmlcharrefreplace_errors(exc: object) -> object:
    """XML charref replace handler."""
    ...

def codec_backslashreplace_errors(exc: object) -> object:
    """Backslash replace handler."""
    ...

def codec_namereplace_errors(exc: object) -> object:
    """Name replace handler."""
    ...
