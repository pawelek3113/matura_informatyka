# Iteracja i rekurencja

### Iteracja - powtarzanie danej czynności w pętli

```py
while i < 10:
	i += 4
```

### Rekurencja - odwoływanie się funkcji do samej siebie

```py
def f(n):
	if n <= 1:
		return 1
	else if n == 2:
		return 2
	else:
		return f(n - 1) + f(n - 2)
```

## Obliczanie $n!$ iteracyjnie i rekurencyjnie

#### Iteracyjnie:

```py
n = int(input())
silnia = 1
for i in range(1, n+1):
	silnia *= i
print(silnia)
```

Złożoność $O(n)$

#### Rekurencyjnie:

```py
def silnia(n):
	if n==0:
		return 1
	else:
		return n*silnia(n-1)

n = int(input())
print(silnia(n))
```

$n! = (n-1)! \cdot n $

Złożoność $O(n)$

---

### Obliczanie $n$-tego wyrazu ciągu Fibonacciego

$fib(n) = \{^{1 \space dla \space n = 1,2}\_{fib(n-1) \space + \space fib(n-2) \space dla \space n > 2} $

#### Iteracyjnie

```py
# fib – tablica, w której przechowujemy kolejne liczby Fibonacciego
fib = [0, 1, 1]

# n - oznacza n-tą liczbę Fibonacciego, którą chcemy obliczyć
n = int(input())

for i in range(3, n + 1):
	fib.append(fib[i - 1] + fib[i - 2])

print(fib[n])
```

#### Rekurencyjnie

```py
def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
```

Matematyczna definicja ciągu Fibonacciego
$fib_n = fib_{n-1} + fib_{n-2}$

Złożoność $O(fib_n)$ albo $O(2^n)$, gdyż fib_n $\leq$ $2^n$!!!
