deg = 0
factors = []
points = []
with open("input.txt", "r", encoding="UTF-8") as file:
    inpt = [x for x in file.read().splitlines()]

    degree = int(inpt[0])
    factors = [int(x) for x in inpt[1].split()]
    # amount_of_queries = inpt[2]
    points = [int(x) for x in inpt[3:]]


def calculate_polynomial(pnts: list[int], deg: int, fctrs: list[int]):
    results = []
    for x in pnts:
        result = fctrs[0]

        for i in range(1, deg+1):
            result = x * result + fctrs[i]

        results.append(result)

    results = [str(x) for x in results]

    return ";".join(results)


print(calculate_polynomial(points, degree, factors))


