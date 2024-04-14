def func(x: int) -> int:
    return -x**4+2*x**3+5*x**2-3


def get_field(start: int, end: int, rect_num: int, callback):
    field = 0

    base = abs(end - start) / rect_num

    x = start
    for i in range(rect_num):
        x += base
        side = callback(x)
        field += side * base

    return field


print(get_field(1, 3, 1000, func))
