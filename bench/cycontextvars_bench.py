"""Tier A benches for cycontextvars."""
from __future__ import annotations
import sys, contextvars
from pathlib import Path
_BENCH_ROOT = Path(__file__).resolve().parent
if str(_BENCH_ROOT) not in sys.path: sys.path.insert(0, str(_BENCH_ROOT))
from cypy import ctx_check_exact, ctx_copy_current, ctxvar_check_exact, ctxvar_new
from _bench_util import BenchSession

def main():
    session = BenchSession("cycontextvars — tier A")
    session.header()
    v = contextvars.ContextVar('t')
    session.section("ctx")
    session.compare("ctx_check_exact", ctx_check_exact, lambda o: type(o) is contextvars.Context, contextvars.copy_context(), param="ctx")
    session.compare("ctxvar_check_exact", ctxvar_check_exact, lambda o: type(o) is contextvars.ContextVar, v, param="var")
    session.compare("ctx_copy_current", ctx_copy_current, contextvars.copy_context, param="copy")
    session.compare("ctxvar_new", ctxvar_new, lambda n,d: contextvars.ContextVar(n.decode(), default=d), b"x", None, param="new")
    session.summary()
if __name__ == '__main__':
    main()
