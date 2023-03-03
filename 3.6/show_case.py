# from __future__ import annotations
from typing import List

def pep515():
    a = 1_0_00_000_0000
    b = 0xf_ff_fff_ffff
    c = 0o7_77_777_7777
    assert 0o7_0 == 5_6

def pep498():
    width, prec = 10,4
    value = 12.34567
    assert "{} {:{}.{}}".format("results:", value, width, prec) == f"results: {value:{width}.{prec}}"
    print("{} {:{}.{}}".format("results:", value, width, prec))
    print(f"results: {value:{width}.{prec}}")
    print(f"{1234:_} {0xfffffff:_x}")

def pep526():
    primes: List[int] = []
    captain:str # Unbound
    # assert captain == None # raise UnboundLocalError
    captain = None
    assert captain == None # raise UnboundLocalError


if __name__=="__main__":
    pep515()
    pep526()
    pep498()
