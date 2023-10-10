def exponentiation_iterative(base: int, exponent: int):
    # base^exponent
    result = 1
    for _ in range(1, exponent + 1):
        result *= base

    return result


def exponentiation_recursive(base: int, exponent: int):
    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        x = exponentiation_recursive(base, exponent // 2)
        return x * x
    else:
        return base * exponentiation_recursive(base, exponent - 1)


a = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print(f"{a}^{n}")
print(f"Iterative way: {exponentiation_iterative(a, n)}")
print(f"Recursive way: {exponentiation_recursive(a, n)}")
