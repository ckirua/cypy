"""Python usage for cypy cycellobject.

Run: python examples/pycellobject.py
"""
from cypy import cell_check, cell_new, cell_get, cell_set

def main() -> None:
    c = cell_new(None)
    assert cell_check(c)
    assert cell_get(c) is None
    cell_set(c, 42)
    assert cell_get(c) == 42
    print("ok", cell_get(c))

if __name__ == "__main__":
    main()
