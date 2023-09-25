# Złożoność czasowa

Ilość czasu potrzebnego do wykonania programu. Najczęściej wyrażana w liczbie wykonanych operacji.

## Notacja O

### Definicja

Jeśli $n$ oznacza wielkość danych wprowadzanych do programu, a $T(n)$ oznacza liczbę wykonanych operacji przez program i
$T(n) = O(f(n))$, to istnieje taka stała liczba naturalna $k$, że:

$T(n) \leq k \cdot f(n)$

$O(f(n))$ daje nam przybliżoną liczbę operacji w najgorszym możliwym przypadku.

### Podstawowe złożoności obliczeniowe:

|                  |                         |
| ---------------- | ----------------------- |
| $O(1)$           | złożoność stała         |
| $O(\log_{2}{n})$ | złożoność logarytmiczna |
| $O(n)$           | złożoność liniowa       |
| $O(n^2)$         | złożoność kwadratowa    |
| $O(2^n)$         | złożoność wykładnicza   |

---

| $n$           | $10$   | $1000$     | $10^6$        |
| ------------- | ------ | ---------- | ------------- |
| $O(1)$        | $1$    | $1$        | $1$           |
| $O(log_2{n})$ | $4$    | $10$       | $20$          |
| $O(n)$        | $10$   | $1000$     | $10^6$        |
| $O(n^2)$      | $100$  | $10^6$     | $10^{12}$     |
| $O(2^n)$      | $1000$ | $10^{300}$ | $10^{301030}$ |

#### Przykład

Oblicz złożoność obliczeniową programu:

```python
# n - liczba ocen z informatyki
n = int(input())
# suma - łączna suma wszystkich ocen
suma = 0
for i in range(1, n+1):
	# ocena - i-ta ocena z informatyki
	ocena = int(input())
	suma += ocena
print(float(suma/n))
```

$n+1+n+1= 2n + 2 \Rightarrow O(n) $
