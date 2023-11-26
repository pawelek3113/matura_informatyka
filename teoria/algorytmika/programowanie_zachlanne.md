# Programowanie zachłanne

---

Algorytm zachłanny – algorytm, który w danym kroku dokonuje najlepszego wyboru. Ponadto, metody zachłanne nie uwzględniają tego, co może stać się w następnych krokach.

---

### Problem wydawania reszty

Problem polegający na wybraniu z danego zbioru monet o określonych nominałach takiej konfiguracji, by wydać żądaną kwotę przy użyciu minimalnej liczby monet

##### Przykład

###### Podejście zachłanne

Mamy wydać k złotych używając najmniejszej liczby monet.
Wybieramy monetę o największym nominale (nie większym od k), pomniejszamy k o wartość tej monety i zaczynamy zadanie od nowa.

```
dostępne monety = 1, 3, 7

kwota_do_wydania = 20 
wybrane_monety = []

kwota_do_wydania = 20, wybrane_monety = [7] -> kwota_do_wydania = 20-7=13
kwota_do_wydania = 13, wybrane_monety = [7,7] -> kwota_do_wydania = 13-7=6
kwota_do_wydania = 6, wybrane_monety = [7,7,3] -> kwota_do_wydania = 6-3=3
kwota_do_wydania = 3, wybrane_monety = [7,7,3,3] -> kwota_do_wydania = 3-3=0
kwota_do_wydania = 0.

```

### Implementacja

```py 
def give_change(amount: int, available_coins: list[int]) -> list[int]:
    available_coins.sort(reverse=True)

    n = amount

    coins = []

    i = 0
    while i <= len(available_coins)-1:
        if available_coins[i] <= n:
            coins.append(available_coins[i])
            n -= available_coins[i]
        else:
            i += 1

    return coins


a_coins = [2, 1, 3, 7]
amount_to_pay = int(input())
print(give_change(amount_to_pay, a_coins))


```

Podejście zachłanne nie zawsze daje optymalne rozwiązanie.

```
dostępne monety = 1, 4, 9
kwota = 12

wybrane_monety = []
kwota = 12, wybrane_monety = [9] -> kwota = 12-9=3
kwota = 3, wybrane_monety = [9, 1] -> kwota = 3-1=2
kwota = 2, wybrane_monety = [9, 1, 1] -> kwota = 2-1=1
kwota = 1, wybrane_monety = [9, 1, 1, 1] -> kwota = 1-1=0
kwota = 0.
```

Wydając resztę zachłannie użyliśmy 4 monety, natomiast można zauważyć, że liczbę 12 można wydać trzema monetami o nominale 4 (3 x 4zl = 12zl).
