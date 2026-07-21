"""Python usage for cypy cysequence.

Run: python examples/pysequence.py
"""
from cypy import seq_check, seq_concat, seq_len

def main() -> None:
    assert seq_check([1, 2])
    assert seq_len([1, 2, 3]) == 3
    assert seq_concat([1], [2]) == [1, 2]
    print("ok", seq_len("ab"))

if __name__ == "__main__":
    main()
