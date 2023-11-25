def prime_decomposition(num: int) -> list[int]:
    n = num
    factors = []

    if n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                factors.append(i)
                n = n//i
            else:
                i += 1
    return factors


print(prime_decomposition(420))
