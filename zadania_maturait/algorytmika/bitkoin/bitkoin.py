n = 1050403310


def prime_decomposition(num: int) -> list[int]:
    x = num

    factors = []

    i = 2
    while i <= x:
        if x % i == 0:
            factors.append(i)
            x /= i
        else:
            i += 1

    return factors


prime_factors = prime_decomposition(n)
prime_factors.sort()

print(";".join(map(str, prime_factors)))
