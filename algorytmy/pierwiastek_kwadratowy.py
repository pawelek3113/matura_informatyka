def metoda_babilonska(S, eps):
    x = S
    while abs(x - S / x) > eps:
        x = (x + S / x) / 2
    return x


def metoda_rownego_podzialu(S, eps):
    start = 0
    end = S

    while abs(start - end) > eps:
        mid = (start + end)/2

        if mid**2 <= S:
            start = mid
        else:
            end = mid

    return (start + end)/2


print(metoda_babilonska(15, 0.01))
print(metoda_rownego_podzialu(15, 0.01))
