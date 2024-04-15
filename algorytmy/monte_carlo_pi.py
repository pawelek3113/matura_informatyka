import random

points = 200000
points_in_circle = 0

for i in range(points):
    # random number between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y <= 1:
        points_in_circle += 1

print(4 * points_in_circle / points)
