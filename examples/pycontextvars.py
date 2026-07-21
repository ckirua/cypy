"""Python usage for cypy cycontextvars.

Run: python examples/pycontextvars.py
"""
from cypy import ctx_check_exact, ctxvar_check_exact, ctx_copy_current, ctxvar_new

def main() -> None:
    v = ctxvar_new(b"demo", 1)
    assert ctxvar_check_exact(v)
    cur = ctx_copy_current()
    assert ctx_check_exact(cur)
    print("ok", type(v).__name__, type(cur).__name__)

if __name__ == "__main__":
    main()
