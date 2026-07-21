"""Python usage for cypy cyweakref.

Run: python examples/pyweakref.py
"""
from cypy import weakref_check, weakref_new_ref

def main() -> None:
    class T:
        pass
    obj = T()
    ref = weakref_new_ref(obj)
    assert weakref_check(ref)
    assert ref() is obj
    print("ok", weakref_check(ref))

if __name__ == "__main__":
    main()
