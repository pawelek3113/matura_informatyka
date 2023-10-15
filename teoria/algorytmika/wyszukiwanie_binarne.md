# Wyszukiwanie binarne

Jedna z podstawowych technik używanych do przeszukiwania danych.

Największą zaletą tej techniki jest fakt, że złożoność czasowa wynosi $O(log_2n)$.

### Wyszukiwanie naiwne

Dla każdej liczby z ciągu $b$ sprawdzamy czy istnieje w ciągu $a$.

```py
def naive_search(a: list, b: list):
    for j in range(len(b)):
        is_found = False

        for i in range(len(a)):
            if a[i] == b[j]:
                is_found = True

        if is_found:
            print(f"{b[j]} found")


seq = [1, 2, 3, 4, 5, 6, 7, 8]
find = [5, 10, 29, 1, 7]

naive_search(seq, find)
# 5 found
# 1 found
# 7 found
```

___

#### Kluczowe obserwacje:
- ciąg przeszukiwany $a$ jest niemalejący,
- chcemy sprawdzić czy liczba z ciągu $b$ występuje w ciągu $a$,
  - jeśli występuje ($a_i == b_j$), to możemy przerwać przeszukiwanie ciągu
  - wykorzystując fakt, że ciąg jest niemalejący, jeśli $a_i < b_j$, to nie ma sensu przeglądać liczb $a_1, ..., a_i$, ponieważ $a_1 \leq ... \leq a_i < b_j$, więc żadna z tych liczb nie może być równa $b_j$ 
  - jeśli $b_j < a_i$ to nie ma sensu przeglądać liczb $a_i, ..., a_n$, ponieważ $b_j < a_i \leq ... \leq a_n$, więc żadna z tych liczb nie może być równa $b_j$

#### Implementacja obserwacji, by zredukować złożoność czasową
___
W pierwszej kolejności musimy wybrać element ciągu $a$, z którym chcemy porównać liczbę $b_j$

Najoptymalniejszym wyborem jest środkowy element ciągu $a$, gdyż w najgorszym wypadku zredukujemy zakres poszukiwań o połowę. Indeks środkowego elementu ciągu $a$ oznaczmy $sr$.
- jeśli $b_j > a_{sr}$, to eliminujemy wyrazy $a_1, ..., a_{sr}$
- jeśli $b_j \leq a_{sr}$, to eliminujemy wyrazy $a_{sr+1}, ..., a_n$

W obu przypadkach usuneliśmy $\frac{1}{2} n$ wyrazów!

Pozostały ciąg (po usunięci niechcianych wyrazów) można traktować jako nowe zadanie i ponownie wybrać środkowy element nowego ciągu i znowu zredukować połowę elementów, aż do uzyskania jednoelementowego ciągu. Wtedy wystarczy sprawdzić czy ten pozostały wyraz jest równy $b_j$.

### Wyszukiwanie binarne

```py
def binary_search(number_to_find, seq):
    begin_idx = 0
    end_idx = len(seq) - 1

    while begin_idx < end_idx:
        mid_idx = (begin_idx + end_idx) // 2
        if number_to_find > seq[mid_idx]:
            begin_idx = mid_idx + 1
        elif number_to_find <= seq[mid_idx]:
            end_idx = mid_idx

    return seq[begin_idx] == number_to_find


sequence = [1, 2, 3, 4, 6, 7, 9, 12, 20, 21]

n = int(input("How many numbers would you like to find?"))

find: list[int] = []

for i in range(n):
    find.append(int(input(f"{i+1}. ")))

for number in set(find):
    if binary_search(number, sequence):
        print(f"{number} found")
    else:
        print(f"{number} not found :(")

```