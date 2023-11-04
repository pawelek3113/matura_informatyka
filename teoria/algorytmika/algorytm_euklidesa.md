# Algorytm Euklidesa

Wyznacza największy wspólny dzielnik dwóch liczb.

---

### Matematycznie

- wypisujemy dzielniki obu liczb
- spośród dzielników znajdujemy wspólne
- spośród wspólnych dzielników znajdujemy największy

#### Przykład

a = 10

b = 22

dzielniki liczby a = {1, 2, 5, 10}

dzielniki liczby b = {1, 2, 11, 22}

wspólne dzielniki = {1, 2}

największy dzielnik = 2

---

### Wersja niezoptymalizowana

#### Obserwacje:

- jeśli $d | a$ i $d | b$ to $d | a - b$
- jeśli $a = 0$ i $b \neq 0$ to $NWD(a,b) = b$, jeśli $b = 0$ i $a \neq 0$ to $NWD(a,b) = a$ 

```py
def nwd(a, b):
	# Redukujemy a i b do momentu, w którym jedno z nich jest 0
	while a!=0 and b!= 0:
		if a >= b:
			a -= b
		else:
			b -= a
	# a = 0 lub b = 0, dlatego zwracamy a+b
	return a + b
```

### Wersja zoptymalizowana

Zamiast odejmować, to $a=r$ -  podstawiamy resztę z dzielenia $a$ przez $b$ za $a$ 

#### Przykład
a = 10
b = 22

##### 10 < 22

b = 2

##### 10 >= 2

a = 0

wynik 0 + 2 = 2

NWD(10,22) = 2




```py
def nwd(a, b):
	# Redukujemy a i b do momentu, w którym jedno z nich jest 0
	while a!=0 and b!= 0:
		if a >= b:
			# a % b oznacza resztę z dzielenia a przez b
			a = a % b
		else:
			b = b % a
	# a = 0 lub b = 0, dlatego zwracamy a+b
	return a + b
```

### Rekurencyjnie
```py
def gcd_recursive(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd_recursive(a % b, b)
    else:
        return gcd_recursive(a, b % a)
```

### Wbudowana funkcja

```py
import math
x = int(input())
y = int(input())
print(f"Math GCD({x}, {y}) = {math.gcd(x, y)}")
```

---

#### Złożoność obliczeniowa zoptymalizowanej wersji:

$O(\log{a+b})$

#### Złożoność pamięciowa:

$O(1)$

# Najmniejsza wspólna wielokrotność - NWW

$NWW(a,b) = \frac{a \cdot b}{NWD(a,b)}$

```py
def NWW(a,b):
    return (a*b)/NWD(a, b)
```