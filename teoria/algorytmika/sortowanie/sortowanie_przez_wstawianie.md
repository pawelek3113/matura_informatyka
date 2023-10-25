# Sortowanie przez wstawianie

Wstawianie obecnego elementu w odpowiednim miejscu w już posortowanym ciągu.

### Opis algorytmu

---

Uznajemy, że pierwszy (na zerowym indeksie) element jest posortowany.

Porównujemy element tablicy znajdujący się na indeksie 1 z poprzednim, już posortowanym. Jeśli element z już posortowanych elementów jest większy od bieżącego, to przesuwamy go w prawo - robimy miejsce dla bieżącego. Porównujemy do momentu, gdy już posortowany element jest mniejszy od bieżącego. Wstawiamy bieżący. Powtarzamy wszystko dla reszty liczb aż posortowana zostanie cała tablica.

### Implementacja:

```py
def insertion_sort(seq: list[int]) -> None:
    n: int = len(seq)

    # zero element is already sorted, so we start from 1
    for i in range(1, n):
        current: int = seq[i]

        # start comparing from previous item
        j: int = i - 1

        # if j is negative that means it has reached the edge of array
        while seq[j] > current and j >= 0:
            # shift (copy) the previous item to the right side
            seq[j+1] = seq[j]
            j -= 1

        seq[j+1] = current


array: list[int] = [6, 4, 5, 7, 2]
insertion_sort(array)

print(array)
```

---

#### Złożoność obliczeniowa: $O(n^2)$

#### Złożoność pamięciowa: $O(1)$

---

[Insertion Sort Algorithm Made Simple | Mosh](https://www.youtube.com/watch?v=nKzEJWbkPbQ)
