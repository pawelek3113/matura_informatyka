# Sito Eratostenesa

Wyznaczenie wszystkich liczb pierwszych w skończonym przedziale.

---

### Mniej wydajne sprawdzanie, czy liczba jest pierwsza

Dla każdej liczby z przedziału $[2, n]$ sprawdzamy, czy jest ona pierwsza, korzystając z [algorytmu testu pierwszości liczby](liczby_pierwsze.md).

```py
n = 100

primes = [x for x in range(2, n+1) if is_prime_faster(x)]
print(primes)

```

#### Złożoność obliczeniowa

$O(n \cdot \sqrt{n})$

### Sito Eratostenesa

Polega na eliminacji wielokrotności liczb pierwszych.

---

Jeśli liczba $p$ jest pierwsza, to liczby $2p$, $3p$... są na pewno żłożone.

Najpierw załóżmy, że liczby $2, 3, 4, ..., n$ są pierwsze

```py
primes = [False, False] + [True] * (n-1)
```

Korzystając z wcześniejszych obserwacji wiemy, że liczby $2p$, $3p$... są złożone, więc dla $p = 2$ oznaczmy wszystkie wielokrotności $2$ (większe od $2$) jako złożone:

```py
# k-ta wielokrotność liczby 2
k = 2
while 2*k <= n:
    primes[2*k] = False
    k+=1

```

Dla kolejnych liczb pierwszych wykonujemy tę samą procedurę:

#### Implementacja

```py
limit = 100

# assume that 0 and 1 are not prime
primes = [False, False] + [True] * (limit-1)

for i in range(2, limit):
    if primes[i]:
        k = 2
        while i * k <= limit:
            # mark multiples of i as composite (non-prime)
            primes[i*k] = False
            k += 1

print([idx for idx, is_prime in enumerate(primes) if is_prime])
```

##### Sito Eratostenesa

---

#### Główne założenia:

- oznaczenie na początku, że wszystkie liczby są pierwsze (oprócz 0 i 1)
- eliminacja wielokrotności liczb pierwszych

---

#### Złożoność obliczeniowa

$O(n \cdot \log{n})$

##### Przykład

```
n = 10

liczby_pierwsze = [0 - False, 1 - False, 2 - True, 3 - True, ..., 10 - True]

for 2...n:
    # i = 2
    if liczby_pierwsze[2]: #True
        k = 2
        while i*k <= n:
            2*2=4 = False
            k+=1
            2*3=6 = False
            k+=1
            2*4=8 = False
            k+=1
            2*5=10 = False
            k+=1
    #liczby_pierwsze = [0 - F, 1 - F, 2 - F, 3 - T, 4 - F, 5 - T, 6 - F, 7 - T, 8 - F, 9 - T, 10 - F]

    # i = 3
    if liczby_pierwsze[3]: #True
        k = 2
        while i*k <= n:
            3*2=6 = False
            k+=1
            3*3=9 = False
            k+=1
    #liczby_pierwsze = [0 - F, 1 - F, 2 - F, 3 - T, 4 - F, 5 - T, 6 - F, 7 - T, 8 - F, 9 - F, 10 - F]

    # i = 4
    if liczby_pierwsze[4]: #False
        pass

    # i = 5
    if liczby_pierwsze[5]: #True
        k = 2
        while i*k <= n:
            5*2=10 = False
            k+=1

    # i = 6
    if liczby_pierwsze[6]: #False
        pass

    # i = 7
    if liczby_pierwsze[7]: #True
        k = 2
        while i*k <= n:
            pass
    #liczby_pierwsze = [0 - F, 1 - F, 2 - F, 3 - T, 4 - F, 5 - T, 6 - F, 7 - T, 8 - F, 9 - F, 10 - F]

    # i = 8
    if liczby_pierwsze[8]: #False

    # i = 9
    if liczby_pierwsze[9]: #False

    # i = 10
    if liczby_pierwsze[10]: #False

    #liczby_pierwsze = [3 - T, 5 - T, 7 - T]
```

### Optymalizacja

Wykreślanie można zacząć od $p^2$, a nie od $2p$.

Nie ma sensu wykreślać wielokrotności $p: 2p, 3p, ..., (p-1)p$, z tego względu, że zostały one wykreślone przez wcześniejsze liczby pierwsze: $2, 3...$

#### Implementacja

```py
limit = 100

# assume that every number is prime (besides 0 and 1)
primes = [False, False] + [True] * (limit-1)

for i in range(2, limit):
    if primes[i]:
        k = i
        while i * k <= limit:
            # mark multiples of i as composite (non-prime)
            primes[i*k] = False
            k += 1

print([idx for idx, is_prime in enumerate(primes) if is_prime])

```

#### Złożoność obliczeniowa

$O(n \log(\log n))$

##### Przykład

```
n = 10

i = 2

k = 2

4 = F, 6 = F, 8 = F, 10 = F

i = 3

k = 3

9 = F

liczby_pierwsze = [2, 3, 5, 7]
```
