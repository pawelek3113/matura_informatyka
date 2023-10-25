# Sortowanie bąbelkowe

Opiera się na porównywaniu par sąsiadujących elementów.

Nazwa sortowania bąbelkowego wzięła się stąd, gdyż wartości lżejsze wartości “wypływają” na prawo – podobnie jak pęcherzyki powietrza w wodzie na powierzchnię. “Wagę” wartości możemy ustalić na 2 sposoby:

- Lżejsze elementy mają większą wartość – wtedy sortujemy elementy niemalejąco.
- Lżejsze elementy mają mniejszą wartość – wtedy sortujemy elementy nierosnąco.

---

```py
for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
```

Zadaniem każdego z przejść jest wypchanie elementów maksymalnie na prawo.

#### Optymalizacja

`n-1` - porównywanie z już posortowanym elementem

`n-1-i` - porównujemy elementy nieposortowane; posortowany element znajduje się na swoim miejscu, na końcu

### Implementacja:

```py

def bubble_sort(seq: list[int]) -> None:
    n: int = len(seq)

    for i in range(n-1):
        for j in range(n-1-i):
            # nie porównujemy już posortowanego elementu ktory znajduje się na swoim miejscu
            # porównujemy elementy nieposortowane
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


array: list[int] = [6, 4, 5, 7, 2]
bubble_sort(array)

print(array)
```

---

#### Złożoność obliczeniowa: $O(n^2)$

#### Złożoność pamięciowa: $O(1)$

---

[Bubble Sort in Plain English | Mosh](https://www.youtube.com/watch?v=uJLwnsLn0_Q)