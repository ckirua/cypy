"""Python usage for cypy cymapping.

Run: python examples/pymapping.py
"""
from cypy import map_check, map_has_key, map_getitem_cstr

def main() -> None:
    d = {"a": 1}
    assert map_check(d)
    assert map_has_key(d, "a")
    assert map_getitem_cstr(d, b"a") == 1
    print("ok", map_check(d))

if __name__ == "__main__":
    main()
