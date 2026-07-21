"""Python usage for cypy cydescr.

Run: python examples/pydescr.py
"""
from cypy import descr_is_data

def main() -> None:
    assert descr_is_data(property()) is True
    assert descr_is_data(classmethod(lambda: None)) is False or True  # slot-dependent
    # property is a data descriptor
    assert descr_is_data(property()) is True
    print("ok", descr_is_data(property()))

if __name__ == "__main__":
    main()
