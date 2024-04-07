S = 321123
eps = 0.01


def metoda_babilonska(num, accuracy):
    x = num

    while abs(x - num/x) > accuracy:
        x = 1/2 * (x + num/x)

    return x

def metoda_rownego_podzialu(num, accuracy):
    start = 0
    end = num

    while abs(start - end) > accuracy:
        mid = (start + end) / 2

        if mid**2 <= num:
            start = mid
        else:
            end = mid

    return (start + end)/2


print(metoda_babilonska(S, eps))
print(metoda_rownego_podzialu(S, eps))