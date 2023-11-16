def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime_faster(number: int) -> bool:
    k = 2
    while k*k <= number:
        if number % k == 0:
            return False
        k += 1

    return True


print(is_prime(37))
print(is_prime_faster(37))
