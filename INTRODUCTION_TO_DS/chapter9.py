import random


def a_k_m(a: int, k: int, m: int) -> int:
    """return a**k%m with efficient way by binary expansion"""
    b = 1
    for i in reversed(bin(k)[2:]):
        if i == 1:
            b = a*b % m
        a = a**2 % m
    return b


def random_div(n: int, repeat: int = 10) -> str:
    """check whther n is a prime number.
    this algorithm doesnt nesceceraly return right answer"""
    if n % 2 == 0:
        return "comosite"
    d_max = int(pow(n, 0.5))
    odd_seq = range(3, d_max+1, 2)
    for cnt in range(repeat):
        d = random.choice(odd_seq)
        if n % d == 0:
            return "composite"
        return "probably prime"


def fermat_check(n: int) -> int:
    """if retur is 0,then n is a prime number ,else n is composite nuber"""
    cnt = 0
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            cnt += 1
    return cnt
