"""Python usage for cypy cypycapsule.

Run: python examples/pypycapsule.py
"""
from cypy import capsule_check_exact, capsule_is_valid

def main() -> None:
    assert capsule_check_exact(object()) is False
    assert capsule_is_valid(object(), b"x") is False
    print("ok", capsule_check_exact(object()))

if __name__ == "__main__":
    main()
