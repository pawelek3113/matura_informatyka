# Potegowanie

### Iteracyjnie

```py
def potega(podstawa: int, wykladnik: int):
    # podstawa^wykladnik
    wynik = 1
    for _ in range(1, wykladnik + 1):
        wynik *= podstawa

    return wynik

print(potega(2,5))

# 1 *= 2
# 2 *= 2
# 4 *= 2
# 8 *= 2
# 16 *= 2
# 32
```

##### Zlożoność $O(n)$

### Rekurencyjnie

W pierwszej kolejności, pomyślmy w jaki sposób możemy ograniczyć liczbę mnożeń. Spójrzmy na przykład:

$3^{100} = 3^{50} \cdot 3^{50}$

Jeśli najpierw policzymy $3^{50}$ i zapiszemy ją w zmiennej $x$, to $3^{100}$ = $x \cdot x$. A więc możemy zredukować liczbę mnożeń o $50$ (uniknęliśmy $50$ mnożeń, bo $x = 3^{50}$ i tym samym nie musimy liczyć $3^{50}$ po raz drugi).

Zanim rozważmy ogólny przypadek obliczania $a^n$, spójrzmy na 2 kluczowe obserwacje:

- Jeśli $2 ∣ n$, to możemy zapisać $x=a^{n/2}$, a potem obliczamy $a^n =x⋅x$ – ograniczamy liczbę mnożeń o tyle ile wynosi policzenie $a^{n/2}$.
- Jeśli $2 ∤ n$, to jedyne co możemy zrobić to zredukować wykładnik do parzystej liczby, czyli zapisać $a^n = a \cdot a^{n−1}$.

```py
def potega(podstawa: int, wykladnik: int):
    if wykladnik == 0:
        return 1

    if wykladnik % 2 == 0:
        x = potega(podstawa, wykladnik // 2)
        return x*x
    else:
        return podstawa * potega(podstawa, wykladnik - 1)

print(potega(2,5))

# potega(2,5)
# 2 * potega(2,4)
# 2 * potega(2,2) * potega(2,2)
# 2 * potega(2,1) * potega(2,1) * potega(2,1) * potega(2,1)
# 2 * 2 * potega(2,0) * 2 * potega(2,0) * 2 * potega(2,0) * 2* potega(2,0)
# 2 * 2 * 1 * 2 * 1 * 2 * 1 * 2 * 1
# 2 * 2 * 2 * 2 * 2
# 32
```

##### Zlożoność $O(log_{2}n)$
