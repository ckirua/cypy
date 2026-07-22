"""Python usage for cypy cysequence.

Run: python examples/pysequence.py
"""
from cypy import seq_check, seq_concat, seq_eq, seq_len

def main() -> None:
    assert seq_check([1, 2])
    assert seq_len([1, 2, 3]) == 3
    assert seq_concat([1], [2]) == [1, 2]
    assert seq_eq([1, 2], [1, 2]) and not seq_eq([1], [2]) and seq_eq([], [])
    assert seq_eq((1, 2), (1, 2)) and not seq_eq((1,), (1, 2)) and seq_eq((), ())
    assert not seq_eq((1, 2), [1, 2]) and not seq_eq((), [])  # same as ``==``
    assert seq_eq("ab", "ab") and not seq_eq("ab", "ba")
    print("ok", seq_len("ab"))

if __name__ == "__main__":
    main()
