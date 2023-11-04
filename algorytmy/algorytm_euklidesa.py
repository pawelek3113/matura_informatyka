"""
NWD - Największy Wspólny Dzielnik
znajdź największą dodatnią liczbę całkowitą która dzieli obie liczby

---
GCD - Greatest Common Divisor
find the largest positive integer that divides each of the integers.
"""

import math
from random import randint


def nwd(a, b) -> int:
    while a != 0 and b != 0:
        if a >= b:
            a -= b
        else:
            b -= a
    return a + b


# optimized
def gcd(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd_recursive(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd_recursive(a % b, b)
    else:
        return gcd_recursive(a, b % a)


for _ in range(10):
    x = randint(1, 100)
    y = randint(1, 100)
    print(f"GCD({x}, {y}) = {gcd(x,y)}")
    print(f"Recursive GCD({x}, {y}) = {gcd_recursive(x,y)}")
    print(f"Math GCD({x}, {y}) = {math.gcd(x, y)}")

