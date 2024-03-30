def side_of_line(point, line):
    # line = ax + b => line = [a, b]
    # point = [X, Y]

    value = line[0] * point[0] + line[1]

    if value == point[1]:
        print("Point is on the line")
    elif value > point[1]:
        print("Point is below the line")
    elif value < point[1]:
        print("Point is above the line")


side_of_line([1.5, 2], [6, -7])
side_of_line([1.5, 4], [6, -7])
side_of_line([1.5, 1], [6, -7])
