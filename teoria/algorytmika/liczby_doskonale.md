# Liczby doskonałe

### Definicja

Liczba doskonała - dodatnia liczba całkowita, której suma dzielników (mniejszych od niej) jest równa jej samej.

#### Przykład
czyDoskonała(28)
dzielniki: 1, 2, 4, 7, 14,  
suma dzielników mniejszych od liczby: 1+2+4+7+14 = 28
czyDoskonała(28) -> PRAWDA

#### Implementacja

```py
def is_perfect(number: int) -> bool:
    sum = 1
    k = 2
    while k * k <= number:
        if number % k == 0:
            sum += k
            if k != number//k:
                sum += number//k

        k += 1

    return sum == number
```