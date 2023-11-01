# Sortowanie przez zliczanie

Uporządkowanie elementów polega na policzeniu ile razy dana liczba występuje w ciągu.

### Opis algorytmu

---

Ustalamy tablicę zawierającą ilości wystąpień poszczególnych liczb z naszej tablicy:

- ustalamy jej rozmiar, jest to największa liczba z naszej tablicy
- wypełniamy zerami.

Następnie wypełniamy tablicę z ilościami wystąpień. Bierzemy liczbę X z naszej tablicy. Jeśli występuje, to zwiększamy ilość jej wystąpień.

`ilosci[X] -> ilość wystąpień liczby z tablicy`

Następnie przechodzimy po każdej liczbie z przedziału od 0 do długości tablicy `ilości`. Jeśli liczba wystąpień danej liczby jest równa zero, pomijamy. W przeciwnym wypadku zapisujemy indeks pętli, który jest liczbą z naszej tablicy, tyle razy, ile występuje.

### Zalety i wady

---

| Zalety    | Wady                        |
| --------- | --------------------------- |
| złożoność | mało uniwersalne            |
| prostota  | trzeba znać rozmiar tablicy |

### Implementacja:

```py
def counting_sort(array: list[int]) -> list[int]:
    if len(array) == 0:
        return array

    border = max(array)
    # array containing amounts of occurrences of numbers
    amounts: list[int] = [0] * (border + 1)

    # filling amounts array
    for i in range(len(array)):
        # take number from the array
        num = array[i]
        # count its occurrence
        amounts[num] += 1

    sorted_array = []

    # loop over numbers from 0 to border+1
    for i in range(0, len(amounts)):
        # skip if the number of occurrences is 0
        if amounts[i] == 0:
            continue
        else:
            # write the number as many times as it occurs
            for j in range(amounts[i]):
                # amounts[i] - number of occurrences
                # i - number from array
                sorted_array.append(i)

    return sorted_array


seq: list[int] = [4, 6, 4, 5, 0, 7, 6, 2, 3]
sorted_seq: list[int] = counting_sort(seq)
print(sorted_seq)
```

---

#### Złożoność obliczeniowa:

$O(n+k)$

#### Złożoność pamięciowa:

$O(n+k)$

---
