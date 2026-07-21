"""Python usage for cypy cygenobject.

Run: python examples/pygenobject.py
"""
from cypy import gen_check, gen_check_exact

def main() -> None:
    def g():
        yield 1
    gen = g()
    assert gen_check(gen) and gen_check_exact(gen)
    assert not gen_check([1])
    print("ok", gen_check(gen))

if __name__ == "__main__":
    main()
