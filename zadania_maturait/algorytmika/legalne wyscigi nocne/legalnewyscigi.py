cash = 50


def exponentiation_recursive(base: int, exponent: int):
    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        x = exponentiation_recursive(base, exponent // 2)
        return x * x
    else:
        return base * exponentiation_recursive(base, exponent - 1)


x = exponentiation_recursive(2, 1000000000)

res = cash * x

print(res % 1000000009)
