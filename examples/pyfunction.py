"""Python usage for cypy cyfunction.

Run: python examples/pyfunction.py
"""
from cypy import func_check, func_get_code, func_get_globals

def main() -> None:
    def f(x):
        return x
    assert func_check(f)
    assert func_get_code(f) is f.__code__
    assert func_get_globals(f) is f.__globals__
    print("ok", func_check(f))

if __name__ == "__main__":
    main()
