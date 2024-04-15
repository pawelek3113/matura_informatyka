# x^4 + 2x^3 + 0x^2 + 1x^1 - 15x^0
# x (x^3 + 2x^2 + 1) - 15
# x (x (x^2 + 2x) + 1) - 15
# x (x (x (x + 2)) + 1) - 15

x = 4
factors = [1, 2, 0, 1, -15]
degree = 4

result = factors[0]

for i in range(1, degree + 1):
    result = x * result + factors[i]

print(result)
