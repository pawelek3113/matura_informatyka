def func(x):
    return x**3 - 4*x**2 + 6*x - 24


def find_root(interval, tolerance):
    a, b = interval

    if func(a) * func(b) > 0:
        return -1

    while abs(a-b) > tolerance:
        mid_point = (a+b)/2

        if func(mid_point) == 0:
            return mid_point

        if func(a) * func(mid_point) < 0:
            b = mid_point
        elif func(mid_point) * func(b) < 0:
            a = mid_point

        if abs(func(mid_point)) <= tolerance:
            return (a+b)/2


print(find_root([-16, 16], 0.1))
