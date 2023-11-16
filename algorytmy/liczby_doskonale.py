def is_perfect(number: int) -> bool:
    sum = 1
    k = 2
    while k * k <= number:
        if number % k == 0:
            sum += k
            if k != number//k:
                sum += number//k

        k += 1

    return sum == number


print(f"Is {28} perfect? {'Yes' if is_perfect(28) else 'No'}")
print(f"Is {496} perfect? {'Yes' if is_perfect(496) else 'No'}")
