"""
Fibonacci sequence
-----
Zero element = 0
First element = 1
Second element = 1
Next element = sum of two previous elements

https://en.wikipedia.org/wiki/Fibonacci_sequence

-----
Recursive solution is less efficient than iterative one

-----
Ciag Fibonacciego

Zerowy element = 0
Pierwszy element = 1
Drugi element = 1
Nastepny element = suma dwoch poprzednich elementow

https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego

-----

Rozwiazanie rekurencyjnie jest mniej wydajne od iteracyjnego
"""


def get_n_fib_numb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    fib_nums = [1, 1, 2]

    for i in range(3, n):
        next_num = fib_nums[i - 1] + fib_nums[i - 2]
        fib_nums.append(next_num)

    return fib_nums[-1]


def get_n_fib_numb_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_n_fib_numb_recursive(n - 1) + get_n_fib_numb_recursive(n - 2)


def get_fib_numbers(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    fib_nums = [1, 1, 2]

    for i in range(3, n):
        next_num = fib_nums[i - 1] + fib_nums[i - 2]
        fib_nums.append(next_num)

    str_fib_nums = map(lambda x: str(x), fib_nums)
    text = " ".join(str_fib_nums)
    return text


num = int(input("Enter a number: "))
print(f"fib({num}) = {get_n_fib_numb(num)}")
print(f"fib({num}) = {get_n_fib_numb_recursive(num)}")
print(f"fib numbers from 1 to {num}: {get_fib_numbers(num)}")
