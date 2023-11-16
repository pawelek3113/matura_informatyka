# Liczby pierwsze

### Definicja

Liczba pierwsza - dodatnia liczba całkowita podzielna przez 1 oraz samą siebie.

### Sprawdzanie, czy liczba jest pierwsza

---
#### Chcemy sprawdzić, czy liczba N jest pierwsza
Jeśli jakaś liczba z przedziału od 2 do N-1 jest dzielnikiem liczby N (dzieli liczbę N; tj. reszta z dzielenia jest równa 0), to N jest złożona - nie jest liczbą pierwszą.

#### Implementacja

```py
def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
```

#### Złożoność obliczeniowa
$O(n)$


### Zoptymalizowana wersja

---

Zamiast testować wszystkie liczby do N-1, wystarczy sprawdzić podzielność
N przez liczby mniejsze lub równe $\sqrt{N}$

#### Dowód

Załóżmy, że $N$ jest złożona. Wtedy istnieją liczby $a, b \in \mathbb {N}$ takie, że $N = ab$ oraz $a \leq b$. Po przemnożeniu nierówności stronami przez $a$ otrzymujemy $a^2 \leq ab$. Ale $ab = N$, więc $a^2 \leq N$. Stąd $a \leq \sqrt{N}$.

#### Implementacja

```py
def is_prime_faster(number: int) -> bool:
    k = 2
    while k*k <= number:
        if number % k == 0:
            return False
        k += 1

    return True
```

#### Złożoność obliczeniowa
$O(\sqrt{n})$