def can_construct_triangle(a, b, c):
    conditions = [(a + b > c), (b + c > a), (c + a > b)]

    if all(conditions):
        return True
    else:
        return False


print(can_construct_triangle(3, 4, 5))
print(can_construct_triangle(7, 24, 25))
print(can_construct_triangle(2, 2, 5))
