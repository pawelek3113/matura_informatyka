def create_line(segment):
    # return line's factors
    first_point, second_point = segment
    a = (first_point[1] - second_point[1]) / (first_point[0] - second_point[0])
    b = first_point[1] - a * first_point[0]

    return [a, b]


def is_on_line(point, line):
    value = line[0] * point[0] + line[1]
    if value == point[1]:
        return True
    else:
        return False


def is_in_interval(point, segment):
    if point[0] >= segment[0][0] and point[0] <= segment[1][0]:
        return True
    else:
        return False


def is_in_segment(point, segment):
    line = create_line(segment)

    if is_on_line(point, line) and is_in_interval(point, segment):
        return True
    else:
        return False


print(is_in_segment([3.5, 2], [[2.5, 1], [4, 2.5]]))
print(is_in_segment([3.5, 3], [[2.5, 1], [4, 2.5]]))
