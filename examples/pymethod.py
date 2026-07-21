"""Python usage for cypy cymethod.

Run: python examples/pymethod.py
"""
from cypy import (
    method_check,
    method_new,
    method_get_function,
    method_get_self,
)

def main() -> None:
    def f(self):
        return 1

    class C:
        pass

    m = method_new(f, C())
    assert method_check(m)
    assert method_get_function(m) is f
    assert isinstance(method_get_self(m), C)
    print("ok", method_check(m))

if __name__ == "__main__":
    main()
